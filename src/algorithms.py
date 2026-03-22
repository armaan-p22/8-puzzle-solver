import heapq
from board import Node
from utils import manhattan_distance

def get_path(node):
    """
    Backtracks from the goal node to the start node to get the sequence of moves.
    Returns a list of actions and the sequences of board states.
    """
    actions = []
    states = []
    current = node

    while current.parent is not None:
        actions.append(current.action)
        states.append(current.state)
        current = current.parent
    
    states.append(current.state) # Add the initial state

    actions.reverse() # Reverse so it goes from start -> goal
    states.reverse()

    return actions, states

def a_star_search(initial_state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """
    Executes A* Search to find the shortest path to the goal.
    :return: A tuple containing (winning_node, nodes_expanded)
    """
    start_node = Node(state=initial_state, g_cost=0)
    start_node.h_cost = manhattan_distance(initial_state, goal_state)

    frontier = []
    heapq.heappush(frontier, start_node)

    explored = set()
    nodes_expanded = 0

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.state == goal_state:
            return current_node, nodes_expanded
        
        explored.add(current_node.state)
        nodes_expanded += 1

        for child in current_node.get_children():
            if child.state not in explored:
                child.h_cost = manhattan_distance(child.state, goal_state)
                heapq.heappush(frontier, child)
    
    return None, nodes_expanded # No solution found
