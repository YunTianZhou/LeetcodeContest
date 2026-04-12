"""
3901. Good Subsequence Queries - Hard


You are given an integer array nums of length n and an integer p.

A non-empty subsequence of nums is called good if:

 - Its length is strictly less than n.

 - The greatest common divisor (GCD) of its elements is exactly p.

You are also given a 2D integer array queries of length q, where each queries[i] = [indi, vali] indicates that you should update nums[indi] to vali.

After each query, determine whether there exists any good subsequence in the current array.

Return the number of queries for which a good subsequence exists.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

The term gcd(a, b) denotes the greatest common divisor of a and b.



Example 1:

Input: nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]

Output: 1

Explanation:

i  [indi, vali]  Operation            Updated nums    Any good Subsequence
0  [0, 3]        Update nums[0] to 3  [3, 8, 12, 16]  No, as no subsequence has GCD exactly p = 2
1  [2, 6]        Update nums[2] to 6  [3, 8, 6, 16]   Yes, subsequence [8, 6] has GCD exactly p = 2

Thus, the answer is 1.


Example 2:

Input: nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]

Output: 2

Explanation:

i  [indi, vali]  Operation            Updated nums  Any good Subsequence
0  [0, 6]        Update nums[0] to 6  [6, 5, 7, 8]  No, as no subsequence has GCD exactly p = 3
1  [1, 9]        Update nums[1] to 9  [6, 9, 7, 8]  Yes, subsequence [6, 9] has GCD exactly p = 3
2  [2, 3]        Update nums[2] to 3  [6, 9, 3, 8]  Yes, subsequence [6, 9, 3] has GCD exactly p = 3

Thus, the answer is 2.


Example 3:

Input: nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]

Output: 0

Explanation:

i  [indi, vali]  Operation            Updated nums  Any good Subsequence
0  [1, 4]        Update nums[1] to 4  [5, 4, 9]     No, as no subsequence has GCD exactly p = 2
1  [2, 8]        Update nums[2] to 8  [5, 4, 8]     No, as no subsequence has GCD exactly p = 2

Thus, the answer is 0.



Constraints:

2 <= n == nums.length <= 5 * 10^4
1 <= nums[i] <= 5 * 10^4
1 <= queries.length <= 5 * 10^4
queries[i] = [indi, vali]
1 <= vali, p <= 5 * 10^4
0 <= indi <= n - 1
"""

from math import gcd


class SegmentTree:
    def __init__(self, arr: list[int], p: int):
        n = len(arr)
        self._n = n
        self._p = p
        self._cnt = 0
        self._tree = [0] * (2 << (n - 1).bit_length())
        self._build(arr, 1, 0, n - 1)

    def _maintain(self, node: int) -> None:
        self._tree[node] = gcd(self._tree[node * 2], self._tree[node * 2 + 1])

    def _set(self, node: int, val: int) -> None:
        if self._tree[node] > 0:
            self._cnt -= 1
        if val % self._p == 0:
            self._tree[node] = val // self._p
            self._cnt += 1
        else:
            self._tree[node] = 0

    def _build(self, a: list[int], node: int, l: int, r: int) -> None:
        if l == r:
            self._set(node, a[l])
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)
        self._build(a, node * 2 + 1, m + 1, r)
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self._set(node, val)
            return
        m = (l + r) // 2
        if i <= m:
            self._update(node * 2, l, m, i, val)
        else:
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self._tree[node]
        if l > qr or r < ql:
            return 0
        m = (l + r) // 2
        return gcd(self._query(node * 2, l, m, ql, qr), 
                   self._query(node * 2 + 1, m + 1, r, ql, qr))

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)

    def check(self) -> bool:
        if self._tree[1] != 1:
            return False
        if self._cnt < self._n or self._n > 6:
            return True
        return any(gcd(self.query(0, i - 1), self.query(i + 1, self._n - 1)) == 1 
                   for i in range(self._n))


class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        seg = SegmentTree(nums, p)
        ans = 0

        for i, x in queries:
            seg.update(i, x)
            if seg.check():
                ans += 1
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countGoodSubseq([4, 8, 12, 16], 2, [[0, 3], [2, 6]]))  # 1

    # Example 2
    print(sol.countGoodSubseq([4, 5, 7, 8], 3, [[0, 6], [1, 9], [2, 3]]))  # 2

    # Example 3
    print(sol.countGoodSubseq([5, 7, 9], 2, [[1, 4], [2, 8]]))  # 0
