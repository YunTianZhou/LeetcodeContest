"""
3574. Maximize Subarray GCD Score - Hard


You are given an array of positive integers nums and an integer k.

You may perform at most k operations. In each operation, you can choose one element in the array and double its value. Each element can be doubled at most once.

The score of a contiguous subarray is defined as the product of its length and the greatest common divisor (GCD) of all its elements.

Your task is to return the maximum score that can be achieved by selecting a contiguous subarray from the modified array.

Note:

A subarray is a contiguous sequence of elements within an array.
The greatest common divisor (GCD) of an array is the largest integer that evenly divides all the array elements.
 


Example 1:

Input: nums = [2,4], k = 1

Output: 8

Explanation:

Double nums[0] to 4 using one operation. The modified array becomes [4, 4].
The GCD of the subarray [4, 4] is 4, and the length is 2.
Thus, the maximum possible score is 2 x 4 = 8.


Example 2:

Input: nums = [3,5,7], k = 2

Output: 14

Explanation:

Double nums[2] to 14 using one operation. The modified array becomes [3, 5, 14].
The GCD of the subarray [14] is 14, and the length is 1.
Thus, the maximum possible score is 1 x 14 = 14.


Example 3:

Input: nums = [5,5,5], k = 1

Output: 15

Explanation:

The subarray [5, 5, 5] has a GCD of 5, and its length is 3.
Since doubling any element doesn't improve the score, the maximum score is 3 x 5 = 15.
 


Constraints:

1 <= n == nums.length <= 1500
1 <= nums[i] <= 10^9
1 <= k <= n
"""

from typing import List
from math import gcd


class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        factor2 = [0] * n
        for i, x in enumerate(nums):
            while (x & 1) == 0:
                x >>= 1
                factor2[i] += 1
        
        ans = 0
        for i in range(n):
            mini = 64
            cnt = 0
            value = nums[i] * 2

            for j in range(i, n):
                if factor2[j] < mini:
                    mini = factor2[j]
                    cnt = 1
                elif factor2[j] == mini:
                    cnt += 1
                
                value = gcd(value, nums[j] * (2 if cnt <= k else 1))
                ans = max(ans, (j - i + 1) * value)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxGCDScore([2, 4], 1))  # 8

    # Example 2
    print(sol.maxGCDScore([3, 5, 7], 2))  # 14

    # Example 3
    print(sol.maxGCDScore([5, 5, 5], 1))  # 15
