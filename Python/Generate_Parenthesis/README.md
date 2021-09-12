Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**

```
Input: n = 1
Output: ["()"]
```
 

**Constraints:**

`1 <= n <= 8`


### **Approach**

When recurring, records the following information down the recursion tree: 

* The previous expression
* How many left/right parenthesis are needed to balance the expression out, if, any new characters were to be added on the right end of the expression. 
