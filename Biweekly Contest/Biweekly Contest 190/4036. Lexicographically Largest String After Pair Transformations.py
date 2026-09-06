"""
4036. Lexicographically Largest String After Pair Transformations - Medium


You are given an integer array nums.

For each integer x in nums, start with a string consisting of exactly x lowercase 'a' characters.

You may perform the following operation any number of times (including zero):

 - Choose two adjacent equal letters and replace them with the next letter in the alphabet.

For example, "aa" can be replaced with "b", and "bb" can be replaced with "c". The pair "zz" cannot be replaced.

For each x, determine the lexicographically largest string that can be obtained.

Return an array of strings where the ith string is the answer for nums[i].

A string a is lexicographically larger than a string b if, at the first position where they differ, a contains a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters are equal, the longer string is lexicographically larger.



Example 1:

Input: nums = [2,5,7]

Output: ["b","ca","cba"]

Explanation:

 - nums[0] = 2: "aa" -> "b".

 - nums[1] = 5: "aaaaa" -> "baaa" -> "bba" -> "ca".

 - nums[2] = 7: "aaaaaaa" -> "baaaaa" -> "bbaaa" -> "bbba" -> "cba".

 - Therefore, ans = ["b", "ca", "cba"].


Example 2:

Input: nums = [3,9,1]

Output: ["ba","da","a"]

Explanation:

 - nums[0] = 3: "aaa" -> "ba".

 - nums[1] = 9: "aaaaaaaaa" -> "baaaaaaa" -> "bbaaaaa" -> "bbbaaa" -> "bbbba" -> "cbba" -> "cca" -> "da".

 - nums[2] = 1: No transformation can be applied, so the result is "a".

 - Therefore, ans = ["ba", "da", "a"].



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
"""

from string import ascii_lowercase


class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans = []
        for i, x in enumerate(nums):
            s = [(x >> 25) * "z"]
            for i in range(min(24, x.bit_length() - 1), -1, -1):
                if x >> i & 1:
                    s.append(ascii_lowercase[i])
            ans.append("".join(s))

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.largestString([2, 5, 7]))  # ["b", "ca", "cba"]

    # Example 2
    print(sol.largestString([3, 9, 1]))  # ["ba", "da", "a"]
