"""
4022. K-th Digit in Infinite String - Medium


You are given an integer k.

An infinite string is formed by concatenating the decimal representations of the positive integers, without separators.

For every nonnegative integer b, block b contains the positive integers from 10 * b through 10 * b + 9. The integers in each block are appended as follows:

 - If b is even, append the integers in increasing order.

 - If b is odd, append the integers in decreasing order.

Therefore, the string starts with the integers 1 through 9, followed by 19 through 10, then 20 through 29, then 39 through 30, and so on.

Return the kth digit (1-indexed) of this string.



Example 1:

Input: k = 4

Output: 4

Explanation:

The string begins as "123456789..". The 4th digit is '4'.


Example 2:

Input: k = 15

Output: 7

Explanation:

The string begins as "123456789191817..". The 15th digit is '7'.


Example 3:

Input: k = 11

Output: 9

Explanation:

The string begins as "12345678919..". The 11th digit is '9'.



Constraints:

1 <= k <= 10^15
"""


class Solution:
    def kthDigit(self, k: int) -> int:
        k -= 1

        cnt, length = 9, 1
        while cnt * length <= k:
            k -= cnt * length
            cnt *= 10
            length += 1

        x = cnt // 9 + k // length
        if x // 10 % 2:
            x += 9 - (x % 10) * 2
        
        tail = k % length
        return x // (10 ** (length - tail - 1)) % 10


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.kthDigit(4))  # 4

    # Example 2
    print(sol.kthDigit(15))  # 7

    # Example 3
    print(sol.kthDigit(11))  # 9
