"""
3651. Minimum Cost Path with Teleportations - Hard


You are given a m x n 2D integer array grid and an integer k. You start at the top-left cell (0, 0) and your goal is to reach the bottom-right cell (m - 1, n - 1).

There are two types of moves available:

Normal move: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is the value of the destination cell.

Teleportation: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may teleport at most k times.

Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).



Example 1:

Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2

Output: 7

Explanation:

Initially we are at (0, 0) and cost is 0.

Current Position  Move                New Position  Total Cost
(0, 0)            Move Down           (1, 0)        0 + 2 = 2
(1, 0)            Move Right          (1, 1)        2 + 5 = 7
(1, 1)            Teleport to (2, 2)  (2, 2)        7 + 0 = 7

The minimum cost to reach bottom-right cell is 7.


Example 2:

Input: grid = [[1,2],[2,3],[3,4]], k = 1

Output: 9

Explanation:

Initially we are at (0, 0) and cost is 0.

Current Position  Move        New Position  Total Cost
(0, 0)            Move Down   (1, 0)        0 + 2 = 2
(1, 0)            Move Right  (1, 1)        2 + 3 = 5
(1, 1)            Move Down   (2, 1)        5 + 4 = 9

The minimum cost to reach bottom-right cell is 9.



Constraints:

2 <= m, n <= 80
m == grid.length
n == grid[i].length
0 <= grid[i][j] <= 10^4
0 <= k <= 10
"""

from typing import List
from math import inf


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])

        values = []
        for i in range(n):
            for j in range(m):
                values.append((grid[i][j], i, j))
        values.sort(key=lambda x: x[0], reverse=True)
        
        rank = [[0] * m for _ in range(n)]
        cur_rank = 0
        prev_val = inf
        for r, (val, i, j) in enumerate(values):
            if val < prev_val:
                cur_rank = r
                prev_val = val
            rank[i][j] = cur_rank

        pre_min = [inf] * (n * m)
        dp = [[inf] * m for _ in range(n)]
        for _ in range(k + 1):
            for i in range(n):
                for j in range(m):
                    curr = 0 if i == 0 and j == 0 else pre_min[rank[i][j]]
                    if i > 0:
                        curr = min(curr, grid[i][j] + dp[i - 1][j])
                    if j > 0:
                        curr = min(curr, grid[i][j] + dp[i][j - 1])
                    dp[i][j] = curr
            
            for i in range(n):
                for j in range(m):
                    r = rank[i][j]
                    pre_min[r] = min(pre_min[r], dp[i][j])
            for i in range(1, n * m):
                pre_min[i] = min(pre_min[i - 1], pre_min[i])

        return dp[n - 1][m - 1]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minCost([[1, 3, 3],[2, 5, 4],[4, 3, 5]], 2))  # 7

    # Example 2
    print(sol.minCost([[1, 2],[2, 3],[3, 4]], 1))  # 9
