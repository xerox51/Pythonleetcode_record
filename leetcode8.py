class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        new_s = s.lstrip()
        if len(new_s) == 0:
            return 0
        if len(new_s) == 1:
            if new_s[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 0
            else:
                return int(new_s)
        if new_s.startswith("+-") or new_s.startswith("-+") or new_s.startswith("--") or new_s.startswith("++"):
            return 0
        if new_s.startswith("-"):
            if new_s[1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 0
            flag = 0
            for i in range(1, len(new_s)):
                if new_s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    flag = i
                    break
            if flag == 0:
                num = -int(new_s[1:])
            else:
                num = -int(new_s[1:flag])
            if num < -2147483648:
                return -2147483648
            else:
                return num
        if new_s.startswith("+"):
            if new_s[1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 0
            flag = 0
            for i in range(1, len(new_s)):
                if new_s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    flag = i
                    break
            if flag == 0:
                num = int(new_s[1:])
            else:
                num = int(new_s[1:flag])
            if num >= 2147483648:
                return 2147483647
            else:
                return num
        if new_s[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 0
        if new_s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            flag = 0
            for i in range(len(new_s)):
                if new_s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    flag = i
                    break
            if flag == 0:
                num = int(new_s)
            else:
                num = int(new_s[0:flag])
            if num >= 2147483648:
                return 2147483647
            else:
                return num
