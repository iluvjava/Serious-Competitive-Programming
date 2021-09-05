Given an integer array nums, return true if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exists, return false.

 

**Example 1:**
```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```
**Example 2:**
```
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```
**Example 3:**
```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```
 

Constraints:

`1 <= nums.length <= 5 * 105`
`-231 <= nums[i] <= 231 - 1`
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

---
### **This is solved using the idea of dynamic programming**

Let's define 2 states function that can be found using dynamic programming in linear time: 

$$
\text{LeftMin}[i] = \min(\text{nums[:i]}) \quad \text{RightMax}[i] = \max(\text{[i:]})
$$

Which basically represents the min and max of the left and right sub array. Then, we only need to iterate through the array and query the folloing information for each of the element to determine the existence of triplets in the array: 

$$
\exist? j: \text{LeftMin}[j]< \text{Nums}[j] < \text{RightMax}[j]
$$

Now, one would have to improve this from left to right to get the solution that uses only constant memory. 


---
### **The Constant Memory**

Hm....

