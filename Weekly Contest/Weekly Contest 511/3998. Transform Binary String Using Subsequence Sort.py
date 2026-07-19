"""
3998. Transform Binary String Using Subsequence Sort - Medium


You are given a binary string s.

You are also given an array of strings strs, where each strs[i] has the same length as s and consists of characters '0', '1', and '?'. Each '?' can be replaced by either '0' or '1'.

You may perform the following operation any number of times (including zero):

 - Choose any subsequence sub of s.

 - Sort sub in non-decreasing order.

 - Replace the chosen subsequence in s with the sorted sub, keeping all other characters unchanged.

Return a boolean array ans, where ans[i] is true if it's possible to replace all '?' in strs[i] with '0' or '1' and transform s into the resulting string using the allowed operation above, otherwise return false.



Example 1:

Input: s = "101", strs = ["1?1","0?1","0?0"]

Output: [true,true,false]

Explanation:

i  strs[i]  Replacement  Result strs[i]  Operation(s)                                            Result
0  "1?1"    ? → 0        "101"           Matches s.                                              true
1  "0?1"    ? → 1        "011"           Select the subsequence at indices [0..2] of s → "101".  true
                                         Sort "101" to get "011" = strs[i].
2  "0?0"    ? → 0 or 1   "000" or "010"  Not feasible.                                           false

Thus, ans = [true, true, false].


Example 2:

Input: s = "1100", strs = ["0011","11?1","1?1?"]

Output: [true,false,true]

Explanation:

i  strs[i]  Replacement           Result strs[i]  Operation(s)                                             Result
0  "0011"   -                     "0011"          Select the subsequence at indices [0..3] of s → "1100".  true
                                                  Sort "1100" to get "0011" = strs[i].
1  "11?1"   ? → 0                 "1101"          Not feasible.                                            false
2  "1?1?"   First ? → 0           "1010"          Select the subsequence at indices [1, 2] of s → "10".    true
            Second ? → 0                          Sort "10" to get "01", so s = "1010".

Thus, ans = [true, false, true].


Example 3:

Input: s = "1010", strs = ["0011"]

Output: [true]

Explanation:

i  strs[i]  Replacement  Result strs[i]  Operation(s)                                               Result
0  "0011"   -            "0011"          Select the subsequence at indices [0, 2, 3] of s → "110".  true
                                         Sort "110" to get "011", so s = "0011" = strs[i].

Thus, ans = [true].



Constraints:

1 <= n == s.length <= 2000
s[i] is either '0' or '1'.
1 <= strs.length <= 2000
strs[i].length == n
strs[i] is either '0', '1', or '?'.
"""


class Solution:
    def transformStr(self, s: str, strs: list[str]) -> list[bool]:
        s_cnt0 = s.count("0")

        def check(t):
            cnt0 = t.count("0")
            if cnt0 > s_cnt0:
                return False
            
            rem = s_cnt0 - cnt0
            sm = 0
            for a, b in zip(s, t):
                if a == "1":
                    sm += 1
                
                if b == "?":
                    if rem > 0:
                        rem -= 1
                    else:
                        sm -= 1
                elif b == "1":
                    sm -= 1

                if sm < 0:
                    return False

            return True

        return [check(t) for t in strs]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.func(...))  # <output 1>

    # Example 2
    print(sol.func(...))  # <output 2>
