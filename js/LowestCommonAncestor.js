class Node {
  constructor(key) {
    this.left = null;
    this.right = null;
    this.key = key;
  }
}

const LCA = (root, p, q) => {
  const LCA_inner = (root, p, q) => {
    if (root == null) return root;
    if (root.key == p || root.key == q) return root;
    var left = LCA_inner(root.left, p, q);
    var right = LCA_inner(root.right, p, q);
    if (left != null && right != null) return root;
    if (left == null && right == null) return null;
    return left != null ? left : right;
  };
  return LCA_inner(root, p, q).key;
};

module.exports.LCA = LCA;
module.exports.Node = Node;

