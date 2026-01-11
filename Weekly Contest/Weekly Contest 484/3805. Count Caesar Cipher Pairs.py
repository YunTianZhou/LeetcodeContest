"""
3805. Count Caesar Cipher Pairs - Medium


You are given an array words of n strings. Each string has length m and contains only lowercase English letters.

Two strings s and t are similar if we can apply the following operation any number of times (possibly zero times) so that s and t become equal.

 - Choose either s or t.

 - Replace every letter in the chosen string with the next letter in the alphabet cyclically. The next letter after 'z' is 'a'.

Count the number of pairs of indices (i, j) such that:

 - i < j

 - words[i] and words[j] are similar.

Return an integer denoting the number of such pairs.



Example 1:

Input: words = ["fusion","layout"]

Output: 1

Explanation:

words[0] = "fusion" and words[1] = "layout" are similar because we can apply the operation to "fusion" 6 times. The string "fusion" changes as follows.

 - "fusion"
 - "gvtjpo"
 - "hwukqp"
 - "ixvlrq"
 - "jywmsr"
 - "kzxnts"
 - "layout"


Example 2:

Input: words = ["ab","aa","za","aa"]

Output: 2

Explanation:

words[0] = "ab" and words[2] = "za" are similar. words[1] = "aa" and words[3] = "aa" are similar.



Constraints:

1 <= n == words.length <= 10^5
1 <= m == words[i].length <= 10^5
1 <= n * m <= 10^5
words[i] consists only of lowercase English letters.
"""

from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, words: List[str]) -> int:
        cnt = defaultdict(int)

        for word in words:
            k = ord(word[0])
            s = "".join(chr((ord(c) - k) % 26) for c in word)
            cnt[s] += 1
            
        return sum(x * (x - 1) // 2 for x in cnt.values())


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countPairs(["fusion", "layout"]))  # 1

    # Example 2
    print(sol.countPairs(["ab", "aa", "za", "aa"]))  # 2
    