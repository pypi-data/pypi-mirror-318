import pytest

from tree_interval import (
    Leaf,
    Position,
    Tree,
    TreeVisualizer,
    VisualizationConfig,
)


def test_visualizer_empty_tree(capsys):
    tree = Tree("Test")
    TreeVisualizer.visualize(tree)
    captured = capsys.readouterr()
    assert "Empty tree" in captured.out


def test_visualizer_position_formats():
    tree = Tree("Test")
    root = Leaf(Position(0, 100, info="Root"))
    tree.root = root

    config = VisualizationConfig(position_format="position")
    TreeVisualizer.visualize(tree, config)

    config.position_format = "tuple"
    TreeVisualizer.visualize(tree, config)


def test_visualizer_node_formatting():
    tree = Tree("Test")
    root = Leaf(Position(0, 100), info={"type": "Module"})
    child = Leaf(Position(10, 50), info={"type": "Function"})
    tree.root = root
    root.add_child(child)

    config = VisualizationConfig(show_info=True, show_size=True)
    TreeVisualizer.visualize(tree, config)


if __name__ == "__main__":
    pytest.main([__file__])
