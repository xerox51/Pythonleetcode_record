class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def tostr(num):
            temp = []
            s = str(num)
            for i in range(len(s)):
                if int(s[i]) != 0:
                    temp.append(num % int(s[i]))
            if sum(temp) == 0 and len(temp) == len(s):
                return True
            else:
                return False
        answer = []
        for i in range(left, right+1):
            if tostr(i):
                answer.append(i)
        return answer
