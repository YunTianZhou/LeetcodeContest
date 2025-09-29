"""
3695. Maximize Alternating Sum Using Swaps - Hard


You are given an integer array nums.

You want to maximize the alternating sum of nums, which is defined as the value obtained by adding elements at even indices and subtracting elements at odd indices. That is, nums[0] - nums[1] + nums[2] - nums[3]...

You are also given a 2D integer array swaps where swaps[i] = [pi, qi]. For each pair [pi, qi] in swaps, you are allowed to swap the elements at indices pi and qi. These swaps can be performed any number of times and in any order.

Return the maximum possible alternating sum of nums.



Example 1:

Input: nums = [1,2,3], swaps = [[0,2],[1,2]]

Output: 4

Explanation:

The maximum alternating sum is achieved when nums is [2, 1, 3] or [3, 1, 2]. As an example, you can obtain nums = [2, 1, 3] as follows.

 - Swap nums[0] and nums[2]. nums is now [3, 2, 1].
 - Swap nums[1] and nums[2]. nums is now [3, 1, 2].
 - Swap nums[0] and nums[2]. nums is now [2, 1, 3].

 
Example 2:

Input: nums = [1,2,3], swaps = [[1,2]]

Output: 2

Explanation:

The maximum alternating sum is achieved by not performing any swaps.


Example 3:

Input: nums = [1,1000000000,1,1000000000,1,1000000000], swaps = []

Output: -2999999997

Explanation:

Since we cannot perform any swaps, the maximum alternating sum is achieved by not performing any swaps.



Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= swaps.length <= 10^5
swaps[i] = [pi, qi]
0 <= pi < qi <= nums.length - 1
[pi, qi] != [pj, qj]
"""

from typing import List
from collections import defaultdict
from heapq import nlargest


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)

        uf = list(range(n))

        def find(x):
            while x != uf[x]:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        for i, j in swaps:
            uf[find(i)] = uf[j]
        
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        
        ans = 0
        for group in groups.values():
            k = sum(1 for i in group if i % 2 == 0)
            add = sum(nlargest(k, (nums[i] for i in group)))
            sub = sum(nums[i] for i in group) - add
            ans += add - sub

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxAlternatingSum([1 ,2, 3], [[0, 2], [1, 2]]))  # 4

    # Example 2
    print(sol.maxAlternatingSum([1, 2, 3], [[1, 2]]))  # 2

    # Example 3
    print(sol.maxAlternatingSum([1, 1000000000, 1, 1000000000, 1, 1000000000], []))  # -2999999997
