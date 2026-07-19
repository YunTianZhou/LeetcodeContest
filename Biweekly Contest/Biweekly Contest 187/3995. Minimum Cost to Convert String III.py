"""
3995. Minimum Cost to Convert String III - Hard


You are given two strings, source and target.

You are also given a 2D string array rules, where rules[i] = [patterni, replacementi], and an integer array costs, where costs[i] is the base cost of applying rules[i]. Both arrays have the same length. Additionally, patterni and replacementi have the same length.

You may apply any rule any number of times. Each rule application works as follows:

 - Choose an index l such that the range of positions from l to l + patterni.length - 1 exists in the current string and none of these positions has been used in a previous rule application.

 - For each index j, the character patterni[j] must either be equal to the current character at position l + j, or be '*'.

 - Replace the characters in this range with replacementi. The replacement is used exactly as given and does not contain wildcards.

 - The cost of this rule application is costs[i] plus the number of '*' characters in patterni.

 - Once a character position has been used in a rule application, it cannot be used in any later rule application.

Since every patterni and replacementi have the same length, character positions are preserved after every rule application.

Return the minimum total cost required to transform source into target. If it is impossible, return -1.



Example 1:

Input: source = "hello", target = "world", rules = [["he","wo"],["llo","rld"]], costs = [3,4]

Output: 7

Explanation:

 - Apply rules[0] to replace "he" with "wo" at cost 3, so the string becomes "wollo".

 - Apply rules[1] to replace "llo" with "rld" at cost 4, so the string becomes "world".

 - The total cost is 3 + 4 = 7.


Example 2:

Input: source = "cat", target = "dog", rules = [["c*t","dog"]], costs = [2]

Output: 3

Explanation:

 - Apply rules[0] to replace "cat" with "dog". The wildcard '*' matches 'a', adding 1 to the base cost 2.

 - The total cost is 2 + 1 = 3.


Example 3:

Input: source = "test", target = "next", rules = [["*e*t","next"]], costs = [4]

Output: 6

Explanation:

 - Apply rules[0] to replace "test" with "next". The first wildcard matches 't' and the second wildcard matches 's', adding 2 to the base cost 4.

 - The total cost is 4 + 2 = 6.


Example 4:

Input: source = "ab", target = "bc", rules = [["a*","bd"]], costs = [9]

Output: -1

Explanation:

No sequence of rule applications can transform source into target, so the answer is -1.



Constraints:

1 <= source.length, target.length <= 5000
source and target consist of lowercase English letters.
1 <= rules.length == costs.length <= 200
rules[i] = [patterni, replacementi]
1 <= patterni.length == replacementi.length <= 20
patterni contains at least one lowercase English letter and at most 5 '*' characters.
replacementi contains only lowercase English letters.
1 <= costs[i] <= 1000
"""

from math import inf


class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        if len(target) != n:
            return -1

        for i, (pattern, replacement) in enumerate(rules):
            costs[i] += pattern.count("*")

        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            for (pattern, replacement), cost in zip(rules, costs):
                m = len(pattern)
                if i + m > n:
                    continue
                
                c = cost + dp[i]
                if c >= dp[i + m]:
                    continue

                if replacement != target[i: i + m]:
                    continue
                
                if any(p != "*" and p != s for p, s in zip(pattern, source[i: i + m])):
                    continue
                
                dp[i + m] = c
        
        return dp[n] if dp[n] != inf else -1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minCost("hello", "world", [["he", "wo"], ["llo", "rld"]], [3, 4]))  # 7

    # Example 2
    print(sol.minCost("cat", "dog", [["c*t", "dog"]], [2]))  # 3

    # Example 3
    print(sol.minCost("test", "next", [["*e*t", "next"]], [4]))  # 6

    # Example 4
    print(sol.minCost("ab", "bc", [["a*", "bd"]], [9]))  # -1
