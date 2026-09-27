"""
4063. Longest Subarray Divisible by K with At Most One Negation I - Medium


You are given an integer array nums and an integer k.

A subarray is valid if its sum is divisible by k, or can become divisible by k by negating one element within that subarray.

Negating an element means replacing its value x with -x.

Return the length of the longest valid subarray. If no valid subarray exists, return 0.

A subarray is a contiguous, non-empty sequence of elements within an array.



Example 1:

Input: nums = [4,1,2], k = 3

Output: 3

Explanation:

The sum of the entire array is 7, and 7 % 3 = 1, so it is not divisible by k = 3.

Negating nums[2] = 2 changes the sum to 4 + 1 - 2 = 3, which is divisible by k.

Therefore, the entire array is a valid subarray, giving a length of 3.


Example 2:

Input: nums = [5,3,4], k = 7

Output: 2

Explanation:

The sum of the entire array is 12, and negating any one of its elements does not make its sum divisible by 7.

However, the subarray [3, 4] has a sum of 7, which is divisible by k = 7 without any negation.

Therefore, the longest valid subarray has a length of 2.


Example 3:

Input: nums = [2,2,5], k = 6

Output: 2

Explanation:

The sum of the entire array is 9, and negating any one of its elements does not make its sum divisible by 6.

The subarray [2, 2] has a sum of 4. Negating either element changes it to [-2, 2] or [2, -2], both of which have a sum of 0.

Therefore, the longest valid subarray has a length of 2.



Constraints:

1 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^5
"""


class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] %= k

        ans = 0
        for i in range(n):
            vis = {0}
            sm = 0
            for j in range(i, n):
                sm = (sm + nums[j]) % k
                vis.add(nums[j] * 2 % k)
                if sm in vis:
                    ans = max(ans, j - i + 1)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestSubarray([4, 1, 2], 3))  # 3

    # Example 2
    print(sol.longestSubarray([5, 3, 4], 7))  # 2

    # Example 3
    print(sol.longestSubarray([2, 2, 5], 6))  # 2
