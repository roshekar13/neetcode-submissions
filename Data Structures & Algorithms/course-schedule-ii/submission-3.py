class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = dict()
        for u,v in prerequisites:
            if u not in adj_list: adj_list[u] = []
            adj_list[u].append(v)
        
        path = []
        seen = set()
        processed = set()
        def dfs(curr):
            seen.add(curr)
            if curr in adj_list:
                for neigh in adj_list[curr]:
                    if neigh in processed: continue
                    if neigh in seen: return False
                    elif not dfs(neigh): return False 

            seen.remove(curr)
            processed.add(curr)
            path.append(curr)
            return True
           
        
        for i in range(numCourses):
            if i in processed: continue
            if not dfs(i): return []
                
        return path
            