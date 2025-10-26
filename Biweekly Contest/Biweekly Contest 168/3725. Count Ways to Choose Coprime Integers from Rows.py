"""
3725. Count Ways to Choose Coprime Integers from Rows - Hard


You are given a m x n matrix mat of positive integers.

Return an integer denoting the number of ways to choose exactly one integer from each row of mat such that the greatest common divisor of all chosen integers is 1.

Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: mat = [[1,2],[3,4]]

Output: 3

Explanation:

Chosen integer in the first row  Chosen integer in the second row  Greatest common divisor of chosen integers
1                                3                                 1
1                                4                                 1
2                                3                                 1
2                                4                                 2

3 of these combinations have a greatest common divisor of 1. Therefore, the answer is 3.


Example 2:

Input: mat = [[2,2],[2,2]]

Output: 0

Explanation:

Every combination has a greatest common divisor of 2. Therefore, the answer is 0.



Constraints:

1 <= m == mat.length <= 150
1 <= n == mat[i].length <= 150
1 <= mat[i][j] <= 150
"""

from typing import List


mx = 150
divisor = [[] for _ in range(mx + 1)]
for i in range(1, mx + 1):
    for j in range(i, mx + 1, i):
        divisor[j].append(i)


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m = max(max(row) for row in mat)
        mod = 10 ** 9 + 7

        f = [1] * (m + 1)
        for row in mat:
            cnt = [0] * (m + 1)
            for x in row:
                for d in divisor[x]:
                    cnt[d] += 1
            for i in range(1, m + 1):
                f[i] = (f[i] * cnt[i]) % mod
        
        for i in range(m, 0, -1):
            for j in range(i * 2, m + 1, i):
                f[i] -= f[j]
        
        return f[1] % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countCoprime([[1, 2], [3, 4]]))  # 3

    # Example 2
    print(sol.countCoprime([[2, 2], [2, 2]]))  # 0
    