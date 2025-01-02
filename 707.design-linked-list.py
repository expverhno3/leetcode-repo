#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start

class Node:
    def __init__(self, val:int=0):
        self.val = val
        self.next:Node = None


class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node()
        self.tail = Node()
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        else:
            cur = self.dummy_head.next
            while index > 0:
                cur = cur.next
                index -= 1
            return cur.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        head = self.dummy_head.next
        self.dummy_head.next = new
        new.next = head
        self.length += 1
        if self.length == 1:
            self.tail = new
        return None

    def addAtTail(self, val: int) -> None:
        tail = self.tail
        new = Node(val)
        self.tail = new
        tail.next = new
        self.length += 1
        if self.length == 1:
            self.dummy_head.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return None
        elif index < 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            cur = self.dummy_head
            while index > 0:
                cur = cur.next
                index -= 1
            new = Node(val)
            new.next = cur.next
            cur.next = new
            self.length += 1
        return None
                

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        cur = self.dummy_head
        if index == self.length-1:
            flag = True
        else:
            flag = False
        while index > 0:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.length -= 1
        if flag:
            self.tail = cur
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

