[[Longest Increasing Subsequence]]


---
### **Intro**

Given sequence $A$, try figuring out: 

> $$
> \exists? 1 \le i < j < k \le n: A[i] <A[j] <A[k]
> $$


This is a variation on the Longest Increasing Subsequence, but the objective is different and we have a constraint for it. 

---
### **Approach 1**

Dynamic programming. 

> For any element, it can be viewed that it divides the array into the left half and the right half, not including it self. If this element is larger than the smallest element in the left sub array and smaller than all the element on the right sub array, then we have a triplet: 

$$
\min_{1\le i < j} \{A[i]\} < A[j] < \max_{j < k \le n} \{A[k]\}
$$

Both the min and max of the sub array can be constructed using dynamic programming. 


---
### **Approach 2**

**Motivations**

Consider a triplets that exists in the array: 

$$
A[i] < A[j] < A[k] \text{ Where: } i < j < k
$$

Consider: 

$$
\begin{aligned}
    i^* &= \min_{1 \le t < k} \{A[t]\}
    \\
    j^* &= \min_{i^* < t < k} \{A[t]\}
    \\
    \implies A[i^*] &< A[j^*] < A[k]
\end{aligned}
$$

The flexibility in triplets allows us to consider an algorithm that only keeps track of 2 numbers which will allows us to identify the triplet. This is an optimization problem in disguise. 

**The Anchoring Tuple Theorem**

Consider the following update routine for the smallest and the second smallest element in the array while iterating through the array: 

$$
\begin{aligned}
    a^{(m)} &= \begin{cases}
        a^{(m - 1)} & A[m] > a^{m - 1}
        \\
        A[m]
    \end{cases}
    \\
    b^{(m)} &= \begin{cases}
        b^{(m - 1)} & A[m] < a^{(m - 1)} \vee \underbrace{A[m] > b^{(m - 1)}}_{\text{Just for completeness}}
        \\
        A[m] & b^{(m - 1)} > A[m] > a^{(m - 1)}
    \end{cases}
    \\
    a^{(1)} &= A[1] 
    \\
    b^{(1)} &= \infty
\end{aligned}
$$

Let $k$ be the smallest index such that: 

> $$
>     b^{(k)} = A[k] \implies A[m] > a^{(m - 1)} = a^{(m)}
> $$

We have found a strictly increasing tuple and we didn't miss any, let this be an assumption. It's obvious that if a strictly increasing tuple doesn't exist, we won't have a triplet. 

**Inductively:** 

> Regardless of whether $a^{(k)}$ is updated or $b^{(k)}$ is updated, we still can asserts the existence of an strictly increasing tuple. 

**if $a^{(k)}$ is updated then:**

$$
\begin{aligned}
    & A[k + 1] < a^{(k)}
    \\
    & a^{(k + 1)} = A[k + 1]
    \\
    & b^{(k + 1)} = b^{(k)} > a^{(k - 1)}
\end{aligned}
$$

The tuple is $b^{(k)}> a^{(k - 1)}$, the existence of $b^{(k)}$ asserts that there is a smaller number that comes before it. 

**if $b^{(k)}$ is updated then:**

$$
\begin{aligned}
    & a^{(k)} < A[k + 1] < b^{(k)}
    \\
    & a^{(k + 1)} = a^{(k)}
    \\
    & b^{(k + 1)} = b^{(k)} > a^{(k + 1)} = a^{(k)}
\end{aligned}
$$

$b^{(k + 1)} > a^{(k)}$ is the tuple, updating the value to make $b^{(k)}$ smaller doesn't destroy the existence of the tuple. 

$\blacksquare$ therefore, the tuple is asserted to exist through out the iteration. 

**Edge Case**

If the tuple never existed, then $b^{(i)} = \infty$ throughout the iteration, and there doesn't exist $A[i] > \infty$ throughout the iteration, therefore, it will never return true. 

**Algorithm**: 

$$
\begin{aligned}
    & \text{for } k = 2, 3, \cdots n
    \\
    & \hspace{1.1em}
    \begin{aligned}
        & \text{update } a^{(k)} \text{ using } a^{(k - 1)}
        \\
        & \text{update } b^{(k)} \text{ using } b^{(k - 1)}
        \\
        & \text{if } A[k] > b^{(k)}: 
        \\
        & \hspace{1.1em} \text{return True}
        \\
        & \text{else}: 
        \\
        & \hspace{1.1em} 
        \text{return false}
    \end{aligned}
\end{aligned}
$$




