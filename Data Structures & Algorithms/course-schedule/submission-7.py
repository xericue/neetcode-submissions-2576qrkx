class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i : [] for i in range(numCourses)}
        indegrees = [0] * numCourses # course -> freq [0, 0...]        
        for i in prerequisites: 
            course, dependency = i
            adj_list[dependency].append(course)
            indegrees[course] += 1

        q = collections.deque()
        
        for i, v in enumerate(indegrees):
            if v == 0:
                q.append(i)
        
        
        #  1 -
        #  ^ |  
        # prereqs -> {{1,0}, {1,1}}

        # both 0 and 1 have indegrees of 1
        # [1,0], [0,1]
        
        total = 0
        while q:
            node = q.popleft() # course with no dependencies
            # TODO tracking what has been processed
            total += 1
            for neighbor in adj_list[node]: # adj_list[node] -> {nextClass1, nextClass2
                indegrees[neighbor] -= 1
                # if its zero append to the queue
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
                    
        return total == numCourses