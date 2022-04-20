class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            if len(s.strip()) != 0:
                return len(s.split())
            else:
                return 0
