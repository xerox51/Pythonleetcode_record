class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        if len(s) > 1:
            t = s.replace(" ", "").lower()
            temp = []
            for i in range(len(t)):
                if t[i].isdigit() or t[i].isalpha():
                    temp.append(t[i])
            return ''.join(temp) == ''.join(reversed(temp))
