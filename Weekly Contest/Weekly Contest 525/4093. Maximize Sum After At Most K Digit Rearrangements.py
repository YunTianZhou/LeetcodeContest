"""
4093. Maximize Sum After At Most K Digit Rearrangements - Medium


You are given an integer array nums of length n and an integer k.

In one operation, you may choose any element of nums and rearrange its decimal digits in any order to form a new integer.

Return the maximum possible sum of the array after performing at most k operations.



Example 1:

Input: nums = [123,45], k = 1

Output: 366

Explanation:

We choose nums[0] = 123 and rearrange its digits to form 321.

The array becomes [321, 45]. Thus, the total sum is 321 + 45 = 366.


Example 2:

Input: nums = [102,90,14], k = 2

Output: 341

Explanation:

We choose nums[0] = 102 and rearrange its digits to form 210.

We choose nums[2] = 14 and rearrange its digits to form 41.

The array becomes [210, 90, 41]. Thus, the total sum is 210 + 90 + 41 = 341.



Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= n
"""


class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        diff = [int("".join(sorted(str(x), reverse=True))) - x for x in nums]
        diff.sort(reverse=True)
        return sum(nums) + sum(diff[:k])


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximizeSum([123, 45], 1))  # 366

    # Example 2
    print(sol.maximizeSum([102, 90, 14], 2))  # 341
