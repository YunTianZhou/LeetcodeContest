"""
3625. Count Number of Trapezoids II - Hard


You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.



Example 1:

Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

Output: 2

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-4.png)

There are two distinct ways to pick four points that form a trapezoid:

The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.


Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png)

There is only one trapezoid which can be formed.



Constraints:

4 <= points.length <= 500
-1000 <= xi, yi <= 1000
All points are pairwise distinct.
"""

from typing import List
from math import gcd, comb
from collections import defaultdict
from itertools import combinations


class Solution:
    def countTrapezoids(self, A: List[List[int]]) -> int:
        slopes = defaultdict(int)
        lines = defaultdict(int)
        mids = defaultdict(int)
        midlines = defaultdict(int)

        for (x1, y1), (x2, y2) in combinations(A, 2):
            dx, dy = x2 - x1, y2 - y1
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy

            inter = dx * y1 - dy * x1
            slopes[dx, dy] += 1
            lines[dx, dy, inter] += 1
            mids[x1 + x2, y1 + y2] += 1
            midlines[x1 + x2, y1 + y2, dx, dy, inter] += 1

        ans = sum(comb(v, 2) for v in slopes.values())
        ans -= sum(comb(v, 2) for v in lines.values())
        ans -= sum(comb(v, 2) for v in mids.values())
        ans += sum(comb(v, 2) for v in midlines.values())
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]))  # 2

    # Example 2
    print(sol.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]))  # 1
