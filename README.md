DFS and BFS Visualization using Pygame

This project provides a visual representation of pathfinding algorithms such as DFS (Depth First Search), BFS (Breadth First Search), and potentially A (A-Star)* using Python and the Pygame library.

Features

Visualization of a grid-based environment.

Implementation and animation of DFS and BFS pathfinding algorithms.

Interactive start using the keyboard.

Requirements

To run this project, you need the following:

Python 3.x

Pygame library

Installation

Clone the repository:

git clone <repository_url>
cd <repository_name>

Install the required dependencies:

pip install pygame

Files

main.py: Entry point of the project.

Grid_making.py: Contains the Grid class responsible for creating and managing the grid.

DFS.py: Implements the DFS algorithm.

BFS.py: Implements the BFS algorithm.

A_star.py: Implements the A* algorithm (if implemented).

Usage

Run the main script:

python main.py

The grid will be displayed on the screen.

Press the Space key to visualize BFS starting from the top-left corner (0, 0) to the bottom-right corner (29, 29).

Close the window to exit the program.

Keyboard Controls

Space: Start the BFS algorithm and reset the grid.

Close Button: Exit the application.

Customization

Adjust the grid size by modifying ROWS and COLS in main.py.

Change the algorithms being used by modifying the initialization of the algorithm class (DFS, BFS, AStar).

Customize colors by changing the RGB tuples in main.py.

Example Output

The program visualizes the BFS traversal across the grid, highlighting the cells as they are visited.

Future Improvements

Add support for obstacles and weighted paths.

Extend visualization to include A*.

Implement additional interactivity (e.g., setting custom start and goal positions).

License

This project is open-source and available under the MIT License.

Author

Developed by [Your Name]. Contributions are welcome!
