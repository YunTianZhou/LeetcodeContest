"""
4068. Maximize Meeting Earnings with Idle Gaps - Hard


You are given a 2D integer array meetings, where meetings[i] = [starti, endi, revenuei] represents a meeting starting at time starti, ending at time endi, with revenue revenuei.

All meetings use half-open intervals [start, end), so meetings that only touch at endpoints do not overlap.

You may select any non-empty subset of meetings such that no two selected meetings overlap. You earn the revenue of each selected meeting.

Arrange the selected meetings in increasing order of their start times. For each pair of adjacent meetings in this order, you also earn 1 unit of revenue per unit of idle time between them. This idle time equals the later meeting's start time minus the earlier meeting's end time.

No idle revenue is earned before the earliest selected meeting starts or after the latest selected meeting ends. If only one meeting is selected, no idle revenue is earned.

Return the maximum total earnings achievable.

A subset of an array is a selection of elements of the array.



Example 1:

Input: meetings = [[2,5,4],[6,8,3]]

Output: 8

Explanation:

Select both meetings. They do not overlap and earn 4 + 3 = 7 units of meeting revenue.

The first meeting ends at time 5, and the second starts at time 6. This idle gap earns 6 - 5 = 1 additional unit.

The maximum total earnings are 7 + 1 = 8.


Example 2:

Input: meetings = [[3,5,4],[4,7,8],[8,10,3]]

Output: 12

Explanation:

Select the meetings at indices 1 and 2. They do not overlap and earn 8 + 3 = 11 units of meeting revenue.

In chronological order, these meetings run from time 4 to 7 and from time 8 to 10. The idle gap earns 8 - 7 = 1 additional unit.

The maximum total earnings are 11 + 1 = 12.


Example 3:

Input: meetings = [[1,2,2],[4,5,2],[7,9,3]]

Output: 11

Explanation:

Select all three meetings. They do not overlap and earn 2 + 2 + 3 = 7 units of meeting revenue.

The idle gap from time 2 to 4 earns 4 - 2 = 2 additional units.

The idle gap from time 5 to 7 earns 7 - 5 = 2 additional units.

The maximum total earnings are 7 + 2 + 2 = 11.



Constraints:

1 <= meetings.length <= 10^5
meetings[i] = [starti, endi, revenuei]
0 <= starti < endi <= 10^9
1 <= revenuei <= 10^9
"""

from bisect import bisect_left


fmax = lambda x, y: x if x > y else y

class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        n = len(meetings)
        meetings.sort(key=lambda x: x[0])

        dp = [0] * n
        ans = max(x for _, _ , x in meetings)
        for i in range(n - 1, -1, -1):
            l, r, x = meetings[i]
            dp[i] = x

            if i + 1 < n:
                gap = meetings[i + 1][0] - l
                dp[i] = fmax(dp[i], gap + dp[i + 1])

            j = bisect_left(meetings, [r])
            if j < n:
                gap = meetings[j][0] - r
                cur = x + gap + dp[j]

                ans = fmax(ans, cur)
                dp[i] = fmax(dp[i], cur)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxEarnings([[2, 5, 4], [6, 8, 3]]))  # 8

    # Example 2
    print(sol.maxEarnings([[3, 5, 4], [4, 7, 8], [8, 10, 3]]))  # 12

    # Example 3
    print(sol.maxEarnings([[1, 2, 2], [4, 5, 2], [7, 9, 3]]))  # 11
