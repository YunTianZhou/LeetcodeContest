"""
4058. Maximum Pulse Value After One Subarray Rotation - Medium


You are given an integer array nums of length n.

Define the pulse value of an integer array arr as the alternating sum starting at index 0: pulse(arr) = arr[0] - arr[1] + arr[2] - arr[3] + ....

You may perform at most one operation on nums:

 - Choose two indices l and r such that 0 <= l < r < n.

 - Left-rotate the subarray nums[l..r] by exactly one position. For example, [a, b, c, d] becomes [b, c, d, a].

Return the maximum pulse value that can be obtained after performing at most one such operation.



Example 1:

Input: nums = [1,5,2]

Output: 6

Explanation:

 - The original pulse value is 1 - 5 + 2 = -2.

 - Rotate the subarray nums[0..1] from [1, 5] to [5, 1].

 - The resulting array is [5, 1, 2] and its pulse value is 5 - 1 + 2 = 6, which is the maximum possible.


Example 2:

Input: nums = [6,4,3]

Output: 7

Explanation:

 - The original pulse value is 6 - 4 + 3 = 5.

 - Rotate the subarray nums[1..2] from [4, 3] to [3, 4].

 - The resulting array is [6, 3, 4] and its pulse value is 6 - 3 + 4 = 7, which is the maximum possible.


Example 3:

Input: nums = [9,7]

Output: 2

Explanation:

The original pulse value is 9 - 7 = 2, which is already maximum. Thus, no rotation is required.



Constraints:

1 <= n == nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from math import inf
from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> int:
        mx = [-inf, 0]
        
        ans = s = 0
        for i, x in enumerate(nums):
            p = i % 2
            s += x if p == 0 else -x
            
            if s > mx[p]:
                mx[p] = s
            else:
                ans = max(ans, mx[p] - s)

        return s + ans * 2


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxValue([1, 5, 2]))  # 6

    # Example 2
    print(sol.maxValue([6, 4, 3]))  # 7

    # Example 3
    print(sol.maxValue([9, 7]))  # 2
