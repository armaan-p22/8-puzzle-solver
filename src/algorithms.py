import heapq
from board import Node
from utils import manhattan_distance
from collections import deque


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

def bfs_search(initial_state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """Breadth-First Search (FIFO Queue)"""
    start_node = Node(state=initial_state, g_cost=0)
    if start_node.state == goal_state:
        return start_node, 0
   
    frontier = deque([start_node])
    frontier_states = {start_node.state} # O(1) lookup set
    explored = set()
    nodes_expanded = 0

    while frontier:
        current_node = frontier.popleft() # Pop from front
        frontier_states.remove(current_node.state) # Keep sync with frontier

        explored.add(current_node.state)
        nodes_expanded += 1

        for child in current_node.get_children():
            if child.state not in explored and child.state not in frontier_states:
                if child.state == goal_state:
                    return child, nodes_expanded
                frontier.append(child)
                frontier_states.add(child.state)
   
    return None, nodes_expanded # No solution

def dfs_search(initial_state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """Depth-First Search (LIFO Stack)"""
    start_node = Node(state=initial_state, g_cost=0)
    frontier = [start_node]
    frontier_states = {start_node.state} # O(1) lookup set
    explored = set()
    nodes_expanded = 0

    while frontier:
        current_node = frontier.pop() # Pop from end
        frontier_states.remove(current_node.state) # Keep sync with frontier

        if current_node.state == goal_state:
            return current_node, nodes_expanded
       
        explored.add(current_node.state)
        nodes_expanded += 1

        # Reverse children so the 'first' generated child is popped first
        for child in reversed(current_node.get_children()):
            if child.state not in explored and child.state not in frontier_states:
                frontier.append(child)
                frontier_states.add(child.state)

    return None, nodes_expanded # No solution
