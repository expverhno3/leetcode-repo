#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        # sol from: https://leetcode.com/problems/counting-bits/solutions/79539/three-line-java-solution/?source=vscode
        
        ans = [0] * (n+1)
        for i in range(1,n+1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
# @lc code=end

