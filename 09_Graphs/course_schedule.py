"""
Problem: Course Schedule

There are numCourses courses labeled from 0 to
numCourses - 1.

You are given prerequisites where:

prerequisites[i] = [a, b]

means you must take course b before course a.

Return True if you can finish all courses.
Otherwise, return False.

Example 1:

Input:
numCourses = 2
prerequisites = [[1, 0]]

Output:
True

Explanation:
Take course 0 first, then course 1.


Example 2:

Input:
numCourses = 2
prerequisites = [[1, 0], [0, 1]]

Output:
False

Explanation:
There is a cycle:

0 -> 1 -> 0

Technique:
BFS + Topological Sort + Indegree

Time Complexity:
O(V + E)

Space Complexity:
O(V + E)

Where:
V = Number of courses
E = Number of prerequisites
"""

from collections import deque
from typing import List


class Solution:

    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        # Adjacency list.
        graph = [[] for _ in range(numCourses)]

        # Indegree counts how many prerequisites
        # each course has.
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:

            graph[prerequisite].append(course)
            indegree[course] += 1

        # Courses with no prerequisites can be
        # taken immediately.
        queue = deque()

        for course in range(numCourses):

            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:

            course = queue.popleft()
            completed += 1

            # Remove this course as a prerequisite
            # for its dependent courses.
            for next_course in graph[course]:

                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If every course was completed,
        # there is no cycle.
        return completed == numCourses


if __name__ == "__main__":

    solution = Solution()

    # Example 1
    numCourses = 2
    prerequisites = [[1, 0]]

    print(
        "Example 1:",
        solution.canFinish(numCourses, prerequisites)
    )

    # Example 2
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    print(
        "Example 2:",
        solution.canFinish(numCourses, prerequisites)
      )
