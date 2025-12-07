"""
3770. Largest Prime from Consecutive Prime Sum - Medium


You are given an integer n.

Return the largest prime number less than or equal to n that can be expressed as the sum of one or more consecutive prime numbers starting from 2. If no such number exists, return 0.



Example 1:

Input: n = 20

Output: 17

Explanation:

The prime numbers less than or equal to n = 20 which are consecutive prime sums are:

 - 2 = 2

 - 5 = 2 + 3

 - 17 = 2 + 3 + 5 + 7

The largest is 17, so it is the answer.


Example 2:

Input: n = 2

Output: 2

Explanation:

The only consecutive prime sum less than or equal to 2 is 2 itself.



Constraints:

1 <= n <= 5 * 10^5
"""

from typing import List
from bisect import bisect_right


m = 5 * 10 ** 5

is_prime = [True] * (m + 2)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False

sm = 0
prime_ps = [0]
for i in range(2, m + 1):
    if is_prime[i]:
        sm += i
        if sm > m:
            break
        if is_prime[sm]:
            prime_ps.append(sm)

class Solution:
    def largestPrime(self, n: int) -> int:
        return prime_ps[bisect_right(prime_ps, n) - 1]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.largestPrime(20))  # 17

    # Example 2
    print(sol.largestPrime(2))  # 2

