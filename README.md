# SOFE3720: 8-Puzzle AI Solver
**Group 9**
* Armaan Parmar (100877218)
* Farzad Shahdad (100861389)
* Waliullah Khan Mohammed (100865624)

## Project Overview
This project implements an intelligent system to solve the classic 8-puzzle game. It demonstrates both informed and uninformed AI search techniques by comparing Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search using the Manhattan Distance heuristic. 

## Features
* **Modular Design:** Clear separation of state representation, search algorithms, and utility functions.
* **Algorithm Comparison:** Side-by-side execution to compare solution depth, nodes expanded, and execution time.
* **Interactive CLI:** Users can run a default test board or input their own custom puzzle states.
* **Input Validation:** Safely catches invalid characters, incorrect lengths, and duplicate numbers.

## How to Run the Program
### Prerequisites
* Python 3.x installed on your system.
* No external libraries are required (only standard Python libraries like `heapq` and `collections` are used).

### Execution Steps
1. Download and extract the source code folder, or clone the repository.
2. Open a terminal or command prompt.
3. Navigate to the root directory of the project (where this README is located).
4. Run the main script using Python:

   ```bash
   python src/main.py
   ```