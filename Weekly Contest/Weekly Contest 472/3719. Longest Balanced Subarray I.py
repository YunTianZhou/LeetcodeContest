"""
3719. Longest Balanced Subarray I - Medium


You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.



Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].

It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.


Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].

It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.


Example 3:

Input: nums = [1,2,3,2]

Output: 3

Explanation:

The longest balanced subarray is [2, 3, 2].

It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.



Constraints:

1 <= nums.length <= 1500
1 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            odd = set()
            even = set()
            
            for j in range(i, n):
                if nums[j] % 2:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])

                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestBalanced([2, 5, 4, 3]))  # 4

    # Example 2
    print(sol.longestBalanced([3, 2, 2, 5, 4]))  # 5

    # Example 3
    print(sol.longestBalanced([1, 2, 3, 2]))  # 3
