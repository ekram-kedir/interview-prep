class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        memo = {}

        def dp(curr, count):
            if count == n - 1:
                return 1

            if (curr, count) in memo:
                return memo[(curr, count)]

            result = 0

            if curr == 'a':
                result = (result + dp('e', count + 1)) % mod

            if curr == 'e':
                result = (result + dp('a', count + 1) + dp('i', count + 1)) % mod

            if curr == 'i':
                result = (result + dp('a', count + 1) + dp('e', count + 1) + dp('o', count + 1) + dp('u', count + 1)) % mod

            if curr == 'o':
                result = (result + dp('i', count + 1) + dp('u', count + 1)) % mod

            if curr == 'u':
                result = (result + dp('a', count + 1)) % mod

            memo[(curr, count)] = result
            return result

        total = 0
        vowels = 'aeiou'
        
        for vowel in vowels:
            total = (total + dp(vowel, 0)) % mod

        return total