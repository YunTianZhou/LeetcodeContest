"""
3872. Longest Arithmetic Sequence After Changing At Most One Element - Medium


You are given an integer array nums.

A subarray is arithmetic if the difference between consecutive elements in the subarray is constant.

You can replace at most one element in nums with any integer. Then, you select an arithmetic subarray from nums.

Return an integer denoting the maximum length of the arithmetic subarray you can select.



Example 1:

Input: nums = [9,7,5,10,1]

Output: 5

Explanation:

 - Replace nums[3] = 10 with 3. The array becomes [9, 7, 5, 3, 1].

 - Select the subarray [9, 7, 5, 3, 1], which is arithmetic because consecutive elements have a common difference of -2.


Example 2:

Input: nums = [1,2,6,7]

Output: 3

Explanation:

 - Select the subarray [-2, 2, 6, 7], which is arithmetic because consecutive elements have a common difference of 4.

 - Replace nums[0] = 1 with -2. The array becomes [-2, 2, 6, 7].



Constraints:

4 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""


class Solution:
    def longestArithmetic(self, nums: list[int]) -> int:
        n = len(nums)

        def calc(nums):
            pre = [2] * n
            pre[0] = 1
            for i in range(2, n):
                if nums[i] + nums[i - 2] == nums[i - 1] * 2:
                    pre[i] = 1 + pre[i - 1]
            return pre

        pre = calc(nums)
        suf = calc(nums[::-1])[::-1]

        ans = max(pre) + 1
        if ans >= n:
            return n

        for i in range(1, n - 1):
            d = nums[i + 1] - nums[i - 1]
            left = i > 1 and (nums[i - 1] - nums[i - 2]) * 2 == d
            right = i + 2 < n and (nums[i + 2] - nums[i + 1]) * 2 == d

            if left and right:
                ans = max(ans, pre[i - 1] + suf[i + 1] + 1)
            elif left:
                ans = max(ans, pre[i - 1] + 2)
            elif right:
                ans = max(ans, suf[i + 1] + 2)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestArithmetic([9, 7, 5, 10, 1]))  # 5

    # Example 2
    print(sol.longestArithmetic([1, 2, 6, 7]))  # 3
