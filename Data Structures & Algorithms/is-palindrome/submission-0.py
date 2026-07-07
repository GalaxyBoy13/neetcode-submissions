class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        for char in cleaned_str:
            result=char+result
        if cleaned_str==result:
            return True
        else: 
            return False