"""
3619. Count Islands With Total Value Divisible by K - Medium


You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.



Example 1:

[graph1](https://assets.leetcode.com/uploads/2025/03/06/example1griddrawio-1.png)

Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.


Example 2:

[graph2](https://assets.leetcode.com/uploads/2025/03/06/example2griddrawio.png)

Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.



Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
0 <= grid[i][j] <= 10^6
1 <= k <= 10^6
"""

from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            res = grid[i][j]
            grid[i][j] = 0
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] > 0:
                    res += dfs(ni, nj)
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    val = dfs(i, j)
                    if val % k == 0:
                        ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countIslands([[0, 2, 1, 0, 0], 
                            [0, 5, 0, 0, 5], 
                            [0, 0, 1, 0, 0], 
                            [0, 1, 4, 7, 0], 
                            [0, 2, 0, 0, 8]], 5))  # 2
    
    # Example 2
    print(sol.countIslands([[3, 0, 3, 0], 
                            [0, 3, 0, 3], 
                            [3, 0, 3, 0]], 3))  # 6
    