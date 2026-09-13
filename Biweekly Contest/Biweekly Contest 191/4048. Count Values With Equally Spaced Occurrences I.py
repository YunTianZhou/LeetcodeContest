"""
4048. Count Values With Equally Spaced Occurrences I - Easy


You are given an integer array nums.

An integer x is called special if:

 - x appears exactly three times in nums.

 - All three occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at indices i1 < i2 < i3, then i2 - i1 = i3 - i2.

Return the number of distinct special integers in nums.



Example 1:

Input: nums = [1,8,1,5,1,5,8,5]

Output: 2

Explanation:

 - 1 is special because it occurs exactly three times at equally spaced indices 0, 2, and 4.

 - 5 is special because it occurs exactly three times at equally spaced indices 3, 5, and 7.

 - 8 is not special because it occurs only twice.

Therefore, the answer is 2.


Example 2:

Input: nums = [8,8,8,8]

Output: 0

Explanation:

8 is not special because it does not occur exactly three times. Therefore, the answer is 0.


Example 3:

Input: nums = [8,6,6,8,8]

Output: 0

Explanation:

8 occurs at indices 0, 3, and 4, which are not equally spaced. 6 occurs only twice. Therefore, no integer is special.



Constraints:

3 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ans = 0

        for x in set(nums):
            if nums.count(x) != 3:
                continue
            
            i1 = nums.index(x)
            i2 = nums.index(x, i1 + 1)
            i3 = nums.index(x, i2 + 1)
            
            if i2 - i1 == i3 - i2:
                ans += 1
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countSpecialIntegers([1, 8, 1, 5, 1, 5, 8, 5]))  # 2

    # Example 2
    print(sol.countSpecialIntegers([8, 8, 8, 8]))  # 0

    # Example 3
    print(sol.countSpecialIntegers([8, 6, 6, 8, 8]))  # 0
