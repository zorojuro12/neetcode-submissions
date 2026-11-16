class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next, nxt.prev = node, node
        node.prev = prev
        node.next = nxt
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next.key
            self.remove(self.cache[lru])
            del self.cache[lru]
        
