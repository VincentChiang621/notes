# HELPER
class Node:
    def __init__(self, next, prev, key, val):
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # stores key -> Node()
        self.LRU = Node(None, None, -1, -1)
        self.MRU = Node(None, None, -1, -1)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeNode(node)
        self.cache[key] = self.addMRU(node.key, node.val)
        return node.val

    def put(self, key: int, val: int) -> None:
        # 1. updating key, val pair (already existing)
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.cache[key] = self.addMRU(key, val)
        # 2. need to evict LRU
        elif len(self.cache) == self.cap:
            deleted = self.removeNode(self.LRU.next)
            print(deleted.key, deleted.val)
            del self.cache[deleted.key]
            self.cache[key] = self.addMRU(key, val)
        # 3. just add new Node
        else:
            self.cache[key] = self.addMRU(key, val)

    def addMRU(self, key, val):
        # HELPER: updates a node to Most recently used
        newNode = Node(self.MRU, self.MRU.prev, key, val)
        self.MRU.prev.next = newNode
        self.MRU.prev = newNode
        return newNode

    def removeNode(self, node):
        # HELPER: removes a LRU key, val pair
        left, right = node.prev, node.next
        left.next = node.next
        right.prev = node.prev
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)