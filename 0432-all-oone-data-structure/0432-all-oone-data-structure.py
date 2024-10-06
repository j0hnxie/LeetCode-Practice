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

    def remove(self, cur_node: Node) -> None:
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
    
    def insert(self, cur_node: Node, new_value: int, key: str) -> Node:
        new_node = Node(new_value)
        new_node.prev = cur_node
        new_node.next = cur_node.next
        cur_node.next.prev = new_node
        cur_node.next = new_node
        new_node.keys.add(key)
        return new_node

    def inc(self, key: str) -> None:
        if key in self.map:
            cur_node = self.map[key]
            cur_node.keys.discard(key)
            next_value = cur_node.value + 1
        else:
            cur_node = self.head
            next_value = 1

        if cur_node.next.value == next_value:
            cur_node.next.keys.add(key)
        else:
            self.insert(cur_node, next_value, key)

        self.map[key] = cur_node.next

        if len(cur_node.keys) == 0 and cur_node != self.head:
            self.remove(cur_node)

    def dec(self, key: str) -> None:
        if key not in self.map:
            return
        
        cur_node = self.map[key]
        cur_node.keys.discard(key)
        next_value = cur_node.value - 1

        if next_value == 0:
            del self.map[key]
        else:
            if cur_node.prev.value == next_value:
                cur_node.prev.keys.add(key)
            else:
                self.insert(cur_node.prev, next_value, key)

            self.map[key] = cur_node.prev
        
        if len(cur_node.keys) == 0:
            self.remove(cur_node)
        

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