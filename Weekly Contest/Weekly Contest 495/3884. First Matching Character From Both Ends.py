"""
3884. First Matching Character From Both Ends - Easy


You are given a string s of length n consisting of lowercase English letters.

Return the smallest index i such that s[i] == s[n - i - 1].

If no such index exists, return -1.



Example 1:

Input: s = "abcacbd"

Output: 1

Explanation:

At index i = 1, s[1] and s[5] are both 'b'.

No smaller index satisfies the condition, so the answer is 1.


Example 2:

Input: s = "abc"

Output: 1

Explanation:

At index i = 1, the two compared positions coincide, so both characters are 'b'.

No smaller index satisfies the condition, so the answer is 1.


Example 3:

Input: s = "abcdab"

Output: -1

Explanation:

For every index i, the characters at positions i and n - i - 1 are different.

Therefore, no valid index exists, so the answer is -1.



Constraints:

1 <= n == s.length <= 100
s consists of lowercase English letters.
"""


class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s[i] == s[n - i - 1]:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.firstMatchingIndex("abcacbd"))  # 1

    # Example 2
    print(sol.firstMatchingIndex("abc"))  # 1

    # Example 3
    print(sol.firstMatchingIndex("abcdab"))  # -1
