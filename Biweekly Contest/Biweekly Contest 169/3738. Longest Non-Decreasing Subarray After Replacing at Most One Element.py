"""
3738. Longest Non-Decreasing Subarray After Replacing at Most One Element - Medium


You are given an integer array nums.

You are allowed to replace at most one element in the array with any other integer value of your choice.

Return the length of the longest non-decreasing subarray that can be obtained after performing at most one replacement.

An array is said to be non-decreasing if each element is greater than or equal to its previous one (if it exists).



Example 1:

Input: nums = [1,2,3,1,2]

Output: 4

Explanation:

Replacing nums[3] = 1 with 3 gives the array [1, 2, 3, 3, 2].

The longest non-decreasing subarray is [1, 2, 3, 3], which has a length of 4.


Example 2:

Input: nums = [2,2,2,2,2]

Output: 5

Explanation:

All elements in nums are equal, so it is already non-decreasing and the entire nums forms a subarray of length 5.



Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        prev_length = 1
        ans = j = 0
        for i in range(n):
            if i + 1 < n and nums[i] <= nums[i + 1]:
                continue

            length = i - j + 1
            ans = max(ans, length + prev_length)

            j = i + 1
            if i > 0 and i + 2 < n and (nums[i] <= nums[i + 2] or nums[i - 1] <= nums[i + 1]):
                prev_length = length
            else:
                prev_length = 1
        
        return min(ans, n)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestSubarray([1, 2, 3, 1, 2]))  # 4

    # Example 2
    print(sol.longestSubarray([2, 2, 2, 2, 2]))  # 5

