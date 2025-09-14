"""
3681. Maximum XOR of Subsequences- Hard


You are given an integer array nums of length n where each element is a non-negative integer.

Select two subsequences of nums (they may be empty and are allowed to overlap), each preserving the original order of elements, and let:

 - X be the bitwise XOR of all elements in the first subsequence.
 - Y be the bitwise XOR of all elements in the second subsequence.

Return the maximum possible value of X XOR Y.

Note: The XOR of an empty subsequence is 0.



Example 1:

Input: nums = [1,2,3]

Output: 3

Explanation:

Choose subsequences:

First subsequence [2], whose XOR is 2.

Second subsequence [2,3], whose XOR is 1.

Then, XOR of both subsequences = 2 XOR 1 = 3.

This is the maximum XOR value achievable from any two subsequences.


Example 2:

Input: nums = [5,2]

Output: 7

Explanation:

Choose subsequences:

First subsequence [5], whose XOR is 5.

Second subsequence [2], whose XOR is 2.

Then, XOR of both subsequences = 5 XOR 2 = 7.

This is the maximum XOR value achievable from any two subsequences.



Constraints:

2 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""

from typing import List


class XorBasis:
    def __init__(self, n: int):
        self.b = [0] * n

    def insert(self, x: int):
        b = self.b

        for i in range(len(b) - 1, -1, -1):
            if x & (1 << i):
                if b[i] == 0:
                    b[i] = x
                    return
                x ^= b[i]

    def max_xor(self) -> int:
        b = self.b
        res = 0

        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        
        return res

class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = XorBasis(max(nums).bit_length())

        for x in nums:
            basis.insert(x)
        
        return basis.max_xor()


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxXorSubsequences([1, 2, 3]))  # 3

    # Example 2
    print(sol.maxXorSubsequences([5, 2]))  # 7
    