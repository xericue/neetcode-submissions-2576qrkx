# this is a combination of two main data structures, hash maps and DLLs
# hash maps - O(1) search of a node by its key
# DLLs - quickly move nodes to a MRU position
#        and remove the LRU node from the other end in O(1)
#        LRU near left, MRU near right
#        these are best done with a dummy left and right node

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node): # remove by node
        node.prev.nxt, node.nxt.prev = node.nxt, node.prev

    def insert(self, node): # insert by node on the right
        prev = self.right.prev
        nxt = self.right
        prev.nxt = node
        nxt.prev = node
        node.prev = prev
        node.nxt = nxt # pointing to self.right dummy node
    
    def get(self, key: int) -> int:
        # move nodes to the right since this touches the node
        if key in self.cache:
            # "update" node as the MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # ask if its already in the cache
        if key in self.cache:
            self.remove(self.cache[key]) # remove it first
        # now that we're clear to insert a value, make a new Node with it
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove LRU, which is our left
            lru = self.left.nxt # we actually need to store a reference to it
            # because we remove it then try to delete it by indexing it,
            # but when we index it it no longer exists
            self.remove(lru) # left is a dummy node; remove from LL
            # also want to remove it from the cache itself
            del self.cache[lru.key]