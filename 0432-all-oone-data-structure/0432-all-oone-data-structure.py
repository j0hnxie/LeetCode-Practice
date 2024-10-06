class Node:
    def __init__(self, value):
        self.value = value
        self.keys = set()
        self.next = None
        self.prev = None
        
class AllOne:

    def __init__(self):
        self.map = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.map:
            cur_node = self.map[key]
            cur_node.keys.discard(key)
            next_value = cur_node.value + 1

            if cur_node.next.value == next_value:
                cur_node.next.keys.add(key)
            else:
                new_node = Node(next_value)
                new_node.prev = cur_node
                new_node.next = cur_node.next
                cur_node.next.prev = new_node
                cur_node.next = new_node
                new_node.keys.add(key)

            self.map[key] = cur_node.next

            if len(cur_node.keys) == 0:
                cur_node.next.prev = cur_node.prev
                cur_node.prev.next = cur_node.next

        else:
            if self.head.next.value == 1:
                self.head.next.keys.add(key)
            else:
                new_node = Node(1)
                new_node.prev = self.head
                new_node.next = self.head.next
                self.head.next.prev = new_node
                self.head.next = new_node
                new_node.keys.add(key)

            self.map[key] = self.head.next

    def dec(self, key: str) -> None:
        if key not in self.map:
            return
        
        cur_node = self.map[key]
        cur_node.keys.discard(key)
        if cur_node.value == 1:
            if len(cur_node.keys) == 0:
                self.head.next = cur_node.next
                self.head.next.prev = self.head
            
            del self.map[key]
        else:
            next_value = cur_node.value - 1
            if cur_node.prev.value == next_value:
                cur_node.prev.keys.add(key)
                cur_node.keys.discard(key)
            else:
                new_node = Node(next_value)
                new_node.prev = cur_node.prev
                new_node.next = cur_node
                cur_node.prev.next = new_node
                cur_node.prev = new_node
                new_node.keys.add(key)

            self.map[key] = cur_node.prev

            if len(cur_node.keys) == 0:
                cur_node.next.prev = cur_node.prev
                cur_node.prev.next = cur_node.next
        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        
        return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()