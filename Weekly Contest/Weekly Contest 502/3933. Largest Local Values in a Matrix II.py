"""
3933. Largest Local Values in a Matrix II - Medium


You are given an n x m integer matrix matrix containing non-negative integers.

A non-zero cell (row, col) checks the cells near it as follows:

 - Let x = matrix[row][col].

 - Consider every cell within x rows and x columns of (row, col).

 - Ignore cells that are outside the matrix.

 - Ignore the cells where both the row distance and column distance are exactly x.

The cell (row, col) is a local maximum if it is non-zero and no considered cell has a value greater than x.

Return an integer denoting the number of local maximums in matrix.



Example 1:

Input: matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

Output: 1

[graph1](https://assets.leetcode.com/uploads/2026/05/13/chatgpt-image-may-14-2026-01_53_19-am.png)

Explanation:

 - For the non-zero cell (3, 3), x = matrix[3][3] = 2.

 - The highlighted cells are the considered cells within x rows and x columns of (3, 3).

 - The four cells with both row and column distances equal to x = 2 are ignored.

 - No considered cell has a value greater than 2, so (3, 3) is a local maximum.

 - There are no other non-zero cells, so the answer is 1.


Example 2:

Input: matrix = [[1,2],[3,4]]

Output: 1

Explanation:

Only the cell with value 4 is a local maximum. Every other non-zero cell considers a cell with a greater value.


Example 3:

Input: matrix = [[1,0,1],[0,1,0],[1,0,1]]

Output: 5

Explanation:

 - For a cell with value 1, the considered cells are the cell itself and its 4-directionally adjacent cells that are inside the matrix.

 - Each of the five cells with value 1 only considers cells with values 0 or 1, so all five of them are local maximums.


Example 4:

Input: matrix = [[1,1],[1,1]]

Output: 4

Explanation:

All cells have the same value. Therefore, no cell considers another cell with a greater value, so all 4 cells are local maximums.



Constraints:

1 <= n == matrix.length <= 200
1 <= m == matrix[i].length <= 200
0 <= matrix[i][j] <= 200
"""


class SparseTable2D:
    def __init__(self, data: list[list[int]], op=max):
        self.n = len(data)
        self.m = len(data[0])
        self.op = op

        mx = max(self.n, self.m)
        self.log = [0] * (mx + 1)
        for i in range(2, mx + 1):
            self.log[i] = self.log[i // 2] + 1

        log_n = self.log[self.n] + 1
        log_m = self.log[self.m] + 1

        self.st = [[None] * log_m for _ in range(log_n)]
        self.st[0][0] = [row.copy() for row in data]

        for ky in range(1, log_m):
            w = 1 << (ky - 1)

            prev = self.st[0][ky - 1]
            curr = [[0] * (self.m - (1 << ky) + 1)
                   for _ in range(self.n)]

            for i in range(self.n):
                for j in range(self.m - (1 << ky) + 1):
                    curr[i][j] = op(
                        prev[i][j],
                        prev[i][j + w]
                    )

            self.st[0][ky] = curr

        for kx in range(1, log_n):
            h = 1 << (kx - 1)

            for ky in range(log_m):
                prev = self.st[kx - 1][ky]

                rows = self.n - (1 << kx) + 1
                cols = self.m - (1 << ky) + 1

                curr = [[0] * cols for _ in range(rows)]

                for i in range(rows):
                    for j in range(cols):
                        curr[i][j] = op(
                            prev[i][j],
                            prev[i + h][j]
                        )

                self.st[kx][ky] = curr

    def query(self, x1, y1, x2, y2):
        kx = self.log[x2 - x1 + 1]
        ky = self.log[y2 - y1 + 1]

        nx = x2 - (1 << kx) + 1
        ny = y2 - (1 << ky) + 1

        op = self.op
        st = self.st[kx][ky]

        return op(
            op(st[x1][y1], st[nx][y1]),
            op(st[x1][ny], st[nx][ny])
        )


class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        st = SparseTable2D(matrix)

        def query(u, d, l, r):
            if u > d or l > r:
                return 0
            
            return st.query(
                max(0, u), max(0, l),
                min(n - 1, d), min(m - 1, r)
            )
        
        ans = 0
        for i in range(n):
            for j in range(m):
                x = matrix[i][j]
                if x == 0:
                    continue

                mx = max(query(i - x, i + x, j - x + 1, j + x - 1),
                         query(i - x + 1, i + x - 1, j - x, j + x))
                if x >= mx:
                    ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countLocalMaximums([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]))  # 1
    
    # Example 2
    print(sol.countLocalMaximums([[1, 2], [3, 4]]))  # 1

    # Example 3
    print(sol.countLocalMaximums([[1, 0, 1], [0, 1, 0], [1, 0, 1]]))  # 5

    # Example 4
    print(sol.countLocalMaximums([[1, 1], [1, 1]]))  # 4
