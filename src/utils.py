def manhattan_distance(state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """
    Calculates the Manhattan Distance heuristic for the 8-puzzle.
    It measures how far each tile is from its goal position.

    :param state: The current board state (tuple).
    :param goal_state: The winning board state (tuple)
    :return: The total Manhattan Distance (integer).
    """
    distance = 0

    # We only calculate distance for tiles 1-8, the blank space '0' doesn't count
    for tile in range(1, 9):
        # Find 1D index of the tile in both states
        current_index = state.index(tile)
        goal_index = goal_state.index(tile)

        # Convert 1D index to 2D coordinates (row, col)
        current_row, current_col = current_index // 3, current_index % 3
        goal_row, goal_col = goal_index // 3, goal_index % 3

        # Add the distance for this specific tile to the total
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance

def print_board(state):
    """
    Prints the 1D tuple state as a formatted 3x3 grid.
    Replaces the '0' with a blank space for better readability.
    """
    print("-------------")
    for i in range(0, 9, 3):
        # Grab the row and replace 0 with a space
        row = [' ' if x == 0 else str(x) for x in state[i:i+3]]
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("-------------")
