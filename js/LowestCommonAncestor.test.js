const LCA = require("./LowestCommonAncestor").LCA; //import the LCA function
const Node = require("./LowestCommonAncestor").Node; //import Node class definition
root = new Node(1);
n2 = new Node(2);
n3 = new Node(3);
n4 = new Node(4);
n5 = new Node(5);
root.successor = [n2, n3];
n2.successor = [n4];
n2.predecessor = [root];
n3.successor = [n4]
n3.predecessor = [root];
n4.successor = [n5];
n4.predecessor = [n2, n3];
n5.predecessor = [n4];

test("LCA of 2, 4 to be 2", () => {
  expect(LCA(root, n2, n4)).toBe(2);
});
test("LCA of 2, 3 to be 1", () => {
  expect(LCA(root, n2, n3)).toBe(1);
});
test("LCA of null and 2", () => {
  expect(LCA(root, null, 2)).toBe(null);
});