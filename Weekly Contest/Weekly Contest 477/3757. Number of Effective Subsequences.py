"""
3757. Number of Effective Subsequences - Hard


You are given an integer array nums.

The strength of the array is defined as the bitwise OR of all its elements.

A subsequence is considered effective if removing that subsequence strictly decreases the strength of the remaining elements.

Return the number of effective subsequences in nums. Since the answer may be large, return it modulo 10^9 + 7.

The bitwise OR of an empty array is 0.



Example 1:

Input: nums = [1,2,3]

Output: 3

Explanation:

- The Bitwise OR of the array is 1 OR 2 OR 3 = 3.
    - Subsequences that are effective are:
    - [1, 3]: The remaining element [2] has a Bitwise OR of 2.
    - [2, 3]: The remaining element [1] has a Bitwise OR of 1.
    - [1, 2, 3]: The remaining elements [] have a Bitwise OR of 0.
 - Thus, the total number of effective subsequences is 3.


Example 2:

Input: nums = [7,4,6]

Output: 4

Explanation:

 - The Bitwise OR of the array is 7 OR 4 OR 6 = 7.
 - Subsequences that are effective are:
    - [7]: The remaining elements [4, 6] have a Bitwise OR of 6.
    - [7, 4]: The remaining element [6] has a Bitwise OR of 6.
    - 7, 6]: The remaining element [4] has a Bitwise OR of 4.
    - 7, 4, 6]: The remaining elements [] have a Bitwise OR of 0.
 - Thus, the total number of effective subsequences is 4.


Example 3:

Input: nums = [8,8]

Output: 1

Explanation:

 - The Bitwise OR of the array is 8 OR 8 = 8.
 - Only the subsequence [8, 8] is effective since removing it leaves [] which has a Bitwise OR of 0.
 - Thus, the total number of effective subsequences is 1.


Example 4:

Input: nums = [2,2,1]

Output: 5

Explanation:

 - The Bitwise OR of the array is 2 OR 2 OR 1 = 3.
    - Subsequences that are effective are:
    - [1]: The remaining elements [2, 2] have a Bitwise OR of 2.
    - [2, 1] (using nums[0], nums[2]): The remaining element [2] has a Bitwise OR of 2.
    - [2, 1] (using nums[1], nums[2]): The remaining element [2] has a Bitwise OR of 2.
    - [2, 2]: The remaining element [1] has a Bitwise OR of 1.
    - [2, 2, 1]: The remaining elements [] have a Bitwise OR of 0.
 - Thus, the total number of effective subsequences is 5.

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""

from typing import List
from functools import reduce
from operator import or_


m = 10 ** 5
mod = 10 ** 9 + 7

pow2 = [0] * (m + 1)
pow2[0] = 1
for i in range(m):
    pow2[i + 1] = pow2[i] * 2 % mod

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        or_all = reduce(or_, nums)
        m = or_all.bit_length()
        u = 1 << m

        dp = [0] * u
        for x in nums:
            dp[x] += 1
        for i in range(m):
            b = 1 << i
            x = 0
            while x < u:
                x |= b
                dp[x] += dp[x ^ b]
                x += 1

        ans = pow2[len(nums)]
        x = or_all
        while True:
            p = pow2[dp[x]]
            ans -= -p if (or_all ^ x).bit_count() % 2 else p
            x = (x - 1) & or_all
            if x == or_all:
                break
        
        return ans % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countEffective([1, 2, 3]))  # 3

    # Example 2
    print(sol.countEffective([7, 4, 6]))  # 4

    # Example 3
    print(sol.countEffective([8, 8]))  # 1

    # Example 4
    print(sol.countEffective([2, 2, 1]))  # 5
    