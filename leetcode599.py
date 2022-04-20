class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = sorted(list(set(list1) & set(list2)))
        fuck = []
        for item in temp:
            fuck.append(list1.index(item)+list2.index(item))
        fucktwo = []
        for i in range(len(fuck)):
            if fuck[i] == min(fuck):
                fucktwo.append(i)
        best = []
        for item3 in fucktwo:
            best.append(temp[item3])
        return best
