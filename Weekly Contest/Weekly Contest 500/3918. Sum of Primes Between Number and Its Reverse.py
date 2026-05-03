"""
3918. Sum of Primes Between Number and Its Reverse- Medium


You are given an integer n.

Let r be the integer formed by reversing the digits of n.

Return the sum of all prime numbers between min(n, r) and max(n, r), inclusive.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.



Example 1:

Input: n = 13

Output: 132

Explanation:

 - The reverse of 13 is 31. Thus, the range is [13, 31].

 - The prime numbers in this range are 13, 17, 19, 23, 29, and 31.

 - The sum of these prime numbers is 13 + 17 + 19 + 23 + 29 + 31 = 132.


Example 2:

Input: n = 10

Output: 17

Explanation:

 - The reverse of 10 is 1. Thus, the range is [1, 10].

 - The prime numbers in this range are 2, 3, 5, and 7.

 - The sum of these prime numbers is 2 + 3 + 5 + 7 = 17.


Example 3:

Input: n = 8

Output: 0

Explanation:

 - The reverse of 8 is 8. Thus, the range is [8, 8].

 - There are no prime numbers in this range, so the sum is 0.



Constraints:

1 <= n <= 1000
"""

from bisect import bisect_left, bisect_right
from itertools import accumulate


m = 1000

is_prime = [True] * (m + 2)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, m + 1) if is_prime[i]]
pref = list(accumulate(primes, initial=0))


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        if n > r:
            n, r = r, n
        return pref[bisect_right(primes, r)] - pref[bisect_left(primes, n)]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.sumOfPrimesInRange(13))  # 132

    # Example 2
    print(sol.sumOfPrimesInRange(10))  # 17

    # Example 3
    print(sol.sumOfPrimesInRange(8))  # 0
