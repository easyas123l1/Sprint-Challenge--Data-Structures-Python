from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check to see if capacity has been reached
        if self.storage.length == self.capacity:
            # If current position exists and its previous node is not the head
            if self.current and self.current is not self.storage.head:
                # Replace the value of the previous node
                self.current.prev.value = item
                # Update where the current node is
                self.current = self.current.prev
            else:
                # Remove from tail and set current position
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
        else:
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
