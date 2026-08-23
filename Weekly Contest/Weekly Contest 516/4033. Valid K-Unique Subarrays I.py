"""
4033. Valid K-Unique Subarrays I - Hard


You are given an integer array nums and an integer k.

You are also given a 2D integer array queries, where queries[i] = [li, ri] represents the subarray nums[li..ri].

For each query, the subarray nums[li..ri] is considered valid if:

 - It contains exactly k distinct numbers, and

 - The frequency of every number in the subarray is even.

Return a boolean array ans, where ans[i] is true if nums[li..ri] is valid, and false otherwise.



Example 1:

Input: nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]

Output: [false,true,false]

Explanation:

i  [li, ri]  Subarray      Unique numbers  Frequency     Validity check
0  [0, 1]    [1, 2]        {1, 2} → 2      {1: 1, 2: 1}  false: Element counts are not even.
1  [0, 3]    [1, 2, 2, 1]  {1, 2} → 2      {1: 2, 2: 2}  true: Exactly k = 2 distinct elements, all appear an even number of times.
2  [1, 2]    [2, 2]        {2} → 1         {2: 2}        false: Number of distinct elements is less than k = 2.

Thus, ans = [false, true, false].


Example 2:

Input: nums = [3,3,3], k = 1, queries = [[1,2],[0,2]]

Output: [true,false]

Explanation:

i  [li, ri]  Subarray   Unique numbers  Frequency  Validity check
0  [1, 2]    [3, 3]     {3} → 1         {3: 2}     true: Exactly k = 1 distinct element, appears an even number of times.
1  [0, 2]    [3, 3, 3]  {3} → 1         {3: 3}     false: 3 does not appear an even number of times.

Thus, ans = [true, false].



Constraints:

2 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= n
1 <= queries.length <= 10^5
queries[i] == [li, ri]
0 <= li < ri <= n - 1
"""

import random
import operator
from itertools import accumulate


class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        
        mp = {x: random.getrandbits(63) for x in set(nums)}
        pref = list(accumulate((mp[x] for x in nums), operator.xor, initial=0))

        def get_bound(k: int) -> list[int]:
            res = [0] * n

            cnt = {}
            j = 0
            for i, x in enumerate(nums):
                cnt[x] = cnt.get(x, 0) + 1

                while len(cnt) > k:
                    y = nums[j]
                    cnt[y] -= 1
                    if cnt[y] == 0:
                        del cnt[y]
                    j += 1
                
                res[i] = j
            
            return res
        
        left = get_bound(k)
        right = get_bound(k - 1)

        return [left[r] <= l < right[r] and pref[r + 1] == pref[l] for l, r in queries]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.validSubarrays([1, 2, 2, 1], 2, [[0, 1], [0, 3], [1, 2]]))  # [False, True, False]

    # Example 2
    print(sol.validSubarrays([3, 3, 3], 1, [[1, 2], [0, 2]]))  # [True, False]
