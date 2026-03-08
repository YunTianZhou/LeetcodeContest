"""
3863. Minimum Operations to Sort a String - Medium


You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.



Example 1:

Input: s = "dog"

Output: 1

Explanation:

 - Sort substring "og" to "go".

 - Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.


Example 2:

Input: s = "card"

Output: 2

Explanation:

 - Sort substring "car" to "acr", so s = "acrd".

 - Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.


Example 3:

Input: s = "gf"

Output: -1

Explanation:

 - It is impossible to sort s under the given constraints. Thus, the answer is -1.



Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.
"""

from itertools import pairwise


class Solution:
    def minOperations(self, s: str) -> int:
        if all(a <= b for a, b in pairwise(s)):
            return 0
        if len(s) <= 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        
        center = s[1: -1]
        return 2 if mx in center or mn in center else 3
        


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations("dog"))  # 1

    # Example 2
    print(sol.minOperations("card"))  # 2

    # Example 3
    print(sol.minOperations("gf"))  # -1
