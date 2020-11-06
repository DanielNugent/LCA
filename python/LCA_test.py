import pytest
import LowestCommonAncestor

Node = LowestCommonAncestor.Node
LCA = LowestCommonAncestor.LCA

root = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
root.successor = [r2,r3]
r2.successor = [r4]
r2.predecessor = [root]
r3.successor = [r4]
r3.predecessor = [root]
r4.successor = [r5]
r4.predecessor = [r2,r3]
r5.predecessor = [r4]


def test_answer():
    assert LCA(root, r2, r4) == 2
    assert LCA(root, r2, r3) == 1
    
def test_null():
    assert LCA(root, None, 2) is None
    