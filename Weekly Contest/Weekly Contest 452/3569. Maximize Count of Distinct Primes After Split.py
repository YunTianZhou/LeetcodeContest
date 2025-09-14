"""
3569. Maximize Count of Distinct Primes After Split - Hard


You are given an integer array nums having length n and a 2D integer array queries where queries[i] = [idx, val].

For each query:

Update nums[idx] = val.
Choose an integer k with 1 <= k < n to split the array into the non-empty prefix nums[0..k-1] and suffix nums[k..n-1] such that the sum of the counts of distinct prime values in each part is maximum.
Note: The changes made to the array in one query persist into the next query.

Return an array containing the result for each query, in the order they are given.

 

Example 1:

Input: nums = [2,1,3,1,2], queries = [[1,2],[3,3]]

Output: [3,4]

Explanation:

Initially nums = [2, 1, 3, 1, 2].
After 1st query, nums = [2, 2, 3, 1, 2]. Split nums into [2] and [2, 3, 1, 2]. [2] consists of 1 distinct prime and [2, 3, 1, 2] consists of 2 distinct primes. Hence, the answer for this query is 1 + 2 = 3.
After 2nd query, nums = [2, 2, 3, 3, 2]. Split nums into [2, 2, 3] and [3, 2] with an answer of 2 + 2 = 4.
The output is [3, 4].


Example 2:

Input: nums = [2,1,4], queries = [[0,1]]

Output: [0]

Explanation:

Initially nums = [2, 1, 4].
After 1st query, nums = [1, 1, 4]. There are no prime numbers in nums, hence the answer for this query is 0.
The output is [0].
 


Constraints:

2 <= n == nums.length <= 5 * 10^4
1 <= queries.length <= 5 * 10^4
1 <= nums[i] <= 10^5
0 <= queries[i][0] < nums.length
1 <= queries[i][1] <= 10^5
"""

from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


# Temp: LazySegmentTree
# Author: 灵茶山艾府
# Link: https://leetcode.cn/discuss/post/mOr1u6/
# Source: 力扣（LeetCode）
class Node:
    __slots__ = 'val', 'todo'


class LazySegmentTree:
    _TODO_INIT = 0

    def __init__(self, n: int, init_val=0):
        if isinstance(init_val, int):
            init_val = [init_val] * n
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]
        self._build(init_val, 1, 0, n - 1)

    def _merge_val(self, a: int, b: int) -> int:
        return max(a, b)

    def _apply(self, node: int, l: int, r: int, todo: int) -> None:
        cur = self._tree[node]
        cur.val += todo
        cur.todo += todo

    def _spread(self, node: int, l: int, r: int) -> None:
        todo = self._tree[node].todo
        if todo == self._TODO_INIT:
            return
        m = (l + r) // 2
        self._apply(node * 2, l, m, todo)
        self._apply(node * 2 + 1, m + 1, r, todo)
        self._tree[node].todo = self._TODO_INIT

    def _maintain(self, node: int) -> None:
        self._tree[node].val = self._merge_val(self._tree[node * 2].val, self._tree[node * 2 + 1].val)

    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        self._tree[node].todo = self._TODO_INIT
        if l == r:
            self._tree[node].val = a[l]
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m) 
        self._build(a, node * 2 + 1, m + 1, r)
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:
            self._apply(node, l, r, f)
            return
        self._spread(node, l, r)
        m = (l + r) // 2
        if ql <= m:
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self._tree[node].val
        self._spread(node, l, r)
        m = (l + r) // 2
        if qr <= m:
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)


m = 10 ** 5
is_prime = [True] * (m + 2)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False

class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        rng = defaultdict(SortedList)
        for i, x in enumerate(nums):
            if is_prime[x]:
                rng[x].add(i)

        seg = LazySegmentTree(n)
        for sl in rng.values():
            if len(sl) > 1:
                seg.update(sl[0] + 1, sl[-1], 1)

        ans = []
        for i, x in queries:
            if x != nums[i]:
                if is_prime[nums[i]]:
                    sl = rng[nums[i]]
                    need_update = len(sl) > 1 and i in (sl[0], sl[-1])

                    if need_update:
                        seg.update(sl[0] + 1, sl[-1], -1)
                    sl.remove(i)
                    if not sl:
                        del rng[nums[i]]
                    elif need_update and len(sl) > 1:
                        seg.update(sl[0] + 1, sl[-1], 1)

                if is_prime[x]:
                    sl = rng[x]
                    need_update = len(sl) and (i < sl[0] or i > sl[-1])

                    if len(sl) > 1 and need_update:
                        seg.update(sl[0] + 1, sl[-1], -1)
                    sl.add(i)
                    if need_update:
                        seg.update(sl[0] + 1, sl[-1], 1)

                nums[i] = x
            
            ans.append(seg.query(0, n - 1) + len(rng))

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumCount([2, 1, 3, 1, 2], [[1, 2], [3, 3]]))  # [3, 4]

    # Example 2
    print(sol.maximumCount([2, 1, 4], [[0, 1]]))  # [0]
