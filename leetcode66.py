class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = int(''.join([str(digits[i]) for i in range(len(digits))])) + 1
        return [int(str(temp)[i]) for i in range(len(str(temp)))]
