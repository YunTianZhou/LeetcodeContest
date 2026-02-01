"""
3826. Minimum Partition Score - Hard


You are given an integer array nums and an integer k.

Your task is to partition nums into exactly k subarrays and return an integer denoting the minimum possible score among all valid partitions.

The score of a partition is the sum of the values of all its subarrays.

The value of a subarray is defined as sumArr * (sumArr + 1) / 2, where sumArr is the sum of its elements.



Example 1:

Input: nums = [5,1,2,1], k = 2

Output: 25

Explanation:

 - We must partition the array into k = 2 subarrays. One optimal partition is [5] and [1, 2, 1].

 - The first subarray has sumArr = 5 and value = 5 x 6 / 2 = 15.

 - The second subarray has sumArr = 1 + 2 + 1 = 4 and value = 4 x 5 / 2 = 10.

 - The score of this partition is 15 + 10 = 25, which is the minimum possible score.


Example 2:

Input: nums = [1,2,3,4], k = 1

Output: 55

Explanation:

 - Since we must partition the array into k = 1 subarray, all elements belong to the same subarray: [1, 2, 3, 4].

 - This subarray has sumArr = 1 + 2 + 3 + 4 = 10 and value = 10 x 11 / 2 = 55.

 - The score of this partition is 55, which is the minimum possible score.


Example 3:

Input: nums = [1,1,1], k = 3

Output: 3

Explanation:

 - We must partition the array into k = 3 subarrays. The only valid partition is [1], [1], [1].

 - Each subarray has sumArr = 1 and value = 1 x 2 / 2 = 1.

 - The score of this partition is 1 + 1 + 1 = 3, which is the minimum possible score.



Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

from typing import List
from math import inf
from itertools import accumulate


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps = list(accumulate(nums, initial=0))

        f = [0] + [inf] * n
        nf = [0] * (n + 1)

        def dfs(l, r, ql, qr):
            if l > r:
                return

            mid = (l + r) // 2
            mn, idx = inf, 0
            for i in range(ql, min(mid, qr) + 1):
                s = ps[mid] - ps[i - 1]
                curr = s * (s + 1) + f[i - 1]
                if curr < mn:
                    mn = curr
                    idx = i

            dfs(l, mid - 1, ql, idx)
            dfs(mid + 1, r, idx, qr)
            nf[mid] = mn

        for _ in range(k):
            dfs(1, n, 1, n)
            f, nf = nf, f
        
        return f[n] // 2


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minPartitionScore([5, 1, 2, 1], 2))  # 25

    # Example 2
    print(sol.minPartitionScore([1, 2, 3, 4], 1))  # 55

    # Example 3
    print(sol.minPartitionScore([1, 1, 1], 3))  # 3
    