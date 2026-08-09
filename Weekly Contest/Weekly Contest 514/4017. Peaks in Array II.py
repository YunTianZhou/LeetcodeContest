"""
4017. Peaks in Array II - Hard


You are given an integer array nums of length n and a 2D integer array queries.

A subarray nums[i..j] is called a peak subarray if:

 - Its length is at least 3.

 - There exists an index k such that i < k < j and:

    - nums[k] > nums[k - 1]

    - nums[k] > nums[k + 1]

You have to process queries of two types:

 - [1, li, ri]: Calculate the number of peak subarrays fully contained within nums[li..ri].

 - [2, indexi, vali]: Update nums[indexi] to vali. This update applies to all subsequent queries.

Return an array answer, where answer[i] is the answer to the ith query of type 1 in the order they appear.



Example 1:

Input: nums = [1,3,2,4], queries = [[1,0,3],[2,1,1],[1,0,3]]

Output: [2,0]

Explanation:

 - Query [1, 0, 3]:

    - [1, 3, 2]: choose k = 1. Then nums[k] = 3, nums[k - 1] = 1, and nums[k + 1] = 2. Since 3 > 1 and 3 > 2, this is a peak subarray.

    - [1, 3, 2, 4]: choose k = 1. Then nums[k] = 3, nums[k - 1] = 1, and nums[k + 1] = 2. Since 3 > 1 and 3 > 2, this is a peak subarray.

 - Query [2, 1, 1]: Update nums[1] to 1. The array becomes [1, 1, 2, 4].

 - Query [1, 0, 3]: There are no peak subarrays now.

 - Thus, answer = [2, 0].


Example 2:

Input: nums = [9,8,9,8], queries = [[1,1,3],[2,2,1],[1,0,2]]

Output: [1,0]

Explanation:

 - Query [1, 1, 3]:

    - nums[1..3] = [8, 9, 8]: choose k = 2. Then nums[k] = 9, nums[k - 1] = 8, and nums[k + 1] = 8. Since 9 > 8 and 9 > 8, this is a peak subarray.

 - Query [2, 2, 1]: Update nums[2] to 1. The array becomes [9, 8, 1, 8].

 - Query [1, 0, 2]: There are no peak subarrays.

 - Thus, answer = [1, 0].


Example 3:

Input: nums = [3,6,2,7,1], queries = [[1,1,3],[2,3,0],[1,0,4]]

Output: [0,3]

Explanation:

 - Query [1, 1, 3]: The only subarray of length at least 3 is [6, 2, 7]. Its only possible peak index is k = 2, but nums[2] = 2 is less than both nums[1] = 6 and nums[3] = 7, so it is not a peak subarray.

 - Query [2, 3, 0]: Update nums[3] to 0. The array becomes [3, 6, 2, 0, 1].

 - Query [1, 0, 4]:

    - [3, 6, 2]: choose k = 1. Then nums[k] = 6, nums[k - 1] = 3, and nums[k + 1] = 2. Since 6 > 3 and 6 > 2, this is a peak subarray.

    - [3, 6, 2, 0]: choose k = 1. Then nums[k] = 6, nums[k - 1] = 3, and nums[k + 1] = 2. Since 6 > 3 and 6 > 2, this is a peak subarray.

    - [3, 6, 2, 0, 1]: choose k = 1. Then nums[k] = 6, nums[k - 1] = 3, and nums[k + 1] = 2. Since 6 > 3 and 6 > 2, this is a peak subarray.

 - Thus, answer = [0, 3].



Constraints:

3 <= n == nums.length <= 10^5
0 <= nums[i] <= 10^5
1 <= queries.length <= 10^5
queries[i] = [1, li, ri] or queries[i] = [2, indexi, vali]
0 <= li < ri <= n - 1
0 <= indexi <= n - 1
0 <= vali <= 10^5
"""


class SegmentTree:
    def __init__(self, nums: list[int]):
        n = len(nums)
        self._n = n
        self._tree = [None] * (4 * n)
        self._build(nums, 1, 0, n - 1)

    def _merge_val(self, a: list[int], b: list[int]) -> list[int]:
        a_sm, a_left, a_right, a_len, a_has = a
        b_sm, b_left, b_right, b_len, b_has = b
        sm = a_sm + b_sm + a_len * b_len - a_right * b_left
        left = a_left if a_has else a_len + b_left
        right = b_right if b_has else b_len + a_right
        return [sm, left, right, a_len + b_len, a_has or b_has]

    def _maintain(self, node: list[int]) -> None:
        self._tree[node] = self._merge_val(self._tree[node * 2], self._tree[node * 2 + 1])

    def _build(self, nums: list[int], node: int, l: int, r: int) -> None:
        if l == r:
            has_peak = 1 <= l <= self._n - 2 and nums[l - 1] < nums[l] > nums[l + 1]
            self._tree[node] = [0, 1, 1, 1, has_peak]
            return

        m = (l + r) // 2
        self._build(nums, node * 2, l, m)
        self._build(nums, node * 2 + 1, m + 1, r)
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, has_peak: bool) -> None:
        if l == r:
            self._tree[node] = [0, 1, 1, 1, has_peak]
            return

        m = (l + r) // 2
        if i <= m:
            self._update(node * 2, l, m, i, has_peak)
        else:
            self._update(node * 2 + 1, m + 1, r, i, has_peak)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> list[int]:
        if ql <= l and r <= qr:
            return self._tree[node]

        m = (l + r) // 2
        if qr <= m:
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(self._query(node * 2, l, m, ql, qr), self._query(node * 2 + 1, m + 1, r, ql, qr))

    def update(self, i: int, has_peak: bool) -> None:
        self._update(1, 0, self._n - 1, i, has_peak)

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)[0]


class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        seg = SegmentTree(nums)
        
        ans = []
        for op, x, y in queries:
            if op == 1:
                ans.append(seg.query(x, y))
            else:
                nums[x] = y
                for i in range(max(1, x - 1), min(n - 1, x + 2)):
                    has_peak = nums[i - 1] < nums[i] > nums[i + 1]
                    seg.update(i, has_peak)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countOfPeaks([1, 3, 2, 4], [[1, 0, 3], [2, 1, 1], [1, 0, 3]]))  # [2, 0]

    # Example 2
    print(sol.countOfPeaks([9, 8, 9, 8], [[1, 1, 3], [2, 2, 1], [1, 0, 2]]))  # [1, 0]

    # Example 3
    print(sol.countOfPeaks([3, 6, 2, 7, 1], [[1, 1, 3], [2, 3, 0], [1, 0, 4]]))  # [0, 3]
