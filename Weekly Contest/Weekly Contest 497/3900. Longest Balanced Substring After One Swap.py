"""
3900. Longest Balanced Substring After One Swap - Medium


You are given a binary string s consisting only of characters '0' and '1'.

A string is balanced if it contains an equal number of '0's and '1's.

You can perform at most one swap between any two characters in s. Then, you select a balanced substring from s.

Return an integer representing the maximum length of the balanced substring you can select.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "100001"

Output: 4

Explanation:

 - Swap "100001". The string becomes "101000".

 - Select the substring "101000", which is balanced because it has two '0's and two '1's.


Example 2:

Input: s = "111"

Output: 0

Explanation:

 - Choose not to perform any swaps.

 - Select the empty substring, which is balanced because it has zero '0's and zero '1's.


Constraints:

1 <= s.length <= 10^5
s consists only of the characters '0' and '1'.
"""


class Solution:
    def longestBalanced(self, s: str) -> int:
        lim = min(s.count("0"), s.count("1")) * 2
        
        mp1 = {0: -1}
        mp2 = {}
        ans = x = 0
        for i, c in enumerate(s):
            x += 1 if c == "0" else -1
            for y in (x, x - 2, x + 2):
                d = i - mp1.get(y, i)
                if d > lim:
                    d = i - mp2.get(y, i)
                ans = max(ans, d)
            
            if x not in mp1:
                mp1[x] = i
            elif x not in mp2:
                mp2[x] = i

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestBalanced("100001"))  # 4

    # Example 2
    print(sol.longestBalanced("111"))  # 0
