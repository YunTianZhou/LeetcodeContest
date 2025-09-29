"""
3700. Number of ZigZag Arrays II - Hard


You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

 - Each element lies in the range [l, r].
 - No two adjacent elements are equal.
 - No three consecutive elements form a strictly increasing or strictly decreasing sequence.

Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).



Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

 - [4, 5, 4]
 - [5, 4, 5]


Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

 - [1, 2, 1], [1, 3, 1], [1, 3, 2]
 - [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
 - [3, 1, 2], [3, 1, 3], [3, 2, 3]

All arrays meet the ZigZag conditions.



Constraints:

3 <= n <= 2000
1 <= l < r <= 2000
"""


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        mod  = 10 ** 9 + 7
        
        mat = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m - 1, m - i - 1, -1):
                mat[i][j] = 1

        cell = [[0] * m for _ in range(m)]
        for i in range(m):
            cell[i][i] = 1

        def mul(a, b):
            c = [[0] * m for _ in range(m)]
            for i in range(m):
                for j in range(m):
                    for k in range(m):
                        c[i][j] += a[i][k] * b[k][j]
                    c[i][j] %= mod
            return c
        
        def qpow(a, x):
            if x == 0:
                return cell
            
            half = qpow(a, x // 2)
            if x % 2 == 0:
                return mul(half, half)
            else:
                return mul(mul(half, half), a)

        final_mat = qpow(mat, n - 1)
        return 2 * sum(final_mat[i][j] for i in range(m) for j in range(m)) % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.zigZagArrays(3, 4, 5))  # 2

    # Example 2
    print(sol.zigZagArrays(3, 1, 3))  # 10
    