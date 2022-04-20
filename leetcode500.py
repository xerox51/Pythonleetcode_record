class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def judge(item):
            list_one = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
            list_two = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
            list_three = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
            temp = []
            for i in range(len(item)):
                temp.append(item[i])
            if set(list_one) | set(temp) == set(list_one):
                return True
            if set(list_two) | set(temp) == set(list_two):
                return True
            if set(list_three) | set(temp) == set(list_three):
                return True
            return False
        answer = []
        for item in words:
            if judge(item.lower()):
                answer.append(item)
        return answer
