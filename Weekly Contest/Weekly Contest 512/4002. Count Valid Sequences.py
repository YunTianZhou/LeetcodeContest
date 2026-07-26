"""
4002. Count Valid Sequences - Medium


You are given two positive integers n and k.

A valid sequence is a sequence of k positive integers such that:

 - The sum of all integers in the sequence is equal to n.

 - The product of all integers in the sequence is even.

Return the number of valid sequences. Since the answer may be very large, return it modulo 10^9 + 7.

Two sequences are considered different if they differ at any index. For example, [1, 1, 2] and [1, 2, 1] are considered different sequences.



Example 1:

Input: n = 5, k = 3

Output: 3

Explanation:

The sequences of length k = 3 whose sum is 5 are:

Sequence   Product        Parity
[1, 1, 3]  1 * 1 * 3 = 3  Odd
[1, 2, 2]  1 * 2 * 2 = 4  Even
[2, 1, 2]  2 * 1 * 2 = 4  Even
[2, 2, 1]  2 * 2 * 1 = 4  Even
[1, 3, 1]  1 * 3 * 1 = 3  Odd
[3, 1, 1]  3 * 1 * 1 = 3  Odd

There are 3 sequences with an even product, thus the answer is 3.


Example 2:

Input: n = 3, k = 2

Output: 2

Explanation:

The sequences of length k = 2 whose sum is 3 are:

Sequence  Product    Parity
[1, 2]    1 * 2 = 2  Even
[2, 1]    2 * 1 = 2  Even

There are 2 sequences with an even product, thus the answer is 2.


Example 3:

Input: n = 5, k = 5

Output: 0

Explanation:

The only possible sequence of length k = 5 whose sum is 5 is [1, 1, 1, 1, 1], which has an odd product. Thus, the answer is 0.



Constraints:

1 <= n <= 5 * 10^5
1 <= k <= n
"""

m = 5 * 10 ** 5
mod = 10 ** 9 + 7

fact = [1] * (m + 1)
inv_fact = [1] * (m + 1)

for i in range(1, m + 1):
    fact[i] = fact[i - 1] * i % mod

inv_fact[m] = pow(fact[m], mod - 2, mod)
for i in range(m - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] * inv_fact[n - r] % mod


class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        ans = comb(n - 1, k - 1)

        if k % 2 == n % 2:
            m = (n - k) // 2
            ans = (ans - comb(m + k - 1, k - 1)) % mod

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countValidSequences(5, 3))  # 3

    # Example 2
    print(sol.countValidSequences(3, 2))  # 2

    # Example 3
    print(sol.countValidSequences(5, 5))  # 0
