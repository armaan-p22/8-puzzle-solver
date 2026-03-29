import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import run_and_compare

def test_input_validation(user_input):
    """Simulates the try-except validation block from main.py"""
    print(f"\n[Test Input String]: '{user_input}'")
    try:
        custom_state = tuple(int(x) for x in user_input.split())
        if len(custom_state) != 9:
            print("--> RESULT: Caught Error - You must enter exactly 9 numbers.")
        elif set(custom_state) != set(range(9)):
            print("--> RESULT: Caught Error - Board must contain exactly one of each number from 0 to 8.")
        else:
            print("--> RESULT: SUCCESS - Valid board. Starting solver...")
    except ValueError:
        print("--> RESULT: Caught Error - Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    print("==================================================")
    print("      8-PUZZLE AUTOMATED TEST SUITE")
    print("==================================================")

    # --- Test Input Validation Edge Cases ---
    print("\n--- PHASE 1: Testing Input Validation ---")
    test_input_validation("1 a")
    test_input_validation("1 1 2 3 4 5 6 7 8")
    test_input_validation("1 2 3 4 5 6 7 8 0 10")
    test_input_validation("1 2 3 4 5 6 7 8 0")

    # --- Test Algorithm Execution ---
    print("\n\n--- PHASE 2: Testing Search Algorithms ---")
    
    test_boards = [
        ("Test 1: Already Solved Board (0 moves expected)", (1, 2, 3, 4, 5, 6, 7, 8, 0)),
        ("Test 2: Default Easy Board (2 moves expected)", (1, 2, 3, 4, 5, 6, 0, 7, 8)),
        ("Test 3: Hard Board (22 moves expected)", (0, 1, 2, 3, 4, 5, 6, 7, 8))
    ]

    for name, board in test_boards:
        print(f"\n==================================================")
        print(f" {name}")
        print(f"==================================================")
        run_and_compare(board)
        
    print("\n*** ALL TESTS COMPLETED ***")