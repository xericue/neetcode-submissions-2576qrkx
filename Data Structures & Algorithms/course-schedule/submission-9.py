class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this looks like a problem where each course is bound by prerequisites, 
        # so im already thinking that this will form a directed acyclic graph, 
        # and the best way to handle all these dependencies and order them would
        # be through a topological sort, which is a graph algorithm that allows 
        # us to find the order of a DAG by putting all of the nodes into a queue 
        # and taking them out by their dependencies or decrementing their dependencies 

        # the first thing i want to do is create an adjacency list

        # and ill want to switch around all of the prerequisites to make this
        # problem more intuitive - it currently has the first element of the
        # array as its "destination", but it would be better described if we
        # went from destination -> needed course -> needed course ... etc. 
        # we dont want to disrupt the adjacency list; we just want to read it

        # we also want to keep a running track of how MANY dependencies each
        # class has so we can start our problem accordingly, because the
        # insertion point of our algorithm will have to be the node(s) with
        # zero dependencies - these will be our first nodes in the queue


        # okay, it actually looks like our adjacency list is a dictionary
        # where i is the course (i in range(numCourses))
        # and val is a list of the goal courses 
        # dictionary because we want to index by the key?
        adj_list = {i : [] for i in range(numCourses)}
        indegrees = [0] * numCourses

        for i in prerequisites:
            goal, dependency = i # unpack
            # now set dependency to goal
            adj_list[dependency].append(goal)
            indegrees[goal] += 1 # make sure we can index by the num of the course
            # because the problem gives it that each course is 0 -> n

        # okay, so we create a list of indegrees and an adjacency list, which is 
        # actually a hash map from required course to future/able-to-be-taken courses.
        # why? now you can index by the dependency and get its unlockables,
        # not the other way around - its a bit weird to manipulate

        q = collections.deque()

        for i, v in enumerate(indegrees):
            if v == 0: # append the DESTINATION/nodes with 0 dependencies
                q.append(i) # append its index; this correctly indexes our adj list
                # because, again, courses are 0 to n

        total = 0
        while q:
            new = q.popleft()
            total += 1 # total must equal numCourses

            for neighbor in adj_list[new]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        # if something depends on itself, it will never get added to the queue
        # because the queue only adds if something has a dependency of zero; so,
        # this can only ever catch a valid DAG
        
        return total == numCourses