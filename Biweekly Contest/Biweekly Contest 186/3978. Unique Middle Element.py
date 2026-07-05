"""
3978. Unique Middle Element - Easy


You are given an integer array nums of odd length n.

Return true if the middle element of nums appears exactly once in the array. Otherwise return false.



Example 1:

Input: nums = [1,2,3]

Output: true

Explanation:

The middle element of nums is 2, which appears exactly once.

Thus, the answer is true.


Example 2:

Input: nums = [1,2,2]

Output: false

Explanation:

The middle element of nums is 2, which appears twice.

Thus, the answer is false.



Constraints:

1 <= n == nums.length <= 100
n is odd.
1 <= nums[i] <= 100
"""


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        return nums.count(nums[n // 2]) == 1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.isMiddleElementUnique([1, 2, 3]))  # True

    # Example 2
    print(sol.isMiddleElementUnique([1, 2, 2]))  # False
