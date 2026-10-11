"""
4078. Three Fibonacci Sum - Easy


You are given an integer n.

The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. Its first few terms are 0, 1, 1, 2, 3, 5, 8, 13, ....

Return true if n can be expressed as the sum of three consecutive terms in the Fibonacci sequence, and false otherwise.



Example 1:

Input: n = 16

Output: true

Explanation:

The three consecutive terms 3, 5, and 8 have a sum of 3 + 5 + 8 = 16.


Example 2:

Input: n = 8

Output: false

Explanation:

Although 1 + 2 + 5 = 8, these terms are not consecutive in the Fibonacci sequence. No three consecutive terms have a sum of 8.


Example 3:

Input: n = 2

Output: true

Explanation:

The first three terms have a sum of 0 + 1 + 1 = 2.



Constraints:

1 <= n <= 10^9
"""


m = 10 ** 9

fib = set()
a = b = 1
while a <= m:
    fib.add(a)
    a, b = a + b, a


class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        return n % 2 == 0 and n // 2 in fib


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.threeFibonacciSum(16))  # True

    # Example 2
    print(sol.threeFibonacciSum(8))  # False

    # Example 3
    print(sol.threeFibonacciSum(2))  # True
