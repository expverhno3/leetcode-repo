#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #NOTE: instead of prerequisite pointing to course, save a list that prerequisite -> course (what next course is)

        next_courses = [[] for _ in range(numCourses)] # adj list: prerequisite -> next course
        num_prerequisites = [0] * numCourses # number of prerequisites of that course

        for pair in prerequisites:
            current_course, prerequisite = pair
            next_courses[prerequisite].append(current_course)
            num_prerequisites[current_course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if num_prerequisites[i] == 0:
                queue.append(i)
        
        counter = 0 # course can be finished
        # finish courses without prerequisite first
        while queue:
            current_course = queue.popleft() # only courses with all prerequisite finished can be finished
            counter += 1


            for next_course in next_courses[current_course]:
                num_prerequisites[next_course] -= 1 # finish prerequisite!
                if num_prerequisites[next_course] == 0:
                    queue.append(next_course)
            
        return counter == numCourses # if all courses can be finished
                
        
# @lc code=end

