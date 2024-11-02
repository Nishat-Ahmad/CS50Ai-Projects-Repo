class Node():
    # Constructor that is basically acting as a setter.
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)              # Appends a new node in the frontier.

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)   # returns true or false of state.

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]            # Adds the latest value added to a variable called node.
            self.frontier = self.frontier[:-1]  # Removes the latest value from the array.
            return node

# Queue Frontier parent class is StackFrontier.
class QueueFrontier(StackFrontier):

    # This is overloaded as queue works on FIFO principle.
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
