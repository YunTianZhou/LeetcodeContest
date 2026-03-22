"""
3877. Minimum Removals to Achieve Target XOR - Medium


You are given an integer array nums and an integer target.

You may remove any number of elements from nums (possibly zero).

Return the minimum number of removals required so that the bitwise XOR of the remaining elements equals target. If it is impossible to achieve target, return -1.

The bitwise XOR of an empty array is 0.



Example 1:

Input: nums = [1,2,3], target = 2

Output: 1

Explanation:

 - Removing nums[1] = 2 leaves [nums[0], nums[2]] = [1, 3].

 - The XOR of [1, 3] is 2, which equals target.

 - It is not possible to achieve XOR = 2 in less than one removal, therefore the answer is 1.


Example 2:

Input: nums = [2,4], target = 1

Output: -1

Explanation:

It is impossible to remove elements to achieve target. Thus, the answer is -1.


Example 3:

Input: nums = [7], target = 7

Output: 0

Explanation:

The XOR of all elements is nums[0] = 7, which equals target. Thus, no removal is needed.



Constraints:

1 <= nums.length <= 40
0 <= nums[i] <= 10^4
0 <= target <= 10^4
"""

from math import inf
from functools import cache


class Solution:
    def minRemovals(self, nums: list[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, x):
            if i == n:
                return 0 if x == target else inf
            return min(dfs(i + 1, x ^ nums[i]), dfs(i + 1, x) + 1)
        
        ans = dfs(0, 0)
        return -1 if ans == inf else ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minRemovals([1, 2, 3], 2))  # 1

    # Example 2
    print(sol.minRemovals([2, 4], 1))  # -1

    # Example 3
    print(sol.minRemovals([7], 7))  # 0
