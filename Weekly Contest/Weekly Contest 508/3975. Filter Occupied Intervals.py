"""
3975. Filter Occupied Intervals - Medium


You are given a 2D integer array occupiedIntervals, where occupiedIntervals[i] = [starti, endi] represents a time interval during which you are occupied. Each interval starts at starti and ends at endi, inclusive. These intervals may overlap.

You are also given two integers freeStart and freeEnd, which define a free time interval from freeStart to freeEnd, inclusive.

Your task is to merge all occupied intervals that overlap or touch, then remove all integer points in the free interval from the merged occupied intervals.

Two intervals touch if the second interval starts immediately after the first one ends. For example, [1, 1] and [2, 2] touch and should be merged into [1, 2].

Return the remaining occupied intervals in sorted order. The returned intervals must be non-overlapping and must contain the minimum number of intervals possible. If there are no remaining occupied points, return an empty list.



Example 1:

Input: occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11

Output: [[2,6],[12,12],[14,16]]

Explanation:

 - After merging, the occupied intervals are [2, 8], [10, 12], and [14, 16].

 - Excluding the free interval [7, 11] results in [2, 6], [12, 12], and [14, 16].


Example 2:

Input: occupiedIntervals = [[1,5],[2,3]], freeStart = 3, freeEnd = 8

Output: [[1,2]]

Explanation:

 - After merging, the occupied interval is [1, 5].

 - Excluding the free interval [3, 8] results in [1, 2].



Constraints:

1 <= occupiedIntervals.length <= 5 * 10^4
occupiedIntervals[i].length == 2
1 <= starti <= endi <= 10^9
1 <= freeStart <= freeEnd <= 10^9
"""


class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: list[list[int]], freeStart: int, freeEnd: int) -> list[list[int]]:
        occupiedIntervals.sort(key=lambda x: x[1])
        
        res = []
        for l, r in occupiedIntervals:
            while res and res[-1][1] + 1 >= l:
                l = min(l, res[-1][0])
                res.pop()
            
            if r < freeStart or l > freeEnd:
                res.append([l, r])
                continue
            
            if l < freeStart and r >= freeStart:
                res.append([l, freeStart - 1])
            if l <= freeEnd and r > freeEnd:
                res.append([freeEnd + 1, r])
        
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.filterOccupiedIntervals([[2, 6], [4, 8], [10, 10], [10, 12], [14, 16]], 7, 11))  # [[2, 6], [12, 12], [14, 16]]

    # Example 2
    print(sol.filterOccupiedIntervals([[1, 5], [2, 3]], 3, 8))  # [[1, 2]]
