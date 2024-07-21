#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        str_nums = [str(num) for num in nums]

        # NOTE: just consider one number only appear once... NOT working when a number shows up multiple times (like: `[5,54,52,67,68,5,52,17,93,53]`)
        # def swap(str_nums:List[str]):
        #     for i in range(1, len(str_nums)):
        #         if str_nums[i] + str_nums[i-1] < str_nums[i-1] + str_nums[i]:
        #             str_nums[i], str_nums[i-1] = str_nums[i-1], str_nums[i]

        # swap(str_nums)

        def quick_sort(l, r):
            # check ob vault, hello-algo -> ch11-sorting -> quick sort
            if l >= r:
                return
            i, j = l, r
            while i < j:
                # NOTE: 哨兵划分，l所在为基准数
                while str_nums[j] + str_nums[l] >= str_nums[l] + str_nums[j] and i < j:
                    j -= 1
                while str_nums[i] + str_nums[l] <= str_nums[l] + str_nums[i] and i < j:
                    i += 1
                str_nums[i], str_nums[j] = str_nums[j], str_nums[i]
            str_nums[i], str_nums[l] = str_nums[l], str_nums[i]
            # after this: left < base number (str_nums[l]) < right
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        quick_sort(0, len(str_nums) - 1)

        res = ""
        for i in range(len(str_nums) - 1, -1, -1):
            res += str_nums[i]

        if res[0] == "0":
            return "0"

        return res


# @lc code=end
