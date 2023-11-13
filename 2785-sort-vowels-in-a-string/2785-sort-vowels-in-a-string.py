class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = "aeiouAEIOU"
        vowel_positions = [i for i, char in enumerate(s) if char in vowels]
        sorted_vowels = sorted((s[i] for i in vowel_positions))

        result_list = list(s)
        for index, char in zip(vowel_positions, sorted_vowels):
            result_list[index] = char

        return "".join(result_list) 