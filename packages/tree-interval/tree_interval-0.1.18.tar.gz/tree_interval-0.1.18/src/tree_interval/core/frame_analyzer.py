"""
Frame Analysis Module.

This module provides functionality for analyzing Python stack frames
and converting them into tree structures.
It bridges runtime execution with static code analysis.
"""

from ast import AST
from inspect import isframe
from types import FrameType
from typing import Optional, cast

from .ast_builder import AstTreeBuilder
from .interval_core import Leaf, Position, Tree


class FrameAnalyzer:
    """
    Analyzes a Python stack frame to identify the corresponding AST node.

    Attributes:
        frame: The Python stack frame to analyze.
        frame_position: Position object for frame's start and end positions.
        ast_builder: AstTreeBuilder instance for AST tree construction.
        tree: The resulting AST tree built from the frame.
        current_node: The currently identified AST node within the tree.
    """

    def __init__(self, frame: Optional[FrameType]):
        """Initializes FrameAnalyzer with a given frame."""
        self.frame = frame
        self.frame_position = (
            Position(0, 0) if frame is None else Position(self.frame)
        )
        if isframe(frame):
            self.ast_builder = AstTreeBuilder(frame)
        else:
            self.ast_builder = None
        self.tree = None
        self.current_node = None
        self.build_tree_done = False

    def find_current_node(self) -> Optional[Leaf]:
        """
        Finds the AST node corresponding to the current frame's position.

        Returns:
            Optional[Leaf]: The AST node at the current frame position,
            or None if not found.
        """
        if not self.build_tree_done:
            self.build_tree()
        if not self.tree or not self.tree.root:
            return None
        if self.current_node is None:
            matching_nodes = []
            for node in self.tree.flatten():
                if hasattr(node, "position") and node.position:
                    matching_nodes.append(
                        (
                            node,
                            abs(
                                node.position.start - self.frame_position.start
                            )
                            + abs(node.position.end - self.frame_position.end),
                        )
                    )

            if matching_nodes:
                self.current_node = min(matching_nodes, key=lambda x: x[1])[0]
        return self.current_node

    def build_tree(self) -> Optional[Tree]:
        """
        Builds a complete AST tree from the frame's AST.

        Returns:
            Optional[Tree]: The complete AST tree, or None if
                            construction fails.
        """
        self.build_tree_done = True
        if (
            not hasattr(self, "tree") or self.tree is None
        ) and self.ast_builder is not None:
            self.tree = self.ast_builder.build_from_frame()
            if not self.tree:
                return None
        if not hasattr(self, "current_node") or self.current_node is None:
            self.find_current_node()
        if self.tree and self.tree.root and self.ast_builder:
            nodes_by_pos = {}
            for node in self.tree.flatten():
                if hasattr(node, "ast_node") and isinstance(
                    node.ast_node, AST
                ):
                    pos = self.ast_builder._get_node_position(
                        cast(AST, node.ast_node)
                    )
                    if pos:
                        pos.selected = node.selected
                        node.position = pos
                        nodes_by_pos[(pos.start, pos.end)] = node

            sorted_positions = sorted(
                nodes_by_pos.keys(), key=lambda x: (x[0], -x[1])
            )

            for start, end in sorted_positions:
                current_node = nodes_by_pos[(start, end)]
                if current_node.match(self.current_node):
                    current_node.selected = True

                for parent_start, parent_end in sorted_positions:
                    if (
                        parent_start <= start
                        and parent_end >= end
                        and (parent_start, parent_end) != (start, end)
                    ):
                        parent_node = nodes_by_pos[(parent_start, parent_end)]
                        if not any(
                            p
                            for p in parent_node.get_ancestors()
                            if p.start <= start and p.end >= end
                        ):
                            parent_node.add_child(current_node)
                            break

        return self.tree
