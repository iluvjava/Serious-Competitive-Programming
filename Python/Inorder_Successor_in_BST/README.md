### **Problem Statement**

> Given the `root` of a binary search tree and a node `p` in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return `null`.

The successor of a node p is the node with the smallest key greater than p.val.



**Constraints:**

The number of nodes in the tree is in the range `[1, 104]`.

`-105 <= Node.val <= 105`

All Nodes will have unique values.


### **Approach**

Do an in-order traversal of the tree. Take note of the value of the current node as we add them into some data structure. If it's larger than the target, then return the current node. 

Simple

