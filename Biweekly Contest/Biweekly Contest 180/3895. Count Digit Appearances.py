"""
3895. Count Digit Appearances - Medium


You are given an integer array nums and an integer digit.

Return the total number of times digit appears in the decimal representation of all elements in nums.



Example 1:

Input: nums = [12,54,32,22], digit = 2

Output: 4

Explanation:

The digit 2 appears once in 12 and 32, and twice in 22. Thus, the total number of times digit 2 appears is 4.


Example 2:

Input: nums = [1,34,7], digit = 9

Output: 0

Explanation:

The digit 9 does not appear in the decimal representation of any element in nums, so the total number of times digit 9 appears is 0.



Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^6
0 <= digit <= 9
"""


class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return sum(str(x).count(str(digit)) for x in nums)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countDigitOccurrences([12, 54, 32, 22], 2))  # 4

    # Example 2
    print(sol.countDigitOccurrences([1, 34, 7], 9))  # 0
