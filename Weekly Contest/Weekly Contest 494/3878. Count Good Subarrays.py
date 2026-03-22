"""
3878. Count Good Subarrays - Hard


You are given an integer array nums.

A subarray is called good if the bitwise OR of all its elements is equal to at least one element present in that subarray.

Return the number of good subarrays in nums.

Here, the bitwise OR of two integers a and b is denoted by a | b.



Example 1:

Input: nums = [4,2,3]

Output: 4

Explanation:

The subarrays of nums are:

Subarray   Bitwise OR     Present in Subarray
[4]        4 = 4          Yes
[2]        2 = 2          Yes
[3]        3 = 3          Yes
[4, 2]     4 | 2 = 6      No
[2, 3]     2 | 3 = 3      Yes
[4, 2, 3]  4 | 2 | 3 = 7  No

Thus, the good subarrays of nums are [4], [2], [3] and [2, 3]. Thus, the answer is 4.


Example 2:

Input: nums = [1,3,1]

Output: 6

Explanation:

Any subarray of nums containing 3 has bitwise OR equal to 3, and subarrays containing only 1 have bitwise OR equal to 1.

In both cases, the result is present in the subarray, so all subarrays are good, and the answer is 6.



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""


class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        or_sums = []
        last = {}

        ans = 0
        for i, x in enumerate(nums):
            for p in or_sums:
                p[0] |= x
            or_sums.append([x, i])

            idx = 1
            for j in range(1, len(or_sums)):
                if or_sums[j][0] != or_sums[j - 1][0]:
                    or_sums[idx] = or_sums[j]
                    idx += 1
            del or_sums[idx:]

            last[x] = i
            for j, (sm, start) in enumerate(or_sums):
                end = or_sums[j + 1][1] - 1 if j + 1 < len(or_sums) else i
                end = min(end, last.get(sm, -1))
                ans += max(0, end - start + 1)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countGoodSubarrays([4, 2, 3]))  # 4

    # Example 2
    print(sol.countGoodSubarrays([1, 3, 1]))  # 6
