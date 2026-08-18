class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        cleaned_lower = []
        for char in s:
            if char.isalnum():
                cleaned.append(char)
        for char in cleaned:
            cleaned_lower.append(char.lower())
        cleaned_copy = cleaned_lower.copy()
        cleaned_copy.reverse()
        if cleaned_lower == cleaned_copy:
            return True
        else:
            return False