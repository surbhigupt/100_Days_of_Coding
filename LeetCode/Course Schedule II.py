class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c]+=1
        
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in graph[node]:
                indegree[i]-=1
                if indegree[i] == 0:
                    queue.append(i)
        
        return res if sum(indegree) == 0 else []