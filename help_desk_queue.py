# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
#Created a Queue class to manage the help desk queue, initialized an empty queue and initialized the front and rear pointers with a value of None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    #Defined an operation to initialize a new Node with the provided value, add it to the end of the line, and update pointers
    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    #Defined an operation to remove and return the value for the Node at the front of the queue and update relevant pointers
    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
    #Defined an operation to print the next customer in the queue
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
    #Defined an operation to print out all customers in the queue
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next

def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            customer = queue.dequeue()
            if customer is not None:
                print(f"{customer} has been helped")
            else:
                print("There are currently no customers in the queue")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            customer = queue.peek()
            if customer is not None:
                print(customer)
            else: 
                print("There are currently no customers in the queue")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")

            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

# my_queue = Queue()
# my_queue.enqueue("Person A")
# my_queue.enqueue("Person B")
# my_queue.enqueue("Person C")
# my_queue.print_queue()

# print(my_queue.dequeue())
# print(my_queue.peek())

# my_queue.print_queue()

if __name__ == "__main__":
    run_help_desk()
