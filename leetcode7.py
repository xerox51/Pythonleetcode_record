class Solution:
    def reverse(self, x: int) -> int:
        if x >= -9 and x <= 9:
            return x
        else:
            temp = []
            y = str(x)
            for i in range(len(y)):
                temp.append(y[i])
            maxindex = len(temp)
            while maxindex > 0:
                if temp[maxindex-1] == "0":
                    maxindex -= 1
                else:
                    break
            del temp[maxindex:]
            if temp[0] != "-":
                answer = int(''.join(reversed(temp)))
                if answer < 2147483648:
                    return answer
                else:
                    return 0
            else:
                answer = int("-" + ''.join(reversed(temp[1:])))
                if answer >= -2147483648:
                    return answer
                else:
                    return 0
