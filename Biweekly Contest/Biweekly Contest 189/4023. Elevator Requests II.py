"""
4023. Elevator Requests II - Hard


You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1.

You are also given an integer start, representing the floor where the elevator begins, and an integer array requests, where requests[i] is a floor that the elevator is requested to reach. All floors in requests are distinct.

At time 0, the elevator is on floor start, and all requests are made simultaneously.

During each second before all requests are fulfilled, the elevator moves exactly one floor, either up or down. A request is fulfilled instantly when the elevator reaches its requested floor. If start appears in requests, that request is fulfilled at time 0.

For each second that a request remains unfulfilled, you receive 1 penalty. Equivalently, a request fulfilled at time t contributes t to the total penalty.

Return the minimum total penalty required to fulfill all requests.



Example 1:

Input: n = 6, start = 4, requests = [1,5]

Output: 6

Explanation:

 - Move from floor 4 (start) to floor 5 in 1 second. Penalty for floor 5 is 1.

 - Move from floor 5 to floor 1 in 4 seconds. Penalty for floor 1 is 5.

Thus, the total penalty is 1 + 5 = 6.


Example 2:

Input: n = 8, start = 3, requests = [3,7,1]

Output: 10

Explanation:

 - Floor 3 (start) is fulfilled instantly. Penalty for floor 3 is 0.

 - Move from floor 3 to floor 1 in 2 seconds. Penalty for floor 1 is 2.

 - Move from floor 1 to floor 7 in 6 seconds. Penalty for floor 7 is 8.

Thus, the total penalty is 0 + 2 + 8 = 10.


Example 3:

Input: n = 10, start = 5, requests = [0,2,9]

Output: 22

Explanation:

 - Move from floor 5 (start) to floor 2 in 3 seconds. Penalty for floor 2 is 3.

 - Move from floor 2 to floor 0 in 2 seconds. Penalty for floor 0 is 5.

 - Move from floor 0 to floor 9 in 9 seconds. Penalty for floor 9 is 14.

Thus, the total penalty is 3 + 5 + 14 = 22.



Constraints:

1 <= n <= 10^9
1 <= requests.length <= 1500
0 <= start, requests[i] <= n - 1
All values in requests are distinct.
"""

from bisect import bisect_left
from math import inf


class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        r = sorted(x for x in requests if x != start)
        p = bisect_left(r, start)
        r.insert(p, start)
        
        m = len(r)

        dp_l = [[inf] * m for _ in range(m)]
        dp_r = [[inf] * m for _ in range(m)]
        dp_l[p][p] = dp_r[p][p] = 0
        
        for i in range(p, -1, -1):
            for j in range(p, m):
                if i == j:
                    continue
                
                remain = m - (j - i)

                dp_l[i][j] = min(
                    remain * (r[i + 1] - r[i]) + dp_l[i + 1][j],
                    remain * (r[j] - r[i])     + dp_r[i + 1][j]
                )

                dp_r[i][j] = min(
                    remain * (r[j] - r[j - 1]) + dp_r[i][j - 1],
                    remain * (r[j] - r[i])     + dp_l[i][j - 1]
                )

        return min(dp_l[0][m - 1], dp_r[0][m - 1])


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.elevatorRequests(6, 4, [1, 5]))  # 6

    # Example 2
    print(sol.elevatorRequests(8, 3, [3, 7, 1]))  # 10

    # Example 3
    print(sol.elevatorRequests(10, 5, [0, 2, 9]))  # 22
