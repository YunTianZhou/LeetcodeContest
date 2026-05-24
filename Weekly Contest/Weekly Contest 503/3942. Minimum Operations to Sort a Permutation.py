"""
3942. Minimum Operations to Sort a Permutation - Medium


You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:

 - Reverse the entire array.

 - Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.



Example 1:

Input: nums = [0,2,1]

Output: 2

Explanation:

 - Rotate Left by one: [2, 1, 0]
 - Reverse the array: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal.


Example 2:

Input: nums = [1,0,2]

Output: 2

Explanation:

 - Reverse the array: [2, 0, 1]
 - Rotate Left by one: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal.


Example 3:

Input: nums = [2,0,1,3]

Output: -1

Explanation:

It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.



Constraints:

1 <= n == nums.length <= 10^5
0 <= nums[i] <= n - 1
nums is a permutation of integers from 0 to n - 1.
"""

from math import inf


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        def solve(nums, rotated=False):
            dec = 0
            for i in range(1, n):
                if nums[i] < nums[i - 1]:
                    if dec != 0 or nums[-1] > nums[0]:
                        return inf
                    dec = i
            return min(dec, (n - dec) % n + (0 if rotated else 2))

        ans = min(solve(nums), solve(nums[::-1], True) + 1)
        return -1 if ans == inf else ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations([0, 2, 1]))  # 2

    # Example 2
    print(sol.minOperations([1, 0, 2]))  # 2

    # Example 3
    print(sol.minOperations([2, 0, 1, 3]))  # -1
