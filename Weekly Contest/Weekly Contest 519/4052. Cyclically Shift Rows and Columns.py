"""
4052. Cyclically Shift Rows and Columns - Easy


You are given an integer n, a 2D integer array grid of size n x n, and two integer arrays rowShift and colShift, each of length n, where:

 - rowShift[i] represents the number of positions to cyclically shift the ith row of grid to the left.

 - colShift[j] represents the number of positions to cyclically shift the jth column of grid upward.

First, cyclically shift each row according to rowShift, then cyclically shift each column of the resulting grid according to colShift.

Return the resulting grid after performing all the shifts.

A cyclic left shift of a row by k positions moves the element at column j to column (j - k + n) % n. All other rows remain unchanged.

A cyclic upward shift of a column by k positions moves the element at row i to row (i - k + n) % n. All other columns remain unchanged.



Example 1:

Input: n = 2, grid = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1]

Output: [[2,4],[3,1]]

Explanation:

The grid changes as follows:

[graph1](https://assets.leetcode.com/uploads/2026/08/18/4743-1.png)


Example 2:

Input: n = 3, grid = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1]

Output: [[7,8,5],[2,3,9],[6,4,1]]

Explanation:

The grid changes as follows:

[graph2](https://assets.leetcode.com/uploads/2026/08/18/4743-2.png)



Constraints:

1 <= n == grid.length == grid[i].length <= 10
1 <= grid[i][j] <= 100
rowShift.length == colShift.length == n
0 <= rowShift[i], colShift[i] < n
"""


class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        res = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                y = (j - rowShift[i]) % n
                x = (i - colShift[y]) % n
                res[x][y] = grid[i][j]
        
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.cyclicShift(2, [[1, 2], [3, 4]], [1, 0], [0, 1]))  # [[2, 4], [3, 1]]

    # Example 2
    print(sol.cyclicShift(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 0], [2, 2, 1]))  # [[7, 8, 5], [2, 3, 9], [6, 4, 1]]
