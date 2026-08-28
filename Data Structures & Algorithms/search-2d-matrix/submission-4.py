class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):

            currentRow = matrix[i]
            
            if target < currentRow[0] or target > currentRow[len(currentRow) - 1]:
                continue

            lo,hi = 0,len(currentRow) - 1

            while lo <= hi: 

                mid = ( lo + hi ) // 2

                if currentRow[mid] == target:
                    return True
                elif target < currentRow[mid]:
                    hi -= 1
                elif target > currentRow[mid]:
                    lo += 1 

        return False



            

        