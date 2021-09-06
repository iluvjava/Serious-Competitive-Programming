### **Problem Statement**

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.


Initially, all next pointers are set to NULL.


**Example 1:**

![](../img2.png)

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
```
**Explanation**: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


**Example 2:**

```
Input: root = []
Output: []
```

**Constraints:**

The number of nodes in the tree is in the range `[0, 212 - 1]`.
`-1000 <= Node.val <= 1000`
 

**Follow-up:**

You may only use constant extra space.

The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

---
### **Approach**

No extra memory, means that we might have to use the tree itself, recur on it and modify it as we recurs along. 

**Inductive Hypothesis**

> Assuming that, All Level $N - 1$ has been fully connected. 

**Base Case**

The tree has level one, to solve it, we connect the left and right child of the root node, and connect them to NULL accordingly. This means: 

```python
root.next = None
root.left.next = root.right
```

**Recusrive Case**

Assuming The first node layer $N$ is given, named as `LeftMost`,and it's parent `Parent`. We want to construct the $N + 1$ layer. 

```python
while (Parent.next is not None): 
    LeftMost.next = Parent.right
    LeftMost = LeftMost.next
    Parent = Parent.next
    LeftMost.next = Parent.left
```

And that is about it, use these components to code it in and you will be good to go. 


