# https://leetcode.com/problems/course-schedule/submissions/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solution 1: create a graph (adjascency), and if we can visit all nodes in a dfs and not having a cycle, then we can finish all courses.
        def Solution1(numCourses, prerequisites):
            curse_prereq = {}
            for a, b in prerequisites:
                if not a in curse_prereq:
                    curse_prereq[a] = []
                    curse_prereq[a].append(b)
                else:
                    curse_prereq[a].append(b)

            # chose an arbitrary starting node p. And do dfs from p. For each node that we have pass, we add it to the seen set. If we node is already in seen, then it means that we have found a loop, so return false. Afte we visit each node's children, and we haven't found a loop, we can just remove the node from the adjacency list, since its course can be taken and we dont need to visit its children again. Notice that we might have a disconected graph, so after finishing the dfs, we take another root note, and do a new dfs starting from there. We repeat this process untill there is not nodes left to visit. It a loop was not found, so we just return True.

            def dfs(course):
                if course in seen:  # it is a loop
                    return True

                if not course in curse_prereq:
                    return False

                else:
                    for prereq in curse_prereq[course]:
                        seen.add(course)  # we add the nodes
                        loop = dfs(prereq)
                        if loop == True:
                            return True
                        seen.remove(course)

                    del curse_prereq[
                        course
                    ]  # remove the node, since we have already visited its children, and we havent found a loop. It meand that this course can be taken, so we dont have to got through it again in the next disconected nodes.
                    return loop

            while len(list(curse_prereq.keys())) > 0:
                seen = set()
                course = list(curse_prereq.keys())[0]
                loop = dfs(course)
                if loop:  # there was a loop
                    return False
            return True

        return Solution1(numCourses, prerequisites)
