"""
3849. Maximum Bitwise XOR After Rearrangement - Medium


You are given two binary strings s and t, each of length n.

You may rearrange the characters of t in any order, but s must remain unchanged.

Return a binary string of length n representing the maximum integer value obtainable by taking the bitwise XOR of s and rearranged t.



Example 1:

Input: s = "101", t = "011"

Output: "110"

Explanation:

 - One optimal rearrangement of t is "011".

 - The bitwise XOR of s and rearranged t is "101" XOR "011" = "110", which is the maximum possible.


Example 2:

Input: s = "0110", t = "1110"

Output: "1101"

Explanation:

 - One optimal rearrangement of t is "1011".

 - The bitwise XOR of s and rearranged t is "0110" XOR "1011" = "1101", which is the maximum possible.


Example 3:

Input: s = "0101", t = "1001"

Output: "1111"

Explanation:

 - One optimal rearrangement of t is "1010".

 - The bitwise XOR of s and rearranged t is "0101" XOR "1010" = "1111", which is the maximum possible.



Constraints:

1 <= n == s.length == t.length <= 2 * 10^5
s[i] and t[i] are either '0' or '1'.
"""


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        n = len(s)

        zero = t.count("0")
        one = n - zero

        ans = []
        for c in s:
            if one > 0 and (zero == 0 or c == "0"):
                one -= 1
                ans.append("1" if c == "0" else "0")
            else:
                zero -= 1
                ans.append(c)

        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumXor("101", "011"))  # "110"

    # Example 2
    print(sol.maximumXor("0110", "1110"))  # "1101"

    # Example 3
    print(sol.maximumXor("0101", "1001"))  # "1111"
