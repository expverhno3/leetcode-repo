1. Arrays and Strings:

   a. Two Pointers:
   - Often used for problems involving comparisons or manipulations of elements.
   - Example: "Increasing Triplet Subsequence" (334) uses two variables to keep track of the smallest and second smallest numbers.

   b. Sliding Window:
   - Useful for problems involving subarrays or substrings.
   - Example: "Max Consecutive Ones III" (1004) uses a sliding window to maintain a valid subarray with at most k zeros.

   c. Prefix Sum:
   - Helpful for range sum queries or finding subarrays with specific properties.

2. Hash Tables:

   - Used for quick lookups and counting frequencies.
   - Can be combined with other techniques like Two Pointers or Sliding Window.
   - Example: "Max Number of K-Sum Pairs" (1679) uses a hash map to count frequencies and find pairs efficiently.

3. Linked Lists:

   - Often involves manipulating pointers and using dummy nodes.
   - Two-pointer technique (fast and slow pointers) is common for finding middle elements or detecting cycles.

4. Stacks:

   - Useful for problems involving matching parentheses, evaluating expressions, or maintaining monotonic properties.
   - Example: "Removing Stars from a String" (2390) uses a stack to efficiently handle the deletion operation.

5. Queues:

   - Often used in BFS algorithms and for processing elements in order.
   - Example: "Dota2 Senate" (649) uses two queues to simulate the voting process efficiently.

6. Trees:

   a. Depth-First Search (DFS):
   - Recursive approach for traversing or searching tree structures.
   - Example: "Longest ZigZag Path in a Binary Tree" (1372) uses DFS to explore all possible zigzag paths.

   b. Breadth-First Search (BFS):
   - Level-order traversal using a queue.
   - Useful for finding shortest paths or level-based properties.

   c. Binary Search Trees (BST):
   - Utilize the ordering property of BSTs for efficient searching, insertion, and deletion.

7. Graphs:

   a. DFS:
   - Used for exploring paths, finding connected components, or topological sorting.
   - Example: "Reorder Routes to Make All Paths Lead to the City Zero" (1466) uses DFS to count the number of edges that need to be reversed.

   b. BFS:
   - Useful for finding shortest paths in unweighted graphs.
   - Example: "Nearest Exit from Entrance in Maze" (1926) uses BFS to find the shortest path to an exit.

8. Heaps / Priority Queues:

   - Useful for maintaining a sorted set of elements with efficient insertion and extraction.
   - Often used in problems involving finding k-th largest/smallest elements or merging sorted lists.
   - Example: "Maximum Subsequence Score" (2542) uses a heap to maintain the k largest elements efficiently.

9. Binary Search:

   - Used for searching in sorted arrays or for problems where the search space can be narrowed down logarithmically.
   - Example: "Koko Eating Bananas" (907) uses binary search to find the minimum eating speed.

10. Backtracking:

    - Used for generating all possible combinations or permutations.
    - Often involves building a solution incrementally and abandoning a path if it's not viable.

11. Dynamic Programming:

    a. 1D Dynamic Programming:
    - Used when the problem can be broken down into overlapping subproblems.
    - Example: "Domino and Tromino Tiling" (790) uses DP to find patterns in the tiling possibilities.

    b. 2D Dynamic Programming:
    - Used for problems involving matrices or two-dimensional decision making.
    - Example: "Best Time to Buy and Sell Stock with Transaction Fee" (714) uses a 2D DP approach to model different states of stock holding.

12. Bit Manipulation:

    - Used for problems involving binary representations or bitwise operations.
    - Example: "Counting Bits" (338) uses bit manipulation to count the number of 1's in binary representations efficiently.

13. Trie (Prefix Tree):

    - Useful for problems involving strings, especially for prefix matching or autocomplete functionalities.
    - Example: "Search Suggestions System" (1397) uses a trie to efficiently store and retrieve word suggestions.

14. Interval Problems:

    - Often involve sorting intervals based on start or end times.
    - Example: "Non-overlapping Intervals" (435) sorts intervals by end time to greedily select non-overlapping intervals.

15. Monotonic Stack:

    - Used for problems where we need to find the next greater/smaller element or maintain a monotonic property.
    - Example: "Online Stock Span" (901) uses a monotonic stack to efficiently calculate price spans.

General Strategies:
1. Always consider edge cases and boundary conditions.
2. Look for patterns or mathematical relationships in the problem.
3. Consider sorting the input if order matters.
4. Think about time and space complexity trade-offs.
5. For optimization problems, consider greedy approaches or binary search on the answer.