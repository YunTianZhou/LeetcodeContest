"""
3963. Create Grid With Exactly One Path - Easy


You are given two integers m and n, representing the number of rows and columns of a grid.

Construct any m x n grid consisting only of the characters '.' and '#', where:

  -'.' represents a free cell.

  -'#' represents an obstacle cell.

A valid path is a sequence of free cells that:

 - Starts at the top-left cell (0, 0).

 - Ends at the bottom-right cell (m - 1, n - 1).

 - Moves only:

    - Right, from (i, j) to (i, j + 1), or

    - Down, from (i, j) to (i + 1, j).

Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.



Example 1:

Input: m = 2, n = 3

Output: ["..#","#.."]

Explanation:

[image1](https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61005pm.png)

The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)


Example 2:

Input: m = 3, n = 3

Output: ["..#","#..","##."]

Explanation:

[image2](https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61129pm.png)

The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)


Example 3:

Input: m = 1, n = 4

Output: ["...."]

Explanation:

The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)



Constraints:

1 <= m, n <= 25
"""


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + (m - 1) * ["#" * (n - 1) + "."]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.createGrid(2, 3))  # ["..#","#.."]

    # Example 2
    print(sol.createGrid(3, 3))  # ["..#","#..","##."]

    # Example 3
    print(sol.createGrid(1, 4))  # ["...."]
