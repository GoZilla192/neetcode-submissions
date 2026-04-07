class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(0, 0) for _ in range(10 ** 4)]

    def put(self, key: int, value: int) -> None:
        idx = key % len(self.hashmap)
        ptr = self.hashmap[idx]

        while ptr.next:
            if ptr.next.key == key:
                ptr.next.val = value
                return 

            ptr = ptr.next
        
        ptr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % len(self.hashmap)
        ptr = self.hashmap[idx]

        while ptr.next:
            if ptr.next.key == key:
                return ptr.next.val
            ptr = ptr.next
        
        return -1

    def remove(self, key: int) -> None:
        idx = key % len(self.hashmap)
        ptr = self.hashmap[idx]

        while ptr.next:
            if ptr.next.key == key:
                ptr.next = ptr.next.next
                return 
            
            ptr = ptr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)