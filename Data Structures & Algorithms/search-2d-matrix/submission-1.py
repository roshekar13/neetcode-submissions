class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_r = 0
        high_r = len(matrix)-1
        while low_r <= high_r:
            mid_r = (low_r + high_r) // 2
            if target in matrix[mid_r]:
                print("we got here")
                #nested binary here
                curr_arr = matrix[mid_r]
                low = 0
                high = len(curr_arr)-1
                while low <= high:
                    mid = (low + high)//2
                    if target == curr_arr[mid]:
                        return True
                    if target > curr_arr[mid]:
                        low = mid + 1
                    else:
                        high = mid -1
            if target > matrix[mid_r][-1]:
                low_r = mid_r + 1
            else:
                high_r = mid_r - 1
        return False
