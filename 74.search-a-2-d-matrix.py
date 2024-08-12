#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def binary_search(head, tail, target, cur_row=None):
            if cur_row is None:  # if search in row
                while head <= tail:
                    mid = (head + tail) // 2
                    print(f'search rows, {head}, {tail}, {mid}')
                    if matrix[mid][0] > target:
                        tail = mid - 1
                    elif matrix[mid][0] < target:
                        head = mid + 1
                    else:
                        return mid, True
                return tail, False
            else: # search in col
                while head <= tail:
                    mid = (head + tail) // 2
                    print(f"{head}, {tail}, {mid}")
                    if matrix[cur_row][mid] > target:
                        tail = mid - 1
                    elif matrix[cur_row][mid] < target:
                        head = mid + 1
                    else:
                        return mid, True
                return tail, False
        res, is_res = binary_search(0, m-1, target)
        print(f"at row {res}")
        if is_res:
            return True
        else:
            res, is_res = binary_search(0,n-1, target, cur_row=res)
            print(f"at col: {res}")
            return is_res
                

        # search row first


# @lc code=end
