"""
3977. Minimum Time to Reach Target With Limited Power - Hard


You are given a directed weighted graph with n nodes labeled from 0 to n - 1.

The graph is represented by a 2D integer array edges, where edges[i] = [ui, vi, ti] indicates a directed edge from node ui to node vi that takes ti seconds to traverse.

You are also given an integer power representing the initial available power, and an integer array cost of length n, where cost[u] represents the power required to forward the signal from node u through any one of its outgoing edges.

You are given two integers source and target.

The signal starts at source at time 0 with power units of power and follows these rules:

 - The signal may traverse a directed edge from node u only if the remaining power is at least cost[u].

 - No power is consumed when the signal arrives at a node, unless it later leaves that node by traversing another edge.

 - When the signal is forwarded from node u, the remaining power is decreased by cost[u] units.

 - Traversing an edge edges[i] = [ui, vi, ti] increases the total time by ti seconds.

Return an integer array answer of size 2, where:

 - answer[0] is the minimum time required for the signal to reach node target.

 - answer[1] is the maximum remaining power among all paths that achieve answer[0].

If the signal cannot reach target, return [-1, -1].



Example 1:

[graph1]()

Input: n = 5, edges = [[0,1,1],[1,4,1],[0,2,1],[2,3,1],[3,4,1]], power = 4, cost = [2,3,1,1,1], source = 0, target = 4

Output: [3,0]

Explanation:

 - The signal starts at node 0 with 4 units of power.

 - The path 0 -> 1 -> 4 is not valid, because after leaving node 0, the signal has 2 units of power remaining, which is less than cost[1] = 3.

 - The valid path 0 -> 2 -> 3 -> 4 takes a total time of 3.

 - The total power consumed along this path is cost[0] + cost[2] + cost[3] = 4, leaving 0 remaining power.

 - Hence, the answer is [3, 0].


Example 2:

[graph2]()

Input: n = 3, edges = [[0,1,2],[1,2,2],[2,0,2]], power = 3, cost = [1,1,1], source = 1, target = 1

Output: [0,3]

Explanation:

 - Since the source and target are the same node, no traversal is required.

 - Hence, the minimum total time taken is 0, and no power is consumed.

 - Therefore, the answer is [0, 3].


Example 3:

[graph3]()

Input: n = 4, edges = [[0,1,3],[2,3,4]], power = 3, cost = [1,1,1,1], source = 0, target = 3

Output: [-1,-1]

Explanation:

There is no valid path from source to target, therefore return [-1, -1].



Constraints:

1 <= n <= 1000
0 <= edges.length <= 1000
edges[i] = [ui, vi, ti]
0 <= ui, vi <= n - 1
1 <= ti <= 109
1 <= power <= 1000
cost.length == n
1 <= cost[i] <= 2000
0 <= source, target <= n - 1
"""

from heapq import heappop, heappush


class Solution:
    def minTimeMaxPower(self, n: int, edges: list[list[int]], power: int, cost: list[int], source: int, target: int) -> list[int]:
        graph = [[] for _ in range(n)]
        for a, b, t in edges:
            graph[a].append((b, t))

        h = [(0, -power, source)]
        max_p = [x - 1 for x in cost]
        while h:
            t, p, a = heappop(h)
            p = -p
            
            if a == target:
                return [t, p]

            if p <= max_p[a]:
                continue
            max_p[a] = p
            
            np = p - cost[a]
            for b, w in graph[a]:
                heappush(h, (t + w, -np, b))
        
        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minTimeMaxPower(5, [[0, 1, 1], [1, 4, 1], [0, 2, 1], [2, 3, 1], [3, 4, 1]], 4, [2, 3, 1, 1, 1], 0, 4))  # [3, 0]

    # Example 2
    print(sol.minTimeMaxPower(3, [[0, 1, 2], [1, 2, 2], [2, 0, 2]], 3, [1, 1, 1], 1, 1))  # [0, 3]

    # Example 3
    print(sol.minTimeMaxPower(4, [[0, 1, 3], [2, 3, 4]], 3, [1, 1, 1, 1], 0, 3))  # [-1, -1]
