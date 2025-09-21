"""
3690. Split and Merge Array Transformation - Medium


You are given two integer arrays nums1 and nums2, each of length n. You may perform the following split-and-merge operation on nums1 any number of times:

 - Choose a subarray nums1[L..R].
 - Remove that subarray, leaving the prefix nums1[0..L-1] (empty if L = 0) and the suffix nums1[R+1..n-1] (empty if R = n - 1).
 - Re-insert the removed subarray (in its original order) at any position in the remaining array (i.e., between any two elements, at the very start, or at the very end).

Return the minimum number of split-and-merge operations needed to transform nums1 into nums2.



Example 1:

Input: nums1 = [3,1,2], nums2 = [1,2,3]

Output: 1

Explanation:

Split out the subarray [3] (L = 0, R = 0); the remaining array is [1,2].

Insert [3] at the end; the array becomes [1,2,3].


Example 2:

Input: nums1 = [1,1,2,3,4,5], nums2 = [5,4,3,2,1,1]

Output: 3

Explanation:

Remove [1,1,2] at indices 0 - 2; remaining is [3,4,5]; insert [1,1,2] at position 2, resulting in [3,4,1,1,2,5].

Remove [4,1,1] at indices 1 - 3; remaining is [3,2,5]; insert [4,1,1] at position 3, resulting in [3,2,5,4,1,1].

Remove [3,2] at indices 0 - 1; remaining is [5,4,1,1]; insert [3,2] at position 2, resulting in [5,4,3,2,1,1].



Constraints:

2 <= n == nums1.length == nums2.length <= 6
-10^5 <= nums1[i], nums2[i] <= 10^5
nums2 is a permutation of nums1.
"""

from typing import List
from collections import deque


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1 = tuple(nums1)
        nums2 = tuple(nums2)

        def nxt(state):
            for l in range(n):
                for r in range(l, n):
                    move = state[l: r + 1]
                    leave = state[: l] + state[r + 1: ]

                    for k in range(len(leave) + 1):
                        yield leave[: k] + move + leave[k: ]
        
        dq = deque([nums1])
        visit = {nums1}
        ans = 0

        while dq:
            for _ in range(len(dq)):
                state = dq.popleft()
                if state == nums2:
                    return ans
                for nstate in nxt(state):
                    if nstate not in visit:
                        dq.append(nstate)
                        visit.add(nstate)
            ans += 1
        
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minSplitMerge([3, 1, 2], [1, 2, 3]))  # 1

    # Example 2
    print(sol.minSplitMerge([1, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 1]))  # 3
    