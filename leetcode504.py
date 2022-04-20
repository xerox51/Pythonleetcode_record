class Solution(object):
    def convertToBase7(self, num):
        def toSeven(n):
            if n >= -6 and n <= 6:
                return str(n)
            if n >= 7:
                item = []
                while n >= 7:
                    m = n % 7
                    item.append(str(m))
                    n = n//7
                item.append(str(n))
                item.reverse()
                return ''.join(item)
            if n == -7:
                return str(-10)

        def negativetoSeven(m):
            return "-" + toSeven(abs(m))

        if num < -7:
            return negativetoSeven(num)
        else:
            return toSeven(num)
