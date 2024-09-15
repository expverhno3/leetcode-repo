NOTE: if there's **MARK** in tag, need to revisit this question

# interview selected 88 questions

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
        - `fast`: 2\*(x+y) if considering 2x step size; if considering circle (because `fast` has repeat circle multiple times ahead of slow so they can meet), then it's x + y + C ("C" is # of steps to repeat multiple circles)
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
  - NOTE: zip(\*matrix) can transpose the matrix, then reverse the order of row -> 90 degree counterclockwise rotation!

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
      - if `nums[middle] == nums[right]`: don't know what's going on, but we are sure we can move `right` pointer back (no way it can increase!)

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

### 二叉搜索树中第 K 小的元素

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

### 数组中的第 K 个最大元素

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
- tag: Array, Backtracking, MARK
- how
  - what is permutation?
    - all numbers are distinct, so permutation just like swap with each other to get
  - how to find all permutation in certain order?
    - find permutation from left to right (**decide order**)
    - fixed first digit first, then find permutation of the remaining digits (where recursion kicks in) (**make choice**)
    - swap current digit with other digits at right (left are considered as fixed digits, and right are changeable digits) (**undo choice**)

### 全排列 II

- id: 47
- name: permutations-ii
- tag: Array, Backtracking
- how
  - same as previous question, but use a `set` to record when fixed one digit, what kind of element has been used.
    - if not be used: swap as above
    - if used: pass, continue find other digit to swap

### 组合总和

