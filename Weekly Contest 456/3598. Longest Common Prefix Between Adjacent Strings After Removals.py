"""
3598. Longest Common Prefix Between Adjacent Strings After Removals - Medium


Remove the element at index i from the words array.
Compute the length of the longest common prefix among all adjacent pairs in the modified array.
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

 

Example 1:

Input: words = ["jump","run","run","jump","run"]

Output: [3,0,0,3,3]

Explanation:

Removing index 0:
words becomes ["run", "run", "jump", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)

Removing index 1:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)

Removing index 2:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)

Removing index 3:
words becomes ["jump", "run", "run", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)

Removing index 4:
words becomes ["jump", "run", "run", "jump"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)


Example 2:

Input: words = ["dog","racer","car"]

Output: [0,0,0]

Explanation:

Removing any index results in an answer of 0.
 


Constraints:

1 <= words.length <= 10^5
1 <= words[i].length <= 10^4
words[i] consists of lowercase English letters.
The sum of words[i].length is smaller than or equal 10^5.
"""

from typing import List
from itertools import pairwise, accumulate


class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n == 1:
            return [0]
        
        def lcp(a, b):
            min_length = min(len(a), len(b))
            for i in range(min_length):
                if a[i] != b[i]:
                    return i
            return min_length
    
        adj_lcp = [lcp(a, b) for a, b in pairwise(words)]
        prefix = list(accumulate(adj_lcp, max, initial=0))
        sufix = list(accumulate(adj_lcp[::-1], max, initial=0))[::-1]

        res = [0] * n
        res[0] = sufix[1]
        res[n - 1] = prefix[n - 2]
        for i in range(1, n - 1):
            res[i] = max(prefix[i - 1], sufix[i + 1], lcp(words[i - 1], words[i + 1]))
        
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestCommonPrefix(["jump", "run", "run", "jump", "run"]))  # [3, 0, 0, 3, 3]

    # Example 2
    print(sol.longestCommonPrefix(["dog", "racer", "car"]))  # [0, 0, 0]
