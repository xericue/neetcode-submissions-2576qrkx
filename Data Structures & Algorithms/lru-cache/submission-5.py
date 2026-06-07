class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nex = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # initialize DLL with dummy nodes for ease of MRU and LRU
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.prev = self.tail
        self.tail.nex = self.head # point them to each other

    def get(self, key: int) -> int:
        # in for a map is O(1)
        if key not in self.cache:
            return -1
        
        # update to MRU
        # why is updating remove and insert?
        # remove it from its initial spot (this links the surrounding
        # nodes together and just entirely removes it
        self.remove(self.cache[key])
        # now insert it at the right, making it MRU
        self.insert_right(self.cache[key])

        # return node value
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # NOW we make it a new node with a new value
        self.cache[key] = Node(key, value)
        self.insert_right(self.cache[key])
        
        if len(self.cache) > self.capacity:
            removed = self.tail.nex
            self.remove(removed)
            del self.cache[removed.key] # since we index
            # our cache by the key, get the key of the removed
            # node

    def insert_right(self, node):
        # insert it in between head and head.prev
        prev = self.head.prev
        nex = self.head # head serves as the node's new next ptr
        
        # link the surrounding nodes to the new node
        prev.nex = node
        nex.prev = node

        # link the node's pointers to the surrounding nodes
        node.prev = prev
        node.nex = nex # pointing to head
    
    def remove(self, node):
        node.prev.nex, node.nex.prev = node.nex, node.prev
        # okay you dont have to return anything here?