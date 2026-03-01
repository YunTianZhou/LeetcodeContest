"""
3858. Minimum Bitwise OR From Grid - Medium

You are given a 2D integer array grid of size m x n.

You must select exactly one integer from each row of the grid.

Return an integer denoting the minimum possible bitwise OR of the selected integers from each row.



Example 1:

Input: grid = [[1,5],[2,4]]

Output: 3

Explanation:

 - Choose 1 from the first row and 2 from the second row.

 - The bitwise OR of 1 | 2 = 3, which is the minimum possible.


Example 2:

Input: grid = [[3,5],[6,4]]

Output: 5

Explanation:

 - Choose 5 from the first row and 4 from the second row.

 - The bitwise OR of 5 | 4 = 5​​​​​​​, which is the minimum possible.


Example 3:

Input: grid = [[7,9,8]]

Output: 7

Explanation:

 - Choosing 7 gives the minimum bitwise OR.



Constraints:

1 <= m == grid.length <= 10^5
1 <= n == grid[i].length <= 10^5
m * n <= 10^5
1 <= grid[i][j] <= 10^5
"""

from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        b = max(map(max, grid)).bit_length()

        ans = 0
        for i in range(b - 1, -1, -1):
            mask = ans | ((1 << i) - 1)
            for row in grid:
                for x in row:
                    if x | mask == mask:
                        break
                else:
                    ans |= 1 << i
                    break
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minimumOR([[1, 5],[2, 4]]))  # 3

    # Example 2
    print(sol.minimumOR([[3, 5],[6, 4]]))  # 5

    # Example 3
    print(sol.minimumOR([[7, 9, 8]]))  # 7
