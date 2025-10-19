"""
3721. Longest Balanced Subarray II - Hard


You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.



Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].

It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.


Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].

It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.


Example 3:

Input: nums = [1,2,3,2]

Output: 3

Explanation:

The longest balanced subarray is [2, 3, 2].

It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from typing import List


# Temp: LazySegmentTree
# Author: 灵茶山艾府
# Link: https://leetcode.cn/discuss/post/mOr1u6/
# Source: 力扣（LeetCode）
class Node:
    __slots__ = 'min', 'max', 'todo'

    def __init__(self):
        self.min = self.max = self.todo = 0


class LazySegmentTree:
    def __init__(self, n: int):
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]

    def _apply(self, node: int, todo: int) -> None:
        cur = self._tree[node]
        cur.min += todo
        cur.max += todo
        cur.todo += todo

    def _spread(self, node: int) -> None:
        todo = self._tree[node].todo
        if todo == 0:
            return
        self._apply(node * 2, todo)
        self._apply(node * 2 + 1, todo)
        self._tree[node].todo = 0

    def _maintain(self, node: int) -> None:
        l_node = self._tree[node * 2]
        r_node = self._tree[node * 2 + 1]
        self._tree[node].min = min(l_node.min, r_node.min)
        self._tree[node].max = max(l_node.max, r_node.max)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:
            self._apply(node, f)
            return
        self._spread(node)
        m = (l + r) // 2
        if ql <= m:
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _find_first(self, node: int, l: int, r: int, ql: int, qr: int, target: int) -> int:
        if l > qr or r < ql or not self._tree[node].min <= target <= self._tree[node].max:
            return -1
        if l == r:
            return l
        self._spread(node)
        m = (l + r) // 2
        idx = self._find_first(node * 2, l, m, ql, qr, target)
        if idx < 0:
            idx = self._find_first(node * 2 + 1, m + 1, r, ql, qr, target)
        return idx

    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    def find_first(self, ql: int, qr: int, target: int) -> int:
        return self._find_first(1, 0, self._n - 1, ql, qr, target)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        st = LazySegmentTree(n + 1)

        prev = {}
        ans = sm = 0
        for i, x in enumerate(nums, start=1):
            v = 1 if x % 2 else -1
            if x in prev:
                st.update(prev[x], i - 1, -v)
            else:
                sm += v
                st.update(i, n, v)
            prev[x] = i

            if (j := st.find_first(0, i - 1, sm)) != -1:
                ans = max(ans, i - j)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestBalanced([2, 5, 4, 3]))  # 4

    # Example 2
    print(sol.longestBalanced([3, 2, 2, 5, 4]))  # 5

    # Example 3
    print(sol.longestBalanced([1, 2, 3, 2]))  # 3
    