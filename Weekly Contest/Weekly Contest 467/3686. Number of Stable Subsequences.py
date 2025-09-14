"""
3686. Number of Stable Subsequences - Hard


You are given an integer array nums.

A subsequence is stable if it does not contain three consecutive elements with the same parity when the subsequence is read in order (i.e., consecutive inside the subsequence).

Return the number of stable subsequences.

Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [1,3,5]

Output: 6

Explanation:

Stable subsequences are [1], [3], [5], [1, 3], [1, 5], and [3, 5].

Subsequence [1, 3, 5] is not stable because it contains three consecutive odd numbers. Thus, the answer is 6.


Example 2:

Input: nums = [2,3,4,2]

Output: 14

Explanation:

The only subsequence that is not stable is [2, 4, 2], which contains three consecutive even numbers.

All other subsequences are stable. Thus, the answer is 14.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        e1 = e2 = o1 = o2 = 0
        for x in nums:
            if x % 2 == 0:
                ne1 = (e1 + o1 + o2 + 1) % mod
                ne2 = (e1 + e2) % mod
                e1, e2 = ne1, ne2
            else:
                no1 = (o1 + e1 + e2 + 1) % mod
                no2 = (o1 + o2) % mod
                o1, o2 = no1, no2
        
        return (e1 + e2 + o1 + o2) % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countStableSubsequences([1, 3, 5]))  # 6

    # Example 2
    print(sol.countStableSubsequences([2, 3, 4, 2]))  # 14
    