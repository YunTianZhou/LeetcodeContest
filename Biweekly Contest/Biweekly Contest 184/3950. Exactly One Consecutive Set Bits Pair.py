"""
3950. Exactly One Consecutive Set Bits Pair - Easy


You are given an integer n.

Return true if its binary representation contains exactly one pair of consecutive set bits, and false otherwise.



Example 1:

Input: nums = 6

Output: true

Explanation:

 - Binary representation of 6 is 110.

 - There is exactly one pair of consecutive set bits ("11"). Thus, the answer is true.


Example 2:

Input: nums = 5

Output: false

Explanation:

 - Binary representation of 5 is 101.

 - There are no consecutive set bits. Thus, the answer is false.



Constraints:

0 <= n <= 10^5
"""


class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        m = n & (n << 1)
        return m != 0 and m & (m - 1) == 0


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.consecutiveSetBits(6))  # True

    # Example 2
    print(sol.consecutiveSetBits(5))  # False
