"""
3873. Maximum Points Activated with One Addition - Hard


You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point. All coordinates in points are distinct.

If a point is activated, then all points that have the same x-coordinate or y-coordinate become activated as well.

Activation continues until no additional points can be activated.

You may add one additional point at any integer coordinate (x, y) not already present in points. Activation begins by activating this newly added point.

Return an integer denoting the maximum number of points that can be activated, including the newly added point.



Example 1:

Input: points = [[1,1],[1,2],[2,2]]

Output: 4

Explanation:

Adding and activating a point such as (1, 3) causes activations:

 - (1, 3) shares x = 1 with (1, 1) and (1, 2) -> (1, 1) and (1, 2) become activated.
 - (1, 2) shares y = 2 with (2, 2) -> (2, 2) becomes activated.

Thus, the activated points are (1, 3), (1, 1), (1, 2), (2, 2), so 4 points in total. We can show this is the maximum activated.


Example 2:

Input: points = [[2,2],[1,1],[3,3]]

Output: 3

Explanation:

Adding and activating a point such as (1, 2) causes activations:

 - (1, 2) shares x = 1 with (1, 1) -> (1, 1) becomes activated.
 - (1, 2) shares y = 2 with (2, 2) -> (2, 2) becomes activated.

Thus, the activated points are (1, 2), (1, 1), (2, 2), so 3 points in total. We can show this is the maximum activated.


Example 3:

Input: points = [[2,3],[2,2],[1,1],[4,5]]

Output: 4

Explanation:

Adding and activating a point such as (2, 1) causes activations:

 - (2, 1) shares x = 2 with (2, 3) and (2, 2) -> (2, 3) and (2, 2) become activated.
 - (2, 1) shares y = 1 with (1, 1) -> (1, 1) becomes activated.

Thus, the activated points are (2, 1), (2, 3), (2, 2), (1, 1), so 4 points in total.



Constraints:

1 <= points.length <= 10^5
points[i] = [xi, yi]
-10^9 <= xi, yi <= 10^9
points contains all distinct coordinates.
"""


class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)

        uf = list(range(n))
        size = [1] * n

        def find(x):
            while x != uf[x]:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        def union(x, y):
            a = find(x)
            b = find(y)
            uf[b] = a
            size[a] += size[b]
            size[b] = 0
        
        rx = {}
        ry = {}
        for i, (x, y) in enumerate(points):
            if x in rx:
                union(i, rx[x])
            if y in ry:
                union(i, ry[y])
            rx[x] = i
            ry[y] = i
        
        top1 = top2 = 0
        for i in range(n):
            x = size[i]
            if x > top1:
                top2 = top1
                top1 = x
            elif x > top2:
                top2 = x
        
        return top1 + top2 + 1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxActivated([[1, 1], [1, 2], [2, 2]]))  # 4

    # Example 2
    print(sol.maxActivated([[2, 2], [1, 1], [3, 3]]))  # 3

    # Example 3
    print(sol.maxActivated([[2, 3], [2, 2], [1, 1], [4, 5]]))  # 4
