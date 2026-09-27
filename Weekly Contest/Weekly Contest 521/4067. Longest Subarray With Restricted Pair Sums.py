"""
4067. Longest Subarray With Restricted Pair Sums - Medium


You are given an integer array nums.

A subarray nums[l..r] is valid if there are no three distinct indices i, j, and k such that l <= i, j, k <= r and:

nums[i] + nums[j] == nums[k]

Return the maximum length of a valid subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [2,3,5,3,2,1]

Output: 3

Explanation:

Consider the subarray [3, 5, 3]. The pairs of elements at distinct indices have the following sums:

3 + 5 = 8
3 + 3 = 6, using the two different occurrences of 3
5 + 3 = 8

None of these sums is an element at the remaining index, so the subarray is valid.

Every subarray of length 4 contains 2, 3, and 5 at distinct indices, where 2 + 3 = 5. Therefore, no longer valid subarray exists, and the answer is 3.


Example 2:

Input: nums = [3,4,5,6]

Output: 4

Explanation:

The sums obtained from every pair of elements at distinct indices are 7, 8, 9, 9, 10, and 11. None of these values appears at the remaining index, so the entire array is valid.



Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 500
"""

from typing import List


class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        cnt = {}

        def can_add(x):
            for y, c in cnt.items():
                if x + y in cnt or cnt.get(x - y, 0) > (x - y == y):
                    return False
            return True

        ans = j = 0
        for i, x in enumerate(nums):
            while not can_add(x):
                cnt[nums[j]] -= 1
                if cnt[nums[j]] == 0:
                    del cnt[nums[j]]
                j += 1
            
            cnt[x] = cnt.get(x, 0) + 1
            ans = max(ans, i - j + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxSubarray([2, 3, 5, 3, 2, 1]))  # 3

    # Example 2
    print(sol.maxSubarray([3, 4, 5, 6]))  # 4
