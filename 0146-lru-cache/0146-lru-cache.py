class LRUCache:
    
    class Node:
        def __init__(self, key: int, val: int, nex = None, pre = None):
            self.prev = pre
            self.next = nex
            self.key = key
            self.val = val

    def __init__(self, capacity: int):
        self.dict = {}
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1, None, self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key in self.dict:
            cur = self.dict[key]
            self.remove(cur)
            self.add(cur)
            return cur.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
            
        new = self.Node(key, value)
        self.dict[key] = new
        self.add(new)
        
        if len(self.dict) > self.cap:
            del self.dict[self.head.next.key]
            self.remove(self.head.next)
            
    def remove(self, cur):
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
    
    def add(self, cur):
        self.tail.prev.next = cur
        cur.prev = self.tail.prev
        self.tail.prev = cur
        cur.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)