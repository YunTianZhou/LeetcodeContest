"""
4094. Count Frequency Staircase Subarrays I - Medium


You are given an integer array nums.

Consider the distinct values of a subarray in the order in which they first appear.

If there are k distinct values, the subarray is called a frequency staircase if the first distinct value occurs exactly once, the second distinct value occurs exactly twice, and so on, with the kth distinct value occurring exactly k times.

Equivalently, the frequencies of the distinct values, in the order of their first occurrence, must be exactly 1, 2, 3, ..., k.

Return the number of frequency staircase subarrays in nums.

A subarray is a contiguous non-empty sequence of elements within an array.

The frequency of a value in a subarray is the number of times it occurs in that subarray.



Example 1:

Input: nums = [5,8,8,2,2,2]

Output: 9

Explanation:

Every single-element subarray has frequencies [1], and there are 6 of them. 3 longer subarrays also qualify:

Subarray                             Values by first appearance    Frequencies
nums[0...2] = [5, 8, 8]             5, then 8                     [1, 2]
nums[2...4] = [8, 2, 2]             8, then 2                     [1, 2]
nums[0...5] = [5, 8, 8, 2, 2, 2]   5, then 8, then 2             [1, 2, 3]

So the answer is 6 + 3 = 9.


Example 2:

Input: nums = [6,6,9,9]

Output: 5

Explanation:

Every single-element subarray has frequencies [1], and there are 4 of them. 1 longer subarray also qualifies:

Subarray                   Values by first appearance    Frequencies
nums[1...3] = [6, 9, 9]   6, then 9                     [1, 2]

So the answer is 4 + 1 = 5.


Example 3:

Input: nums = [2,3,4,4,3,4]

Output: 8

Explanation:

Every single-element subarray has frequencies [1], and there are 6 of them. 2 longer subarrays also qualify:

Subarray                          Values by first appearance    Frequencies
nums[1...3] = [3, 4, 4]          3, then 4                     [1, 2]
nums[0...5] = [2, 3, 4, 4, 3, 4] 2, then 3, then 4             [1, 2, 3]

So the answer is 6 + 2 = 8.



Constraints:

1 <= nums.length <= 1500
1 <= nums[i] <= 10^5
"""


class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            vis = set()
            missing = {}
            need = 0

            for j in range(i, n):
                x = nums[j]

                if x not in vis:
                    vis.add(x)
                    missing[x] = len(vis)
                    need += len(vis)
                
                if x in missing and need <= n - j:
                    missing[x] -= 1
                    need -= 1
                    if missing[x] == 0:
                        del missing[x]
                else:
                    break
                
                if not missing:
                    ans += 1
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countStaircase([5, 8, 8, 2, 2, 2]))  # 9

    # Example 2
    print(sol.countStaircase([6, 6, 9, 9]))  # 5

    # Example 3
    print(sol.countStaircase([2, 3, 4, 4, 3, 4]))  # 8
