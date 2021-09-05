[[Dynamic Programming]], [[Array]]

---
### **Problem Statement**

Given Array of integers, find subset of element such that it sums up to $K$, another integer. 

---
### **Solution**

Let $\text{T}[i, k]$ be a state function, denoting a boolean, representing whether there exists a subset in the sub-array upto to the $i$ the element can be summed up to exactly $K$. 

Let the array be $\text{A}$, with size $n$. 

$$
\text{T}[i, k] := \mathbf{1}\lbrace\exist S\in \{1, 2, 3, \cdots, n\} \text{ s.t: } \sum_{j\in S}^{}\text{A}[j] = k\rbrace
$$

Recursion is: 

> $$
> \text{T}[i, k] = \left(
    \bigvee_{j = 0}^{i - 1} T[j, k - A[i]] 
\right)\vee \mathbf{1}\{A[i] = k\} \vee \text{T}[j - 1, k]
> $$

The base case would consists of: 

> $$
> \text{T}[0, 0] = \text{True} \quad \text{T}[0, k] = \text{False}\;\forall k
> $$


That is everything you need for dynamic programming. 

---
### **Improvement**

Not sure. But I know for sure there is a trick that can reduce the memory usage. 

---
### **Variants**

Longest sub-set that sum up to a $>, <, =$ to $k$. 


