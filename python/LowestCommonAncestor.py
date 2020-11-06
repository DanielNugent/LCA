class Node:
    def __init__(self, key):
        self.key = key
        self.predecessor = []
        self.successor = []



def LCA(root, x, y):
    if(not hasattr(x, 'key')): 
        return None
    if(root is None):
        return None
    if(root.key == x.key or root.key == y.key):
        return root.key
    if(x.key == y.key):
        return x.key
    order = []


    for i in range(len(x.predecessor)):
        for j in range(len(y.predecessor)):
            if(x.predecessor[i].key == y.predecessor[j].key):
                order.append(x.predecessor[i].key)

    if(order == []):
        if(x.key > y.key):
            order.append(LCA(root,x.predecessor[0],y))
        else:
            order.append(LCA(root,x,y.predecessor[0]))

    return max(order)

