"""
4084. Last Visited Cell in a Directional Grid - Medium


You are given an m x n matrix grid where each cell contains one of the following characters:

 - 'L': move one cell left.

 - 'R': move one cell right.

 - 'U': move one cell up.

 - 'D': move one cell down.

You start at cell (0, 0), which is considered visited. At each step, move to the cell indicated by the character in your current cell.

The process ends if the indicated move would either leave the grid or enter a cell that has already been visited. In either case, the move is not made.

Return an integer array [r, c] representing the row and column indices of the last visited cell. The indices are 0-based.



Example 1:

Input: grid = [["R","D"],["U","L"]]

Output: [1,0]

Explanation:

Start at cell (0, 0), which contains 'R', so move right to (0, 1).

At cell (0, 1), the character is 'D', so move down to (1, 1).

At cell (1, 1), the character is 'L', so move left to (1, 0).

At cell (1, 0), the character is 'U', which indicates moving to (0, 0). However, (0, 0) has already been visited, so this move is not made.

Therefore, the process ends at the last visited cell (1, 0), so the answer is [1, 0].


Example 2:

Input: grid = [["R","R","R"]]

Output: [0,2]

Explanation:

Start at cell (0, 0), which contains 'R', so move right to (0, 1).

At cell (0, 1), the character is 'R', so move right to (0, 2).

At cell (0, 2), the character is 'R', which indicates moving to (0, 3). However, (0, 3) is outside the grid, so this move is not made.

Therefore, the process ends at the last visited cell (0, 2), so the answer is [0, 2].



Constraints:

1 <= m == grid.length <= 10^5
1 <= n == grid[i].length <= 10^5
m * n <= 10^5
grid[i][j] is one of 'L', 'R', 'U', or 'D'.
"""


directions = {
    "U": (-1, 0), 
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        n, m = len(grid), len(grid[0])
        
        vis = [[False] * m for _ in range(n)]
        x = y = 0
        while True:
            vis[x][y] = True

            dx, dy = directions[grid[x][y]]
            i, j = x + dx, y + dy
            if i < 0 or i >= n or j < 0 or j >= m or vis[i][j]:
                break
            
            x, y = i, j
        
        return [x, y]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.lastVisitedCell([["R", "D"], ["U", "L"]]))  # [1, 0]

    # Example 2
    print(sol.lastVisitedCell([["R", "R", "R"]]))  # [0, 2]
