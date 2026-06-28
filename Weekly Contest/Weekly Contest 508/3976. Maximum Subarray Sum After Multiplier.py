"""
3976. Maximum Subarray Sum After Multiplier - Medium


You are given an integer array nums and a positive integer k.

You must choose exactly one subarray of nums and perform exactly one of the following operations:

 - Multiply each number in the chosen subarray by k.

 - Divide each number in the chosen subarray by k.

    - When dividing a positive number by k, use the floor value of the division result.

    - When dividing a negative number by k, use the ceiling value of the division result.

Return the maximum possible sum of a non-empty subarray in the resulting array.

Note that the subarray chosen for the operation and the subarray chosen for the sum may be different.



Example 1:

Input: nums = [1,-2,3,4,-5], k = 2

Output: 14

Explanation:

 - Multiply each number in the subarray [3, 4] by 2.

 - This results in nums = [1, -2, 6, 8, -5].

 - The subarray with the largest sum is [6, 8], so the output is 6 + 8 = 14.


Example 2:

Input: nums = [-5,-4,-3], k = 2

Output: -1

Explanation:

 - Divide each number in the subarray [-3] by 2.

 - This results in nums = [-5, -4, -1].

 - The subarray with the largest sum is [-1], so the output is -1.



Constraints:

1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^5
"""

from math import inf


class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        def get(is_mul):
            dp0 = dp1 = dp2 = ans = -inf

            for x in nums:
                if is_mul == 0:
                    val = x * k
                else:
                    val = x // k if x > 0 else (x + k - 1) // k

                dp0, dp1, dp2 = (
                    max(x, dp0 + x),
                    max(val, dp0 + val, dp1 + val),
                    max(dp2 + x, dp1 + x)
                )
                
                ans = max(ans, dp0, dp1, dp2)

            return ans

        return max(get(True), get(False))


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxSubarraySum([1, -2, 3, 4, -5], 2))  # 14

    # Example 2
    print(sol.maxSubarraySum([-5, -4, -3], 2))  # -1
