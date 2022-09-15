class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {}
        for i in range(numCourses):
            preMap[i] = [] 
        
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        taken = set()
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            if preMap[curr] == []:
                if curr not in taken:
                    taken.add(curr)
                    res.append(curr)
                return True
            
            visited.add(curr)
            prereqs = preMap[curr]
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            visited.remove(curr)
            
            taken.add(curr)
            res.append(curr)
            
            preMap[curr] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res