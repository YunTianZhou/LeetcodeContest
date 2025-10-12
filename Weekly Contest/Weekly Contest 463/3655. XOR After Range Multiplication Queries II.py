"""
3655. XOR After Range Multiplication Queries II - Hard


You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].

For each query, you must apply the following operations in order:

Set idx = li.
While idx <= ri:
    Update: nums[idx] = (nums[idx] * vi) % (10^9 + 7)
    Set idx += ki.

Return the bitwise XOR of all elements in nums after processing all queries.



Example 1:

Input: nums = [1,1,1], queries = [[0,2,1,4]]

Output: 4

Explanation:

A single query [0, 2, 1, 4] multiplies every element from index 0 through index 2 by 4.

The array changes from [1, 1, 1] to [4, 4, 4].

The XOR of all elements is 4 ^ 4 ^ 4 = 4.


Example 2:

Input: nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]

Output: 31

Explanation:

The first query [1, 4, 2, 3] multiplies the elements at indices 1 and 3 by 3, transforming the array to [2, 9, 1, 15, 4].

The second query [0, 2, 1, 2] multiplies the elements at indices 0, 1, and 2 by 2, resulting in [4, 18, 2, 15, 4].

Finally, the XOR of all elements is 4 ^ 18 ^ 2 ^ 15 ^ 4 = 31.



Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= q == queries.length <= 10^5
queries[i] = [li, ri, ki, vi]
0 <= li <= ri < n
1 <= ki <= n
1 <= vi <= 10^5
"""

from typing import List
from collections import defaultdict


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        groups = defaultdict(list)
        for i, (l, _, k, _) in enumerate(queries):
            groups[k, l % k].append(i)
        
        for (k, s), group in groups.items():
            ls = []
            for i in group:
                l, r, _, v = queries[i]
                ls.append((l, v % mod))
                ls.append((r + 1, pow(v, mod - 2, mod) % mod))
            ls.sort(key=lambda x: x[0], reverse=True)

            mul = 1
            for i in range(s, n, k):
                while ls and i >= ls[-1][0]:
                    mul = mul * ls.pop()[1] % mod
                nums[i] = nums[i] * mul % mod

        ans = 0
        for x in nums:
            ans ^= x
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.xorAfterQueries([1, 1, 1], [[0, 2, 1, 4]]))  # 4

    # Example 2
    print(sol.xorAfterQueries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]))  # 31
    