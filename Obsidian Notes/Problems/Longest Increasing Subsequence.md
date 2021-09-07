[[Dynamic Programming]]

---
### **Intro**

Given an array of integer, look for a subset of indices and keeping the order such that when indexed by that set of indices, the new array is strictly increasing. Find the longest length of such subarray. 


> $$
> \max_{S\subseteq [n]} \left\lbrace
>     |S| \text{ s.t: } \forall\; 1\le i < |S| \; \text{A}[S[i]] < A[S[i + 1]]
> \right\rbrace
> $$

Where, $S$ is the set of sub-indices selected ans sorted, $A$ is the Array. For simplicity, denote $S\uparrow$ as indexing the $A$ with indeices in $S$ such that the sub-array is monotonic increasing. 

---
### **Approach**

**Classic Wrong approach:**

Consider state function: 

$$
\text{DP}[i] := |S|, S\subseteq \{1, 2, \cdots i\} \text{ st: }S\uparrow 
$$

This is wrong because we have no information as to what is tha last element in $A[i \in S]$. A recurrence relations ship can't be constructed base on this state function. 

**Correct Approach:** $\mathcal{O}(n^2)$

Consider State Function: 

> $$
> \text{DP}[i] := |S|, S\subseteq \{1, 2, \cdots i\}, \underbrace{i\in S}_{\text{New stuff}} \text{ st: }S\uparrow 
> $$

**Explanation:** 

$\text{DP}[i]$ denotes the set of sub indices that makes an increasing sub array, including the $i$ th element of the array $A$. 

**Recursion:** 

> $$
> \text{DP}[i] := 
> \max \left\lbrace
>     \max_{1\le j < i} \left\lbrace
>         \text{DP}[j] + 1 \text{ s.t: } A[j] < A[i]
>     \right\rbrace, 1
> \right\rbrace
> $$

**Explaination**

For each sub-sequence that ends with $j < 1$, if its last element is strictly less than $A[i]$, then that is a valid sub-sequence. 

Enumerate through all such subsequence and find the subsequence with maximum length. 

---
### **Improvements**

There exists a $\mathcal{O}(n\log(n))$ solution to it. 

Agree with this fact: 

> $$
>     \text{DP}[i] < \text{DP}[j] \text{ where: } i < j
> $$

The optimality definition of $\text{DP}$ asserts this. 

When optimizing $\text{DP}[i]$, perform binary search to find the largest $j$ such that: $A[j] < A[i]$. 
  * if such an index doesn't exist, then $A[i]$ is larger than all it's prevous element and it has to be a start of a new subsequence. 
  * if it exists, then we found $\text{DP}[i]$, and we used binary search which reduced the complexity. 


---
### **Modifications and Extentions**

Looking for increasing, decreasing, non-decreasing, non-increasing sub array. 

Looking for the longest such array, and sometimes they can query for the actual array, or the length of the array, OR, the existence of such a sub-array. 