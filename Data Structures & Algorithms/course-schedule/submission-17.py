class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # okay so this algorithm is going to handle a lot of indegree decrements
        # and will therefore require a traversal algorithm that goes from the 
        # course with zero indegrees all the way to the courses with the most
        # indegrees. we want to start from fund comp to the last courses to see
        # if its possible to finish all of them

        # kahn's algo
        # - also catches circular dependencies

        # init
        adj_list = {i : [] for i in range(numCourses)}
        indegrees = collections.defaultdict(int)
        q = collections.deque()

        # 1 -> 0
        # switch around prereqs so that you work on unlocking classes, not getting
        # upper bound by them first

        for locked, key in prerequisites:
            adj_list[key].append(locked) # adj list should be the courses that the KEY -> UNLOCKS
            indegrees[locked] += 1

        for k, v in adj_list.items():
            if indegrees[k] == 0: # that means this "locked" course has zero prereqs; we can take it
                q.append(k)

        # logic
        # need to traverse while our queue(?+????????????) is still True...
        # or a heap
        total = 0
        while q:
            node = q.popleft() # node w/ zero indegrees
            # but it unlocks stuff

            total += 1

            for unlocked_class in adj_list[node]:
                indegrees[unlocked_class] -= 1
                if indegrees[unlocked_class] == 0:
                    q.append(unlocked_class)
            

        # just decrement one indegree from the nodes affected by the currently processed one
        # and if it has indegrees = 0 then go process it

        return total == numCourses
    """
    okay first off how does kahn's algo work Lol Lol Yea Yea
    """