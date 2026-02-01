"""
3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND - Medium


You are given an integer array nums.

Return the length of the longest strictly increasing subsequence in nums whose bitwise AND is non-zero. If no such subsequence exists, return 0.



Example 1:

Input: nums = [5,4,7]

Output: 2

Explanation:

One longest strictly increasing subsequence is [5, 7]. The bitwise AND is 5 AND 7 = 5, which is non-zero.


Example 2:

Input: nums = [2,3,6]

Output: 3

Explanation:

The longest strictly increasing subsequence is [2, 3, 6]. The bitwise AND is 2 AND 3 AND 6 = 2, which is non-zero.


Example 3:

Input: nums = [0,1]

Output: 1

Explanation:

One longest strictly increasing subsequence is [1]. The bitwise AND is 1, which is non-zero.



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""

from typing import List
from bisect import bisect_left


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        m = max(nums).bit_length()

        ans = 0
        for b in range(m):
            lis = []

            for x in nums:
                if x >> b & 1:
                    i = bisect_left(lis, x)
                    if i < len(lis):
                        lis[i] = x
                    else:
                        lis.append(x)

            ans = max(ans, len(lis))
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestSubsequence([5, 4, 7]))  # 2

    # Example 2
    print(sol.longestSubsequence([2, 3, 6]))  # 3

    # Example 3
    print(sol.longestSubsequence([0, 1]))  # 1
    