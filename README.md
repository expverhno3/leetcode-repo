NOTE: if there's **MARK** in tag, need to revisit this question


## 链表

### 合并两个有序链表

- id: 21
- name: merge-two-sorted-lists
- tag: Recursion, Linked List
- how
  - use two pointers & compare value

### 反转链表

- id: 206
- name: reverse-linked-list
- tag: Recursion, Linked List
- how
  - use two pointers
  - construct result linked list by pointing back


### 分隔链表

- id: 86
- name: partition-list
- tag: Linked List, Two Pointers
- how
  - traverse given list and based on the partition value construct two list (one list with nodes > x, one list with nodes <= x)
  - connect two list together & **point end node to none**

### 删除链表中的节点

- id: 237
- name: delete-node-in-a-linked-list
- tag: Linked List
- how
  - !trick: no need to copy each node one by one
  - just copy the value of next node, then skip the next node!

### 随机链表的复制

- id: 138
- name: copy-list-with-random-pointer
- tag: Hash Table, Linked List, MARK
- how
  - Sol 1 (2 pass):
    - iterate original list to construct hash table mapping old list node -> copied new list node
    - iterate original list again to build pointers (next & random)
  - Sol 2 (1 pass):
    - iterate original list, and maintain a "visited" hash table (mapping: original node -> copied new node): current node, next node, random node at first, then construct the link of current copied node


--- 


## 栈与队列

### 有效的括号

- id: 20
- name: valid-parentheses
- tag: Stack, String
- how
  - push open parentheses into stack
  - if found close parentheses, check if it matches top of stack
    - if matched: pop stack and go on

### 最小栈

- id: 155
- name: min-stack
- tag: Stack, Design
- how:
  - use space to trade time
  - maintain two stacks: one keep the order of "push", one keep the min value at top of stack
  - check if popped value is the same as top of min stack, if true, pop the min stack.

### 用栈实现队列

- id: 232
- name: implement-queue-using-stacks
- tag: Stack, Design, Queue
- how:
  - stack: FILO; pop stack and use another stack to take the popped value: FIFO (== reverse order of stack == queue)

### 字符串解码

