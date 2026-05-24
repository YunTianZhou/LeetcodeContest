"""
3943. Number of Pairs After Increment - Hard


You are given two integer arrays nums1 and nums2, and a 2D integer array queries.

Each queries[i] is one of the following types:

 - [1, x, y, val] - Add val to every element in nums2[x..y].

  - [2, tot] - Compute the number of pairs (j, k) such that nums1[j] + nums2[k] == tot.

Return an integer array answer, where answer[j] is the number of pairs for the jth query of type 2.



Example 1:

Input: nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]

Output: [2,1]

Explanation:

 - queries[0] = [2, 5]: Valid pairs are nums1[0] + nums2[1] = 1 + 4 = 5 and nums1[1] + nums2[0] = 2 + 3 = 5.

 - queries[1] = [1, 0, 0, 2]: Add 2 to nums2[0], resulting in nums2 = [5, 4].

 - queries[2] = [2, 5]: Valid pair is nums1[0] + nums2[1] = 1 + 4 = 5.

 - Thus, the answer = [2, 1].


Example 2:

Input: nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]]

Output: [2,6]

Explanation:

 - queries[0] = [2, 4]: Valid pairs are nums1[0] + nums2[2] = 1 + 3 and nums1[1] + nums2[2] = 1 + 3.

 - queries[1] = [1, 0, 1, 1]: Add 1 to nums2[0] and nums2[1], resulting in nums2 = [3, 3, 3].

 - queries[2] = [2, 4]: Every element of nums1 = [1, 1] pairs with every element of nums2 = [3, 3, 3] as 1 + 3 = 4. That gives 2 × 3 = 6 pairs in total.

 - Thus, the answer = [2, 6].


Example 3:

Input: nums1 = [2,5,8,4], nums2 = [1,3,8], queries = [[2,9],[1,1,2,1],[2,10]]

Output: [1,0]

Explanation:

 - queries[0] = [2, 9]: Only valid pair is nums1[2] + nums2[0] = 8 + 1 = 9.

 - queries[1] = [1, 1, 2, 1]: Add 1 to nums2[1] and nums2[2], resulting in​​​​​​​ nums2 = [1, 4, 9].

 - queries[2] = [2, 10]: No pair sums to 10.

 - Thus, the answer = [1, 0].



Constraints:

1 <= nums1.length <= 5
1 <= nums2.length <= 5 * 10^4
1 <= nums1[i], nums2[i] <= 10^5
1 <= queries.length <= 5 * 10^4
queries[i].length == 2 or 4
queries[i] == [1, x, y, val], or
queries[i] == [2, tot]
0 <= x <= y < nums2.length
1 <= val <= 10^5
1 <= tot <= 10^9
"""

from collections import defaultdict
from math import isqrt


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums2)
        b = isqrt(n) + 1
        
        cnt = [defaultdict(int) for _ in range(b)]
        lazy = [0] * b
        for i, x in enumerate(nums2):
            cnt[i // b][x] += 1

        def update(l, r, g):
            for i in range(l, r + 1):
                cnt[g][nums2[i]] -= 1
                nums2[i] += x
                cnt[g][nums2[i]] += 1

        res = []
        for q in queries:
            op, *args = q
            
            if op == 1:
                l, r, x = args
                gl = (l + b - 1) // b
                gr = r // b
                if gl > gr:
                    update(l, r, gr)
                else:
                    update(l, gl * b - 1, gl - 1)
                    update(gr * b, r, gr)
                    for i in range(gl, gr):
                        lazy[i] += x
            else:
                tot = args[0]
                ans = 0
                for x in nums1:
                    for i in range(b):
                        ans += cnt[i][tot - x - lazy[i]]
                res.append(ans)

        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.numberOfPairs([1, 2], [3, 4], [[2, 5], [1, 0, 0, 2], [2, 5]]))  # [2, 1]

    # Example 2
    print(sol.numberOfPairs([1, 1], [2, 2, 3], [[2, 4], [1, 0, 1, 1], [2, 4]]))  # [2, 6]

    # Example 3
    print(sol.numberOfPairs([2, 5, 8, 4], [1, 3, 8], [[2, 9], [1, 1, 2, 1], [2, 10]]))  # [1, 0]
