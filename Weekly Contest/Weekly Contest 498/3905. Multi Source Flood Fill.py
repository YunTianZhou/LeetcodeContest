"""
3905. Multi Source Flood Fill - Medium


You are given two integers n and m representing the number of rows and columns of a grid, respectively.

You are also given a 2D integer array sources, where sources[i] = [ri, ci, colori] indicates that the cell (ri, ci) is initially colored with colori. All other cells are initially uncolored and represented as 0.

At each time step, every currently colored cell spreads its color to all adjacent uncolored cells in the four directions: up, down, left, and right. All spreads happen simultaneously.

If multiple colors reach the same uncolored cell at the same time step, the cell takes the color with the maximum value.

The process continues until no more cells can be colored.

Return a 2D integer array representing the final state of the grid, where each cell contains its final color.



Example 1:

Input: n = 3, m = 3, sources = [[0,0,1],[2,2,2]]

Output: [[1,1,2],[1,2,2],[2,2,2]]

Explanation:

The grid at each time step is as follows:

[graph1](https://assets.leetcode.com/uploads/2026/03/29/g50new.png)

At time step 2, cells (0, 2), (1, 1), and (2, 0) are reached by both colors, so they are assigned color 2 as it has the maximum value among them.


Example 2:

Input: n = 3, m = 3, sources = [[0,1,3],[1,1,5]]

Output: [[3,3,3],[5,5,5],[5,5,5]]

Explanation:

The grid at each time step is as follows:

[graph2](https://assets.leetcode.com/uploads/2026/03/29/g51new.png)


Example 3:

Input: n = 2, m = 2, sources = [[1,1,5]]

Output: [[5,5],[5,5]]

Explanation:

The grid at each time step is as follows:

[graph3](https://assets.leetcode.com/uploads/2026/03/29/g52new.png)

Since there is only one source, all cells are assigned the same color.



Constraints:

1 <= n, m <= 10^5
1 <= n * m <= 10^5
1 <= sources.length <= n * m
sources[i] = [ri, ci, colori]
0 <= ri <= n - 1
0 <= ci <= m - 1
1 <= colori <= 10^6
All (ri, ci) in sources are distinct.
"""

from collections import deque


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        ans = [[0] * m for _ in range(n)]
        dq = deque()
        for i, j, c in sorted(sources, reverse=True, key=lambda x: x[2]):
            dq.append((i, j))
            ans[i][j] = c

        while dq:
            i, j = dq.popleft()
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < n and 0 <= nj < m and ans[ni][nj] == 0:
                    dq.append((ni, nj))
                    ans[ni][nj] = ans[i][j]

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.colorGrid(3, 3, [[0, 0, 1], [2, 2, 2]]))  # [[1, 1, 2], [1, 2, 2], [2, 2, 2]]

    # Example 2
    print(sol.colorGrid(3, 3, [[0, 1, 3], [1, 1, 5]]))  # [[3, 3, 3], [5, 5, 5], [5, 5, 5]]

    # Example 3
    print(sol.colorGrid(2, 2, [[1, 1, 5]]))  # [[5, 5], [5, 5]]
