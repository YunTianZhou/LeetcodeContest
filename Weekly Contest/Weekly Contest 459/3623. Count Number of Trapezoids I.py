"""
3623. Count Number of Trapezoids I - Medium


You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-7.png)

There are three distinct ways to pick four points that form a horizontal trapezoid:

Using points [1,0], [2,0], [3,2], and [2,2].
Using points [2,0], [3,0], [3,2], and [2,2].
Using points [1,0], [3,0], [3,2], and [2,2].


Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png)

There is only one horizontal trapezoid that can be formed.



Constraints:

4 <= points.length <= 10^5
-10^8 <= xi, yi <= 10^8
All points are pairwise distinct.
"""

from typing import List
from collections import Counter


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10 ** 9 + 7

        cnt = Counter(y for x, y in points)
        comb_sum = ans = 0
        for _, k in cnt.items():
            comb = k * (k - 1) // 2
            ans = (ans + comb_sum * comb) % mod
            comb_sum = (comb_sum + comb) % mod

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]]))  # 3

    # Example 2
    print(sol.countTrapezoids([[0,0],[1,0],[0,1],[2,1]]))  # 1
