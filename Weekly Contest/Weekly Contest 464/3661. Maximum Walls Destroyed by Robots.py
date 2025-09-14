"""
3661. Maximum Walls Destroyed by Robots - Hard


There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:

robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.

Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.

Robots are not destroyed by bullets.



Example 1:

Input: robots = [4], distance = [3], walls = [1,10]

Output: 1

Explanation:

robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.

Thus, the answer is 1.


Example 2:

Input: robots = [10,2], distance = [5,1], walls = [5,2,7]

Output: 3

Explanation:

robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.

Thus, the answer is 3.


Example 3:

Input: robots = [1,2], distance = [100,1], walls = [10]

Output: 0

Explanation:

In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.



Constraints:

1 <= robots.length == distance.length <= 10^5
1 <= walls.length <= 10^5
1 <= robots[i], walls[j] <= 10^9
1 <= distance[i] <= 10^5
All values in robots are unique
All values in walls are unique
"""

from typing import List
from bisect import bisect_left, bisect_right
from functools import cache


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        robots = list(zip(robots, distance))
        robots.sort(key=lambda x: x[0])
        walls.sort()

        def count(l, r):
            if l > r:
                return 0
            return bisect_right(walls, r) - bisect_left(walls, l)

        @cache
        def dfs(i, prev):
            if i == n:
                return 0
                
            p, d = robots[i]
            ans = 0
            
            left = p - d
            if i > 0:
                pp, pd = robots[i - 1]
                left = max(left, pp + pd * prev + 1)
            ans = max(ans, dfs(i + 1, False) + count(left, p))

            right = p + d
            if i != n - 1:
                np, _ = robots[i + 1]
                right = min(right, np - 1)
            ans = max(ans, dfs(i + 1, True) + count(p, right))

            return ans

        return dfs(0, False)
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxWalls([4], [3], [1, 10]))  # 1

    # Example 2
    print(sol.maxWalls([10, 2], [5, 1], [5, 2, 7]))  # 3

    # Example 3
    print(sol.maxWalls([1, 2], [100, 1], [10]))  # 0
