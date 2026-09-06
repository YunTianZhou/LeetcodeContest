"""
4046. Minimum Cost Path With At Most K Turns - Hard


You are given a 2D integer array grid of size m x n, where grid[i][j] represents the cost of visiting cell (i, j), and an integer k.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

From each cell, you may move one step in any of the four directions: up, down, left, or right.

The cost of a path is the sum of the values of all visited cells, including the starting and ending cells. If a cell is visited more than once, its value is included each time it is visited.

Return the minimum possible path cost to reach (m - 1, n - 1) using at most k turns. If no such path exists, return -1.

A turn occurs when the direction changes between two consecutive moves. For example, moving right and then down counts as one turn, while moving right and then right does not.



Example 1:

Input: grid = [[2,7,3],[1,4,5]], k = 1

Output: 12

Explanation:

 - An optimal path is (0, 0) -> (1, 0) -> (1, 1) -> (1, 2). The moves are down, right, right.

 - The direction changes from down to right once, so the path uses exactly k = 1 turn.

 - The total path cost is 2 + 1 + 4 + 5 = 12.


Example 2:

Input: grid = [[4,1,9],[3,2,5],[4,8,6]], k = 2

Output: 20

Explanation:

 - An optimal path is (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> (2, 2). The moves are down, right, right, down.

 - The direction changes from down to right and from right to down, so the path uses exactly k = 2 turns.

 - The total path cost is 4 + 3 + 2 + 5 + 6 = 20.


Example 3:

Input: grid = [[1,9],[3,4]], k = 0

Output: -1

Explanation:

 - It is impossible to reach (1, 1) using k = 0 turns. Thus, the answer is -1.



Constraints:

1 <= m == grid.length <= 75
1 <= n == grid[i].length <= 75
0 <= grid[i][j] <= 1000
0 <= k < min(m, n)
"""

from math import inf


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        if n > 1 and m > 1 and k == 0:
            return -1

        dp = [[inf] * m for _ in range(n)]
        ndp = [[inf] * m for _ in range(n)]
        dp[0][0] = grid[0][0]

        for _ in range(k + 1):
            for i in range(n):
                cur = inf
                for j in range(m):
                    cur = min(dp[i][j], cur + grid[i][j])
                    ndp[i][j] = min(ndp[i][j], cur)

                cur = inf
                for j in range(m - 1, -1, -1):
                    cur = min(dp[i][j], cur + grid[i][j])
                    ndp[i][j] = min(ndp[i][j], cur)

            for j in range(m):
                cur = inf
                for i in range(n):
                    cur = min(dp[i][j], cur + grid[i][j])
                    ndp[i][j] = min(ndp[i][j], cur)

                cur = inf
                for i in range(n - 1, -1, -1):
                    cur = min(dp[i][j], cur + grid[i][j])
                    ndp[i][j] = min(ndp[i][j], cur)

            dp, ndp = ndp, dp
        
        return dp[n - 1][m - 1]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minCost([[2, 7, 3], [1, 4, 5]], 1))  # 12

    # Example 2
    print(sol.minCost([[4, 1, 9], [3, 2, 5], [4, 8, 6]], 2))  # 20

    # Example 3
    print(sol.minCost([[1, 9], [3, 4]], 0))  # -1
