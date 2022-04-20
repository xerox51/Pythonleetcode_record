class Solution(object):
    def longestPalindrome(self, s):
        temp = []
        for i in range(len(s)):
            temp.append(s[i])
        answer1 = []
        answer2 = []
        answer3 = []
        answer3_f = 0
        for item in set(temp):
            if temp.count(item) % 2 == 0:
                answer1.append(temp.count(item))
            if temp.count(item) == 1:
                answer2.append(temp.count(item))
            if temp.count(item) % 2 == 1 and temp.count(item) > 2:
                answer3.append(temp.count(item))
        if answer3:
            answer3_f = sum(answer3) - len(answer3)
        if answer1 and answer2 and answer3:
            return sum(answer1) + answer3_f + 1
        if not answer1 and answer2 and answer3:
            return answer3_f + 1
        if not answer1 and not answer2 and answer3:
            return answer3_f + 1
        if answer1 and not answer2 and not answer3:
            return sum(answer1)
        if answer1 and answer2 and not answer3:
            return sum(answer1)+1
        if not answer1 and answer2 and not answer3:
            return 1
        if answer1 and not answer2 and answer3:
            return sum(answer1) + answer3_f + 1
