"""
3567. Minimum Absolute Difference in Sliding Submatrix - Medium


You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
 


Example 1:

Input: grid = [[1,8],[3,-2]], k = 2

Output: [[2]]

Explanation:

There is only one possible k x k submatrix: [[1, 8], [3, -2]].
Distinct values in the submatrix are [1, 8, 3, -2].
The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].


Example 2:

Input: grid = [[3,-1]], k = 1

Output: [[0,0]]

Explanation:

Both k x k submatrix has only one distinct element.
Thus, the answer is [[0, 0]].


Example 3:

Input: grid = [[1,-2,3],[2,3,5]], k = 2

Output: [[1,2]]

Explanation:

There are two possible k x k submatrix:
Starting at (0, 0): [[1, -2], [2, 3]].
Distinct values in the submatrix are [1, -2, 2, 3].
The minimum absolute difference in the submatrix is |1 - 2| = 1.
Starting at (0, 1): [[-2, 3], [3, 5]].
Distinct values in the submatrix are [-2, 3, 5].
The minimum absolute difference in the submatrix is |3 - 5| = 2.
Thus, the answer is [[1, 2]].
 


Constraints:

1 <= m == grid.length <= 30
1 <= n == grid[i].length <= 30
-10^5 <= grid[i][j] <= 10^5
1 <= k <= min(m, n)
"""

from typing import List
from itertools import pairwise


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        
        res = [[0] * (m - k + 1) for _ in range(n - k + 1)]
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                sub = list(sorted(x for row in grid[i: i + k] for x in row[j: j + k]))
                res[i][j] = min((y - x for x, y in pairwise(sub) if x != y), default=0)
        
        return res
        


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minAbsDiff([[1, 8], [3, -2]], 2))  # [[2]]

    # Example 2
    print(sol.minAbsDiff([[3, -1]], 1))  # [[0, 0]]

    # Example 3
    print(sol.minAbsDiff([[1, -2, 3], [2, 3, 5]], 2))  # [[1, 2]]

    # Additional test cases
    print(sol.minAbsDiff([[5, 5], [5, 5]], 2))  # [[0]]

    print(sol.minAbsDiff([
        [1, 3, 6, 10],
        [2, 8, 5, 7],
        [9, 4, 3, 2],
        [6, 1, 0, -1]
    ], 3))  # [[1, 1], [1, 1]]

    print(sol.minAbsDiff([[7]], 1))  # [[0]]
