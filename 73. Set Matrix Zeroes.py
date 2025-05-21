class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colums = len(matrix)
        rows = len(matrix[0])
        x= []
        y= []
        for i in range(colums):
                for e in range(rows):
                    if matrix[i][e] == 0:
                        x.append(e)
                        y.append(i)
        for fila in y:
            for col in range(rows):
                matrix[fila][col] = 0
        for col in x:
            for fila in range(colums):
                matrix[fila][col] = 0 


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colums = len(matrix)
        rows = len(matrix[0])
        x= set()
        y= set()
        dic= {}
        for i in range(colums):
                for e in range(rows):
                    if matrix[i][e] == 0:
                        x.add(e)
                        y.add(i)
        for fila in y:
            for col in range(rows):
                matrix[fila][col] = 0
        for col in x:
            for fila in range(colums):
                matrix[fila][col] = 0 
        