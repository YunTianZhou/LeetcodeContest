"""
3636. Threshold Majority Queries - Hard


You are given an integer array nums of length n and an array queries, where queries[i] = [li, ri, thresholdi].

Return an array of integers ans where ans[i] is equal to the element in the subarray nums[li...ri] that appears at least thresholdi times, selecting the element with the highest frequency (choosing the smallest in case of a tie), or -1 if no such element exists.



Example 1:

Input: nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]

Output: [1,-1,2]

Explanation:

Query      Sub-array           Threshold  Frequency table  Answer
[0, 5, 4]  [1, 1, 2, 2, 1, 1]  4          1 → 4, 2 → 2     1
[0, 3, 3]  [1, 1, 2, 2]        3          1 → 2, 2 → 2    -1
[2, 3, 2]  [2, 2]              2          2 → 2            2


Example 2:

Input: nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]

Output: [3,2,3,2]

Explanation:

Query      Sub-array              Threshold  Frequency table  Answer
[0, 6, 4]  [3, 2, 3, 2, 3, 2, 3]  4          3 → 4, 2 → 3     3
[1, 5, 2]  [2, 3, 2, 3, 2]        2          2 → 3, 3 → 2     2
[2, 4, 1]  [3, 2, 3]              1          3 → 2, 2 → 1     3
[3, 3, 1]  [2]                    1          2 → 1            2



Constraints:

1 <= nums.length == n <= 10^4
1 <= nums[i] <= 10^9
1 <= queries.length <= 5 * 10^4
queries[i] = [li, ri, thresholdi]
0 <= li <= ri < n
1 <= thresholdi <= ri - li + 1
"""

from typing import List
from math import sqrt, ceil
from collections import defaultdict, Counter


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)
        m = ceil(sqrt(n))

        buskets = [[] for _ in range(m)]
        for i, (l, r, t) in enumerate(queries):
            buskets[l // m].append((l, r, t, i))
        
        ans = [-1] * q
        for k in range(m):
            if not buskets[k]:
                continue
            buskets[k].sort(key=lambda x: x[1])
            
            bound = m * (k + 1)
            j = bound
            cnt = defaultdict(int)
            mx = (0, 0)
            for l, r, t, i in buskets[k]:
                while j <= r:
                    cnt[nums[j]] += 1
                    mx = max(mx, (cnt[nums[j]], -nums[j]))
                    j += 1

                curr_cnt = Counter(nums[l: min(bound, r + 1)])
                curr_mx = mx
                for x, c in curr_cnt.items():
                    curr_mx = max(curr_mx, (c + cnt[x], -x))

                if curr_mx[0] >= t:
                    ans[i] = -curr_mx[1]

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.subarrayMajority(
        nums=[1, 1, 2, 2, 1, 1], 
        queries=[[0, 5, 4],[0, 3, 3],[2, 3, 2]])
    )  # [1, -1, 2]

    # Example 2
    print(sol.subarrayMajority(
        nums=[3, 2, 3, 2, 3, 2, 3],
        queries=[[0, 6, 4], [1, 5, 2], [2, 4, 1], [3, 3, 1]])
    )  # [3, 2, 3, 2]
