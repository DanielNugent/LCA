class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def find_path(root, path, k):
    if root is None:
        return False

    path.append(root.key)
    if(root.key == k):
        return True
    if((root.left != None and find_path(root.left, path, k)) or (root.right != None and find_path(root.right, path, k))):
        return True
    path.pop()
    return False


def LCA(root, x, y):
    p1 = []
    p2 = []
    if(not find_path(root, p1, x) or not find_path(root, p2, y)):
        return -1
    k = 0
    while(k < len(p1) and k < len(p2)):
        if(p1[k] != p2[k]):
            break
        k = k + 1
    return p1[k-1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

a1 = LCA(root, 4, 5)
a2 = LCA(root, 4, 6)
a3 = LCA(root, 3, 4)
a4 = LCA(root, 2, 4)

print(a1, a2, a3, a4)
# print "LCA(4, 5) = %d" %(LCA(root, 4, 5))
# print "LCA(4, 6) = %d" %(LCA(root, 4, 6))
# print "LCA(3, 4) = %d" %(LCA(root,3,4))
# print "LCA(2, 4) = %d" %(LCA(root,2, 4))
