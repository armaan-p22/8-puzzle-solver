class Node:
    def __init__(self, state, parent=None, action=None, g_cost=0, h_cost=0):
        """
        Represents a state in the 8-puzzle search space.
        
        :param state: A 1D tuple representing the 3x3 board (e.g., (1, 2, 3, 4, 5, 6, 7, 8, 0))
                      Using a tuple instead of a list makes it hashable for the 'visited' set!
        :param parent: The Node that generated this Node (used to trace the solution path).
        :param action: The move made to get to this state ('UP', 'DOWN', 'LEFT', 'RIGHT').
        :param g_cost: The path cost from the initial state to this node (depth).
        :param h_cost: The heuristic estimated cost to the goal (Manhattan distance).
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.g_cost = g_cost
        self.h_cost = h_cost
    
    @property
    def f_cost(self):
        """Total cost function for A* Search (f = g + h)"""
        return self.g_cost + self.h_cost
    
    def __lt__(self, other):
        """
        Less-than operator override. 
        This is needed so Python's built-in PriorityQueue (heapq) knows how to
        sort the nodes when implementing A*. It will sort by the lowest f_cost.
        """
        return self.f_cost < other.f_cost

    def __eq__(self, other):
        """Lets us easily compare if two nodes have the same board state."""
        return self.state == other.state
    
    def __hash__(self):
        """Allows the Node's state to be stored in a Python set() for the 'visited' list."""
        return hash(self.state)

    def get_children(self):
        """
        Generates valid child nodes by sliding the '0' (blank) tile.
        Returns a list of Node objects.
        """
        children = []
        zero_index = self.state.index(0) # Find the blank space

        # Calculate 2D grid coordinates (0-2) from the 1D index
        row = zero_index // 3
        col = zero_index % 3

        # Define possible moves: (row_change, col_change, action_name)
        moves = [
            (-1, 0, 'UP'),    
            (1, 0, 'DOWN'),   
            (0, -1, 'LEFT'),  
            (0, 1, 'RIGHT')   
        ]

        for dr, dc, action in moves:
            new_row, new_col = row + dr, col + dc

            # Check if the move stays withing the 3x3 boundaries
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Convert 2D target back to a 1D index
                target_index = new_row * 3 + new_col

                # Create a new state by swapping 0 with the target tile
                new_state = list(self.state)
                new_state[zero_index], new_state[target_index] = new_state[target_index], new_state[zero_index]

                # Create the child Node
                child_node = Node(
                    state=tuple(new_state),
                    parent=self,
                    action=action,
                    g_cost=self.g_cost + 1 # The path cost increases by 1 per move
                )
                children.append(child_node)