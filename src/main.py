import time
from algorithms import a_star_search, bfs_search, dfs_search, get_path
from utils import print_board

def run_and_compare(initial_state):
    print("Initial Board:")
    print_board(initial_state)

    algorithms = [
        ("Breadth-First Search", bfs_search),
        ("Depth-First Search", dfs_search),
        ("A* Search (Manhattan Distance)", a_star_search)
    ]

    for name, algo in algorithms:
        print(f"\n--- Running {name} ---")
        start_time = time.time()

        winning_node, expanded = algo(initial_state)

        end_time = time.time()

        if winning_node:
            actions, states = get_path(winning_node)
            print("Status: Solved!")
            print(f"Solution Depth: {len(actions)} moves")
            print(f"Nodes Expanded: {expanded}")
            print(f"Time Taken: {end_time - start_time:.4f} seconds")
            if len(actions) > 30:
                print(f"Moves: {actions[:10]} ... [Too many moves to display ({len(actions)})] ... {actions[-5:]}")
            else:
                print(f"Moves: {actions}")
        else:
            print("Status: No solution found.")

if __name__ == "__main__":
    print("Welcome to the 8-Puzzle AI Solver!")
    print("1. Run default test board")
    print("2. Enter a custom board")
   
    choice = input("Select an option (1 or 2): ")
   
    if choice == '2':
        print("\nEnter 9 numbers (0-8) separated by spaces.")
        print("Use '0' to represent the blank space.")
        print("Example: 1 2 3 4 5 6 0 7 8")
        user_input = input("Board: ")
       
        try:
            # Convert the string input into a tuple of integers
            custom_state = tuple(int(x) for x in user_input.split())
           
            # Validation Rules:
            if len(custom_state) != 9:
                print("\nError: You must enter exactly 9 numbers.")
            elif set(custom_state) != set(range(9)):
                print("\nError: Board must contain exactly one of each number from 0 to 8.")
            else:
                print("\nStarting solver...")
                print("(Note: If the board is mathematically unsolvable, the algorithms will search all 181,440 states before returning 'No solution')")
                run_and_compare(custom_state)
               
        except ValueError:
            print("\nError: Invalid input! Please enter numbers only, separated by spaces.")
           
    else:
        # A solvable puzzle requiring exactly 5 moves
        test_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
        print("\nRunning default test board...")
        run_and_compare(test_state)
