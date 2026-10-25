"""
4090. Count Magical Substring Pairs I - Medium


You are given a string s of length n consisting of lowercase English letters.

For every triplet of indices (i, j, k) satisfying 0 <= i <= j < k < n, define:

s1 = s[i..j]
s2 = s[j + 1..k]

A pair of substrings (s1, s2) is called magical if the number of distinct characters in s1 is equal to the number of distinct characters in s2.

Return the number of triplets (i, j, k) for which (s1, s2) is a magical pair.

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: s = "aba"

Output: 2

Explanation:

There are 2 valid triplets:

No.    (i, j, k)    s1     s2     distinct(s1)    distinct(s2)
1      (0, 0, 1)    "a"    "b"    1               1
2      (1, 1, 2)    "b"    "a"    1               1


Example 2:

Input: s = "kkk"

Output: 4

Explanation:

There are 4 valid triplets:

No.    (i, j, k)    s1      s2      distinct(s1)    distinct(s2)
1      (0, 0, 1)    "k"     "k"     1               1
2      (0, 0, 2)    "k"     "kk"    1               1
3      (0, 1, 2)    "kk"    "k"     1               1
4      (1, 1, 2)    "k"     "k"     1               1


Example 3:

Input: s = "abcac"

Output: 7

Explanation:

There are 7 valid triplets:

No.    (i, j, k)    s1      s2       distinct(s1)    distinct(s2)
1      (0, 0, 1)    "a"     "b"      1               1
2      (1, 1, 2)    "b"     "c"      1               1
3      (2, 2, 3)    "c"     "a"      1               1
4      (3, 3, 4)    "a"     "c"      1               1
5      (0, 1, 3)    "ab"    "ca"     2               2
6      (0, 1, 4)    "ab"    "cac"    2               2
7      (1, 2, 4)    "bc"    "ac"     2               2



Constraints:

2 <= s.length <= 2000
s consists of lowercase English letters.
"""


class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        a = [ord(c) - ord("a") for c in s]

        ans = 0
        for j in range(n):
            freq = [0] * 27

            vis = [False] * 26
            cnt = 0
            for i in range(j, -1, -1):
                if not vis[a[i]]:
                    vis[a[i]] = True
                    cnt += 1
                freq[cnt] += 1
            
            vis = [False] * 26
            cnt = 0
            for k in range(j + 1, n):
                if not vis[a[k]]:
                    vis[a[k]] = True
                    cnt += 1
                ans += freq[cnt]
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countMagicalPairs("aba"))  # 2

    # Example 2
    print(sol.countMagicalPairs("kkk"))  # 4

    # Example 3
    print(sol.countMagicalPairs("abcac"))  # 7
