"""
3974. Maximum Total Sum of K Selected Elements - Medium


You are given an integer array nums and two integers k and mul.

Select exactly k elements from nums. Process these elements one by one in any order you choose.

For each selected element, independently choose one of the following:

 - Add the element's value to the total sum, or

 - Multiply the element by the current value of mul and add the result to the total sum.

After processing each selected element, mul decreases by 1, regardless of which option was chosen. The current value of mul may become 0 or negative.

Return an integer denoting the maximum possible total sum.



Example 1:

Input: nums = [6,1,2,9], k = 3, mul = 2

Output: 26

Explanation:

One optimal way:

 - One optimal selection is nums[3] = 9, nums[0] = 6, and nums[2] = 2.

 - Process nums[3] = 9 first: choose multiplication, so it contributes 9 * 2 = 18. Now, mul becomes 1.

 - Process nums[0] = 6 next: choose multiplication, so it contributes 6 * 1 = 6. Now, mul becomes 0.

 - Process nums[2] = 2 last: choose addition, so it contributes 2.

 - The total sum is 18 + 6 + 2 = 26.


Example 2:

Input: nums = [3,7,5,2], k = 2, mul = 4

Output: 43

Explanation:

One optimal way:

 - One optimal selection is nums[1] = 7 and nums[2] = 5.

 - Process nums[1] = 7 first: choose multiplication, so it contributes 7 * 4 = 28. Now, mul becomes 3.

 - Process nums[2] = 5 next: choose multiplication, so it contributes 5 * 3 = 15.

 - The total sum is 28 + 15 = 43.


Example 3:

Input: nums = [4,4], k = 1, mul = 1

Output: 4

Explanation:

One optimal way:

 - One optimal selection is nums[0] = 4.

 - Process nums[0] = 4: choose multiplication, so it contributes 4 * 1 = 4.

 - The total sum is 4.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= nums.length
1 <= mul <= 10^5
"""


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        ans = 0
        
        nums.sort(reverse=True)
        for x in nums[:k]:
            if mul > 1:
                ans += mul * x
                mul -= 1
            else:
                ans += x
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxSum([6, 1, 2, 9], 3, 2))  # 26

    # Example 2
    print(sol.maxSum([3, 7, 5, 2], 2, 4))  # 43

    # Example 3
    print(sol.maxSum([4, 4], 1, 1))  # 4
