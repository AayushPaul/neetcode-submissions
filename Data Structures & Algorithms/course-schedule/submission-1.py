class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites: 
            preMap[course].append(prereq)
        
        visitedCourses = set() 

        def dfs(course): 
            #Cycle Detected 
            if course in visitedCourses: 
                return False 

            if preMap[course] == []: 
                return True 

            visitedCourses.add(course)
            for pre in preMap[course]: 
                if not dfs(pre): 
                    return False 
            
            visitedCourses.remove(course) 
            preMap[course] = [] 
            return True 

        for course in range(numCourses): 
            if not dfs(course): 
                return False 
        
        return True 
    
    #Time: O(n + p), Space: O(n + p)