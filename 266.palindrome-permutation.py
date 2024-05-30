
"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true
"""

from collections import Counter
def canPermutePalindrome(s:str) -> bool:
    return sum([v%2 for v in Counter(s).values()]) <= 1