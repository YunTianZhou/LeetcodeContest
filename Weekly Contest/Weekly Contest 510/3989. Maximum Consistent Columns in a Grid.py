"""
3989. Maximum Consistent Columns in a Grid - Hard


You are given a 2D integer array grid of size m x n, and an integer limit.

You may remove zero or more columns from the grid, but at least one column must remain. The relative order of the remaining columns must be preserved.

A grid is called consistent if for every row i, and for every pair of adjacent remaining columns a and b with a < b, the following holds: |grid[i][b] - grid[i][a]| <= limit.

Return the maximum number of columns that can remain such that the resulting grid is consistent.



Example 1:

Input: grid = [[-2,0,3]], limit = 2

Output: 2

Explanation:

 - Remove column 2 and keep columns 0 and 1, which gives |grid[0][1] - grid[0][0]| = |0 - (-2)| = 2 <= limit.

  - Thus, the maximum number of columns that can remain is 2.


Example 2:

Input: grid = [[1,-1,1],[2,2,2]], limit = 1

Output: 2

Explanation:

 - Remove column 1 and keep columns 0 and 2, which gives
    - |grid[0][2] - grid[0][0]| = |1 - 1| = 0 <= limit and
    - |grid[1][2] - grid[1][0]| = |2 - 2| = 0 <= limit.

 - Thus, the maximum number of columns that can remain is 2.


Example 3:

Input: grid = [[-5,5]], limit = 9

Output: 1

Explanation:

 - Remove either column 0 or column 1, since |grid[0][1] - grid[0][0]| = |5 - (-5)| = 10 > limit.

 - Thus, the maximum number of columns that can remain is 1.

 

Constraints:

1 <= m == grid.length <= 250
1 <= n == grid[i].length <= 250
-10^5 <= grid[i][j] <= 10^5
0 <= limit <= 10^5
"""


class Solution:
    def maxConsistentColumns(self, grid: list[list[int]], limit: int) -> int:
        n, m = len(grid), len(grid[0])

        dp = [1] * m
        for i in range(m):
            for j in range(i - 1, -1, -1):
                if dp[j] >= dp[i] and all(abs(grid[k][i] - grid[k][j]) <= limit for k in range(n)):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxConsistentColumns([[-2, 0, 3]], 2))  # 2

    # Example 2
    print(sol.maxConsistentColumns([[1, -1, 1], [2, 2, 2]], 1))  # 2

    # Example 3
    print(sol.maxConsistentColumns([[-5, 5]], 9))  # 1
