#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # --- impl inspired from https://leetcode.com/problems/course-schedule-ii/solutions/1642354/c-python-simple-solutions-w-explanation-topological-sort-using-bfs-dfs/?source=vscode
        from collections import defaultdict, deque

        # build graph: prerequisite -> courses coming after prerequisite
        graph = defaultdict(list)
        # build in-degree list: course -> number of prerequisites
        in_degree = defaultdict(int)
        # queue to store nodes that have zero in-degree
        queue = deque()
        # result list to store finished courses
        result = []
        # number of courses remaining to be finished
        courses_remaining = numCourses

        # iterate through all prerequisites and build graph and in-degree list
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1

        # find courses don't require prerequisite
        for course in range(numCourses):
            if course not in in_degree:
                queue.append(course)
        
        # start from course with zero in-degree, and keep finding until all courses are finished
        while queue:
            finished_course = queue.popleft()
            result.append(finished_course)
            courses_remaining -= 1
            for next_course in graph[finished_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return result if courses_remaining == 0 else []


        # --- init impl (too slow)
        # from collections import defaultdict, deque
        # next_courses = defaultdict(list)
        # previous_courses = defaultdict(set)
        # for course, prerequisite in prerequisites:
        #     next_courses[prerequisite].append(course)
        #     previous_courses[course].add(prerequisite)
        
        # res = []
        # q = deque()
        # courses_remained = numCourses
        # for i in range(numCourses):
        #     if i not in previous_courses:
        #         q.append(i)
        
        # while q:
        #     course_finish = q.popleft()
        #     res.append(course_finish)
        #     courses_remained -= 1
        #     nexts = next_courses[course_finish]
        #     for n in nexts:
        #         if n not in q and n not in res and previous_courses[n].issubset(res):
        #             q.append(n)

        
        # return res if courses_remained == 0 else []
            
            
        
# @lc code=end

