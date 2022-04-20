class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def counts(i, items):
            flag = True
            tempstr = strs[0]
            for j in range(len(items)):
                if not strs[j][0:i].startswith(tempstr[0:i]):
                    flag = False
            return flag
        if len(strs) == 1:
            return strs[0]
        temp = []
        for item in strs:
            temp.append(len(item))
        if min(temp) == 0:
            return ""
        if min(temp) == 1:
            flag = True
            for item in strs:
                if not item.startswith(strs[0][0]):
                    flag = False
            if flag:
                return strs[0][0]
            else:
                return ""
        else:
            for i in range(min(temp)+1):
                flag_two = counts(min(temp)+1-i, strs)
                if flag_two:
                    return strs[0][0:min(temp)+1-i]
                    break
            return ""
