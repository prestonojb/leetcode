class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = [] 
        
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            if preMap[curr] == []:
                return True
            
            visited.add(curr)
            prereqs = preMap[curr]
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            visited.remove(curr)
            
            preMap[curr] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True