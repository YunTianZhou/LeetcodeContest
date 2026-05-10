"""
3928. Minimum Cost to Buy Apples II - Hard


You are given an integer n and an integer array prices of length n, where prices[i] is the price of apples at shop i.

You are also given a 2D integer array roads, where roads[i] = [ui, vi, costi, taxi] represents a bidirectional road:

 - ui and vi are the shops connected by the road.

 - costi is the cost to travel the road without carrying apples.

 - taxi is the multiplier applied to costi when traveling with apples.

For each shop i, you can either:

 - Buy apples locally at shop i for prices[i].

 - Travel empty to any shop j using any number of roads, buy apples for prices[j], and return to shop i while carrying apples, paying cost * tax on each road used for the return trip.

The forward path, where you travel empty, and the return path may be different.

Return an integer array ans of length n, where ans[i] is the minimum total cost to buy apples starting from shop i.



Example 1:

Input: n = 2, prices = [8,3], roads = [[0,1,1,2]]

Output: [6,3]

Explanation:

(graph1)(https://assets.leetcode.com/uploads/2025/08/22/screenshot-2025-08-23-at-23341-am.png)

Shop i  prices[i]  Shop j  prices[j]  costi  taxi  Travel cost  Return cost  Total           Minimum
0       8          1       3          1      2     1            1 * 2 = 2    1 + 2 + 3 = 6   min(8, 6) = 6
1       3          0       8          1      2     1            1 * 2 = 2    1 + 2 + 8 = 11  min(3, 11) = 3

Thus, the answer is [6, 3].


Example 2:

Input: n = 3, prices = [9,4,6], roads = [[0,1,1,3],[1,2,4,2]]

Output: [8,4,6]

Explanation:

(graph2)(https://assets.leetcode.com/uploads/2025/08/22/screenshot-2025-08-23-at-23736-am.png)

Shop i  prices[i]  Shop j  prices[j]  costi  taxi  Travel cost  Return cost  Total           Minimum
0       9          1       4          1      3     1            1 * 3 = 3    1 + 3 + 4 = 8   min(9, 8) = 8
1       4          2       6          4      2     4            4 * 2 = 8    4 + 8 + 6 = 18  min(4, 18) = 4
2       6          1       4          4      2     4            4 * 2 = 8    4 + 8 + 4 = 16  min(6, 16) = 6

Thus, the answer is [8, 4, 6].


Example 3:

Input: n = 3, prices = [10,11,1], roads = [[0,2,1,3],[1,2,3,4],[0,1,5,2]]

Output: [5,11,1]

Explanation:

(graph3)(https://assets.leetcode.com/uploads/2025/08/22/screenshot-2025-08-23-at-24644-am.png)

Shop i  prices[i]  Shop j  prices[j]  costi  taxi  Travel cost  Return cost  Total            Minimum
0       10         2       1          1      3     1            1 * 3 = 3    1 + 3 + 1 = 5    min(10, 5) = 5
1       11         2       1          3      4     3            3 * 4 = 12   3 + 12 + 1 = 16  min(11, 16) = 11
2       1          0       10         1      3     1            1 * 3 = 3    1 + 3 + 10 = 14  min(1, 14) = 1

Thus, the answer is [5, 11, 1].



Constraints:

1 <= n <= 1000
prices.length == n
1 <= prices[i] <= 10^9
0 <= roads.length <= min(n * (n - 1) / 2, 2000)
roads[i] = [ui, vi, costi, taxi]
0 <= ui, vi <= n - 1
ui != vi
1 <= costi <= 10^9
1 <= taxi <= 100
There are no repeated edges.
"""

from heapq import heappop, heappush


class Solution:
    def minCost(self, n: int, prices: list[int], roads: list[list[int]]) -> list[int]:
        graph_come = [[] for _ in range(n)]
        graph_back = [[] for _ in range(n)]
        for a, b, w, t in roads:
            graph_come[a].append((b, w))
            graph_come[b].append((a, w))
            graph_back[a].append((b, w * t))
            graph_back[b].append((a, w * t))

        def get_cost(graph, start):
            cost = [prices[start]] * n
            cost[start] = 0
            
            h = [(0, start)]
            while h:
                x, a = heappop(h)
                if x > cost[a]: 
                    continue
                
                for b, w in graph[a]:
                    y = x + w
                    if y < cost[b]:
                        heappush(h, (y, b))
                        cost[b] = y

            return cost

        ans = [0] * n
        for start in range(n):
            cost_come = get_cost(graph_come, start)
            cost_back = get_cost(graph_back, start)

            ans[start] = min(cost_come[store] + cost_back[store] + prices[store]
                             for store in range(n))
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minCost(2, [8, 3], [[0, 1, 1, 2]]))  # [6, 3]

    # Example 2
    print(sol.minCost(3, [9, 4, 6], [[0, 1, 1, 3], [1, 2, 4, 2]]))  # [8, 4, 6]

    # Example 3
    print(sol.minCost(3, [10, 11, 1], [[0, 2, 1, 3], [1, 2, 3, 4], [0, 1, 5, 2]]))  # [5, 11, 1]
