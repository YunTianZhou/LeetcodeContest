"""
4027. Elevator Requests III - Hard


You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1.

You are also given an integer start and a 2D integer array requests, where requests[i] = [arrivali, floori] indicates that a request for floori is made at time arrivali.

At time 0, the elevator is at floor start.

At each second, the elevator may move up by 1 floor, move down by 1 floor, or remain on its current floor.

A request can be fulfilled only at or after its arrival time; it is fulfilled instantly when the elevator is on its requested floor at any time from its arrival time onward.

Return the minimum time needed to fulfill all requests.



Example 1:

Input: n = 9, start = 0, requests = [[0,8],[6,5]]

Output: 9

Explanation:

 - Move from floor 0 (start) to floor 5 (requests[1][1]) in 5 seconds, reaching at time 5. Since requests[1][0] = 6, wait until time 6 to fulfill it.

 - Move from floor 5 to floor 8 (requests[0][1]) in 3 seconds, fulfilling it at time 9.

Thus, all requests are fulfilled by time 9.


Example 2:

Input: n = 8, start = 5, requests = [[1,7],[7,3]]

Output: 7

Explanation:

 - Move from floor 5 (start) to floor 7 (requests[0][1]) in 2 seconds, reaching at time 2. Since requests[0][0] = 1 has already passed, floor 7 is fulfilled at time 2.

 - Move from floor 7 to floor 3 (requests[1][1]) in 4 seconds, reaching at time 6. Since requests[1][0] = 7, wait until time 7.

Thus, all requests are fulfilled by time 7.


Example 3:

Input: n = 7, start = 3, requests = [[0,5],[0,1],[6,3]]

Output: 8

Explanation:

 - Move from floor 3 (start) to floor 5 (requests[0][1]) in 2 seconds, fulfilling it at time 2.

 - Move from floor 5 to floor 1 (requests[1][1]) in 4 seconds, fulfilling it at time 6.

 - Move from floor 1 to floor 3 (requests[2][1]) in 2 seconds, reaching at time 8. Its request arrived at requests[2][0] = 6, so floor 3 is fulfilled at time 8.

Thus, all requests are fulfilled by time 8.



Constraints:

1 <= n <= 10^9
1 <= requests.length <= 16
requests[i] == [arrivali, floori]
0 <= arrivali <= 10^9
0 <= start, floori <= n - 1
"""

from math import inf


class Solution:
    def elevatorRequests(self, kofds: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)

        dp = [[inf] * m for _ in range(1 << m)]
        for i in range(m):
            t, x = requests[i]
            dp[1 << i][i] = max(t, abs(x - start))
        
        for mask in range(1 << m):
            if (mask & (mask - 1)) == 0:
                continue
            
            for i in range(m):
                if (mask >> i & 1) == 0:
                    continue
                
                t, x = requests[i]
                for j in range(m):
                    if i == j or (mask >> j & 1) == 0:
                        continue
                   
                    cur = dp[mask ^ (1 << i)][j] + abs(x - requests[j][1])
                    if cur < dp[mask][i]:
                        dp[mask][i] = cur
                        if cur <= t:
                            dp[mask][i] = t
                            break
                
        return min(dp[(1 << m) - 1])


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.elevatorRequests(9, 0, [[0, 8], [6, 5]]))  # 9

    # Example 2
    print(sol.elevatorRequests(8, 5, [[1, 7], [7, 3]]))  # 7

    # Example 3
    print(sol.elevatorRequests(7, 3, [[0, 5], [0, 1], [6, 3]]))  # 8