- id: 394
- name: decode-string
- tag: Stack, Recursion, String, MARK
- how
  - first: how we deal with "()"?
    - keep looking util the most inner ), then "unpack" operation from inner to outer
  - use stack to save previous states, then pop back when we get to its corresponding ")"
  - must maintain the relationship between number and the kept string in stack (if # of number > # of string: will make previous string being copied more)

### 数据流的中位数

- id: 295
- name: find-median-from-data-stream
- tag: Design, Two Pointers, Data Stream, Sorting, Heap (Priority Queue), MARK
- how: [check code](295.find-median-from-data-stream.py)


--- 


## 哈希表

### 有效的字母异位词

- id: 242
- name: valid-anagram
- tag: Hash Table, String, Sorting

### 字符串中的第一个唯一字符

- id: 387
- name: first-unique-character-in-a-string
- tag: Queue, Hash Table, String, Counting

### 同构字符串

- id: 205
- name: isomorphic-strings
- tag: Hash Table, String

### 回文排列

- id: 266
- name: palindrome-permutation
- tag: Bit Manipulation, Hash Table, String

### 最长回文串

- id: 409
- name: longest-palindrome
- tag: Greedy, Hash Table, String


--- 


## 双指针

### 判断子序列

- id: 392
- name: is-subsequence
- tag: Two Pointers, String, Dynamic Programming

### 链表的中间结点

- id: 908
- name: middle-of-the-linked-list
- tag: Linked List, Two Pointers

### 相交链表

- id: 160
- name: intersection-of-two-linked-lists
- tag: Hash Table, Linked List, Two Pointers

### 两数之和 II - 输入有序数组

- id: 167
- name: two-sum-ii-input-array-is-sorted
- tag: Array, Two Pointers, Binary Search

### 环形链表 II

- id: 142
- name: linked-list-cycle-ii
- tag: Hash Table, Linked List, Two Pointers

### 反转字符串中的单词

- id: 151
- name: reverse-words-in-a-string
- tag: Two Pointers, String

### 无重复字符的最长子串

- id: 3
- name: longest-substring-without-repeating-characters
- tag: Hash Table, String, Sliding Window

### 三数之和

- id: 15
- name: 3sum
- tag: Array, Two Pointers, Sorting

### 滑动窗口最大值

- id: 239
- name: sliding-window-maximum
- tag: Queue, Array, Sliding Window, Monotonic Queue, Heap (Priority Queue)


--- 


## 模拟

### 字符串相加

- id: 415
- name: add-strings
- tag: Math, String, Simulation

### 旋转字符串

- id: 812
- name: rotate-string
- tag: String, String Matching

### 验证栈序列

- id: 983
- name: validate-stack-sequences
- tag: Stack, Array, Simulation

### Z 字形变换

- id: 6
- name: zigzag-conversion
- tag: String

### 螺旋矩阵

- id: 54
- name: spiral-matrix
- tag: Array, Matrix, Simulation

### 螺旋矩阵 II

- id: 59
- name: spiral-matrix-ii
- tag: Array, Matrix, Simulation

### 旋转图像

- id: 48
- name: rotate-image
- tag: Array, Math, Matrix

### 字符串转换整数 (atoi)

- id: 8
- name: string-to-integer-atoi
- tag: String


--- 


## 查找

### 二分查找

- id: 792
- name: binary-search
- tag: Array, Binary Search

### 第一个错误的版本

- id: 278
- name: first-bad-version
- tag: Binary Search, Interactive

### 寻找数组的中心下标

- id: 724
- name: find-pivot-index
- tag: Array, Prefix Sum

### 寻找重复数

- id: 287
- name: find-the-duplicate-number
- tag: Bit Manipulation, Array, Two Pointers, Binary Search

### 寻找旋转排序数组中的最小值 II

- id: 154
- name: find-minimum-in-rotated-sorted-array-ii
- tag: Array, Binary Search


--- 


## 搜索

### 二叉树的层序遍历

- id: 102
- name: binary-tree-level-order-traversal
- tag: Tree, Breadth-First Search, Binary Tree

### 二叉树的锯齿形层序遍历

- id: 103
- name: binary-tree-zigzag-level-order-traversal
- tag: Tree, Breadth-First Search, Binary Tree

### 二叉树的最近公共祖先

- id: 236
- name: lowest-common-ancestor-of-a-binary-tree
- tag: Tree, Depth-First Search, Binary Tree

### 二叉搜索树中第K小的元素

- id: 230
- name: kth-smallest-element-in-a-bst
- tag: Tree, Depth-First Search, Binary Search Tree, Binary Tree

### 二叉搜索树的最近公共祖先

- id: 235
- name: lowest-common-ancestor-of-a-binary-search-tree
- tag: Tree, Depth-First Search, Binary Search Tree, Binary Tree

### 将二叉搜索树转化为排序的双向链表

- id: 758
- name: convert-binary-search-tree-to-sorted-doubly-linked-list
- tag: Stack, Tree, Depth-First Search, Binary Search Tree, Linked List, Binary Tree, Doubly-Linked List

### 数组中的第K个最大元素

- id: 215
- name: kth-largest-element-in-an-array
- tag: Array, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)

### 课程表

- id: 207
- name: course-schedule
- tag: Depth-First Search, Breadth-First Search, Graph, Topological Sort


--- 


## 回溯

### 二叉树的最大深度

- id: 104
- name: maximum-depth-of-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree

### 路径总和 II

- id: 113
- name: path-sum-ii
- tag: Tree, Depth-First Search, Backtracking, Binary Tree

### 全排列

- id: 46
- name: permutations
- tag: Array, Backtracking

### 全排列 II

- id: 47
- name: permutations-ii
- tag: Array, Backtracking

### 组合总和

- id: 39
- name: combination-sum
- tag: Array, Backtracking

### 组合总和 II

- id: 40
- name: combination-sum-ii
- tag: Array, Backtracking

### 单词搜索

- id: 79
- name: word-search
- tag: Array, String, Backtracking, Matrix


--- 


## 分治

### 翻转二叉树

- id: 226
- name: invert-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree

### 对称二叉树

- id: 101
- name: symmetric-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree

### Pow(x, n)

- id: 50
- name: powx-n
- tag: Recursion, Math

