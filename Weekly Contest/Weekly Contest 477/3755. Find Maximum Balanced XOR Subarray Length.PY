"""
3755. Find Maximum Balanced XOR Subarray Length - Medium


Given an integer array nums, return the length of the longest subarray that has a bitwise XOR of zero and contains an equal number of even and odd numbers. If no such subarray exists, return 0.



Example 1:

Input: nums = [3,1,3,2,0]

Output: 4

Explanation:

The subarray [1, 3, 2, 0] has bitwise XOR 1 XOR 3 XOR 2 XOR 0 = 0 and contains 2 even and 2 odd numbers.


Example 2:

Input: nums = [3,2,8,5,4,14,9,15]

Output: 8

Explanation:

The whole array has bitwise XOR 0 and contains 4 even and 4 odd numbers.


Example 3:

Input: nums = [0]

Output: 0

Explanation:

No non-empty subarray satisfies both conditions.



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        mp = {(0, 0): -1}
        ans = diff = xor = 0
        for i, x in enumerate(nums):
            diff += 1 if x % 2 else -1
            xor ^= x
            t = (diff, xor)
            if t in mp:
                ans = max(ans, i - mp[t])
            else:
                mp[t] = i
        return ans
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxBalancedSubarray([3, 1, 3, 2, 0]))  # 4

    # Example 2
    print(sol.maxBalancedSubarray([3, 2, 8, 5, 4, 14, 9, 15]))  # 8

    # Example 3
    print(sol.maxBalancedSubarray([0]))  # 0
    