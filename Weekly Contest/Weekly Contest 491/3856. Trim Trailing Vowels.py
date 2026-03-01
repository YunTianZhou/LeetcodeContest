"""
3856. Trim Trailing Vowels - Easy


You are given a string s that consists of lowercase English letters.

Return the string obtained by removing all trailing vowels from s.

The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "idea"

Output: "id"

Explanation:

Removing "idea", we obtain the string "id".


Example 2:

Input: s = "day"

Output: "day"

Explanation:

There are no trailing vowels in the string "day".


Example 3:

Input: s = "aeiou"

Output: ""

Explanation:

Removing "aeiou", we obtain the string "".



Constraints:

1 <= s.length <= 100
s consists of only lowercase English letters.
"""


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip("aeiou")


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.trimTrailingVowels("idea"))  # "id"

    # Example 2
    print(sol.trimTrailingVowels("day"))  # "day"

    # Example 3
    print(sol.trimTrailingVowels("aeiou"))  # ""
