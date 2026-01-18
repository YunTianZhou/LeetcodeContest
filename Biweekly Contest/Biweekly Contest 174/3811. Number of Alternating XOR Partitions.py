"""
3811. Number of Alternating XOR Partitions - Medium


You are given an integer array nums and two distinct integers target1 and target2.

A partition of nums splits it into one or more contiguous, non-empty blocks that cover the entire array without overlap.

A partition is valid if the bitwise XOR of elements in its blocks alternates between target1 and target2, starting with target1.

Formally, for blocks b1, b2, …:

 - XOR(b1) = target1

 - XOR(b2) = target2 (if it exists)

 - XOR(b3) = target1, and so on.

Return the number of valid partitions of nums, modulo 109 + 7.

Note: A single block is valid if its XOR equals target1.



Example 1:

Input: nums = [2,3,1,4], target1 = 1, target2 = 5

Output: 1

Explanation:

 - The XOR of [2, 3] is 1, which matches target1.

 - The XOR of the remaining block [1, 4] is 5, which matches target2.

 - This is the only valid alternating partition, so the answer is 1.


Example 2:

Input: nums = [1,0,0], target1 = 1, target2 = 0

Output: 3

Explanation:

 - The XOR of [1, 0, 0] is 1, which matches target1.

 - The XOR of [1] and [0, 0] are 1 and 0, matching target1 and target2.

 - The XOR of [1, 0] and [0] are 1 and 0, matching target1 and target2.

 - Thus, the answer is 3.


Example 3:

Input: nums = [7], target1 = 1, target2 = 7

Output: 0

Explanation:

 - The XOR of [7] is 7, which does not match target1, so no valid partition exists.



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i], target1, target2 <= 10^5
target1 != target2
"""

from typing import List
from collections import defaultdict


class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod = 10 ** 9 + 7
        
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        cnt1[0] += 1

        xor_sm = 0
        for x in nums:
            xor_sm ^= x
            curr1 = cnt1[xor_sm ^ target1]
            curr2 = cnt2[xor_sm ^ target2]
            cnt1[xor_sm] = (cnt1[xor_sm] + curr2) % mod
            cnt2[xor_sm] = (cnt2[xor_sm] + curr1) % mod

        return (curr1 + curr2) % mod
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.alternatingXOR([2, 3, 1, 4], 1, 5))  # 1

    # Example 2
    print(sol.alternatingXOR([1, 0, 0], 1, 0))  # 3

    # Example 3
    print(sol.alternatingXOR([7], 1, 7))  # 0
    