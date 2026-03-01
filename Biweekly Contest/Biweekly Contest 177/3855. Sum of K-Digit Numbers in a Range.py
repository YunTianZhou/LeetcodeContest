"""
3855. Sum of K-Digit Numbers in a Range - Hard


You are given three integers l, r, and k.

Consider all possible integers consisting of exactly k digits, where each digit is chosen independently from the integer range [l, r] (inclusive). If 0 is included in the range, leading zeros are allowed.

Return an integer representing the sum of all such numbers.​​​​​​​ Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: l = 1, r = 2, k = 2

Output: 66

Explanation:

 - All numbers formed using k = 2 digits in the range [1, 2] are 11, 12, 21, 22.

 - The total sum is 11 + 12 + 21 + 22 = 66.


Example 2:

Input: l = 0, r = 1, k = 3

Output: 444

Explanation:

 - All numbers formed using k = 3 digits in the range [0, 1] are 000, 001, 010, 011, 100, 101, 110, 111​​​​​​​.

 - These numbers without leading zeros are 0, 1, 10, 11, 100, 101, 110, 111.

 - The total sum is 444.


Example 3:

Input: l = 5, r = 5, k = 10

Output: 555555520

Explanation:

 - 5555555555 is the only valid number consisting of k = 10 digits in the range [5, 5].

 - The total sum is 5555555555 % (10^9 + 7) = 555555520.



Constraints:

0 <= l <= r <= 9
1 <= k <= 10^9
"""


class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod = 10 ** 9 + 7
        s = ((l + r) * (r - l + 1) // 2)
        x = (pow(10, k, mod) - 1) * pow(9, mod - 2, mod)
        y = pow(r - l + 1, k - 1, mod)
        return s * x * y % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.sumOfNumbers(1, 2, 2))  # 66

    # Example 2
    print(sol.sumOfNumbers(0, 1, 3))  # 444

    # Example 3
    print(sol.sumOfNumbers(5, 5, 10))  # 555555520
