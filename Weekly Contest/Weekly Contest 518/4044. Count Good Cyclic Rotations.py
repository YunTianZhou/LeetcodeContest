"""
4044. Count Good Cyclic Rotations - Medium


You are given an integer array nums of even length n.

A cyclic rotation of nums is obtained by choosing a prefix of nums whose length is between 0 and n - 1 (inclusive), and moving it to the end of the array while preserving the order of all elements.

A cyclic rotation is good if the sum of its first n / 2 elements is strictly greater than the sum of its last n / 2 elements.

Return the number of cyclic rotations of nums that are good.



Example 1:

Input: nums = [1,2,3,4,5,6]

Output: 3

Explanation:

The cyclic rotations of nums are:

Cyclic rotation     Sum of first n / 2 elements  Sum of last n / 2 elements
[1, 2, 3, 4, 5, 6]  1 + 2 + 3 = 6                4 + 5 + 6 = 15
[2, 3, 4, 5, 6, 1]  2 + 3 + 4 = 9                5 + 6 + 1 = 12
[3, 4, 5, 6, 1, 2]  3 + 4 + 5 = 12               6 + 1 + 2 = 9
[4, 5, 6, 1, 2, 3]  4 + 5 + 6 = 15               1 + 2 + 3 = 6
[5, 6, 1, 2, 3, 4]  5 + 6 + 1 = 12               2 + 3 + 4 = 9
[6, 1, 2, 3, 4, 5]  6 + 1 + 2 = 9                3 + 4 + 5 = 12

The first half has a greater sum than the second half for 3 rotations. Thus, the answer is 3.


Example 2:

Input: nums = [1,2,1,2]

Output: 0

Explanation:

The cyclic rotations of nums are:

Cyclic rotation  Sum of first n / 2 elements  Sum of last n / 2 elements
[1, 2, 1, 2]     1 + 2 = 3                    1 + 2 = 3
[2, 1, 2, 1]     2 + 1 = 3                    2 + 1 = 3
[1, 2, 1, 2]     1 + 2 = 3                    1 + 2 = 3
[2, 1, 2, 1]     2 + 1 = 3                    2 + 1 = 3

No cyclic rotation is good because the two sums are equal for every rotation. Thus, the answer is 0.



Constraints:

2 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^9
n is even.
"""


class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        h = n // 2

        tot = sum(nums)
        if tot % 2:
            return h

        sm = sum(nums[: h])
        ans = 0
        for i in range(h):
            if sm * 2 != tot:
                ans += 1
            sm += nums[i + h] - nums[i]
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countGoodRotations([1, 2, 3, 4, 5, 6]))  # 3

    # Example 2
    print(sol.countGoodRotations([1, 2, 1, 2]))  # 0
