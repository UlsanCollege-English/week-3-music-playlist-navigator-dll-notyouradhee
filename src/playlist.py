
### `/src/playlist.py` (starter)

class _DNode:
    __slots__ = ("title", "prev", "next")
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        
        new_node = _DNode(title)
        if not self.head:  # first song
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def play_first(self):
        
        if not self.head:
            self.current = None
            return None
        self.current = self.head
        return self.current.title

    def next(self):
       
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.title
        return None

    def prev(self):
       
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.title
        return None

    def insert_after_current(self, title):
        
        if not self.current:
            return False 

        new_node = _DNode(title)
        nxt = self.current.next
        self.current.next = new_node
        new_node.prev = self.current
        new_node.next = nxt
        if nxt:
            nxt.prev = new_node
        else:
           
            self.tail = new_node
        return True

    def remove_current(self):
       
        if not self.current:
            return False

        prev_node, next_node = self.current.prev, self.current.next

        # detach
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        # move current
        self.current = next_node if next_node else prev_node
        return True

    def to_list(self):
       
        result = []
        node = self.head
        while node:
            result.append(node.title)
            node = node.next
        return result
