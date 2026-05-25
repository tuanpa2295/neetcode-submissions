class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_index = 0
        e_index = len(s) - 1

        while s_index < e_index:
            if not s[s_index].isalnum():
              s_index += 1
            elif not s[e_index].isalnum():
              e_index -= 1
            elif s[s_index].lower() == s[e_index].lower():
              s_index += 1
              e_index -= 1
            else:
              return False
        return True