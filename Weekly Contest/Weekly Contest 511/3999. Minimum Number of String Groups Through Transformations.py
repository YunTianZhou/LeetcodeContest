"""
3999. Minimum Number of String Groups Through Transformations - Hard


You are given an array of strings words.

Define a transformation on a string s as follows:

 - Let E be the subsequence of characters at even indices of s.

 - Let O be the subsequence of characters at odd indices of s.

 - Independently cyclically shift E and O by any number of positions to the right, possibly zero.

 - Reconstruct the string by placing the shifted E characters back into even indices and the shifted O characters back into odd indices.

 - Two strings are equivalent if one can be transformed into the other by a single transformation.

Partition words into the minimum number of groups such that:

 - Every string belongs to exactly one group.

 - Every pair of strings in the same group are equivalent.

Return an integer denoting the minimum number of groups.



Example 1:

Input: words = ["ntgwz","zwntg"]

Output: 1

Explanation:

 - For "ntgwz", the even-index subsequence is "ngz" and the odd-index subsequence is "tw".

 - Shift "ngz" right by 1 position to obtain "zng", and shift "tw" right by 1 position to obtain "wt".

 - After reconstructing the string, we obtain "zwntg".

 - Therefore, both strings are equivalent and belong to the same group.


Example 2:

Input: words = ["abc","cab","bac","acb","bca","cba"]

Output: 3

Explanation:

The strings can be partitioned into the following groups:

 - ["abc","cba"]
 - ["cab","bac"]
 - ["acb","bca"]


Example 3:

Input: words = ["leet","abb","bab","deed","edde","code","bba"]

Output: 5

Explanation:

The strings can be partitioned into the following groups:

 - ["abb","bba"]
 - ["deed","edde"]
 - ["leet"]
 - ["bab"]
 - ["code"]

All pairs of strings in each group are equivalent.



Constraints:

1 <= words.length <= 10^5
1 <= words[i].length <= 5 * 10^5
The sum of words[i].length does not exceed 5 * 10^5.
words[i] consist of lowercase English letters.
"""


class Solution:
    def minimumGroups(self, words: list[str]) -> int:
        def get_id(s):
            n = len(s)
            s = s + s

            i, j, k = 0, 1, 0
            while j < n and k < n:
                if s[i + k] == s[j + k]:
                    k += 1
                elif s[i + k] < s[j + k]:
                    j += k + 1
                    k = 0
                else:
                    i, j = j, max(i + k, j) + 1
                    k = 0
            
            return s[i: i + n]

        return len({get_id(s[::2]) + get_id(s[1::2]) for s in words})


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minimumGroups(["ntgwz", "zwntg"]))  # 1

    # Example 2
    print(sol.minimumGroups(["abc", "cab", "bac", "acb", "bca", "cba"]))  # 3

    # Example 3
    print(sol.minimumGroups(["leet", "abb", "bab", "deed", "edde", "code", "bba"]))  # 5
