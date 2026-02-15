"""
3845. Maximum Subarray XOR with Bounded Range - Hard


You are given a non-negative integer array nums and an integer k.

You must select a subarray of nums such that the difference between its maximum and minimum elements is at most k. The value of this subarray is the bitwise XOR of all elements in the subarray.

Return an integer denoting the maximum possible value of the selected subarray.



Example 1:

Input: nums = [5,4,5,6], k = 2

Output: 7

Explanation:

 - Select the subarray [5, 4, 5, 6].

 - The difference between its maximum and minimum elements is 6 - 4 = 2 <= k.

 - The value is 4 XOR 5 XOR 6 = 7.


Example 2:

Input: nums = [5,4,5,6], k = 1

Output: 6

Explanation:

 - Select the subarray [5, 4, 5, 6].

 - The difference between its maximum and minimum elements is 6 - 6 = 0 <= k.

 - The value is 6.



Constraints:

1 <= nums.length <= 4 * 10^4
0 <= nums[i] < 2^15
0 <= k < 2^15
"""

from typing import List
from collections import deque


class Solution:
    def maxXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = max(nums).bit_length()

        left = [0] * n
        mx = deque()
        mn = deque()
        j = 0
        for i in range(n):
            while mx and nums[i] >= nums[mx[-1]]:
                mx.pop()
            mx.append(i)

            while mn and nums[i] <= nums[mn[-1]]:
                mn.pop()
            mn.append(i)

            while nums[mx[0]] - nums[mn[0]] > k:
                if mx[0] == j:
                    mx.popleft()
                if mn[0] == j:
                    mn.popleft()
                j += 1

            left[i] = j

        ans = 0
        for b in range(m - 1, -1, -1): 
            cnt = {0: 1}
            j = sum_i = sum_j = 0
            ans = (ans << 1) | 1
            for i in range(n):
                while j < left[i]:
                    cnt[sum_j] -= 1
                    sum_j ^= nums[j] >> b
                    j += 1
                sum_i ^= nums[i] >> b
                if cnt.get(sum_i ^ ans, 0) > 0:
                    break
                cnt[sum_i] = cnt.get(sum_i, 0) + 1
            else:
                ans ^= 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxXor([5, 4, 5, 6], 2))  # 7

    # Example 2
    print(sol.maxXor([5, 4, 5, 6], 1))  # 6
