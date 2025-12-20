"""
3781. Maximum Score After Binary Swaps - Medium


You are given an integer array nums of length n and a binary string s of the same length.

Initially, your score is 0. Each index i where s[i] = '1' contributes nums[i] to the score.

You may perform any number of operations (including zero). In one operation, you may choose an index i such that 0 <= i < n - 1, where s[i] = '0', and s[i + 1] = '1', and swap these two characters.

Return an integer denoting the maximum possible score you can achieve.



Example 1:

Input: nums = [2,1,5,2,3], s = "01010"

Output: 7

Explanation:

We can perform the following swaps:

 - Swap at index i = 0: "01010" changes to "10010"
 - Swap at index i = 2: "10010" changes to "10100"

Positions 0 and 2 contain '1', contributing nums[0] + nums[2] = 2 + 5 = 7. This is maximum score achievable.


Example 2:

Input: nums = [4,7,2,9], s = "0000"

Output: 0

Explanation:

There are no '1' characters in s, so no swaps can be performed. The score remains 0.



Constraints:

n == nums.length == s.length
1 <= n <= 10^5
1 <= nums[i] <= 10^9
s[i] is either '0' or '1'
"""

from typing import List
from heapq import heappush, heappop


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        hp = []
        ans = 0
        
        for x, c in zip(nums, s):
            heappush(hp, -x)

            if c == "1":
                ans += -heappop(hp)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumScore([2, 1, 5, 2, 3], "01010"))  # 7

    # Example 2
    print(sol.maximumScore([4, 7, 2, 9], "0000"))  # 0
    