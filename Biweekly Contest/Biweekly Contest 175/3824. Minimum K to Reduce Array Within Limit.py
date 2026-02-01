"""
3824. Minimum K to Reduce Array Within Limit - Medium


You are given a positive integer array nums.

For a positive integer k, define nonPositive(nums, k) as the minimum number of operations needed to make every element of nums non-positive. In one operation, you can choose an index i and reduce nums[i] by k.

Return an integer denoting the minimum value of k such that nonPositive(nums, k) <= k^2.



Example 1:

Input: nums = [3,7,5]

Output: 3

Explanation:

When k = 3, nonPositive(nums, k) = 6 <= k2.

 - Reduce nums[0] = 3 one time. nums[0] becomes 3 - 3 = 0.
 - Reduce nums[1] = 7 three times. nums[1] becomes 7 - 3 - 3 - 3 = -2.
 - Reduce nums[2] = 5 two times. nums[2] becomes 5 - 3 - 3 = -1.


Example 2:

Input: nums = [1]

Output: 1

Explanation:

When k = 1, nonPositive(nums, k) = 1 <= k2.

 - Reduce nums[0] = 1 one time. nums[0] becomes 1 - 1 = 0.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        n = len(nums)

        base = int(sum(nums) ** (1 / 3))
        l = base
        r = base + n
        while l < r:
            k = (l + r) // 2
            op = sum((x + k - 1) // k for x in nums)
            
            if op <= k * k:
                r = k
            else:
                l = k + 1

        return r


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minimumK([3, 7, 5]))  # 3

    # Example 2
    print(sol.minimumK([1]))  # 1
