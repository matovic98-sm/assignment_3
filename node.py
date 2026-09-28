# Implement your Node class here
class Node:
    #Initialized a new node with a value and initialized the next pointer with a value of None
    def __init__(self, value):
        self.value = value
        self.next = None

# Design Memo
#A stack was the right choice for the undo/redo system because stacks use a Last In, First Out (LIFO) model. This 
#is useful for situations where it is necessary to go back and reverse operations based on the most recent actions.
#In this implementation, two stacks were utilized to keep track of undo and redo actions, so that the most recent 
#action could be undone first and then moved to the redo stack so that it could be restored if needed. A queue was 
#a better fit for the help desk because it follows the First In, First Out (FIFO) model, meaning that it is better 
#suited for tasks that require handling requests in the order in which they arrive. Using a queue allows for adding
#new customers to the end and removing customers who have been helped from the front, unlike a stack, where actions
#are added and removed from the top. My implementation differs from Python’s built-in lists because my stacks and 
#queues were created using Node objects and pointers that reference the location of other nodes, instead of relying
#on index locations or other Python list methods.

