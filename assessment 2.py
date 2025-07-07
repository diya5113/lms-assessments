# Node class to represent each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

# LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def add_node(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node
        print(f"Added node with data: {data}")

    def print_list(self):
        """Print all elements in the list."""
        if not self.head:
            print("The linked list is empty.")
            return
        current = self.head
        print("Linked List: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        try:
            if n <= 0:
                raise ValueError("Index must be a positive integer (1-based).")

            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n == 1:  # Delete the head node
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node at position {n} with data: {deleted_data}")
                return

            current = self.head
            for i in range(n - 2):  # Traverse to node before the nth node
                if not current.next:
                    raise IndexError("Index out of range.")
                current = current.next

            if not current.next:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node at position {n} with data: {deleted_data}")

        except Exception as e:
            print(f"Error: {e}")

# Sample testing
if __name__ == "__main__":
    # Create a LinkedList object
    ll = LinkedList()

    # Add nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    # Print the list
    ll.print_list()

    # Delete nodes
    ll.delete_nth_node(2)  # Delete node at position 2 (data: 20)
    ll.print_list()

    ll.delete_nth_node(1)  # Delete head node (data: 10)
    ll.print_list()

    ll.delete_nth_node(5)  # Invalid index (out of range)
    ll.delete_nth_node(0)  # Invalid index (non-positive)

    # Delete remaining nodes
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    # Try deleting from an empty list
    ll.delete_nth_node(1)
