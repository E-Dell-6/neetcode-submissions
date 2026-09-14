class Solution:

    def isPalindrome(self, s: str) -> bool:

        start = 0
        finish = len(s) - 1

        while start < finish:
            if not s[start].isalnum():
                start += 1
                continue

            if not s[finish].isalnum():
                finish -= 1
                continue

            if s[finish].lower() == s[start].lower():
                finish -= 1
                start += 1
                continue

            else:
                return False

        return True