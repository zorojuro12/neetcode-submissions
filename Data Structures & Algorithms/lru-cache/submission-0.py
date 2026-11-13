class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps key to node

        # make a doubly linked list of dummy node
        # left node = LRU
        # right node = MRU

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node): #remove the node
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node): #insert the node at the MRU position behind the right dummy pointer
            prev, next = self.right.prev, self.right
            prev.next = next.prev = node
            node.prev = prev
            node.next = next


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
