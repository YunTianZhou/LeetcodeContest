"""
3714. Longest Balanced Substring II - Medium


You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.



Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.


Example 2:

Input: s = "aabcc"

Output: 3

Explanation:

The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.


Example 3:

Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".



Constraints:

1 <= s.length <= 10^5
s contains only the characters 'a', 'b', and 'c'.
"""


class Solution:
    def longestBalanced(self, s: str) -> int:
        s = [ord(c) - ord("a") for c in s]
        ans = 0

        # One letter
        prev = -1
        cnt = 0
        for c in s:
            if c == prev:
                cnt += 1
            else:
                cnt = 1
                prev = c

            ans = max(ans, cnt)

        # Two letters
        for rem in ((0, 1), (1, 2), (0, 2)):
            cnt = [0] * 3
            mp = {0: -1}

            for i, c in enumerate(s):
                if c in rem:
                    cnt[c] += 1
                else:
                    mp.clear()
                
                diff = cnt[rem[0]] - cnt[rem[1]]
                if diff in mp:
                    ans = max(ans, i - mp[diff])
                else:
                    mp[diff] = i

        # Three letters
        mp = {(0, 0): -1}
        cnt = [0] * 3

        for i, c in enumerate(s):
            cnt[c] += 1

            diff = (cnt[0] - cnt[1], cnt[1] - cnt[2])
            if diff in mp:
                ans = max(ans, i - mp[diff])
            else:
                mp[diff] = i
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestBalanced("abbac"))  # 4

    # Example 2
    print(sol.longestBalanced("aabcc"))  # 3

    # Example 3
    print(sol.longestBalanced("aba"))  # 2
