"""
3614. Process String with Special Operations II - Hard


You are given a string s consisting of lowercase English letters and the special characters: '*', '#', and '%'.

You are also given an integer k.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.

Return the kth character of the final string result. If k is out of the bounds of result, return '.'.



Example 1:

Input: s = "a#b%*", k = 1

Output: "a"

Explanation:

i  s[i]  Operation                  Current result
0  'a'   Append 'a'                 "a"
1  '#'   Duplicate result           "aa"
2  'b'   Append 'b'                 "aab"
3  '%'   Reverse result             "ba"
4  '*'   Remove the last character  "ba"
The final result is "ba". The character at index k = 1 is 'a'.


Example 2:

Input: s = "cd%#*#", k = 3

Output: "d"

Explanation:

i  s[i]  Operation                  Current result
0  'c'   Append 'c'                 "c"
1  'd'   Append 'd'                 "cd"
2  '%'   Reverse result             "dc"
3  '#'   Duplicate result           "dcdc"
4  '*'   Remove the last character  "dcd"
5  '#'   Duplicate result           "dcddcd"
The final result is "dcddcd". The character at index k = 3 is 'd'.


Example 3:

Input: s = "z*#", k = 0

Output: "."

Explanation:

i  s[i]  Operation                  Current result
0  'z'   Append 'z'                 "z"
1  '*'   Remove the last character  ""
2  '#'   Duplicate the string       ""
The final result is "". Since index k = 0 is out of bounds, the output is '.'.



Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters and special characters '*', '#', and '%'.
0 <= k <= 10^15
The length of result after processing s will not exceed 10^15.
"""


class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for c in s:
            if c == '*':
                if length > 0:
                    length -= 1
            elif c == '#':
                length *= 2
            elif c == '%':
                # Reversing doesn't change the length
                pass
            else:
                length += 1

        if k >= length:
            return '.'
        
        for c in reversed(s):
            if c == '*':
                length += 1
            elif c == '#':
                length //= 2
                if k >= length:
                    k -= length
            elif c == '%':
                k = length - k - 1
            else:
                length -= 1
                if k >= length:
                    return c


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.processStr("a#b%*", 1))  # "a"

    # Example 2
    print(sol.processStr("cd%#*#", 3))  # "d"

    # Example 3
    print(sol.processStr("z*#", 0))  # "."
