class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = self.next = None # initially, a node will have no prev or next

class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = {} # kv store/map key to Nodes
        self.capacity = capacity

        # ohhh this is where we store our sentinels
        self.LRU = Node(-1, -1)
        self.MRU = Node(-1, -1)

        # make sure they're initially connected
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

        # helper function - remove node from list, remove any node from list
    def _remove(self, node):
        # must update the previous node (achieved with DLL) and next
        node.prev.next = node.next
        node.next.prev = node.prev

    # helper function - insert any node at rightmost position
    def _insert(self, node):
        # at RIGHTMOST position
        # node's prev and next must be initialized
        # tail's next must be updated
        # sentinel's prev must be updated
        self.MRU.prev.next = node
        node.prev = self.MRU.prev

        self.MRU.prev = node
        node.next = self.MRU

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        
        # first, we need to make sure it's somehow updated according to
        # its usage - hence where the DLL comes in to remove and reinsert
        # it at the end
        self._remove(self.lru_cache[key])
        self._insert(self.lru_cache[key])
        return self.lru_cache[key].val # because its storing nodes (key, val)


    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            # update it
            self._remove(self.lru_cache[key])
        
        self.lru_cache[key] = Node(key, value) # now a pointer
        self._insert(self.lru_cache[key]) # self.insert(key to node)

        if len(self.lru_cache) > self.capacity: # you can take the len of a map
            # remove and delete LRU from internal hash map
            lru = self.LRU.next # NOT self.left, thats the sentinel
            self._remove(lru)
            del self.lru_cache[lru.key] # del key word deletes from hash map!!!

