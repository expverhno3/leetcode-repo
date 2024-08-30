#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.key2val = {}
        self.val2key = {}

    def insert(self, val: int) -> bool:
        if val in self.val2key:
            return False
        self.val2key[val] = hash(val)
        self.key2val[hash(val)] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.val2key:
            key = self.val2key[val]
            del(self.val2key[val])
            del(self.key2val[key])
            return True
        return False

    def getRandom(self) -> int:
        import random
        return random.choice(list(self.val2key.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