- id: 39
- name: combination-sum
- tag: Array, Backtracking
- how
  - choose number from 0 to (len(nums)-1), and you can only look forward (can't choose previous numbers)
  - choose -> subtract this number from target -> next decision -> undo decision

### 组合总和 II

- id: 40
- name: combination-sum-ii
- tag: Array, Backtracking, MARK
- how
  - focus on how to prune! (sorted + don't choose same value at the same level repeatedly)

### 单词搜索

- id: 79
- name: word-search
- tag: Array, String, Backtracking, Matrix, MARK
- how
  - backtracking basically is an "optimized" brute-force searching.
  - Optimization done by pruning
  - modify element in-place is far more efficient than create a new object to save paths to avoid accessing repeatedly

---

## 分治

### 翻转二叉树

- id: 226
- name: invert-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- how
  - easy!
  - method 1: recursion
  - method 2: use stack to save nodes, pop out node and inverse its children

### 对称二叉树

- id: 101
- name: symmetric-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree, MARK
- how
  - [ref](https://leetcode.cn/problems/symmetric-tree/solutions/2361627/101-dui-cheng-er-cha-shu-fen-zhi-qing-xi-8oba/?envType=study-plan-v2&envId=selected-coding-interview)
  - use a recursion function to test if values of corresponding nodes are equal

### Pow(x, n)

- id: 50
- name: powx-n
- tag: Recursion, Math, MARK
- how
  - fast power analysis (check your Obsidian note!)

### 平衡二叉树

- id: 110
- name: balanced-binary-tree
- tag: Tree, Depth-First Search, Binary Tree, MARK
- [how](https://leetcode.cn/problems/balanced-binary-tree/solutions/8737/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/?envType=study-plan-v2&envId=selected-coding-interview)
  - from bottom to top
    - calculate the depth of current node
      - None -> 0
      - leave node -> 1
      - leave node's parent node -> max(left, right) + 1
    - prune
      - if depth diff > 1: terminate, return False

### 从前序与中序遍历序列构造二叉树

- id: 105
- name: construct-binary-tree-from-preorder-and-inorder-traversal
- tag: Tree, Array, Hash Table, Divide and Conquer, Binary Tree
- how
  - construct a recursion function to build tree
    - parameter: root value & where root value is in inorder list & left boundary & right boundary
    - use dictionary to enhance efficient
      - dict\[value of node\] = index in inorder list

### 二叉树的序列化与反序列化

- id: 297
- name: serialize-and-deserialize-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Design, String, Binary Tree, MARK
- how
  - serialize & deserialize with same method (BFS or DFS)

---

## 动态规划

### 斐波那契数

- id: 509
- name: fibonacci-number
- tag: Recursion, Memoization, Math, Dynamic Programming
- how
  - recursion -> use dp table to avoid repeated calculation -> use only 2 variable to update

### 爬楼梯

- id: 70
- name: climbing-stairs
- tag: Memoization, Math, Dynamic Programming
- how
  - same as fib

### 一维数组的动态和

- id: 1480
- name: running-sum-of-1d-array
- tag: Array, Prefix Sum
- how
  - append sum of last number in `res` and current `num` in nums

### 买卖股票的最佳时机

- id: 121
- name: best-time-to-buy-and-sell-stock
- tag: Array, Dynamic Programming
- how
  - use two variable to track lowest price and largest profit
    - cost: min(current_price, cost)
    - profit: max(current_price - cost, profit)

### 最小路径和

- id: 64
- name: minimum-path-sum
- tag: Array, Dynamic Programming, Matrix
- how
  - change grid into min path sum to each box
  - init first row and first column (only update from one direction)
  - compare up and left, choose min to sum

### 最大子数组和

- id: 53
- name: maximum-subarray
- tag: Array, Divide and Conquer, Dynamic Programming, MARK
- how
  - define `dp[i]` as max sum of subarray that ends at index i
  - update: compare `nums[i]` and `dp[i-1] + nums[i]`

### 打家劫舍

- id: 198
- name: house-robber
- tag: Array, Dynamic Programming
- how
  - meaning of `dp[i]`: if house i is the last house, max money can be robbed
  - init: `dp[0]=nums[0]`, `dp[1]=max(nums[0], nums[1])`
  - update
    - `dp[i] = max(nums[i] + nums[i-2], nums[i-1])`
      - meaning: rob current house, or rob the neighboring house & give up current house

### 打家劫舍 II

- id: 213
- name: house-robber-ii
- tag: Array, Dynamic Programming, MARK
- how
  - what's the difference with previous question: first and last house is connected (circular)
    - either rob first house OR last house
    - apply solution of previous question to `nums[0:len(nums)-1]` and `nums[1:]`, then taking the MAX value

### 最长递增子序列

- id: 300
- name: longest-increasing-subsequence
- tag: Array, Binary Search, Dynamic Programming, MARK
- how
  - use `tails` list to save strict increasing subsequence of `nums`
  - how to update `tails` during iterating `nums`
    - `tails` is empty -> put `num` to `tails[0]`
    - use dichotomy to find the position where `num` should be placed (use `left` pointer to indicate, and it's 1 step right or at same position with `right` pointer), then put new `num` there
      - property of this update rule
        - if there's smaller number than last numbers in `tails`, it will be placed, but the result will stay the same (length of `tails` doesn't change)
        - last number strictly larger than previous number in `tails`, but will use smallest possible number (eg. `tails` is (1,2,5), and `num` is 3, `tails` will become (1,2,3))
    - after iteration, just return the valid length of `tails` (aka longest increasing subsequence)

### 正则表达式匹配

- id: 10
- name: regular-expression-matching
- tag: Recursion, String, Dynamic Programming, MARK
- how
  - intuition: start from first char
    - if they are the same -> matched!
    - if not: how about check next char?
  - use dp table
    - definition: `dp[i][j]` means: if previous i chars of `s` can be matched with previous j chars of `p`
      - from `dp[i-1][j]` to `dp[i][j]` -> add char `s[i-1]`
    - dp table init
      - `dp[0][0]`: true (empty strings are matched)
      - only when all even positions of `p` are `*`, first row can be true
    - state transition:
      - if new `p` char is not `*`
        - if `dp[i-1][j-1]==1 && s[i-1]==p[i-1]`: previous string are matched & add a same char -> true
        - if `dp[i-1][j-1]==1 && p[i-1] == "."`: previous string are matched & "\*" matched any char -> true
      - if new `p` char is `*`
        - `dp[i][j-2]==1`: previous i-1 chars of `s` string is matched, and we can safely consider any char with `*` to be ignored -> true
        - `dp[i - 1][j]==1 && (p[j-1] == s[i-1] or p[j-1] == ".")`: previous i-1 chars are matched, and new char is also matched

### 丑数 II

- id: 264
- name: ugly-number-ii
- tag: Hash Table, Math, Dynamic Programming, Heap (Priority Queue), MARK
- how
  - essence of question: how to generate a list of number that only has factor of certain prime number and avoid repeatedly generating them?
  - use a list to save result, and newer number only comes from previous result times certain factor (say x)
  - avoid generating duplicates: **use pointer to indicate potential base of each factor**, if used -> move forward

---

## 贪心

### 买卖股票的最佳时机 II

- id: 122
- name: best-time-to-buy-and-sell-stock-ii
- tag: Greedy, Array, Dynamic Programming, MARK
- how
  - calculate price difference of each day
    - if > 0: we make profit from this diff
    - if < 0: no operation, no loss
  - idea behind this: holding stock for a long time can be divided into buy-sell in the same day

### 搜索二维矩阵 II

- id: 240
- name: search-a-2d-matrix-ii
- tag: Array, Binary Search, Divide and Conquer, Matrix, MARK
- how
  - where to start
    - intuitive: corner, but which corner?
    - matrix rotate -> binary search tree -> choose root node (top right or bottom left)
  - why choose these nodes are efficient
    - once flag number is compared, a row / column can be safely ignored (reduce search space most)

### 盛最多水的容器

- id: 11
- name: container-with-most-water
- tag: Greedy, Array, Two Pointers, MARK
- how
  - intuitive: use two pointers, and put them at 2 ends
  - how to move
    - if move the long one: no way the volume can be larger
    - if move the short one: possible to get larger volume, but not sure -> need to keep the largest value and compare

### 最大数

- id: 179
- name: largest-number
- tag: Greedy, Array, String, Sorting, MARK
- how
  - ALL ABOUT SORTING!! PLEASE REVIEW "QUICK SORTING"
  - define your sorting rule:
    - x, y are `str` type, and if `xy > yx`, then `x > y`
    - sort entire list of str under this rule, then concatenate to a string in reverse order

### 分发糖果

- id: 135
- name: candy
- tag: Greedy, Array, MARK
- how
  - when value of index `i` needs to be determined by its neighboring elements -> iterate forward and backward (two times, but still LINEAR time)
    - compare rating with previous one, `if ratings[i - 1] < ratings[i]` -> `i` needs to get one more candy
    - compare rating with next one, `if ratings[i] < ratings[i+1]` -> `i` needs to get one more candy
  - how to combine two iteration result: need to satisfy both rules
    - choose `max` in the results (no matter what, larger ensure obeying the rule)

### 最多能完成排序的块 II

- id: 768
- name: max-chunks-to-make-sorted-ii
- tag: Stack, Greedy, Array, Sorting, Monotonic Stack, MARK
- how
  - use a stack to save head of "chunks"
  - heads of chunks should be _ascending_
    - if new number is smaller than previous head -> need to merge current chunk and previous chunk

---

## 位运算

### 位 1 的个数

- id: 191
- name: number-of-1-bits
- tag: Bit Manipulation, Divide and Conquer
- how
  - easy! in while loop until number == 0
    - take remainder, if == 1 -> counter increment
    - number // 2

### 2 的幂

- id: 231
- name: power-of-two
- tag: Bit Manipulation, Recursion, Math
- how
  - two's power has property: $(n-1) & n == 0$

### 两整数之和

- id: 371
- name: sum-of-two-integers
- tag: Bit Manipulation, Math
- how
  - ((a & b) << 1) + (a ^ b)

### 只出现一次的数字

- id: 136
- name: single-number
- tag: Bit Manipulation, Array
- how
  - XOR: same number -> 0; number showing once stays

### 只出现一次的数字 II

- id: 137
- name: single-number-ii
- tag: Bit Manipulation, Array, MARK
- how
  - use Finite State Machine
  - just focus on one bit
    - if one number shows 3 times -> set its x bit is 1, then at position x, 1 will shows 3 times
    - use two variable: `one` to indicate this position 1 shows one time, `two` to indicate this position shows two time
    - draw truth table, and write state transition expression
  - same rules apply to all bit positions

---

## 数学

### 除自身以外数组的乘积

- id: 238
- name: product-of-array-except-self
- tag: Array, Prefix Sum, MARK
- how
  - use prefix product, but during iterating array, **OFFSET** by 1 position (both backward and forward)
    - iterate from left to right: `[1, x[0], x[0]*x[1], x[0]*x[1]*x[2]]`, from right to left: `[x[1]x[2]x[3], x[2]x[3], x[3], 1]`
    - point-wise multiplication to get result

### 多数元素

- id: 169
- name: majority-element
- tag: Array, Hash Table, Divide and Conquer, Counting, Sorting, MARK
- how
  - voting algo!
    - assume first number as majority number (M):
      - if current_number == M -> votes += 1
      - else -> votes -= 1
      - votes == 0 -> assign a new M
      - last M is just answer
    - why
      - assume vote majority number +1, and vote non-majority number as -1, if get votes==0 -> remaining numbers has the same majority number as the entire array

### 整数拆分

- id: 343
- name: integer-break
- tag: Math, Dynamic Programming, MARK
- how
  - [ref](https://leetcode.cn/problems/integer-break/solutions/29098/343-zheng-shu-chai-fen-tan-xin-by-jyd/?envType=study-plan-v2&envId=selected-coding-interview)
  - basically, break numbers into combination of 3, or 2 is sub-optimal

### 格雷编码

- id: 89
- name: gray-code
- tag: Bit Manipulation, Math, Backtracking, MARK
- how
  - n-th gray code formula: gray(n) = n ^ (n >> 1)

### 找出游戏的获胜者

- id: 1823
- name: find-the-winner-of-the-circular-game
- tag: Recursion, Queue, Array, Math, Simulation, MARK
- how
  - simulation: top to bottom
  - solution: bottom to top -> where the only element when $n=1$ goes when $n$ goes up (how index changes)

### 有效数字

- id: 65
- name: valid-number
- tag: String, MARK
- how
  - finite state machine

### 第 N 位数字

- id: 400
- name: nth-digit
- tag: Math, Binary Search
- how
  - fuck! this is insane (how to store previous number, how to manipulate carefully with +1 or -1, // or % or \*\*)
  - PLEASE use detailed example(s?) to derive assignment equation

### 数字 1 的个数

- id: 233
- name: number-of-digit-one
- tag: Recursion, Math, Dynamic Programming
- how
  - hard but:
    - classification: deal with different cases
    - summarize from some examples
    - [solution here](https://leetcode.cn/problems/number-of-digit-one/solutions/2362053/233-shu-zi-1-de-ge-shu-qing-xi-tu-jie-by-pgb1/?envType=study-plan-v2&envId=selected-coding-interview)

---

# hot 100

## 哈希

### 两数之和

- id: 1
- name: two-sum
- tag: Array, Hash Table
- how
  - use a hash table to save (value -> index)
  - iterate again, test if (target - current_number) is in the hash table

### 字母异位词分组

- id: 49
- name: group-anagrams
- tag: Array, Hash Table, String, Sorting
- how
  - hash each char -> get sum -> use as key, mapping to a list of anagrams

### 最长连续序列

- id: 128
- name: longest-consecutive-sequence
- tag: Union Find, Array, Hash Table
- how
  - core problem: how do you know this is the right beginning number of longest consecutive sequence?
    - because (current_number - 1) doesn't exist in this array!
  - how do i know its length:
    - keep tracking if (current_number + 1) is in array


--- 


## 双指针

### 移动零

- id: 283
- name: move-zeroes
- tag: Array, Two Pointers, MARK
- how
  - use two pointers, `anchor` and `explorer`, they start at the same position (0)
  - update rule:
    - if `explorer` points to a non-zero number -> swap number `explorer` points to with `anchor`'s, and `anchor` moves one step forward
  - why this work?
    - they begin at the same place: swap with non-zero self
    - if meets 1 zero: `explorer` just pass it, `anchor` points to the zero, after update, `anchor` still points to the first zero
    - if meets multiple zero: `anchor` still points to them

### 盛最多水的容器

- id: 11
- name: container-with-most-water
- tag: Greedy, Array, Two Pointers
- duplicate, check: [here](#盛最多水的容器)

### 三数之和

- id: 15
- name: 3sum
- tag: Array, Two Pointers, Sorting
- duplicate, [check](#三数之和)

### 接雨水

- id: 42
- name: trapping-rain-water
- tag: Stack, Array, Two Pointers, Dynamic Programming, Monotonic Stack
- how
  - pattern: high1 -> low -> high2, where high2 >= high1
  - $O(N)$
  - iterate from left to right, maintain the highest, count "sinks" in (1,0,2,1,3)
  - iterate from right to left, count sinks like (3,0,2,0,1)
  - sum left result and right result


--- 


## 滑动窗口

### 无重复字符的最长子串

- id: 3
- name: longest-substring-without-repeating-characters
- tag: Hash Table, String, Sliding Window
- duplicate, [check here](#无重复字符的最长子串)

### 找到字符串中所有字母异位词

- id: 438
- name: find-all-anagrams-in-a-string
- tag: Hash Table, String, Sliding Window
- how
  - hash map: use frequency check
  - sliding window -> only consider chars within window
  - if char out of window in `p`: char_freq ++
  - if char in window in `p`: char_freq --
  - each time check if char_freq values are all 0: anagrams, record `i`


--- 


## 子串

### 和为 K 的子数组

- id: 560
- name: subarray-sum-equals-k
- tag: Array, Hash Table, Prefix Sum, MARK
- how
  - combine prefix sum with frequency table
  - check how many times the prefix sum == (current_prefix_sum - target_value), and add this frequency to result

### 滑动窗口最大值

- id: 239
- name: sliding-window-maximum
- tag: Queue, Array, Sliding Window, Monotonic Queue, Heap (Priority Queue)
- [duplicate](#滑动窗口最大值) (MARK)

### 最小覆盖子串

- id: 76
- name: minimum-window-substring
- tag: Hash Table, String, Sliding Window, MARK
- how
  1. init hash table to save frequency of chars in `t`
  2. use two pointers to represent window
  3. expand sliding window by move `end` pointer
     1. use a `counter` to "count" how many chars are remained to be matched
     2. once matched, calculate the width of window. then shrink the window while keep it valid by moving `start` pointer


--- 


## 普通数组

### 最大子数组和

- id: 53
- name: maximum-subarray
- tag: Array, Divide and Conquer, Dynamic Programming
- [duplicate](#最大子数组和)

### 合并区间

- id: 56
- name: merge-intervals
- tag: Array, Sorting
- how
  - sort based on left bound
  - compare left bound and right bound to check if interval i can be merged with interval (i-1)

### 轮转数组

- id: 189
- name: rotate-array
- tag: Array, Math, Two Pointers, MARK
- how
  - use "reverse" to achieve $O(N)$ operations and $O(1)$ space
  - from ----->--> to <--<------ to --->------> (reverse all, then reverse first $k$ elements and the remaining elements)

### 除自身以外数组的乘积

- id: 238
- name: product-of-array-except-self
- tag: Array, Prefix Sum
- [duplicate](#除自身以外数组的乘积)

### 缺失的第一个正数

- id: 41
- name: first-missing-positive
- tag: Array, Hash Table, MARK
- how
  - about how to use array itself to indicate presence of certain element and avoid destroying original data
  - start from ideal situation: array ranges from \[1,n\] -> missing element can't be greater than n!
  - how to indicate presence: at `nums[i]`, its value should be `i+1`
  - but at place `i+1`, its value is modified -> use swap


--- 


## 矩阵

### 矩阵置零

- id: 73
- name: set-matrix-zeroes
- tag: Array, Hash Table, Matrix
- how
  - use first row and first column to save "state" of the row or column (if this row or column should be all zero)

### 螺旋矩阵

- id: 54
- name: spiral-matrix
- tag: Array, Matrix, Simulation
- [duplicate](#螺旋矩阵)

### 旋转图像

- id: 48
- name: rotate-image
- tag: Array, Math, Matrix
- [duplicate](#旋转图像)

### 搜索二维矩阵 II

- id: 240
- name: search-a-2d-matrix-ii
- tag: Array, Binary Search, Divide and Conquer, Matrix
- [duplicate](#搜索二维矩阵-ii)


--- 


## 链表

### 相交链表

- id: 160
- name: intersection-of-two-linked-lists
- tag: Hash Table, Linked List, Two Pointers
- [duplicate](#相交链表)

### 反转链表

- id: 206
- name: reverse-linked-list
- tag: Recursion, Linked List
- [duplicate](#反转链表)

### 回文链表

- id: 234
- name: palindrome-linked-list
- tag: Stack, Recursion, Linked List, Two Pointers, MARK
- how
  - fast-slow pointers + reverse linked list
    - fast-slow pointers -> used for finding where middle of linked list is
    - reverse linked list -> made it easier to compare

### 环形链表

- id: 141
- name: linked-list-cycle
- tag: Hash Table, Linked List, Two Pointers
- how
  - fast-slow pointers

### 环形链表 II

- id: 142
- name: linked-list-cycle-ii
- tag: Hash Table, Linked List, Two Pointers
- [duplicate](#环形链表-II)

### 合并两个有序链表

- id: 21
- name: merge-two-sorted-lists
- tag: Recursion, Linked List
- [duplicate](#合并两个有序链表)

### 两数相加

- id: 2
- name: add-two-numbers
- tag: Recursion, Linked List, Math
- how
  - use a `carry` variable

### 删除链表的倒数第 N 个结点

- id: 19
- name: remove-nth-node-from-end-of-list
- tag: Linked List, Two Pointers
- how
  - use two pointers, they spaced with (n+1), when `fast` hit the None at the end, `slow` points to just before the node to be deleted

### 两两交换链表中的节点

- id: 24
- name: swap-nodes-in-pairs
- tag: Recursion, Linked List
- how
  - use three variables:
    - `cur`: start from `head`, move 2 nodes/step
    - `cur_next`: indicate node to be swapped with `cur`
    - `prev`: one node before `cur`, need to update its `next` once next cycle of swap was done

### K 个一组翻转链表

- id: 25
- name: reverse-nodes-in-k-group
- tag: Recursion, Linked List
- how
  - move pointer, cut connection between groups, reverse

### 随机链表的复制

- id: 138
- name: copy-list-with-random-pointer
- tag: Hash Table, Linked List
- [duplicate](#随机链表的复制)

### 排序链表

- id: 148
- name: sort-list
- tag: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort, MARK
- how
  - merge sort: split array into 2 units, merge two units with order. unit increase at each iteration, start from 1.
    - eg. (4,2,3,1,5), iter1: split into single digit, merge two digits, (2,4 / 1,3 / 5); iter2: (1,2,3,4/5); iter3: (1,2,3,4,5)
  - iterate linked list once for length
  - split (disconnect link)
  - merge (sort and connect)

### 合并 K 个升序链表

- id: 23
- name: merge-k-sorted-lists
- tag: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort, MARK
- how
  - push heads of all linked list into the heap (min-heap)
  - pop out `node`, linked it to `result` linked list
  - if out `node` has a "next", push it into heap
  - complexity: $O(n\times k \times lg(k))$

### LRU 缓存

- id: 146
- name: lru-cache
- tag: Design, Hash Table, Linked List, Doubly-Linked List, MARK
- how
  - use two dict to indicate "linked list"
    - `before` and `next`: key -> next/before key (next and before refer to if this key is "recently used")
  - `_delete`: reconnect and remove from all dict
  - `_connect`: connect linked list in two dictionary
  - `_append`: add new key to the "end" of linked list (where just before the `tail`)


--- 


## 二叉树

### 二叉树的中序遍历

- id: 94
- name: binary-tree-inorder-traversal
- tag: Stack, Tree, Depth-First Search, Binary Tree
- how
  - easy...

### 二叉树的最大深度

- id: 104
- name: maximum-depth-of-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- [duplicate](#二叉树的最大深度)


### 翻转二叉树

- id: 226
- name: invert-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- [duplicate](#翻转二叉树)

### 对称二叉树

- id: 101
- name: symmetric-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- [duplicate](#对称二叉树)

### 二叉树的直径

- id: 543
- name: diameter-of-binary-tree
- tag: Tree, Depth-First Search, Binary Tree, MARK
- how
  - find depth of each sub-tree
  - keep `diameter` as global variable during finding the depth

### 二叉树的层序遍历

- id: 102
- name: binary-tree-level-order-traversal
- tag: Tree, Breadth-First Search, Binary Tree
- [duplicate](#二叉树的层序遍历)

### 将有序数组转换为二叉搜索树

- id: 108
- name: convert-sorted-array-to-binary-search-tree
- tag: Tree, Binary Search Tree, Array, Divide and Conquer, Binary Tree
- how
  - use number at the middle as root
  - recursively use sub-array until sub-array is empty

### 验证二叉搜索树

- id: 98
- name: validate-binary-search-tree
- tag: Tree, Depth-First Search, Binary Search Tree, Binary Tree, MARK
- how
  - don't just compare left or right with root, use upper_bound and lower_bound to compare

### 二叉搜索树中第K小的元素

- id: 230
- name: kth-smallest-element-in-a-bst
- tag: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- [duplicate](#二叉搜索树中第K小的元素)

### 二叉树的右视图

- id: 199
- name: binary-tree-right-side-view
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- how
  - breadth first search (level-order)
  - take the last element of each level

### 二叉树展开为链表

- id: 114
- name: flatten-binary-tree-to-linked-list
- tag: Stack, Tree, Depth-First Search, Linked List, Binary Tree
- how
  - M1
    - recursion
    - find tail node of left branch, connect it to `root.right`, then connect `root.right` to head node of left branch
  - M2
    - no recursion
    - just find rightmost node of left branch, connect it to right branch, connect root to start of left branch
    - move `root` to right

### 从前序与中序遍历序列构造二叉树

- id: 105
- name: construct-binary-tree-from-preorder-and-inorder-traversal
- tag: Tree, Array, Hash Table, Divide and Conquer, Binary Tree
- [duplicate](#从前序与中序遍历序列构造二叉树)

### 路径总和 III

- id: 437
- name: path-sum-iii
- tag: Tree, Depth-First Search, Binary Tree, MARK
- how
  - backtracking: calculate path sum, save its frequency in a hash table, look up table if there's a previous_path_sum == (current_path_sum - target_sum), undo this node (decrease 1 in frequency table)
    - meaning: there's a path that can be "deleted" from the current path so that partial path sum is equal to target_sum

### 二叉树的最近公共祖先

- id: 236
- name: lowest-common-ancestor-of-a-binary-tree
- tag: Tree, Depth-First Search, Binary Tree
- [duplicate](#二叉树的最近公共祖先)

### 二叉树中的最大路径和

- id: 124
- name: binary-tree-maximum-path-sum
- tag: Tree, Depth-First Search, Dynamic Programming, Binary Tree, MARK
- how
  - find max gain can get from root's sub-tree
    - if all sub-trees are negative -> max gain can get is 0
    - if both sub-trees are positive -> choose max from left or right
  - but we also want max path (no necessarily passing root) -> max path sum = node.val + left_gain + right_gain
    - then update a "global" variable keep track of max value


--- 


## 图论

### 岛屿数量

- id: 200
- name: number-of-islands
- tag: Depth-First Search, Breadth-First Search, Union Find, Array, Matrix, MARK
- how
  - iterate through all positions
  - implement dfs
    - look around, and keep finding until it's not part of island
    - make a sign to indicate visited

### 腐烂的橘子

- id: 994
- name: rotting-oranges
- tag: Breadth-First Search, Array, Matrix, MARK
- how
  - SIMULATION: keep track of newly rotten at current time step, make adjacent ones rotten and track (**BFS**)
  - cannot use DFS!!

### 课程表

- id: 207
- name: course-schedule
- tag: Depth-First Search, Breadth-First Search, Graph, Topological Sort
- [duplicate](#课程表)

### 实现 Trie (前缀树)

- id: 208
- name: implement-trie-prefix-tree
- tag: Design, Trie, Hash Table, String
- how
  - use different structure to save full words and to match its prefix
    - full words -> use set (hash table)
    - prefix chars -> nested dictionary


--- 


## 回溯

### 全排列

- id: 46
- name: permutations
- tag: Array, Backtracking
- [duplicate](#全排列)

### 子集

- id: 78
- name: subsets
- tag: Bit Manipulation, Array, Backtracking, MARK
- how
  - CLASSIC backtracking, what we need for dfs function:
    - current state
    - range of sub-problem
  - notes: copy Python list: `arr[:]`

### 电话号码的字母组合

- id: 17
- name: letter-combinations-of-a-phone-number
- tag: Hash Table, String, Backtracking
- how
  - backtracking
    - state: current combination
    - range_restrict: which digit
  - fix one digit's letter selection, then iterate other digits' all choices

### 组合总和

- id: 39
- name: combination-sum
- tag: Array, Backtracking
- [duplicate](#组合总和)

### 括号生成

- id: 22
- name: generate-parentheses
- tag: String, Dynamic Programming, Backtracking
- how
  - keep track of number of parentheses that are open OR closed

### 单词搜索

- id: 79
- name: word-search
- tag: Array, String, Backtracking, Matrix
- [duplicate](#单词搜索)

### 分割回文串

- id: 131
- name: palindrome-partitioning
- tag: String, Dynamic Programming, Backtracking, MARK
- how
  - consider a string as two parts: `prefix` + `suffix`
  - check if `prefix` is a palindrome, if it is -> take that as part of the answer then partition the `suffix` -> concatenate `prefix` with answers returned from partition `suffix`

### N 皇后

- id: 51
- name: n-queens
- tag: Array, Backtracking, MARK
- how
  - parameters of backtracking
    - row state: record which row includes
    - col state
    - diag state
    - counter diag state
    - current row
  - each row -> a new depth of recursion
  - at each depth of recursion: try one column that is valid (not occurring in previous "state")


--- 


## 二分查找

### 搜索插入位置

- id: 35
- name: search-insert-position
- tag: Array, Binary Search
- how
  - use some examples to understand in the end, where each pointer is, and the relation between answer and them

### 搜索二维矩阵

- id: 74
- name: search-a-2d-matrix
- tag: Array, Binary Search, Matrix
- how
  - binary search row or col

### 在排序数组中查找元素的第一个和最后一个位置

- id: 34
- name: find-first-and-last-position-of-element-in-sorted-array
- tag: Array, Binary Search
- how
  - found mid, then slide to both direction

### 搜索旋转排序数组

- id: 33
- name: search-in-rotated-sorted-array
- tag: Array, Binary Search
- how
  - find how many digits are rotated (also binary search)
  - then convert it back to sorted list
  - another binary search :)

### 寻找旋转排序数组中的最小值

- id: 153
- name: find-minimum-in-rotated-sorted-array
- tag: Array, Binary Search
- how
  - still binary search
  - rotated array looks like `[↗️↘️]`, so we want `left` moved to min

### 寻找两个正序数组的中位数

- id: 4
- name: median-of-two-sorted-arrays
- tag: Array, Binary Search, Divide and Conquer, MARK
- how (this is hardest of binary search so far)
  - to find median -> which element is at the middle of two merged array (which divide merged array into 2 parts, i.e. `left` half and `right` half)
    - but merge and sort two arrays cost too much, how to avoid?
  - use two pointers to indicate the beginning of `right` half of array at `nums1` and `nums2`
    - how to init pointers? put first pointer (`partition_x`) at middle of shorter array (let's say `nums1` is shorter), then second includes remaining amount of elements at `nums2`
    - so the assuming max of left half should between `(nums1[partition_x-1], nums2[partition_y-1])`, and min of left half should be in `(nums1[partition_x], nums2[partition_y])`
  - if left_max < right_min -> our guess succeed! we can find median!


--- 


## 栈

### 有效的括号

- id: 20
- name: valid-parentheses
- tag: Stack, String
- [duplicate](#有效的括号)

### 最小栈

- id: 155
- name: min-stack
- tag: Stack, Design
- [duplicate](#最小栈)

### 字符串解码

- id: 394
- name: decode-string
- tag: Stack, Recursion, String
- [duplicate](#字符串解码)

### 每日温度

- id: 739
- name: daily-temperatures
- tag: Stack, Array, Monotonic Stack, MARK
- how
  - keep the stack as *index of higher temp*
  - if found a temp > temperature at index of top of stack: pop stack, calculate how many days since it to today

### 柱状图中最大的矩形

- id: 84
- name: largest-rectangle-in-histogram
- tag: Stack, Array, Monotonic Stack, MARK
- how
  - keep track of height that in *ascending* order
  - so when height start to drop, we can know that at the from top of stack to previous bar, the limiting height is the height at top of stack
  - width: previous bar (i-1) - one bar before top of stack (stack\[-1\])


--- 


## 堆

### 数组中的第K个最大元素

- id: 215
- name: kth-largest-element-in-an-array
- tag: Array, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)
- [duplicate](#数组中的第K个最大元素)

### 前 K 个高频元素

- id: 347
- name: top-k-frequent-elements
- tag: Array, Hash Table, Divide and Conquer, Bucket Sort, Counting, Quickselect, Sorting, Heap (Priority Queue)
- how
  - construct frequency table
  - use a custom class to contain both key and value, and implement `__lt__` to use heap (only compare value)

### 数据流的中位数

- id: 295
- name: find-median-from-data-stream
- tag: Design, Two Pointers, Data Stream, Sorting, Heap (Priority Queue)
- [duplicate](#数据流的中位数)

--- 


## 贪心算法

### 买卖股票的最佳时机

- id: 121
- name: best-time-to-buy-and-sell-stock
- tag: Array, Dynamic Programming
- [duplicate](#买卖股票的最佳时机)

### 跳跃游戏

- id: 55
- name: jump-game
- tag: Greedy, Array, Dynamic Programming
- how
  - keep track of farthest index can reach of visited indexes
    - if it's current index and the value is 0 -> never goes out
    - if it's greater than length of nums -> definitely reach end

### 跳跃游戏 II

- id: 45
- name: jump-game-ii
- tag: Greedy, Array, Dynamic Programming, MARK
- how
  - DP is too slow :(
  - use greedy:
    - calculate boundary of current jump (aka farthest idx of current jump)
    - when reach the boundary of current jump: update boundary, number of jumps ++

### 划分字母区间

- id: 763
- name: partition-labels
- tag: Greedy, Hash Table, Two Pointers, String
- how
  - build a dict to save where each character last shows (rightmost position)
  - keep track of one partition's rightmost, when reach that: create a new partition


--- 


## 动态规划

### 爬楼梯

- id: 70
- name: climbing-stairs
- tag: Memoization, Math, Dynamic Programming
- [duplicate](#爬楼梯)

### 杨辉三角

- id: 118
- name: pascals-triangle
- tag: Array, Dynamic Programming
- how
  - move left and move right of previous row with padding 0

### 打家劫舍

- id: 198
- name: house-robber
- tag: Array, Dynamic Programming
- [duplicate](#打家劫舍)

### 完全平方数

- id: 279
- name: perfect-squares
- tag: Breadth-First Search, Math, Dynamic Programming, MARK
- how
  - init with calculating all squares less than `n`
  - init `dp` table with all `inf`, meaning of dp table: `dp[i]` -> minimum number of perfect square numbers that sum to n
  - update dp table: at each i from 1 to n, `dp[i] = min(dp[i], dp[i-square] + 1)`, `square` need to iterate through all `square < i`

### 零钱兑换

- id: 322
- name: coin-change
- tag: Breadth-First Search, Array, Dynamic Programming, MARK
- how
  - build `dp` table
    - length: `amount+1` (to include when `amount == 0`)
    - init value: `dp[0]=0`, else: inf
    - update rule: `dp[i] = min(dp[i],dp[i-coin] + 1)`, which means at amount `i`, min amount of coins depends on amount of `i-coin` + 1 coin

### 单词拆分

- id: 139
- name: word-break
- tag: Trie, Memoization, Array, Hash Table, String, Dynamic Programming
- how
  - `dp` table
    - represent whether the substring of s from index 0 to i-1 (i.e., `s[:i]`) can be segmented into words from the dictionary
    - init with `False`
    - update: at `j` it's True, and `s[j:i]` is one of the words: then `dp[i] = True`

### 最长递增子序列

- id: 300
- name: longest-increasing-subsequence
- tag: Array, Binary Search, Dynamic Programming
- [duplicate](#最长递增子序列)

### 乘积最大子数组

- id: 152
- name: maximum-product-subarray
- tag: Array, Dynamic Programming
- how
  - maximum product comes from
    - num itself
    - previous max product * self
    - previous min product (very negative) * self (which is also a negative)
  - all we need to track:
    - max_product_so_far
    - min_product_so_far
    - global max product, i.e. the final result

### 分割等和子集

- id: 416
- name: partition-equal-subset-sum
- tag: Array, Dynamic Programming, MARK
- how
  - iterate dp table backward -> use number once
  - iterate dp table forward -> use one element repeatedly

### 最长有效括号

- id: 32
- name: longest-valid-parentheses
- tag: Stack, String, Dynamic Programming, MARK
- how
  - most important: what does `dp[i]` represent?
    - longest valid parentheses *ends* at i
  - how can we know? when to update?
    - only two cases:
      - meet ")", and there's "(" just before it
      - meet ")", but its previous char is also ")"
        - why: meet the end of like ...())
        - what's the case dp can update: there's a "(" at the very beginning to wrap ...()


--- 


## 多维动态规划

### 不同路径

- id: 62
- name: unique-paths
- tag: Math, Dynamic Programming, Combinatorics
- how
  - just simulate -> number of paths of cell (i,j) depends on cell at its top and cell at its left

### 最小路径和

- id: 64
- name: minimum-path-sum
- tag: Array, Dynamic Programming, Matrix
- [duplicate](#最小路径和)

### 最长回文子串

- id: 5
- name: longest-palindromic-substring
- tag: Two Pointers, String, Dynamic Programming
- how
  - iterate through entire string
  - two kinds of palindrome: odd ("aba") and even ("abba")
    - odd: assume `i` at `b`
    - even: assume `i` and `i+1` at `b`
  - then use two pointers to move towards two directions to extend palindrome

### 最长公共子序列

- id: 1143
- name: longest-common-subsequence
- tag: String, Dynamic Programming, MARK
- how
  - build a table to record matched
  - increment based on diagonal element

### 编辑距离

- id: 72
- name: edit-distance
- tag: String, Dynamic Programming, MARK
- how
  - construct dp table
    - meaning of each cell (i,j) -> min edit distance after editing previous i word1 chars and matches previous j chars of word2
  - why difficult: what does transition from up/left/diagonal cell represent? (delete, insert, replace)


--- 


## 技巧

### 只出现一次的数字

- id: 136
- name: single-number
- tag: Bit Manipulation, Array
- [duplicate](#只出现一次的数字)

### 多数元素

- id: 169
- name: majority-element
- tag: Array, Hash Table, Divide and Conquer, Counting, Sorting
- [duplicate](#多数元素)

### 颜色分类

- id: 75
- name: sort-colors
- tag: Array, Two Pointers, Sorting, MARK
- how
  - use 3 pointers to indicate **boundary** of three regions, and use `mid` to iterate through entire array

### 下一个排列

- id: 31
- name: next-permutation
- tag: Array, Two Pointers, MARK
- how
  - find pattern! aka simulation
  - swap element and reverse sub-array

### 寻找重复数

- id: 287
- name: find-the-duplicate-number
- tag: Bit Manipulation, Array, Two Pointers, Binary Search
- [duplicate](#寻找重复数)


--- 

# Top Interview 150

## 数组 / 字符串

### 合并两个有序数组

- id: 88
- name: merge-sorted-array
- tag: Array, Two Pointers
- how
  - empty in the tail of `nums1` -> start filling from `nums1`'s tail -> required to use pointers start from tail and iterate backward

### 移除元素

- id: 27
- name: remove-element
- tag: Array, Two Pointers
- how
  - use two pointers
    - `anchor` to indicate the position to fill
    - `explorer` to iterate through the array, ignore elements equals to `val`, and swap non-val with `anchor`

### 删除有序数组中的重复项

- id: 26
- name: remove-duplicates-from-sorted-array
- tag: Array, Two Pointers
- how
  - still similar way as previous question: use two pointers
    - `anchor` to indicate the position that are duplicates
    - `explorer` to iterate through the array, pass duplicates and swap non-duplicate with `anchor`

### 删除有序数组中的重复项 II

- id: 80
- name: remove-duplicates-from-sorted-array-ii
- tag: Array, Two Pointers, MARK
- how
  - what's special about this question
    - sorted
    - at most 2 duplicates
    - doesn't matter how to deal with elements outside of wanted array
  - so we can just iterate through the array and "rewrite" it

### H 指数

- id: 274
- name: h-index
- tag: Array, Counting Sort, Sorting, MARK
- how
  - sort reversely
  - iterate through the array and count how many papers have citations greater than i
  - NOTE: methods of "count"
    - counter (along with iteration)
    - `sum(condition)`, used in this question

### O(1) 时间插入、删除和获取随机元素

- id: 380
- name: insert-delete-getrandom-o1
- tag: Design, Array, Hash Table, Math, Randomized
- how
  - use two hash maps

### 加油站

- id: 134
- name: gas-station
- tag: Greedy, Array, MARK
- how
  - if total gas is less than total cost, return -1
  - otherwise, there must be a solution
  - assume start from 0
    - use `local_sums` to track current tank
    - use `global_sums` to track total gas
    - if at any point `local_sums < 0`, means we can't start from previous `start` to `i`, so we set `start = i+1` and reset `local_sums = 0` (tank)

### 罗马数字转整数

- id: 13
- name: roman-to-integer
- tag: Hash Table, Math, String
- how
  - iterate through the string
  - use `prev_num` to track previous number
  - use `sums` to track sums
  - if current number is greater than previous number, means we need to subtract it (e.g. IV = 4)

### 整数转罗马数字

- id: 12
- name: integer-to-roman
- tag: Hash Table, Math, String
- how
  - iterate from large base numbers with stride 2
  - deal with special cases: 4, 9, >= 5

### 最后一个单词的长度

- id: 58
- name: length-of-last-word
- tag: String
- how
  - pointer + flag

### 最长公共前缀

- id: 14
- name: longest-common-prefix
- tag: Trie, String
- how
  - iterate, compare with first string's char at that index

### 找出字符串中第一个匹配项的下标

- id: 28
- name: find-the-index-of-the-first-occurrence-in-a-string
- tag: Two Pointers, String, String Matching
- how
  - iterate haystack, compare with first char of needle, if same, compare substring with needle

### 文本左右对齐

- id: 68
- name: text-justification
- tag: Array, String, Simulation
- how
  - divide word group (details in dealing with space of last word and single word)


--- 


## 双指针

### 验证回文串

- id: 125
- name: valid-palindrome
- tag: Two Pointers, String
- how 
  - use two pointers
    - `left` to iterate forward
    - `right` to iterate backward
    - skip non-alphanumeric characters
    - compare characters


--- 


## 滑动窗口

### 长度最小的子数组

- id: 209
- name: minimum-size-subarray-sum
- tag: Array, Binary Search, Prefix Sum, Sliding Window
- how
  - my impl
    - use a `window` to track current window (a queue)
    - use `current_sum` to track current sum of `window`
    - init with empty window
    - keep appending new elements along iteration
    - if there's reach to `target`, calculate `diff` and pop leftmost element from `window` until `diff` is less than current `window`'s leftmost element
  - better impl
    - use two pointers indicating `window` boundary
    - keep moving right pointer and calculate `current_sum`
    - if `current_sum` is greater than `target`, move left pointer
    - keep tracking min length

### 串联所有单词的子串

- id: 30
- name: substring-with-concatenation-of-all-words
- tag: Hash Table, String, Sliding Window
- how
  - use two pointers (`left` and `right`) and a counter to track the frequency of words
  - approach: 
    1. create a frequency table for words in `words`
    2. initialize `left` and `right` pointers to the start of `s`
    3. move `right` pointer to the right and check if the substring `s[left:right+1]` is a permutation of `words`
    4. if it is, increment the counter and move `left` pointer to the right
    5. if not, move `left` pointer to the right based on the frequency table to find the next possible permutation
  - note: 
    - words in `s` may not be equal to words in `words` (e.g., words in `s` may be a permutation of words in `words`)
    - moving `left` pointer based on the frequency table helps to avoid jumping to the right unnecessarily and reduces the time complexity


--- 


## 矩阵

### 有效的数独

- id: 36
- name: valid-sudoku
- tag: Array, Hash Table, Matrix
- how
  - use a 9x9 grid to represent the Sudoku board, and check each row, column, and 3x3 block to ensure that each number from 1 to 9 appears only once in each unit
  - how to know appear once: convert a list into a *set*, and compare their length
  - a trick to take matrix's column: `for col in zip(*matrix):`

### 生命游戏

- id: 289
- name: game-of-life
- tag: Array, Matrix, Simulation
- how
  - don't update status of "life" inplace once determined, just save it in a new array


--- 


## 哈希表

### 赎金信

- id: 383
- name: ransom-note
- tag: Hash Table, String, Counting
- how
  - use hash table to count the number of each character
  - compare the counts

### 单词规律

- id: 290
- name: word-pattern
- tag: Hash Table, String
- how
  - mapping one word to one char in pattern
  - compare the following:
    1. length of pattern & length of words
    2. the mapping of pattern & words (one pattern to multiple words?)
    3. mapping of words & pattern (one word to multiple pattern?)

### 快乐数

- id: 202
- name: happy-number
- tag: Hash Table, Math, Two Pointers
- how
  - simulation
  - save all previous results in a set
  - if `n` is not a happy number, repeat the process until `n` becomes a happy number
  - if previous result shows again -> there's a loop in this calculation -> `n` cannot be a happy number

### 存在重复元素 II

- id: 219
- name: contains-duplicate-ii
- tag: Array, Hash Table, Sliding Window
- how
  - use a hash table to store the numbers we've seen and their most recent indices
  - iterate through the array, and for each number, check if it's in the hash table and if its most recent index is within k places of the current index


--- 


## 区间

### 汇总区间

- id: 228
- name: summary-ranges
- tag: Array
- how
  - simulation
  - only keep track of `start`, and append range to `res` when `start` needs to change


### 插入区间

- id: 57
- name: insert-interval
- tag: Array, MARK
- how
  - consider the result containing 3 parts:
    1. `left` -> largest of the intervals smaller than start of new "merged" interval
    2. `merged` -> "merged" interval, its start comes from interval to be merged and `newInterval`'s start, its end comes from interval to be merged and `newInterval`'s end
    3. `right` -> smallest start of intervals larger than end of new "merged" interval


### 用最少数量的箭引爆气球

- id: 452
- name: minimum-number-of-arrows-to-burst-balloons
- tag: Greedy, Array, Sorting
- how
  - sort interval based on start
  - maintain `prev_range` and a counter
  - check if new interval's start is within previous range (aka. start <= previous_range's end)


--- 


## 栈

### 简化路径

- id: 71
- name: simplify-path
- tag: Stack, String
- how
  - split based on "/"
  - pop according to number of "."

### 逆波兰表达式求值

- id: 150
- name: evaluate-reverse-polish-notation
- tag: Stack, Array, Math
- how
  - push not operands to stack
  - meet operand: pop 2 ops from stack, perform operation

### 基本计算器

- id: 224
- name: basic-calculator
- tag: Stack, Recursion, Math, String
- how
  - put things in one bracket in the stack
  - if there's a "(" -> put current stack into another, replace things in this bracket to current stack, after done with processing current stack, pop previous stack back


--- 


## 链表

### 反转链表 II

- id: 92
- name: reverse-linked-list-ii
- tag: Linked List, MARK
- how
  - USE DUMMY node to indicate start of linked list rather than "dynamic" previous node

### 删除排序链表中的重复元素 II

- id: 82
- name: remove-duplicates-from-sorted-list-ii
- tag: Linked List, Two Pointers
- how
  - `prevprev` -> previous unique number
  - `prev` -> start of duplicate numbers
  - `cur` -> explore, once find duplicate, move to next number, and use `prev` to delete these duplicates along its way to `cur`

### 旋转链表

- id: 61
- name: rotate-list
- tag: Linked List, Two Pointers
- how
  - count total number of nodes
  - cut at new linked list's tail, remaining part's tail connect to old `head`
  - better: just iterate through entire linked list, connect the tail to head to form a circle, then find new tail, and cut the circle


--- 


## 二叉树

### 相同的树

- id: 100
- name: same-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- how
  - just traverse in the same order, keep comparing

### 从中序与后序遍历序列构造二叉树

- id: 106
- name: construct-binary-tree-from-inorder-and-postorder-traversal
- tag: Tree, Array, Hash Table, Divide and Conquer, Binary Tree, MARK
- how
  - property of inorder and postorder
    - inorder: left -> root -> right
    - postorder: left -> right -> root
  - utilize
    - keep popping out postorder list -> get the root of tree/subtree
    - since all values of tree are unique -> we can easily find the index of current node at inorder list -> easy to find the boundary of current node's left subtree and right subtree

### 填充每个节点的下一个右侧节点指针 II

- id: 117
- name: populating-next-right-pointers-in-each-node-ii
- tag: Tree, Depth-First Search, Breadth-First Search, Linked List, Binary Tree
- how
  - use queue, BFS
  - connect last node's `next` to null, others to next node in queue

### 路径总和

- id: 112
- name: path-sum
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- how
  - DFS
  - deal with False case at one place
  - once there's a True, always return True along the depth

### 求根节点到叶节点数字之和

- id: 129
- name: sum-root-to-leaf-numbers
- tag: Tree, Depth-First Search, Binary Tree
- how
  - dfs(root, cur_sum)
  - avoid adding and reducing root.val in the dfs function, only when found that it is leaf node then add it to non local variable `res`

### 二叉搜索树迭代器

- id: 173
- name: binary-search-tree-iterator
- tag: Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator, MARK
- how
  - in-order: left subtree -> root -> right subtree
  - use stack to "remember" nodes to be visited later (found leftmost, and next step is root)
  - using stack.pop() to pop out current node and root node, then add new nodes to stack, using same function to push leftmost nodes into stack

### 完全二叉树的节点个数

- id: 222
- name: count-complete-tree-nodes
- tag: Bit Manipulation, Tree, Binary Search, Binary Tree, MARK
- how
  - count depth: recursively, only count left ("all nodes in the last level are as far left as possible")
  - count nodes: also recursively, only count "full" tree (since it has formula), and count the not full subtree recursively


--- 


## 二叉树层次遍历

### 二叉树的层平均值

- id: 637
- name: average-of-levels-in-binary-tree
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- how
  - level order

--- 


## 二叉搜索树

### 二叉搜索树的最小绝对差

- id: 530
- name: minimum-absolute-difference-in-bst
- tag: Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
- how
  - in-order traverse


--- 


## 图

### 被围绕的区域

- id: 130
- name: surrounded-regions
- tag: Depth-First Search, Breadth-First Search, Union Find, Array, Matrix, MARK
- how
  - initial idea: find a "O", and find its adjacent "O"s to find if any of its neighbors are on border -> return False to make it invalid
    - why this can't work: hard to mark visited and don't interfere validation
  - better idea: directly search on border "O"s, and mark their neighbors. and keep these marks as "O"s, replace other with "X"

### 克隆图

- id: 133
- name: clone-graph
- tag: Depth-First Search, Breadth-First Search, Graph, Hash Table
- how
  - use a hash table to mapping old node -> new node

### 除法求值

- id: 399
- name: evaluate-division
- tag: Depth-First Search, Breadth-First Search, Union Find, Graph, Array, String, Shortest Path, MARK
- how
  1. adjacent table
    - build a adjacent table (`adj[i][j]` -> i / j)
    - backtracking, using $x1 / x2 = (x1 / x3) \times (x3 / x2)$
  2. graph
    - graph: `dict[dict[str]]`, key: variable, `graph[key1][key2] = key1 / key2`

### 课程表 II

- id: 210
- name: course-schedule-ii
- tag: Depth-First Search, Breadth-First Search, Graph, Topological Sort, MARK
- how
  - try to reduce unused information as much as possible (do I need to know what kind of courses are prerequisite for a course? not really, all I need to know if a course can be finished is: how many prerequisites remaining for this course)
  - check if one value or element in a set/list has VERY high cost!!


--- 


## 图的广度优先搜索

### 蛇梯棋

- id: 909
- name: snakes-and-ladders
- tag: Breadth-First Search, Array, Matrix, MARK
- how
  - use BFS: keep track of steps to reach each position
  - make use of "dp" idea
  - why not DFS: it's like backtracking, and there's too much to search: can be faster go backward

### 最小基因变化

- id: 433
- name: minimum-genetic-mutation
- tag: Breadth-First Search, Hash Table, String, MARK
- how
  - brute search... just try to mutate every position of `startGene` and check if that mutation was in `bank`, if it is, then check if it's equal to `endGene`

### 单词接龙

- id: 127
- name: word-ladder
- tag: Breadth-First Search, Hash Table, String
- how
  - same as previous problem...


--- 


## 字典树

### 添加与搜索单词 - 数据结构设计

- id: 211
- name: design-add-and-search-words-data-structure
- tag: Depth-First Search, Design, Trie, String, MARK
- how
  - recursion
  - use prefix dict, and *add a end indicator*
  - meet "." -> recursion, if any returns True
  - meet other char -> check if in dict, if it is, replace with new dict

### 单词搜索 II

- id: 212
- name: word-search-ii
- tag: Trie, Array, String, Backtracking, Matrix, MARK
- how
  - pass set to a function, the function can modify it **inplace**
  - build a prefix dict, then search with saving visited positions


--- 


## 回溯

### 组合

- id: 77
- name: combinations
- tag: Backtracking, MARK
- how
  - a basic framework of backtracking
  - use a stack as parameter, and pass it to backtrack
  - then the only thing need to change at every choice to be made: where to start (using first element as "fixed" element and find combination of the following positions)

### N 皇后 II

- id: 52
- name: n-queens-ii
- tag: Backtracking, MARK
- how
  - revisit n-queen problem :)
  - you can specify an *order* to fill in the queens -> save you from maintaining "row" position info and avoid queens placed at the same row
  - therefore, all info required for this dfs function is: col + diag + reversed diag


--- 


## 分治

### 建立四叉树

- id: 427
- name: construct-quad-tree
- tag: Tree, Array, Divide and Conquer, Matrix
- how
  - check if all cells are the same to reduce requirement for deep recursion (only deep recursion for nodes with many different parts)


--- 


## Kadane 算法

NOTE: core idea of maximum sub-array
- iterate through every element: should this new element (`x`) be added to potential max sub-array or act as beginning of new sub-array?
  - decided by: whether `x` + previous_sum > `x`

### 环形子数组的最大和

- id: 918
- name: maximum-sum-circular-subarray
- tag: Queue, Array, Divide and Conquer, Dynamic Programming, Monotonic Queue, MARK
- two cases
  1. same as normal max subarray
  2. one part at beginning, one part at ending (using circular characteristic)
- consider case 2, manipulate this equation
  - max_sum = prefix + suffix = total_sum - subarray_in_middle = total_sum - min(subarray_in_middle) -> problem converted to find min subarray (same algo)

--- 


## 二分查找

### 寻找峰值

- id: 162
- name: find-peak-element
- tag: Array, Binary Search
- how
  - go through all possible cases to find peak


--- 


## 堆

### 数组中的第K个最大元素

- id: 215
- name: kth-largest-element-in-an-array
- tag: Array, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)

### IPO

- id: 502
- name: ipo
- tag: Greedy, Array, Sorting, Heap (Priority Queue)

### 查找和最小的 K 对数字

- id: 373
- name: find-k-pairs-with-smallest-sums
- tag: Array, Heap (Priority Queue)

### 数据流的中位数

- id: 295
- name: find-median-from-data-stream
- tag: Design, Two Pointers, Data Stream, Sorting, Heap (Priority Queue)


--- 


## 位运算

### 二进制求和

- id: 67
- name: add-binary
- tag: Bit Manipulation, Math, String, Simulation

### 颠倒二进制位

- id: 190
- name: reverse-bits
- tag: Bit Manipulation, Divide and Conquer

### 位1的个数

- id: 191
- name: number-of-1-bits
- tag: Bit Manipulation, Divide and Conquer

### 只出现一次的数字

- id: 136
- name: single-number
- tag: Bit Manipulation, Array

### 只出现一次的数字 II

- id: 137
- name: single-number-ii
- tag: Bit Manipulation, Array

### 数字范围按位与

- id: 201
- name: bitwise-and-of-numbers-range
- tag: Bit Manipulation


--- 


## 数学

### 回文数

- id: 9
- name: palindrome-number
- tag: Math

### 加一

- id: 66
- name: plus-one
- tag: Array, Math

### 阶乘后的零

- id: 172
- name: factorial-trailing-zeroes
- tag: Math

### x 的平方根 

- id: 69
- name: sqrtx
- tag: Math, Binary Search

### Pow(x, n)

- id: 50
- name: powx-n
- tag: Recursion, Math

### 直线上最多的点数

- id: 149
- name: max-points-on-a-line
- tag: Geometry, Array, Hash Table, Math


--- 


## 一维动态规划

### 爬楼梯

- id: 70
- name: climbing-stairs
- tag: Memoization, Math, Dynamic Programming

### 打家劫舍

- id: 198
- name: house-robber
- tag: Array, Dynamic Programming

### 单词拆分

- id: 139
- name: word-break
- tag: Trie, Memoization, Array, Hash Table, String, Dynamic Programming

### 零钱兑换

- id: 322
- name: coin-change
- tag: Breadth-First Search, Array, Dynamic Programming

### 最长递增子序列

- id: 300
- name: longest-increasing-subsequence
- tag: Array, Binary Search, Dynamic Programming


--- 


## 多维动态规划

### 三角形最小路径和

- id: 120
- name: triangle
- tag: Array, Dynamic Programming

### 最小路径和

- id: 64
- name: minimum-path-sum
- tag: Array, Dynamic Programming, Matrix

### 不同路径 II

- id: 63
- name: unique-paths-ii
- tag: Array, Dynamic Programming, Matrix

### 最长回文子串

- id: 5
- name: longest-palindromic-substring
- tag: Two Pointers, String, Dynamic Programming

### 交错字符串

- id: 97
- name: interleaving-string
- tag: String, Dynamic Programming

### 编辑距离

- id: 72
- name: edit-distance
- tag: String, Dynamic Programming

### 买卖股票的最佳时机 III

- id: 123
- name: best-time-to-buy-and-sell-stock-iii
- tag: Array, Dynamic Programming

### 买卖股票的最佳时机 IV

- id: 188
- name: best-time-to-buy-and-sell-stock-iv
- tag: Array, Dynamic Programming

### 最大正方形

- id: 221
- name: maximal-square
- tag: Array, Dynamic Programming, Matrix


--- 



