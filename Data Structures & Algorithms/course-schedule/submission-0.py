class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert list to adjacency list
        courses = {i: [] for i in range (numCourses)}
        for a,b in prerequisites:
            courses[b].append(a)
        
        # set flags
        visiting = set()
        visited = set()

        # DFS, triggers a flag if cycle detected
        def dfs(curr):
            if curr in visiting: return True
            if curr in visited: return False

            visiting.add(curr)

            for neigh in courses[curr]:
                if dfs(neigh):
                    return True
            
            # Backtrack: done exploring this node's path
            visiting.remove(curr)
            visited.add(curr)
            return False
    
        for i in range(numCourses):
            if i not in visited:
                if dfs(i): return False
        
        return True



