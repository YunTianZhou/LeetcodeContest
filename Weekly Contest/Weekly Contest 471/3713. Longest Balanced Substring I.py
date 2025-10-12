"""
3713. Longest Balanced Substring I - Medium


You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.



Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.


Example 2:

Input: s = "zzabccy"

Output: 4

Explanation:

The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​


Example 3:

Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".



Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(n):
            mp = defaultdict(int)
            mx = cnt = 0
            
            for j in range(i, n):
                mp[s[j]] += 1
                curr = mp[s[j]]

                if curr > mx:
                    mx = curr
                    cnt = 1
                elif curr == mx:
                    cnt += 1
                
                if cnt == len(mp):
                    ans = max(ans, j - i + 1)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestBalanced("abbac"))  # 4

    # Example 2
    print(sol.longestBalanced("zzabccy"))  # 4

    # Example 3
    print(sol.longestBalanced("aba"))  # 2
    