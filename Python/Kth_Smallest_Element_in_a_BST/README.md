### **Problem Statement**

Given the root of a binary search tree, and an integer `k`, return the `k` th smallest element in the binary search tree. 

---
### **Approach**

The current value of the node is ranked between the number of nodes in the left sub tree and the number of nodes on the right sub tree. 

$$
\text{All Nodes Left Sub Tree} < \text{Node} < \text{All Nodes Right Sub Tree}
$$

We need to recursively sum up all the nodes to find out the position of the current nodes. 

>To avoid stack overflow for it, we would want to use stack directly


**Algorithm:**

Define the state function for each node in the stack

$$
\text{S}[n] := \begin{cases}
    1 & \text{Left node in the stack}
    \\
    2 & \text{Left and this node in the stack}
\end{cases}
$$

**Initialise:**

$$
\text{Stack} = \{\text{root}\} \quad \text{Queue} = \{\}
$$

**Algorithm:**

$$
\begin{aligned}
    & \text{While } \text{len(Statck)} \neq 0: 
    \\&\hspace{1.1em}
    \begin{aligned}
        & \text{Node} = \text{Stack.peek()}
        \\
        & \text{If Node is None}: 
        \\
        &\hspace{1.1em}
        \text{Stack.pop()}
        \\&\hspace{1.1em}
        \text{Continue}
        \\  
        & \text{If Node} \not\in \text{S}: 
        \\
        &\hspace{1.1em} \text{Stack} +_= \text{Node.left}
        \\
        &\hspace{1.1em}
        \text{S[Node]} = 1
        \\
        & \text{Else:}
        \\
        &\hspace{1.1em} \text{If } \text{S[Node]} = 1:
        \\&\hspace{2.2em}
        \text{Queue} +_= \text{Node.val}
        \\&\hspace{2.2em}
        \text{Stack} +_= \text{Node.right}
        \\&\hspace{1.1em}
        \text{ElseIf} 
        \\&\hspace{2.2em}
        \text{Stack.pop()}
    \end{aligned}
    \\&\text{Return Queue[k]}
\end{aligned}
$$

