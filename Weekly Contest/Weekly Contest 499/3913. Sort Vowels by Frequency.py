"""
3913. Sort Vowels by Frequency - Medium


You are given a string s consisting of lowercase English characters.

Rearrange only the vowels in the string so that they appear in non-increasing order of their frequency.

If multiple vowels have the same frequency, order them by the position of their first occurrence in s.

Return the modified string.

Vowels are 'a', 'e', 'i', 'o', and 'u'.

The frequency of a letter is the number of times it occurs in the string.



Example 1:

Input: s = "leetcode"

Output: "leetcedo"

Explanation:

 - Vowels in the string are ['e', 'e', 'o', 'e'] with frequencies: e = 3, o = 1.

 - Sorting in non-increasing order of frequency and placing them back into the vowel positions results in "leetcedo".

 
Example 2:

Input: s = "aeiaaioooa"

Output: "aaaaoooiie"

Explanation:

 - Vowels in the string are ['a', 'e', 'i', 'a', 'a', 'i', 'o', 'o', 'o', 'a'] with frequencies: a = 4, o = 3, i = 2, e = 1.

 - Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in "aaaaoooiie".


Example 3:

Input: s = "baeiou"

Output: "baeiou"

Explanation:

 - Each vowel appears exactly once, so all have the same frequency.

 - Thus, they retain their relative order based on first occurrence, and the string remains unchanged.



Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_set = "aeiou"
        
        cnt = {}
        vowels = []
        for c in s:
            if c in vowel_set:
                if c in cnt:
                    cnt[c] += 1
                else:
                    vowels.append(c)
                    cnt[c] = 1
        
        vowels.sort(reverse=True, key=lambda c: cnt[c])

        ans = list(s)
        j = 0
        for i, c in enumerate(s):
            if c in vowel_set:
                ans[i] = t = vowels[j]
                cnt[t] -= 1
                if cnt[t] == 0:
                    j += 1

        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.sortVowels("leetcode"))  # "leetcedo"

    # Example 2
    print(sol.sortVowels("aeiaaioooa"))  # "aaaaoooiie"

    # Example 3
    print(sol.sortVowels("baeiou"))  # "baeiou"
