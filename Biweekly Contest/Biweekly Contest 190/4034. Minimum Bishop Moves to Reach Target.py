"""
4034. Minimum Bishop Moves to Reach Target - Medium


There is an 8 x 8 empty chessboard with 1-indexed rows and columns.

You are given an array source = [sr, sc] representing the starting position of a bishop, and an array target = [tr, tc] representing the target position.

In one move, the bishop travels one or more squares along a single diagonal direction, staying within the board.

Return the minimum number of moves for the bishop to land exactly on target. If it can never reach target, return -1.



Example 1:

Input: source = [8,1], target = [1,8]

Output: 1

Explanation:

[graph1](https://assets.leetcode.com/uploads/2026/07/22/image.png)

A single diagonal move takes the bishop straight from (8, 1) to (1, 8).


Example 2:

Input: source = [4,2], target = [1,3]

Output: 2

Explanation:

[graph2](https://assets.leetcode.com/uploads/2026/07/22/screenshot-2026-07-23-at-23625am.png)

The bishop moves from (4, 2) to (3, 1), then from (3, 1) to (1, 3), reaching the target in 2 moves.


Example 3:

Input: source = [1,1], target = [3,4]

Output: -1

Explanation:

No matter how many diagonal moves it makes, the bishop starting at (1, 1) can never land on (3, 4). Thus, the answer is -1.



Constraints:

source.length == target.length == 2
1 <= sr, sc, tr, tc <= 8
source != target
"""


class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        if sum(source) % 2 != sum(target) % 2:
            return -1
        elif abs(target[0] - source[0]) == abs(target[1] - source[1]):
            return 1
        else:
            return 2


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minBishopMoves([8, 1], [1, 8]))  # 1

    # Example 2
    print(sol.minBishopMoves([4, 2], [1, 3]))  # 2

    # Example 3
    print(sol.minBishopMoves([1, 1], [3, 4]))  # -1
