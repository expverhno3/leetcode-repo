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
- how
  - construct two hash table, and compare
  - hash table: char as key and frequency as value

### 字符串中的第一个唯一字符

- id: 387
- name: first-unique-character-in-a-string
- tag: Queue, Hash Table, String, Counting
- how
  - make a frequency table then check it.

### 同构字符串

- id: 205
- name: isomorphic-strings
- tag: Hash Table, String
- how
  - (please don't use frequency table again!)
  - since they can replace each char with another corresponding char: build two table to save this mapping relationship: s2t and t2s
  - then iterate to build table and check if there's conflict

### 回文排列

- id: 266
- name: palindrome-permutation
- tag: Bit Manipulation, Hash Table, String
- how
  - observe property: chars in palindrome appear in pair, only one char in the middle can be single.
  - make a frequency table, then calculate the frequency % 2 to check its parity
  - sum over parity and if there's more than 1 odd number: False

### 最长回文串

- id: 409
- name: longest-palindrome
- tag: Greedy, Hash Table, String
- how
  - can only keep one odd char
  - sum even frequency and odd frequency -1
  - if no odd frequency: sum is result
  - if there's odd frequency: sum + 1


--- 


## 双指针

### 判断子序列

- id: 392
- name: is-subsequence
- tag: Two Pointers, String, Dynamic Programming
- how
  - iterate the target string, use pointer to track which char we are going to track
  - by the end of iteration, we should be able to take out the same s string

### 链表的中间结点

- id: 908
- name: middle-of-the-linked-list
- tag: Linked List, Two Pointers
- how
  - two pointers, one go 2 steps, one go 1 step. then the slow one will point to the middle

### 相交链表

- id: 160
- name: intersection-of-two-linked-lists
- tag: Hash Table, Linked List, Two Pointers
- how
  - create a table of one linked list, then iterate through the other

### 两数之和 II - 输入有序数组

- id: 167
- name: two-sum-ii-input-array-is-sorted
- tag: Array, Two Pointers, Binary Search
- how
  - use two pointers, one start at the beginning, the other starts at the end

### 环形链表 II

- id: 142
- name: linked-list-cycle-ii
- tag: Hash Table, Linked List, Two Pointers
- how
  - check this & comment of "Shinkyu" [solution](https://leetcode.com/problems/linked-list-cycle-ii/solutions/1701128/c-java-python-slow-and-fast-image-explanation-beginner-friendly) 
  - basically: `fast` has step size 2 and `slow` has step size 1
    - if meet: there's a circular connection
      - how long is the circle: `x` denotes # of step before start of circle, `y` denotes # of step between start of circle until `fast` and `slow` meet
        - `slow`: x + y
        - `fast`: 2*(x+y) if considering 2x step size; if considering circle (because `fast` has repeat circle multiple times ahead of slow so they can meet), then it's x + y + C ("C" is # of steps to repeat multiple circles)
        - from here we can calculate $C = x + y$
        - therefore, we can reset `fast` to the beginning, then both `fast` and `slow` run $x$ steps, they can meet together again at the beginning of circle.

### 反转字符串中的单词

- id: 151
- name: reverse-words-in-a-string
- tag: Two Pointers, String
- how
  - two methods
    1. use a list to save where the word begins and ends (my solution)
    2. reverse entire string, then reverse word, using two pointers, one at the beginning, one at the end, swap with each other

### 无重复字符的最长子串

- id: 3
- name: longest-substring-without-repeating-characters
- tag: Hash Table, String, Sliding Window
- how
  - use two pointer: one points at the beginning of sub-string, one at the end of substring
  - then maintain a table to keep track of index of each character, if found two same character within the scope of two pointer, move left to the right of previous repeated character

### 三数之和

- id: 15
- name: 3sum
- tag: Array, Two Pointers, Sorting
- how
  - fix one and find the other two using two pointer
  - fix left pointer, then find middle and right

### 滑动窗口最大值

- id: 239
- name: sliding-window-maximum
- tag: Queue, Array, Sliding Window, Monotonic Queue, Heap (Priority Queue), MARK
- how
  - [ref here](https://leetcode.com/problems/sliding-window-maximum/solutions/3918847/video-ex-amazon-explains-a-solution-with-python-javascript-java-and-c/)
  - build a queue stores idx of "potential" max value
    - on the left side of queue, the idx correspond larger value
    - on the left side of queue, the idx is also smaller
    - therefore, the leftmost idx will be the max value of this window
    - how to build: compare the last value and the right pointer, if last value is smaller, then it can't be the wanted max value, pop out
  - after the windows length is reach, left pointer need to move, and compare it with leftmost idx


--- 


## 模拟

### 字符串相加

- id: 415
- name: add-strings
- tag: Math, String, Simulation
- how
  - padding two string to the same length
  - convert int digit by digit
  - deal with carry digit

### 旋转字符串

- id: 812
- name: rotate-string
- tag: String, String Matching
- how
  - move original string until first char of goal == rotated original string
  - compare entire string

### 验证栈序列

- id: 946
- name: validate-stack-sequences
- tag: Stack, Array, Simulation, MARK
- how
  - basically keep pushing into stack, until we meet the element that needs to be pushed into "popped". Then keep popping. After that continue pushing element. we just need to know when to pop, so if this operation is viable, stack temporarily store numbers should be empty

### Z 字形变换

- id: 6
- name: zigzag-conversion
- tag: String
- how
  - still: simulate this process

### 螺旋矩阵

- id: 54
- name: spiral-matrix
- tag: Array, Matrix, Simulation, MARK
- how
  - always pop the first row of matrix
  - then **rotate** the matrix my counterclockwise for 90 degree
  - NOTE: zip(*matrix) can transpose the matrix, then reverse the order of row -> 90 degree counterclockwise rotation!

### 螺旋矩阵 II

- id: 59
- name: spiral-matrix-ii
- tag: Array, Matrix, Simulation, MARK
- how
  - fill in matrix with invalid values
  - define different direction update rules
  - when updating meets boundary (out of index OR run into valid value), change direction

### 旋转图像

- id: 48
- name: rotate-image
- tag: Array, Math, Matrix
- how
  - transpose then reverse order of each row
  - NOTE: use `A[:]` to modify the list, if use `A=...`, it will copy things to another place

### 字符串转换整数 (atoi)

- id: 8
- name: string-to-integer-atoi
- tag: String
- how
  - use state machine
    - there's 3 cases: space, number, sign
    - as long as how states are transferred, it can automatically parse


--- 


## 查找

### 二分查找

- id: 704
- name: binary-search
- tag: Array, Binary Search
- how
  - NOTE: while condition is <=, not just <

### 第一个错误的版本

- id: 278
- name: first-bad-version
- tag: Binary Search, Interactive
- how
  - binary search
  - return `left` value: finally there will be `left` at the first bad version position, and `left > right`

### 寻找数组的中心下标

- id: 724
- name: find-pivot-index
- tag: Array, Prefix Sum, MARK
- how
  - sum up the entire array
  - then linearly search from the left side: move out the current value, check if right sum == left sum, if not, put that value to the left sum
  - keep comparing until we iterate the entire array

### 寻找重复数

- id: 287
- name: find-the-duplicate-number
- tag: Bit Manipulation, Array, Two Pointers, Binary Search
- how
  - duplicate number will generate a cycle (if considered values as index), then we can use fast-slow pointers to find the start of cycle to find the duplicate number

### 寻找旋转排序数组中的最小值 II

- id: 154
- name: find-minimum-in-rotated-sorted-array-ii
- tag: Array, Binary Search
- how
  - 1. linear search
    - sort the array, then compare the element with the next element
  - 2. binary search (MARK)
    - compare the middle element with the last element
      - if `nums[middle] > nums[right]`: min value at the right half, let `left = middle + 1`
      - if `nums[right] > nums[middle]`: min value at the left half, let `right = middle` (why not `middle - 1`? because `middle` can point at the min)
      - if `nums[right] == nums[right]`: don't know what's going on, but we are sure we can move `right` pointer back (no way it can increase!)


--- 


## 搜索

### 二叉树的层序遍历

- id: 102
- name: binary-tree-level-order-traversal
- tag: Tree, Breadth-First Search, Binary Tree
- how
  - put nodes in a queue, append new nodes at the end, popleft to indicate traverse
  - how to know how many nodes at each level? (MARK)
    - length of queue == number of nodes at each level 

### 二叉树的锯齿形层序遍历

- id: 103
- name: binary-tree-zigzag-level-order-traversal
- tag: Tree, Breadth-First Search, Binary Tree
- how
  - use a flag to indicate level order (need to use `.reverse()` or not)

### 二叉树的最近公共祖先

- id: 236
- name: lowest-common-ancestor-of-a-binary-tree
- tag: Tree, Depth-First Search, Binary Tree, MARK
- how
  - recursively find:
    - end condition: if p or q is at root: root is LCA -> return LCA
    - return LCA of both branch (left and right)
      - if p and q at same branch && one is the other's parent node: whatever q or q at the top level is LCA
      - if p and q at same branch && their direct parent is not the same -> root is LCA
      - if p and q at different branch: both branch will have return value -> root is LCA

### 二叉搜索树中第K小的元素

- id: 230
- name: kth-smallest-element-in-a-bst
- tag: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- how
  1. In-order traverse (MARK)
     1. return values from left to middle to right
     2. since it's binary search tree -> left node > root > right node
     3. in-order traverse will return nodes in ascending order
     4. optimization: no need to save all the values -> just return the one we want!

### 二叉搜索树的最近公共祖先

- id: 235
- name: lowest-common-ancestor-of-a-binary-search-tree
- tag: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- how
  - since it's binary search tree, we only need to compare the value of p and q with root:
    - if at the same side: both q an p are > or < than root value: find at that single branch
    - if at different sides: root is LCA

### 将二叉搜索树转化为排序的双向链表

- id: 758
- name: convert-binary-search-tree-to-sorted-doubly-linked-list
- tag: Stack, Tree, Depth-First Search, Binary Search Tree, Linked List, Binary Tree, Doubly-Linked List
- problem
  - convert binary search tree into a sorted circular doubly-linked list using inplace transformation
- how
  - in order traverse
  - use head to pin first node (smallest, aka first node of traverse), then keep updating node.left (since we are in-order traverse, start operating after left all used)


### 数组中的第K个最大元素

- id: 215
- name: kth-largest-element-in-an-array
- tag: Array, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)
- how
  - push previous k numbers into a heap
  - then pushpop the following elements (push new element in, then pop the smallest number out)
    - heap maintains top k largest numbers
    - heap top is the smallest number of k largest numbers, the result wanted

### 课程表

- id: 207
- name: course-schedule
- tag: Depth-First Search, Breadth-First Search, Graph, Topological Sort, MARK
- how
  - based on (course, prerequisite) vector, build a **adj list**: index is prerequisite and saved a list that with this prerequisite finished, this course can be done next
  - need info from the other direction: maintain a **number_prerequisite** that states the number of prerequisite course of each course, can be used to indicate if this course can be started
  - use a queue to save all courses can be finished
  - use a counter to count number of courses finished


--- 


## 回溯

### 二叉树的最大深度

- id: 104
- name: maximum-depth-of-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- how
  - level order traverse
  - recursion: return max depth of left and right nodes; if root doesn't exist, return 0

### 路径总和 II

- id: 113
- name: path-sum-ii
- tag: Tree, Depth-First Search, Backtracking, Binary Tree
- how
  - depth first, pre-order, accumulate previous nodes' values
  - check if it's leaf node (no children), then sum up and check if == target
  - pop out and continue

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


