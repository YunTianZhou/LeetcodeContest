"""
3733. Minimum Time to Complete All Deliveries - Medium


You are given two integer arrays of size 2: d = [d1, d2] and r = [r1, r2].

Two delivery drones are tasked with completing a specific number of deliveries. Drone i must complete di deliveries.

Each delivery takes exactly one hour and only one drone can make a delivery at any given hour.

Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone i must recharge every ri hours (i.e. at hours that are multiples of ri).

Return an integer denoting the minimum total time (in hours) required to complete all deliveries.



Example 1:

Input: d = [3,1], r = [2,3]

Output: 5

Explanation:

The first drone delivers at hours 1, 3, 5 (recharges at hours 2, 4).

The second drone delivers at hour 2 (recharges at hour 3).


Example 2:

Input: d = [1,3], r = [2,2]

Output: 7

Explanation:

The first drone delivers at hour 3 (recharges at hours 2, 4, 6).

The second drone delivers at hours 1, 5, 7 (recharges at hours 2, 4, 6).


Example 3:

Input: d = [2,1], r = [3,4]

Output: 3

Explanation:

The first drone delivers at hours 1, 2 (recharges at hour 3).

The second drone delivers at hour 3.



Constraints:

d = [d1, d2]
1 <= di <= 10^9
r = [r1, r2]
2 <= ri <= 3 * 10^4
"""

from typing import List
from math import lcm


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        m = lcm(r1, r2)
        
        low = d1 + d2 - 1
        high = (d1 + d2) * 2
        while low + 1 < high:
            mid = (low + high) // 2

            if (d1 <= mid - mid // r1 and
                d2 <= mid - mid // r2 and
                d1 + d2 <= mid - mid // m):
                high = mid
            else:
                low = mid

        return high



if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minimumTime([3, 1], [2, 3]))  # 5

    # Example 2
    print(sol.minimumTime([1, 3], [2, 2]))  # 7

    # Example 3
    print(sol.minimumTime([2, 1], [3, 4]))  # 3
    