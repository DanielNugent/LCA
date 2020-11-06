class Node {
  constructor(key) {
    this.key = key;
    this.successor = []
    this.predecessor = []
  }
}

const LCA = (root, x, y) => {
  if(!x || !y) return null;
  if(!x.key || !y.key || root == null) return null;
  if(root.key === x.key || root.key === y.key) return root.key;
  if(x.key === y.key) return x.key;
  order = [];
  x.predecessor.forEach(predX => {
    y.predecessor.forEach(predY => {
      if(predX.key === predY.key) order.push(predX.key);
    })
  })
  if(order.length === 0){
    if(x.key > y.key) order.push(LCA(root, x.predecessor[0], y));
    else order.push(LCA(root, x, y.predecessor[0]));
  }
  return Math.max(...order); 
};
module.exports.LCA = LCA;
module.exports.Node = Node;

