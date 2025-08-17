"""
3568. Minimum Moves to Clean the Classroom - Medium


You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

 

Example 1:

Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

The student starts at cell (0, 0) with 2 units of energy.
Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
The student collects all the litter using 2 moves. Thus, the output is 2.


Example 2:

Input: classroom = ["LS", "RL"], energy = 4

Output: 3

Explanation:

The student starts at cell (0, 1) with 4 units of energy.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
The student collects all the litter using 3 moves. Thus, the output is 3.


Example 3:

Input: classroom = ["L.S", "RXL"], energy = 3

Output: -1

Explanation:

No valid path collects all 'L'.

 

Constraints:

1 <= m == classroom.length <= 20
1 <= n == classroom[i].length <= 20
classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
1 <= energy <= 50
There is exactly one 'S' in the grid.
There are at most 10 'L' cells in the grid.
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        n, m = len(classroom), len(classroom[0])

        start = 0
        litter_cnt = 0
        litter_idx = {}
        for i, row in enumerate(classroom):
            for j, cell in enumerate(row):
                if cell == "S":
                    start = (i, j)
                elif cell == "L":
                    litter_idx[(i, j)] = litter_cnt
                    litter_cnt += 1

        if litter_cnt == 0:
            return 0
        
        full_mask = (1 << litter_cnt) - 1
        dq = deque([(start, energy, full_mask)])
        visit = defaultdict(int)
        visit[start, full_mask] = energy

        ans = 1
        while dq:
            for _ in range(len(dq)):
                (i, j), curr_energy, mask = dq.popleft()

                if curr_energy < visit[(i, j), mask]:
                    continue
                
                for next_i, next_j in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= next_i < n and 0 <= next_j < m and classroom[next_i][next_j] != "X":
                        next_energy = curr_energy - 1
                        next_mask = mask
                        if classroom[next_i][next_j] == "R":
                            next_energy = energy
                        elif classroom[next_i][next_j] == "L":
                            next_mask &= ~(1 << litter_idx[next_i, next_j])
                            if next_mask == 0:
                                return ans

                        if next_energy > visit[(next_i, next_j), next_mask]:
                            visit[(next_i, next_j), next_mask] = next_energy
                            dq.append(((next_i, next_j), next_energy, next_mask))

            ans += 1
        
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minMoves(["S.", "XL"], 2))  # 2

    # Example 2
    print(sol.minMoves(["LS", "RL"], 4))  # 3

    # Example 3
    print(sol.minMoves(["L.S", "RXL"], 3))  # -1
