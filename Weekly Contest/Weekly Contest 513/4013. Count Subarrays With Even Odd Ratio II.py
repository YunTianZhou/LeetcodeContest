"""
4013. Count Subarrays With Even Odd Ratio II - Hard


You are given an integer array nums and two integers a and b.

For a subarray, let:

 - x be the number of even elements.

 - y be the number of odd elements.

The ratio of even to odd elements in a subarray is defined as x / y, where ratios are compared by their exact rational values.

A subarray is considered valid if:

 - y > 0, and

 - x / y <= a / b.

Return the number of valid subarrays in nums.



Example 1:

Input: nums = [1,2,1,2], a = 3, b = 2

Output: 7

Explanation:

The following are the valid subarrays:

Subarray    Values        Even Count  Odd Count  Ratio
nums[0..0]  [1]           0           1          0 / 1
nums[0..1]  [1, 2]        1           1          1 / 1
nums[0..2]  [1, 2, 1]     1           2          1 / 2
nums[0..3]  [1, 2, 1, 2]  2           2          2 / 2
nums[1..2]  [2, 1]        1           1          1 / 1
nums[2..2]  [1]           0           1          0 / 1
nums[2..3]  [1, 2]        1           1          1 / 1

Thus, the number of valid subarrays is 7.


Example 2:

Input: nums = [2,2,1], a = 2, b = 1

Output: 3

Explanation:

The following are the valid subarrays:

Subarray    Values     Even Count  Odd Count  Ratio
nums[0..2]  [2, 2, 1]  2           1          2 / 1
nums[1..2]  [2, 1]     1           1          1 / 1
nums[2..2]  [1]        0           1          0 / 1

Thus, the number of valid subarrays is 3.


Example 3:

Input: nums = [2,2,2], a = 1, b = 1

Output: 0

Explanation:

Every subarray contains 0 odd numbers, so no subarray is valid.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= a, b <= 10^9
"""

from itertools import accumulate


class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        pref = list(accumulate((-b if x % 2 == 0 else a for x in nums), initial=0))

        def merge_sort(nums: list[int]) -> int:
            n = len(nums)

            if n <= 16:
                cnt = 0

                for i in range(n):
                    for j in range(i, 0, -1):
                        if nums[j] >= nums[j - 1]:
                            cnt += j
                            break
                        nums[j], nums[j - 1] = nums[j - 1], nums[j]
                
                return cnt

            half = n // 2
            left = nums[:half]
            right = nums[half:]
            cnt = merge_sort(left) + merge_sort(right)

            l = r = 0
            for i in range(n):
                if l < half and (r >= n - half or left[l] <= right[r]):
                    nums[i] = left[l]
                    l += 1
                else:
                    cnt += l
                    nums[i] = right[r]
                    r += 1
            
            return cnt
        
        return merge_sort(pref)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countRatioSubarrays([1, 2, 1, 2], 3, 2))  # 7

    # Example 2
    print(sol.countRatioSubarrays([2, 2, 1], 2, 1))  # 3

    # Example 3
    print(sol.countRatioSubarrays([2, 2, 2], 1, 1))  # 0
