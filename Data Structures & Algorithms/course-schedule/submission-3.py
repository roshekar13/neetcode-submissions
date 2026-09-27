class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = dict()
        for curr,prereq in prerequisites:
            if curr not in adj_list: adj_list[curr] = []
            adj_list[curr].append(prereq)
        
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
            return True
        

        for i in range(numCourses):
            if i in processed: continue
            if not dfs(i): return False
        return True
        





