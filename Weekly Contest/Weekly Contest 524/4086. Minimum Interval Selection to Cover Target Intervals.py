"""
4086. Minimum Interval Selection to Cover Target Intervals - Hard


You are given two 2D integer arrays, availableIntervals and targetIntervals, each representing a list of closed intervals.

Select a subset of intervals from availableIntervals so that every real point contained in any interval in targetIntervals belongs to at least one selected interval.

Points outside the target intervals do not need to be covered. Selected intervals may overlap or extend beyond the target intervals.

Return the minimum number of intervals you need to select. If it is impossible to cover all the target intervals, return -1.



Example 1:

Input: availableIntervals = [[1,4],[1,7],[3,9],[5,10],[10,15]], targetIntervals = [[1,3],[2,5],[7,8],[10,13],[11,15],[12,13]]

Output: 3

Explanation:

The target intervals cover the ranges [1, 5], [7, 8], and [10, 15]. By selecting [1, 4], [3, 9], and [10, 15] from availableIntervals, all target intervals can be fully covered with three intervals.


Example 2:

Input: availableIntervals = [[4,6],[1,4],[2,5]], targetIntervals = [[3,4],[2,5],[6,7]]

Output: -1

Explanation:

It is impossible to select intervals from availableIntervals to cover all the intervals in targetIntervals.


Example 3:

Input: availableIntervals = [[1,2],[3,4]], targetIntervals = [[1,4]]

Output: -1

Explanation:

Selecting both available intervals leaves every real point strictly between 2 and 3 uncovered. For example, 2.5 belongs to the target interval but to neither available interval.



Constraints:

1 <= availableIntervals.length, targetIntervals.length <= 5 * 10^4
availableIntervals[i].length == targetIntervals[j].length == 2
1 <= availableIntervals[i][0] <= availableIntervals[i][1] <= 10^5
1 <= targetIntervals[j][0] <= targetIntervals[j][1] <= 10^5
"""

from typing import List


class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        n = len(availableIntervals)
        availableIntervals.sort(key=lambda p: p[0])
        targetIntervals.sort(key=lambda p: p[0])
        
        ans = i = right = 0
        for l, r in targetIntervals:
            while right < r:
                cur = max(l, right)

                while i < n and availableIntervals[i][0] <= cur:
                    right = max(right, availableIntervals[i][1])
                    i += 1
                if right < r and right <= cur:
                    return -1
                
                ans += 1
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    available_intervals = [[1, 4], [1, 7], [3, 9], [5, 10], [10, 15]]
    target_intervals = [[1, 3], [2, 5], [7, 8], [10, 13], [11, 15], [12, 13]]
    print(sol.minSelection(available_intervals, target_intervals))  # 3

    # Example 2
    available_intervals = [[4, 6], [1, 4], [2, 5]]
    target_intervals = [[3, 4], [2, 5], [6, 7]]
    print(sol.minSelection(available_intervals, target_intervals))  # -1

    # Example 3
    available_intervals = [[1, 2], [3, 4]]
    target_intervals = [[1, 4]]
    print(sol.minSelection(available_intervals, target_intervals))  # -1
