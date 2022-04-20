class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        temp = set(s)
        if len(temp) == 1:
            return 1
        
        if len(s) == len(temp):
            return len(s)

        else:
            counts = [1 for l in range(len(s)-1)]
            for i in range(0,len(s)-1):
                flag = s[i]
                for j in range(i+1,len(s)):
                    if s[j] != flag and flag not in s[i:j-1]:
                        counts[i] += 1
                        flag = s[j]
                        if flag in s[i:j-1]:
                            counts[i] -= 1
                            break
                        
            return max(counts)          
