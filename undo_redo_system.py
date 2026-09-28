# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here

#Created a Stack class to manage the undo/redo system, initialized an empty stack and initialized the top pointer with a value of None
class Stack:
    def __init__(self):
        self.top = None
    #Defined an operation to add a new Node to the top of the stack with the provided value
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    #Defined an operation to remove and return the value of the item at the top of the stack
    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value
    #Defined an operation to return the value of the top Node without removing it
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None
    #Defined an operation to print out the current contents of the stack
    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            #Cleared the value of the redo_stack by setting its value to a new instance of the Stack class
            redo_stack = Stack()

            print(f"Action performed: {action}")
            
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()
            
            if action is not None:
                redo_stack.push(action)
            else:
                print("No actions to undo")
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            action = redo_stack.pop()

            if action is not None:
                undo_stack.push(action)
            else:
                print("No actions to redo")


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")

            undo_stack.print_stack()           

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")

            redo_stack.print_stack()            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")
              
               #----Test Code----#
# my_stack = Stack()
# my_stack.push("Page 1")
# my_stack.push("Page 2")
# my_stack.push("Page 3")
# my_stack.print_stack()

# print(my_stack.pop())
# print(my_stack.peek())

if __name__ == "__main__":
    run_undo_redo()