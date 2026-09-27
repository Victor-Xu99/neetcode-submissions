class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char for char in s if char.isalnum())
        left = 0
        right = len(cleaned_string) - 1
        while left <= right:
            if cleaned_string[left].lower() == cleaned_string[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
    

        