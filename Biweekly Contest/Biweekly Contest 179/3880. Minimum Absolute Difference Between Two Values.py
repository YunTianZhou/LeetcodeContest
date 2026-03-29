"""
3880. Minimum Absolute Difference Between Two Values - Easy


You are given an integer array nums consisting only of 0, 1, and 2.

A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2.

Return the minimum absolute difference between i and j among all valid pairs. If no valid pair exists, return -1.

The absolute difference between indices i and j is defined as abs(i - j).



Example 1:

Input: nums = [1,0,0,2,0,1]

Output: 2

Explanation:

The valid pairs are:

 - (0, 3) which has absolute difference of abs(0 - 3) = 3.
 - (5, 3) which has absolute difference of abs(5 - 3) = 2.

Thus, the answer is 2.


Example 2:

Input: nums = [1,0,1,0]

Output: -1

Explanation:

There are no valid pairs in the array, thus the answer is -1.



Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 2
"""

from math import inf


class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        prev1 = prev2 = -inf
        ans = inf

        for i, x in enumerate(nums):
            if x == 1:
                ans = min(ans, i - prev2)
                prev1 = i
            elif x == 2:
                ans = min(ans, i - prev1)
                prev2 = i
        
        return -1 if ans == inf else ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minAbsoluteDifference([1, 0, 0, 2, 0, 1]))  # 2

    # Example 2
    print(sol.minAbsoluteDifference([1, 0, 1, 0]))  # -1
