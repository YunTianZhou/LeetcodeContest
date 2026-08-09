"""
4016. Maximum Area of Two Non-Overlapping Square Submatrices - Medium


You are given a 2D integer matrix mat of size m x n, where:

 - mat[r][c] == 1 means the cell at row r and column c is usable.

 - mat[r][c] == 0 means it is not usable.

Your task is to find two submatrices that satisfy the following conditions:

 - Both submatrices must be squares of the same side length k.

 - The two submatrices must not share any cell.

 - Each submatrix can only cover cells where mat[r][c] == 1.

Return the maximum possible area of each of the two squares. If it is not possible to choose two such squares, return 0.



Example 1:

[image1](https://assets.leetcode.com/uploads/2026/06/13/image.png)

Input: mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]

Output: 4

Explanation:

The largest equal non-overlapping squares have side length k = 2 with area 4.

 - First square starts at top-left (0, 0) and covers cells (0, 0), (0, 1), (1, 0), and (1, 1).

 - Second square starts at top-left (1, 2) and covers cells (1, 2), (1, 3), (2, 2), and (2, 3).

Thus, the answer is 4.


Example 2:

[image2](https://assets.leetcode.com/uploads/2026/06/13/screenshot-2026-06-13-at-83728pm.png)

Input: mat = [[0,1],[1,0]]

Output: 1

Explanation:

The largest equal non-overlapping squares have side length k = 1 with area 1.

 - First square starts at top-left (0, 1) and covers cell (0, 1).

 - Second square starts at top-left (1, 0) and covers cell (1, 0).

Thus, the answer is 1.


Example 3:

[image3](https://assets.leetcode.com/uploads/2026/06/13/screenshot-2026-06-13-at-83751pm.png)

Input: mat = [[0,0],[0,1]]

Output: 0

Explanation:

There is only one usable cell, so it is impossible to choose two non-overlapping squares. Thus, the answer is 0.



Constraints:

mat.length == m
mat[i].length == n
1 <= m, n <= 500
mat[i][j] is either 0 or 1.
"""


class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        def get_pref(mat: list[list[int]]) -> list[int]:
            n, m = len(mat), len(mat[0])

            dp = [0] * (m + 1)
            pref = [0] * (n + 1)
            for i in range(1, n + 1):
                prev = dp[0]
                for j in range(1, m + 1):
                    dp[j], prev = (
                        min(dp[j], dp[j - 1], prev) + 1 if mat[i - 1][j - 1] == 1 else 0,
                        dp[j]
                    )
                
                pref[i] = max(pref[i - 1], max(dp))
            
            return pref
        
        up = get_pref(mat)
        down = get_pref(mat[::-1])[::-1]
        ans1 = max(min(x, y) for x, y in zip(up, down))

        rotated = list(zip(*mat))
        left = get_pref(rotated)
        right = get_pref(rotated[::-1])[::-1]
        ans2 = max(min(x, y) for x, y in zip(left, right))

        return max(ans1, ans2) ** 2


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxArea([[1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]]))  # 4

    # Example 2
    print(sol.maxArea([[0, 1], [1, 0]]))  # 1

    # Example 3
    print(sol.maxArea([[0, 0], [0, 1]]))  # 0
