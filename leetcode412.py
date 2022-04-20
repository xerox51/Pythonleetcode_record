class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        temp = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                temp.append("FizzBuzz")
            if i % 5 == 0 and i % 3:
                temp.append("Buzz")
            if i % 3 == 0 and i % 5:
                temp.append("Fizz")
            if i % 5 and i % 3:
                temp.append(str(i))
        return temp