### 平衡二叉树

- id: 110
- name: balanced-binary-tree
- tag: Tree, Depth-First Search, Binary Tree

### 从前序与中序遍历序列构造二叉树

- id: 105
- name: construct-binary-tree-from-preorder-and-inorder-traversal
- tag: Tree, Array, Hash Table, Divide and Conquer, Binary Tree

### 二叉树的序列化与反序列化

- id: 297
- name: serialize-and-deserialize-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Design, String, Binary Tree


--- 


## 动态规划

### 斐波那契数

- id: 1013
- name: fibonacci-number
- tag: Recursion, Memoization, Math, Dynamic Programming

### 爬楼梯

- id: 70
- name: climbing-stairs
- tag: Memoization, Math, Dynamic Programming

### 一维数组的动态和

- id: 1603
- name: running-sum-of-1d-array
- tag: Array, Prefix Sum

### 买卖股票的最佳时机

- id: 121
- name: best-time-to-buy-and-sell-stock
- tag: Array, Dynamic Programming

### 最小路径和

- id: 64
- name: minimum-path-sum
- tag: Array, Dynamic Programming, Matrix

### 最大子数组和

- id: 53
- name: maximum-subarray
- tag: Array, Divide and Conquer, Dynamic Programming

### 打家劫舍

- id: 198
- name: house-robber
- tag: Array, Dynamic Programming

### 打家劫舍 II

- id: 213
- name: house-robber-ii
- tag: Array, Dynamic Programming

### 最长递增子序列

- id: 300
- name: longest-increasing-subsequence
- tag: Array, Binary Search, Dynamic Programming

### 正则表达式匹配

- id: 10
- name: regular-expression-matching
- tag: Recursion, String, Dynamic Programming

### 丑数 II

- id: 264
- name: ugly-number-ii
- tag: Hash Table, Math, Dynamic Programming, Heap (Priority Queue)


--- 


## 贪心

### 买卖股票的最佳时机 II

- id: 122
- name: best-time-to-buy-and-sell-stock-ii
- tag: Greedy, Array, Dynamic Programming

### 搜索二维矩阵 II

- id: 240
- name: search-a-2d-matrix-ii
- tag: Array, Binary Search, Divide and Conquer, Matrix

### 盛最多水的容器

- id: 11
- name: container-with-most-water
- tag: Greedy, Array, Two Pointers

### 最大数

- id: 179
- name: largest-number
- tag: Greedy, Array, String, Sorting

### 分发糖果

- id: 135
- name: candy
- tag: Greedy, Array

### 最多能完成排序的块 II

- id: 779
- name: max-chunks-to-make-sorted-ii
- tag: Stack, Greedy, Array, Sorting, Monotonic Stack


--- 


## 位运算

### 位1的个数

- id: 191
- name: number-of-1-bits
- tag: Bit Manipulation, Divide and Conquer

### 2 的幂

- id: 231
- name: power-of-two
- tag: Bit Manipulation, Recursion, Math

### 两整数之和

- id: 371
- name: sum-of-two-integers
- tag: Bit Manipulation, Math

### 只出现一次的数字

- id: 136
- name: single-number
- tag: Bit Manipulation, Array

### 只出现一次的数字 II

- id: 137
- name: single-number-ii
- tag: Bit Manipulation, Array


--- 


## 数学

### 除自身以外数组的乘积

- id: 238
- name: product-of-array-except-self
- tag: Array, Prefix Sum

### 多数元素

- id: 169
- name: majority-element
- tag: Array, Hash Table, Divide and Conquer, Counting, Sorting

### 整数拆分

- id: 343
- name: integer-break
- tag: Math, Dynamic Programming

### 格雷编码

- id: 89
- name: gray-code
- tag: Bit Manipulation, Math, Backtracking

### 找出游戏的获胜者

- id: 1951
- name: find-the-winner-of-the-circular-game
- tag: Recursion, Queue, Array, Math, Simulation

### 有效数字

- id: 65
- name: valid-number
- tag: String

### 第 N 位数字

- id: 400
- name: nth-digit
- tag: Math, Binary Search

### 数字 1 的个数

- id: 233
- name: number-of-digit-one
- tag: Recursion, Math, Dynamic Programming


--- 


