const LCA = require("./LowestCommonAncestor").LCA; //import the LCA function
const Node = require("./LowestCommonAncestor").Node; //import Node class definition
var root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);
root.left.right = new Node(5);
root.right.left = new Node(6);
root.right.right = new Node(7);

test("LCA of 4,5 to be 2", () => {
  expect(LCA(root, 4, 5)).toBe(2);
});
test("LCA of 4,6 to be 1", () => {
  expect(LCA(root, 4, 6)).toBe(1);
});
test("LCA of 3,4 to be 1", () => {
  expect(LCA(root, 3, 4)).toBe(1);
});
test("LCA of 2, 4 to be 2", () => {
  expect(LCA(root, 2, 4)).toBe(2);
});
