class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def mutiply(x, n):
            if x == 1 or n == 0:
                return 1
            if x == 0:
                return 0
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n % 2 == 0:
                return mutiply(x*x, n/2)
            if n % 2 != 0:
                return x*mutiply(x*x, (n-1)/2)
        return mutiply(x, n)
