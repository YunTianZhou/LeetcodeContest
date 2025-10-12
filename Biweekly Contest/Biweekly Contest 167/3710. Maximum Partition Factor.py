"""
3710. Maximum Partition Factor - Hard


You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

The Manhattan distance between two points points[i] = [xi, yi] and points[j] = [xj, yj] is |xi - xj| + |yi - yj|.

Split the n points into exactly two non-empty groups. The partition factor of a split is the minimum Manhattan distance among all unordered pairs of points that lie in the same group.

Return the maximum possible partition factor over all valid splits.

Note: A group of size 1 contributes no intra-group pairs. When n = 2 (both groups size 1), there are no intra-group pairs, so define the partition factor as 0.



Example 1:

Input: points = [[0,0],[0,2],[2,0],[2,2]]

Output: 4

Explanation:

We split the points into two groups: {[0, 0], [2, 2]} and {[0, 2], [2, 0]}.

 - In the first group, the only pair has Manhattan distance |0 - 2| + |0 - 2| = 4.

 - In the second group, the only pair also has Manhattan distance |0 - 2| + |2 - 0| = 4.

The partition factor of this split is min(4, 4) = 4, which is maximal.


Example 2:

Input: points = [[0,0],[0,1],[10,0]]

Output: 11

Explanation:

We split the points into two groups: {[0, 1], [10, 0]} and {[0, 0]}.

 - In the first group, the only pair has Manhattan distance |0 - 10| + |1 - 0| = 11.

 - The second group is a singleton, so it contributes no pairs.

The partition factor of this split is 11, which is maximal.



Constraints:

2 <= points.length <= 500
points[i] = [xi, yi]
-10^8 <= xi, yi <= 10^8
"""

from typing import List
from collections import deque


class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return 0

        graph = [[0] * n for _ in range(n)]
        max_dst = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dst = abs(x1 - x2) + abs(y1 - y2)
                graph[i][j] = dst
                graph[j][i] = dst
                max_dst = max(max_dst, dst)
     
        def ok(lim):
            color = [-1] * n
            for i in range(n):
                if color[i] != -1: 
                    continue
                    
                color[i] = 0
                dq = deque([i])
                while dq:
                    a = dq.popleft()
                    
                    for b in range(n):
                        if a == b:
                            continue
                            
                        if graph[a][b] < lim:
                            if color[b] == -1:
                                color[b] = 1 - color[a]
                                dq.append(b)
                            elif color[a] == color[b]:
                                return False

            return True
                                
        l = -1
        r = max_dst + 1
        while l + 1 < r:
            mid = (l + r) // 2

            if ok(mid):
                l = mid
            else:
                r = mid

        return l


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxPartitionFactor([[0, 0], [0, 2], [2, 0], [2, 2]]))  # 4

    # Example 2
    print(sol.maxPartitionFactor([[0, 0], [0, 1], [10, 0]]))  # 11
    