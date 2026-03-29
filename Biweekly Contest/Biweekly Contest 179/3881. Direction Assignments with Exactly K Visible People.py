"""
3881. Direction Assignments with Exactly K Visible People - Medium


You are given three integers n, pos, and k.

There are n people standing in a line indexed from 0 to n - 1. Each person independently chooses a direction:

 - 'L': visible only to people on their right

 - 'R': visible only to people on their left

A person at index pos sees others as follows:

 - A person i < pos is visible if and only if they choose 'L'.

 - A person i > pos is visible if and only if they choose 'R'.

Return the number of possible direction assignments such that the person at index pos sees exactly k people.

Since the answer may be large, return it modulo 10^9 + 7.



Example 1:

Input: n = 3, pos = 1, k = 0

Output: 2

Explanation:

 - Index 0 is to the left of pos = 1, and index 2 is to the right of pos = 1.

 - To see k = 0 people, index 0 must choose 'R' and index 2 must choose 'L', keeping both invisible.

 - The person at index 1 can choose 'L' or 'R' since it does not affect the count. Thus, the answer is 2.


Example 2:

Input: n = 3, pos = 2, k = 1

Output: 4

Explanation:

 - Index 0 and index 1 are left of pos = 2, and there is no index to the right.

 - To see k = 1 person, exactly one of index 0 or index 1 must choose 'L', and the other must choose 'R'.

 - There are 2 ways to choose which index is visible from the left.

 - The person at index 2 can choose 'L' or 'R' since it does not affect the count. Thus, the answer is 2 + 2 = 4.


Example 3:

Input: n = 1, pos = 0, k = 0

Output: 2

Explanation:

 - There are no indices to the left or right of pos = 0.

 - To see k = 0 people, no additional condition is required.

 - The person at index 0 can choose 'L' or 'R'. Thus, the answer is 2.



Constraints:

1 <= n <= 10^5
0 <= pos, k <= n - 1
"""


m = 10 ** 5
mod = 10 ** 9 + 7

fact = [1] * (m + 1)
inv_fact = [1] * (m + 1)

for i in range(1, m + 1):
    fact[i] = fact[i - 1] * i % mod

inv_fact[m] = pow(fact[m], mod - 2, mod)
for i in range(m - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] * inv_fact[n - r] % mod

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        return comb(n - 1, k) * 2 % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countVisiblePeople(3, 1, 0))  # 2

    # Example 2
    print(sol.countVisiblePeople(3, 2, 1))  # 4

    # Example 3
    print(sol.countVisiblePeople(1, 0, 0))  # 2
