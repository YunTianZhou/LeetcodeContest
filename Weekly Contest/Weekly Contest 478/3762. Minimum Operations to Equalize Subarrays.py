"""
3762. Minimum Operations to Equalize Subarrays - Hard


You are given an integer array nums and an integer k.

In one operation, you can increase or decrease any element of nums by exactly k.

You are also given a 2D integer array queries, where each queries[i] = [li, ri].

For each query, find the minimum number of operations required to make all elements in the subarray nums[li..ri] equal. If it is impossible, the answer for that query is -1.

Return an array ans, where ans[i] is the answer for the ith query.



Example 1:

Input: nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]

Output: [1,2]

Explanation:

One optimal set of operations:

i  [li, ri]  nums[li..ri]  Possibility  Operation                          Final nums[li..ri]  ans[i]
0  [0, 1]    [1, 4]        Yes          nums[0] + k = 1 + 3 = 4 = nums[1]  [4, 4]              1
1  [0, 2]    [1, 4, 7]     Yes          nums[0] + k = 1 + 3 = 4 = nums[1]  [4, 4, 4]           2
                                        nums[2] - k = 7 - 3 = 4 = nums[1]

Thus, ans = [1, 2].


Example 2:

Input: nums = [1,2,4], k = 2, queries = [[0,2],[0,0],[1,2]]

Output: [-1,0,1]

Explanation:

One optimal set of operations:

i  [li, ri]  nums[li..ri]  Possibility  Operations                         Final nums[li..ri]  ans[i]
0  [0, 2]   [1, 2, 4]      No           -                                  [1, 2, 4]           -1
1  [0, 0]   [1]            Yes          Already equal                      [1]                 0
2  [1, 2]   [2, 4]         Yes          nums[1] + k = 2 + 2 = 4 = nums[2]  [4, 4]              1

Thus, ans = [-1, 0, 1].



Constraints:

1 <= n == nums.length <= 4 * 10^4
1 <= nums[i] <= 10^9
1 <= k <= 10^9
1 <= queries.length <= 4 * 10^4
queries[i] = [li, ri]
0 <= li <= ri <= n - 1
"""

from typing import List, Tuple
from bisect import bisect_left


class Node:
    __slots__ = "l", "r", "sm", "sm_val"

    def __init__(self, l: int = 0, r: int = 0, sm: int = 0, sm_val: int = 0):
        self.l = l
        self.r = r
        self.sm = sm
        self.sm_val = sm_val

    def copy(self):
        return Node(self.l, self.r, self.sm, self.sm_val)


class PersistentSegmentTree:
    def __init__(self, s: List[int]):
        self.n = len(s)
        self.s = s
        self._tree = [Node()]
        self.p = 1
        root = self._build(1, self.n)
        self._roots = [root]

    def _new_node(self, node: Node):
        self._tree.append(node)
        p = self.p
        self.p += 1
        return p, self._tree[p]

    def _build(self, l: int, r: int) -> int:
        p, curr = self._new_node(Node())
        if l == r:
            return p

        m = (l + r) // 2
        left = self._build(l, m)
        right = self._build(m + 1, r)
        curr.l = left
        curr.r = right
        return p

    def _update(self, node: int, l: int, r: int, pos: int, val: int) -> int:
        if l > r:
            return 0

        p, curr = self._new_node(self._tree[node].copy())
        if l == r:
            curr.sm += val
            curr.sm_val += val * self.s[l - 1]
            return p

        m = (l + r) // 2
        if pos <= m:
            new_left = self._update(curr.l, l, m, pos, val)
            curr.l = new_left
        else:
            new_right = self._update(curr.r, m + 1, r, pos, val)
            curr.r = new_right

        curr.sm = self._tree[curr.l].sm + self._tree[curr.r].sm
        curr.sm_val = self._tree[curr.l].sm_val + self._tree[curr.r].sm_val
        return p

    def add(self, pos: int, val: int) -> None:
        new_root = self._update(self._roots[-1], 1, self.n, pos, val)
        self._roots.append(new_root)

    def _query(self, node1: int, node2: int, l: int, r: int, k: int) -> Tuple[int, int]:
        if l == r:
            return l, k * self.s[l - 1]
        curr1 = self._tree[node1]
        curr2 = self._tree[node2]

        m = (l + r) // 2
        left = self._tree[curr1.l].sm - self._tree[curr2.l].sm
        left_val = self._tree[curr1.l].sm_val - self._tree[curr2.l].sm_val
        if k <= left:
            return self._query(curr1.l, curr2.l, l, m, k)
        else:
            x, v = self._query(curr1.r, curr2.r, m + 1, r, k - left)
            return x, v + left_val

    def query(self, l: int, r: int, k: int) -> Tuple[int, int, int]:
        mid, left = self._query(self._roots[r], self._roots[l - 1], 1, self.n, k)
        tot = self._tree[self._roots[r]].sm_val - self._tree[self._roots[l - 1]].sm_val
        return self.s[mid - 1], left, tot - left


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)

        max_len = [1] * n
        value = [0] * n
        value[0] = nums[0] // k
        for i in range(1, n):
            if nums[i] % k == nums[i - 1] % k:
                max_len[i] = max_len[i - 1] + 1
            value[i] = nums[i] // k

        s = sorted(set(value))
        seg = PersistentSegmentTree(s)
        for x in value:
            i = bisect_left(s, x) + 1
            seg.add(i, 1)

        ans = [-1] * q
        for i, (l, r) in enumerate(queries):
            if r - max_len[r] >= l:
                continue
            t = (r - l + 1) // 2 + 1
            mid, left, right = seg.query(l + 1, r + 1, t)
            ans[i] = (mid * t - left) + (right - mid * (r - l - t + 1))

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations([1, 4, 7], 3, [[0, 1], [0, 2]]))  # [1, 2]

    # Example 2
    print(sol.minOperations([1, 2, 4], 2, [[0, 2], [0, 0], [1, 2]]))  # [-1, 0, 1]
