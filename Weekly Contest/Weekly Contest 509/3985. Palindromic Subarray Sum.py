"""
3985. Palindromic Subarray Sum - Hard


You are given an integer array nums.

Return the maximum possible sum of a subarray of nums that is a palindrome.



Example 1:

Input: nums = [10,10]

Output: 20

Explanation:

The whole array [10,10] is a palindrome. Therefore, the maximum sum is 10 + 10 = 20.


Example 2:

Input: nums = [1,2,3,2,1,5,6]

Output: 9

Explanation:

The contiguous subarray [1,2,3,2,1] is a palindrome. Its sum is 1 + 2 + 3 + 2 + 1 = 9 and it is the maximum sum.


Example 3:

Input: nums = [7,1,2,1,7,3,4,3,4]

Output: 18

Explanation:

The contiguous subarray [7,1,2,1,7] is a palindrome. Its sum is 7 + 1 + 2 + 1 + 7 = 18 and it is the maximum sum.


Example 4:

Input: nums = [1,2,3,4,5]

Output: 5

Explanation:

No subarray with length greater than 1 is a palindrome. The largest element in the array is 5. Therefore, the answer is 5.

Example 5:

Input: nums = [1000]

Output: 1000

Explanation:

The subarray with only one element is a palindrome. Therefore, the answer is 1000.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from itertools import accumulate


class Solution:
    def getSum(self, nums: list[int]) -> int:
        n = len(nums)
        
        ps = list(accumulate(nums, initial=0))
        p = [0] * (n * 2 - 1)
        
        ans = center = right = 0
        for i in range(n * 2 - 1):
            l = i // 2
            r = (i + 1) // 2

            if nums[l] != nums[r]:
                continue
            
            if right > r:
                p[i] = min(right - r - 1, p[center - (i - center)])
                
            l -= p[i] + 1
            r += p[i] + 1

            while l >= 0 and r < n and nums[l] == nums[r]:
                p[i] += 1
                l -= 1
                r += 1

            ans = max(ans, ps[r] - ps[l + 1])

            if r > right:
                right = r
                center = i

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.getSum([10, 10]))  # 20

    # Example 2
    print(sol.getSum([1, 2, 3, 2, 1, 5, 6]))  # 9

    # Example 3
    print(sol.getSum([7, 1, 2, 1, 7, 3, 4, 3, 4]))  # 18

    # Example 4
    print(sol.getSum([1, 2, 3, 4, 5]))  # 5

    # Example 5
    print(sol.getSum([1000]))  # 1000
