"""
3628. Maximum Number of Subsequences After One Inserting - Medium


You are given a string s consisting of uppercase English letters.

You are allowed to insert at most one uppercase English letter at any position (including the beginning or end) of the string.

Return the maximum number of "LCT" subsequences that can be formed in the resulting string after at most one insertion.



Example 1:

Input: s = "LMCT"

Output: 2

Explanation:

We can insert a "L" at the beginning of the string s to make "LLMCT", which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].


Example 2:

Input: s = "LCCT"

Output: 4

Explanation:

We can insert a "L" at the beginning of the string s to make "LLCCT", which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].


Example 3:

Input: s = "L"

Output: 0

Explanation:

Since it is not possible to obtain the subsequence "LCT" by inserting a single letter, the result is 0.



Constraints:

1 <= s.length <= 10^5
s consists of uppercase English letters.

"""


class Solution:
    def numOfSubsequences(self, s: str) -> int:
        dp_lct = [0] * 3
        dp_ct = [0] * 2
        cnt_t = s.count("T")
        increase_c = 0
        for c in s:
            if c == "L":
                dp_lct[0] += 1
            elif c == "C":
                dp_lct[1] += dp_lct[0]
                dp_ct[0] += 1
            elif c == "T":
                dp_lct[2] += dp_lct[1]
                dp_ct[1] += dp_ct[0]
                cnt_t -= 1
            increase_c = max(increase_c, dp_lct[0] * cnt_t)
        
        increase_l = dp_ct[1]
        increase_t = dp_lct[1]
        return dp_lct[2] + max(increase_c, increase_l, increase_t)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.numOfSubsequences("LMCT"))  # 2

    # Example 2
    print(sol.numOfSubsequences("LCCT"))  # 4

    # Example 3
    print(sol.numOfSubsequences("L"))  # 0
