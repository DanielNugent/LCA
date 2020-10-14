import pytest
import LowestCommonAncestor

Node = LowestCommonAncestor.Node
LCA = LowestCommonAncestor.LCA
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


def test_answer():
    assert LCA(root, 4, 5) == 2
    assert LCA(root, 4, 6) == 1
    assert LCA(root, 3, 4) == 1
    assert LCA(root, 2, 4) == 2
    