class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x >= 0 and x <= 9:
            return True
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
