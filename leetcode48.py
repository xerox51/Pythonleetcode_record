class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i = 0
        temp_list = []
        while i < len(matrix):
            temp = []
            for items in matrix:
                temp.append(items[i])
            temp_list.append(temp)
            i += 1
        for i in range(len(matrix)):
            matrix[i] = temp_list[i]
            matrix[i].reverse()
