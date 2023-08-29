class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time complexity : O(log(m * n))
        # Get length of row and column 
        r = len(matrix)
        c = len(matrix[0])

        # Set low, high and mid for binary search to select row 
        low = 0
        high = r-1
        mid = low + (high-low)//2

        # Set row index to mid 
        row_idx = mid

        # Binary search to find element row 
        while low <= high:
            if matrix[mid][0] == target or matrix[mid][c-1]== target:
                return True
            elif matrix[mid][0] < target and matrix[mid][c-1] > target:
                row_idx = mid
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1 

            mid = low + (high-low)//2
        
        # Set low, high and mid for binary serach to select column
        low = 0
        high = c-1
        mid = low + (high-low)//2

        # Binary search to select column index
        while low <= high:
            if matrix[row_idx][mid] == target:
                return True
            elif matrix[row_idx][mid]< target:
                 low = mid + 1
            else:
                high = mid -1 
            mid = low + (high-low)//2

        return False
