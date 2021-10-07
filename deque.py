class Deque:
    class Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        if self.tail is None:
            self.tail = new_node
        self.head = new_node

    def push_right(self, value):
        new_node = self.Node(value)
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.tail = new_node

    def pop_left(self):
        node_to_delete = self.head
        if node_to_delete is None:
            return
        if node_to_delete.next is not None:
            node_to_delete.next.prev = None
        self.head = node_to_delete.next
        print(f"Element {node_to_delete.value} was deleted")

    def pop_right(self):
        node_to_delete = self.tail
        if self.tail is None:
            return
        if node_to_delete.prev is not None:
            node_to_delete.prev.next = None
        self.tail = node_to_delete.prev
        print(f"Element {node_to_delete.value} was deleted")

    def find_by_value(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                print(f"Element {value} is in deque")
                return True
            current_node = current_node.next
        print(f"Element {value} isn't in deque")
        return False

    def print_deque(self):
        current_node = self.head
        print("\nDeque")
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print("\n")

    def deque_to_list(self):
        result = list()
        current_node = self.head
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return result
