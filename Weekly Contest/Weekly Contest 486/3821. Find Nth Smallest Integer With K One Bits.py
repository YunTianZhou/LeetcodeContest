"""
3821. Find Nth Smallest Integer With K One Bits - Hard


You are given two positive integers n and k.

Return an integer denoting the nth smallest positive integer that has exactly k ones in its binary representation. It is guaranteed that the answer is strictly less than 250.



Example 1:

Input: n = 4, k = 2

Output: 9

Explanation:

The 4 smallest positive integers that have exactly k = 2 ones in their binary representations are:

 - 3 = 112
 - 5 = 1012
 - 6 = 1102
 - 9 = 10012


Example 2:

Input: n = 3, k = 1

Output: 4

Explanation:

The 3 smallest positive integers that have exactly k = 1 one in their binary representations are:

 - 1 = 12
 - 2 = 102
 - 4 = 1002



Constraints:

1 <= n <= 2^50
1 <= k <= 50
The answer is strictly less than 2^50.
"""


m = 50

comb = [[0] * (m + 1) for _ in range(m + 1)]
for i in range(m + 1):
    comb[i][0] = 1
    for j in range(1, i + 1):
        comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1]

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        for i in range(m - 1, -1, -1):
            x = comb[i][k]
            if x < n:
                ans |= 1 << i
                n -= x
                k -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.nthSmallest(4, 2))  # 9

    # Example 2
    print(sol.nthSmallest(3, 1))  # 4
    