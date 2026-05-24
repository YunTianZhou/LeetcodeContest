"""
3941. Password Strength - Medium


You are given a string password.

The strength of the password is calculated based on the following rules:

 - 1 point for each distinct lowercase letter ('a' to 'z').

 - 2 points for each distinct uppercase letter ('A' to 'Z').

 - 3 points for each distinct digit ('0' to '9').

 - 5 points for each distinct special character from the set "!@#$".

Each character contributes at most once, even if it appears multiple times.

Return an integer denoting the strength of the password.



Example 1:

Input: password = "aA1!"

Output: 11

Explanation:

 - The distinct characters are 'a', 'A', '1' and '!'.

 - Thus, the strength = 1 + 2 + 3 + 5 = 11.


Example 2:

Input: password = "bbB11#"

Output: 11

Explanation:

 - The distinct characters are 'b', 'B', '1' and '#'.

 - Thus, the strength = 1 + 2 + 3 + 5 = 11.



Constraints:

1 <= password.length <= 10^5
password consists of lowercase and uppercase English letters, digits, and special characters from "!@#$".
"""


class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0

        for c in set(password):
            if c.islower():
                ans += 1
            elif c.isupper():
                ans += 2
            elif c.isdigit():
                ans += 3
            elif c in "!@#$":
                ans += 5
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.passwordStrength("aA1!"))  # 11

    # Example 2
    print(sol.passwordStrength("bbB11#"))  # 11
