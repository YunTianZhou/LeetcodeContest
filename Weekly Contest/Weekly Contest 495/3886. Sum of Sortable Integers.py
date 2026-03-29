"""
3886. Sum of Sortable Integers - Hard


You are given an integer array nums of length n.

An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

 - Partition nums into consecutive subarrays of length k.

 - Cyclically rotate each subarray independently any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers k.



Example 1:

Input: nums = [3,1,2]

Output: 3

Explanation:

 - For n = 3, possible divisors are 1 and 3.
 - For k = 1: each subarray has one element. No rotation can sort the array.
 - For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.

Only k = 3 is sortable. Hence, the answer is 3.


Example 2:

Input: nums = [7,6,5]

Output: 0

Explanation:

 - For k = 1: each subarray has one element. No rotation can sort the array.
 - For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
 - For n = 3, possible divisors are 1 and 3.

No k is sortable. Hence, the answer is 0.


Example 3:

Input: nums = [5,8]

Output: 3

Explanation:

 - For n = 2, possible divisors are 1 and 2.

Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.



Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^5
"""


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        next_dec = [n] * n
        j = n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                j = i
            next_dec[i] = j

        ans = 0
        for d in range(1, n + 1):
            if n % d > 0:
                continue
            mx = 0
            for l in range(0, n, d):
                r = l + d - 1
                i = next_dec[l]
                if i < r:
                    j = next_dec[i + 1]
                    if j < r or nums[l] < nums[r] or nums[i + 1] < mx:
                        break
                    mx = nums[i]
                else:
                    if nums[l] < mx:
                        break
                    mx = nums[r]
            else:
                ans += d

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.sortableIntegers([3, 1, 2]))  # 3

    # Example 2
    print(sol.sortableIntegers([7, 6, 5]))  # 0

    # Example 3
    print(sol.sortableIntegers([5, 8]))  # 3
