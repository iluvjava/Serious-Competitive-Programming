### **Problem Statement**

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


**Example 1:**

![](./../img1.png)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**
```
Input: preorder = [-1], inorder = [-1
Output: [-1]
```

**Constraints:**

* 1 <= preorder.length <= 3000
* inorder.length == preorder.length
* -3000 <= preorder[i], inorder[i] <= 3000
* preorder and inorder consist of unique values.
* Each value of inorder also appears in preorder.
* preorder is guaranteed to be the preorder traversal of the tree.
* inorder is guaranteed to be the inorder traversal of the tree.

---
### **Approach**

> Understand pre-order, in-order traversal and then use recursion. 

Fix a node root $r$ in Pre-order traversal array $P$, then there exists the same node in the In-order traversal array $I$, and the following can be said: 

$$
\begin{aligned}
    P & = [r, *[L(r)], *[R(r)]]
    \\
    I &= [*[L(r)], r, *[R(r)]]
\end{aligned}
$$

Where, $L(r)$, $R(r)$ are the left and the right sub tree of the given node $r$. And it's denotede as $*[\bullet]$ to represent the action of upacking a array. 

**The recursive Solution**

To solve the problem, we need to identify the root and then recur on the left and right subtrees of the root. 

**Observe:**

> For unique value in Pre-order traversal array, find it in the other in-order traversal array which then locates the left sub-tree and right sub tree, split it and recur, and locate on the next element in the Pre-order Traversal. 

**This is the python implementation**

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
    
    def BuildRecur(left, right): # build tree using left and right boundary. 
        nonlocal PreorderIdx
        if left > right: 
            return None
        RootVal = preorder[PreorderIdx] 
        Root = TreeNode(RootVal)
        PreorderIdx += 1
        Root.left = BuildRecur(left, InOrderIdxMap[RootVal] - 1) 
        Root.right = BuildRecur(InOrderIdxMap[RootVal] + 1, right)
        return Root
    
    InOrderIdxMap = {}  # Mapping value of node to index in In-order traversal. 
                        # This is needed for quick look up. 
    PreorderIdx = 0
    for Idx, Val in enumerate(inorder):
        InOrderIdxMap[Val] = Idx
    
    return BuildRecur(0, len(preorder) - 1)

```
