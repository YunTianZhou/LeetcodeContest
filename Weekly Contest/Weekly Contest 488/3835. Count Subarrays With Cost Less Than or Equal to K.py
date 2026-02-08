"""
3835. Count Subarrays With Cost Less Than or Equal to K - Medium


You are given an integer array nums, and an integer k.

For any subarray nums[l..r], define its cost as:

cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1).

Return an integer denoting the number of subarrays of nums whose cost is less than or equal to k.



Example 1:

Input: nums = [1,3,2], k = 4

Output: 5

Explanation:

We consider all subarrays of nums:

 - nums[0..0]: cost = (1 - 1) * 1 = 0
 - nums[0..1]: cost = (3 - 1) * 2 = 4
 - nums[0..2]: cost = (3 - 1) * 3 = 6
 - nums[1..1]: cost = (3 - 3) * 1 = 0
 - nums[1..2]: cost = (3 - 2) * 2 = 2
 - nums[2..2]: cost = (2 - 2) * 1 = 0

There are 5 subarrays whose cost is less than or equal to 4.


Example 2:

Input: nums = [5,5,5,5], k = 0

Output: 10

Explanation:

For any subarray of nums, the maximum and minimum values are the same, so the cost is always 0.

As a result, every subarray of nums has cost less than or equal to 0.

For an array of length 4, the total number of subarrays is (4 * 5) / 2 = 10.


Example 3:

Input: nums = [1,2,3], k = 0

Output: 3

Explanation:

The only subarrays of nums with cost 0 are the single-element subarrays, and there are 3 of them.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= k <= 10^15
"""

from typing import List
from collections import deque


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = deque()
        mn = deque()
        ans = j = 0
        for i, x in enumerate(nums):
            while mx and x >= nums[mx[-1]]:
                mx.pop()
            mx.append(i)
            
            while mn and x <= nums[mn[-1]]:
                mn.pop()
            mn.append(i)

            while (nums[mx[0]] - nums[mn[0]]) * (i - j + 1) > k:
                if mx[0] == j:
                    mx.popleft()
                if mn[0] == j:
                    mn.popleft()
                j += 1

            ans += i - j + 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countSubarrays([1, 3, 2], 4))  # 5

    # Example 2
    print(sol.countSubarrays([5, 5, 5, 5], 0))  # 10

    # Example 3
    print(sol.countSubarrays([1, 2, 3], 0))  # 3
    