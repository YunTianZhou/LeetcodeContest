"""
3629. Minimum Jumps to Reach End via Prime Teleportation - Medium


You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.

Return the minimum number of jumps required to reach index n - 1.



Example 1:

Input: nums = [1,2,4,6]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.

Thus, the answer is 2.


Example 2:

Input: nums = [2,3,4,7,9]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.

Thus, the answer is 2.


Example 3:

Input: nums = [4,6,5,8]

Output: 3

Explanation:

Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.
 


Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^6
"""

from typing import List
from collections import defaultdict


m = 10 ** 6
is_prime = [True] * (m + 2)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums)

        mp = defaultdict(list)
        for i in range(n):
            mp[nums[i]].append(i)

        visited = [False] * n
        visited[0] = True
        stack = [0]
        ans = 0
        while stack:
            new_stack = []
            for i in stack:
                if i == n - 1:
                    return ans

                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    new_stack.append(i + 1)

                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    new_stack.append(i - 1)
                
                if is_prime[nums[i]]:
                    for x in range(nums[i] * 2, m + 1, nums[i]):
                        if x not in mp:
                            continue
                        for j in mp[x]:
                            if not visited[j]:
                                visited[j] = True
                                new_stack.append(j)
                        del mp[x]
                        
            stack = new_stack
            ans += 1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minJumps([1, 2, 4, 6]))  # 2

    # Example 2
    print(sol.minJumps([2, 3, 4, 7, 9]))  # 2

    # Example 3
    print(sol.minJumps([4, 6, 5, 8]))  # 3
