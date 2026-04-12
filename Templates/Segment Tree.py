# Temp: SegmentTree
# Author: 灵茶山艾府
# Link: https://leetcode.cn/discuss/post/mOr1u6/
# Source: 力扣（LeetCode）


class SegmentTree:
    def __init__(self, arr, default=0):
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        self._n = n
        self._tree = [0] * (2 << (n - 1).bit_length())
        self._build(arr, 1, 0, n - 1)

    def _merge_val(self, a: int, b: int) -> int:
        return max(a, b)
        # return min(a, b)

    def _maintain(self, node: int) -> None:
        self._tree[node] = self._merge_val(self._tree[node * 2], self._tree[node * 2 + 1])

    def _build(self, a: list[int], node: int, l: int, r: int) -> None:
        if l == r:
            self._tree[node] = a[l]
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)
        self._build(a, node * 2 + 1, m + 1, r)
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self._tree[node] = self._merge_val(self._tree[node], val)
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
        m = (l + r) // 2
        if qr <= m:
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)

    def get(self, i: int) -> int:
        return self._query(1, 0, self._n - 1, i, i)
