"""
3624. Number of Integers With Popcount-Depth Equal to K II - Hard


You are given an integer array nums.

For any positive integer x, define the following sequence:

p0 = x
pi+1 = popcount(pi) for all i >= 0, where popcount(y) is the number of set bits (1's) in the binary representation of y.
T
his sequence will eventually reach the value 1.

The popcount-depth of x is defined as the smallest integer d >= 0 such that pd = 1.

For example, if x = 7 (binary representation "111"). Then, the sequence is: 7 → 3 → 2 → 1, so the popcount-depth of 7 is 3.

You are also given a 2D integer array queries, where each queries[i] is either:

[1, l, r, k] - Determine the number of indices j such that l <= j <= r and the popcount-depth of nums[j] is equal to k.
[2, idx, val] - Update nums[idx] to val.

Return an integer array answer, where answer[i] is the number of indices for the ith query of type [1, l, r, k].



Example 1:

Input: nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]

Output: [2,1]

Explanation:

i  queries[i]  nums   binary(nums)  popcount-depth  [l, r]  k  Valid nums[j]  updated nums  Answer
0  [1,0,1,1]   [2,4]  [10, 100]     [1, 1]          [0, 1]  1  [0, 1]         -             2
1  [2,1,1]     [2,4]  [10, 100]     [1, 1]          -       -  -              [2,1]         -
2  [1,0,1,0]   [2,1]  [10, 1]       [1, 0]          [0, 1]  0  [1]            -             1
Thus, the final answer is [2, 1].


Example 2:

Input: nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]

Output: [3,1,0]

Explanation:

i  queries[i]  nums       binary(nums)    popcount-depth  [l, r]  k  Valid nums[j]  updated nums  Answer
0  [1,0,2,2]   [3, 5, 6]  [11, 101, 110]  [2, 2, 2]       [0, 2]  2  [0, 1, 2]      -             3
1  [2,1,4]     [3, 5, 6]  [11, 101, 110]  [2, 2, 2]       -       -  -              [3, 4, 6]     -
2  [1,1,2,1]   [3, 4, 6]  [11, 100, 110]  [2, 1, 2]       [1, 2]  1  [1]            -             1
3  [1,0,1,0]   [3, 4, 6]  [11, 100, 110]  [2, 1, 2]       [0, 1]  0  []             -             0
Thus, the final answer is [3, 1, 0].


Example 3:

Input: nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]

Output: [1,0,1]

Explanation:

i  queries[i] nums    binary(nums)  popcount-depth  [l, r]  k  Valid nums[j]  updated nums  Answer
0  [1,0,1,1]  [1, 2]  [1, 10]       [0, 1]          [0, 1]  1  [1]            -             1
1  [2,0,3]    [1, 2]  [1, 10]       [0, 1]          -       -  -              [3, 2]        -
2  [1,0,0,1]  [3, 2]  [11, 10]      [2, 1]          [0, 0]  1  []             -             0
3  [1,0,0,2]  [3, 2]  [11, 10]      [2, 1]          [0, 0]  2  [0]            -             1
Thus, the final answer is [1, 0, 1].



Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^15
1 <= queries.length <= 10^5
queries[i].length == 3 or 4
queries[i] == [1, l, r, k] or,
queries[i] == [2, idx, val]
0 <= l <= r <= n - 1
0 <= k <= 5
0 <= idx <= n - 1
1 <= val <= 10^15
"""

from typing import List


class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx: int, delta: int):
        idx += 1
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        idx += 1
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

    def range_query(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = 64

        dep = [0] * (m + 1)
        dep[0] = m
        for i in range(2, m + 1):
            dep[i] = 1 + dep[i.bit_count()]

        def popcount_depth(x):
            if x <= m:
                return dep[x]
            else:
                return 1 + dep[x.bit_count()]
        
        bit = [BinaryIndexedTree(n) for _ in range(6)]
        values = [0] * n
        for i, x in enumerate(nums):
            values[i] = popcount_depth(x)
            bit[values[i]].update(i, 1)

        result = []
        for query in queries:
            if query[0] == 1:
                l, r, k = query[1:]
                result.append(bit[k].range_query(l, r))
            elif query[0] == 2:
                idx, val = query[1:]
                old_value = values[idx]
                new_value = popcount_depth(val)

                values[idx] = new_value
                bit[old_value].update(idx, -1)
                bit[new_value].update(idx, 1)

        return result


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.popcountDepth([2, 4], [[1, 0, 1, 1], [2, 1, 1], [1, 0, 1, 0]]))  # [2, 1]

    # Example 2
    print(sol.popcountDepth([3, 5, 6], [[1, 0, 2, 2], [2, 1, 4], [1, 1, 2, 1], [1, 0, 1, 0]]))  # [3, 1, 0]

    # Example 3
    print(sol.popcountDepth([1, 2], [[1, 0, 1, 1], [2, 0, 3], [1, 0, 0, 1], [1, 0, 0, 2]]))  # [1, 0, 1]
