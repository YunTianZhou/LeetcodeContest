"""
3579. Minimum Steps to Convert String with Operations - Hard


You are given two strings, word1 and word2, of equal length. You need to transform word1 into word2.

For this, divide word1 into one or more contiguous substrings. For each substring substr you can perform the following operations:

Replace: Replace the character at any one index of substr with another lowercase English letter.

Swap: Swap any two characters in substr.

Reverse Substring: Reverse substr.

Each of these counts as one operation and each character of each substring can be used in each type of operation at most once (i.e. no single index may be involved in more than one replace, one swap, or one reverse).

Return the minimum number of operations required to transform word1 into word2.

 

Example 1:

Input: word1 = "abcdf", word2 = "dacbe"

Output: 4

Explanation:

Divide word1 into "ab", "c", and "df". The operations are:

For the substring "ab",
Perform operation of type 3 on "ab" -> "ba".
Perform operation of type 1 on "ba" -> "da".
For the substring "c" do no operations.
For the substring "df",
Perform operation of type 1 on "df" -> "bf".
Perform operation of type 1 on "bf" -> "be".


Example 2:

Input: word1 = "abceded", word2 = "baecfef"

Output: 4

Explanation:

Divide word1 into "ab", "ce", and "ded". The operations are:

For the substring "ab",
Perform operation of type 2 on "ab" -> "ba".
For the substring "ce",
Perform operation of type 2 on "ce" -> "ec".
For the substring "ded",
Perform operation of type 1 on "ded" -> "fed".
Perform operation of type 1 on "fed" -> "fef".


Example 3:

Input: word1 = "abcdef", word2 = "fedabc"

Output: 2

Explanation:

Divide word1 into "abcdef". The operations are:

For the substring "abcdef",
Perform operation of type 3 on "abcdef" -> "fedcba".
Perform operation of type 2 on "fedcba" -> "fedabc".
 


Constraints:

1 <= word1.length == word2.length <= 100
word1 and word2 consist only of lowercase English letters.
"""

from collections import defaultdict


class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)

        def tranform_cost(sub1: str, sub2: str) -> int:
            prev = defaultdict(int)
            cost = 0

            for i in range(len(sub1)):
                if sub1[i] != sub2[i]:
                    if prev[sub2[i], sub1[i]] > 0:
                        prev[sub2[i], sub1[i]] -= 1
                    else:
                        prev[(sub1[i], sub2[i])] += 1
                        cost += 1

            return cost
        
        min_op = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                min_op[i][j] = min(tranform_cost(word1[i: j + 1],       word2[i: j + 1]),
                                   tranform_cost(word1[i: j + 1][::-1], word2[i: j + 1]) + 1)


        dp = [n] * (n + 1)
        dp[0] = 0
        for j in range(n):
            for i in range(j + 1):
                dp[j + 1] = min(dp[j + 1], dp[i] + min_op[i][j])

        return dp[n]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations("abcdf", "dacbe"))  # 4

    # Example 2
    print(sol.minOperations("abceded", "baecfef"))  # 4

    # Example 3
    print(sol.minOperations("abcdef", "fedabc"))  # 2
