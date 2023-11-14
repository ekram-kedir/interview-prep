class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i = -1
            j = 0

            for k in range(len(s)):
                if s[k] == letter:
                    if i == -1:
                        i = k
                    j = k

            between = set(s[i + 1 : j])
            ans += len(between)

        return ans