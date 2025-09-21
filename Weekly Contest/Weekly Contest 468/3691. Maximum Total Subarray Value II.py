"""
3691. Maximum Total Subarray Value II - Hard


You are given an integer array nums of length n and an integer k.

You must select exactly k distinct non-empty subarrays nums[l..r] of nums. Subarrays may overlap, but the exact same subarray (same l and r) cannot be chosen more than once.

The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.



Example 1:

Input: nums = [1,3,2], k = 2

Output: 4

Explanation:

One optimal approach is:

Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.

Adding these gives 2 + 2 = 4.


Example 2:

Input: nums = [4,2,5,1], k = 3

Output: 12

Explanation:

One optimal approach is:

Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
Choose nums[1..3] = [2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.

Adding these gives 4 + 4 + 4 = 12.



Constraints:

1 <= n == nums.length <= 5 * 10^4
0 <= nums[i] <= 10^9
1 <= k <= min(10^5, n * (n + 1) / 2)
"""

from typing import List
from heapq import heappop, heappush, heapify


class SparseTable:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        k = self.log[self.n] + 1
        self.st_min = [[0] * k for _ in range(self.n)]
        self.st_max = [[0] * k for _ in range(self.n)]
        
        for i in range(self.n):
            self.st_min[i][0] = data[i]
            self.st_max[i][0] = data[i]
        
        for j in range(1, k):
            for i in range(self.n - (1 << j) + 1):
                self.st_min[i][j] = min(self.st_min[i][j-1], self.st_min[i + (1 << (j - 1))][j-1])
                self.st_max[i][j] = max(self.st_max[i][j-1], self.st_max[i + (1 << (j - 1))][j-1])

    def query(self, l: int, r: int) -> int:
        j = self.log[r - l + 1]
        mn = min(self.st_min[l][j], self.st_min[r - (1 << j) + 1][j])
        mx = max(self.st_max[l][j], self.st_max[r - (1 << j) + 1][j])
        return mx - mn


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SparseTable(nums)

        heap = [(-st.query(l, n - 1), l, n - 1) for l in range(n)]
        heapify(heap)

        ans = 0
        while k > 0 and heap:
            score, l, r = heappop(heap)
            score = -score

            ans += score
            k -= 1

            if l < r:
                heappush(heap, (-st.query(l, r - 1), l, r - 1))
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxTotalValue([1, 3, 2], 2))  # 4

    # Example 2
    print(sol.maxTotalValue([4, 2, 5, 1], 3))  # 12
    