class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        max_length = 0

        for index, character in enumerate(s[:-1]):
            substring = [character]

            for next_char in s[index + 1:]:
                if next_char not in substring:
                    substring.append(next_char)
                    max_length = max(len(substring), max_length)
                else:
                    max_length = max(len(substring), max_length)
                    substring = []
                    break


        return max_length
