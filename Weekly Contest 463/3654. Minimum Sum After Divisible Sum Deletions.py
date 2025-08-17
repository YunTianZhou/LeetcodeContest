"""
3654. Minimum Sum After Divisible Sum Deletions - Medium


You are given an integer array nums and an integer k.

You may repeatedly choose any contiguous subarray of nums whose sum is divisible by k and delete it; after each deletion, the remaining elements close the gap.

Return the minimum possible sum of nums after performing any number of such deletions.



Example 1:

Input: nums = [1,1,1], k = 2

Output: 1

Explanation:

Delete the subarray nums[0..1] = [1, 1], whose sum is 2 (divisible by 2), leaving [1].



Example 2:

Input: nums = [3,1,4,1,5], k = 3

Output: 5

Explanation:

First, delete nums[1..3] = [1, 4, 1], whose sum is 6 (divisible by 3), leaving [3, 5].

Then, delete nums[0..0] = [3], whose sum is 3 (divisible by 3), leaving [5].

The remaining sum is 5.
 


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5
"""

from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        ps = [0] * (n + 1)
        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] = nums[i] + ps[i - 1]
        
        last = [-2] * k
        last[0] = -1
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i] = dp[i - 1]
            j = last[ps[i] % k]
            if j != -2:
                dp[i] = max(dp[i], ps[i] - ps[j] + dp[j])
            last[ps[i] % k] = i

        return sum(nums) - dp[n - 1]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minArraySum([1, 1, 1], 2))  # 1

    # Example 2
    print(sol.minArraySum([3, 1, 4, 1, 5], 3))  # 5
    