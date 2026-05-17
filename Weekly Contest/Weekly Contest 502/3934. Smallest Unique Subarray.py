"""
3934. Smallest Unique Subarray - Hard


You are given an integer array nums.

Find the minimum length of a subarray that is not identical to any other subarray in nums.

Return an integer denoting the minimum possible length of such a subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.



Example 1:

Input: nums = [3,3,3]

Output: 3

Explanation:

 - Subarrays of length 1: [3] → appears 3 times
 - Subarrays of length 2: [3, 3] → appears 2 times
 - Subarrays of length 3: [3, 3, 3] → appears once

The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.


Example 2:

Input: nums = [2,1,2,3,3]

Output: 1

Explanation:

Subarrays of length 1:

 - [2] → appears 2 times
 - [1] → appears once
 - [3] → appears 2 times

The subarray [1] is unique, so the smallest unique subarray length is 1.


Example 3:

Input: nums = [1,1,2,2,1]

Output: 2

Explanation:

Subarrays of length 1:

 - [1] → appears 3 times
 - [2] → appears 2 times

Subarrays of length 2:

 - [1, 1] → appears once
 - [1, 2] → appears once
 - [2, 2] → appears once
 - [2, 1] → appears once

There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from collections import defaultdict


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        base = 10 ** 5 + 3

        pow_base = [1] * (n + 1)
        for i in range(1, n + 1):
            pow_base[i] = pow_base[i - 1] * base % mod

        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = (pref[i] * base + x) % mod

        l = 0
        r = n
        while l + 1 < r:
            mid = (l + r) // 2
            
            mp = defaultdict(int)
            for i in range(mid, n + 1):
                h = (pref[i] - pref[i - mid] * pow_base[mid]) % mod
                mp[h] += 1
            
            if 1 in mp.values():
                r = mid
            else:
                l = mid

        return r


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.smallestUniqueSubarray([3, 3, 3]))  # 3

    # Example 2
    print(sol.smallestUniqueSubarray([2, 1, 2, 3, 3]))  # 1

    # Example 3
    print(sol.smallestUniqueSubarray([1, 1, 2, 2, 1]))  # 2
