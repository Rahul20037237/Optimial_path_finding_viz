# DFS  BFS and A* Visualization using Pygame

This project provides a visual representation of pathfinding algorithms such as **DFS (Depth First Search)**, **BFS (Breadth First Search)**, and potentially **A* (A-Star)** using Python and the Pygame library.

## Features
- Visualization of a grid-based environment.
- Implementation and animation of DFS and BFS pathfinding algorithms.
- Interactive start using the keyboard.

## Requirements
To run this project, you need the following:

- Python 3.x
- Pygame library

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

## Files
- **main.py**: Entry point of the project.
- **Grid_making.py**: Contains the `Grid` class responsible for creating and managing the grid.
- **DFS.py**: Implements the DFS algorithm.
- **BFS.py**: Implements the BFS algorithm.
- **A_star.py**: Implements the A* algorithm (if implemented).

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```

2. The grid will be displayed on the screen.

3. Press the **Space** key to visualize BFS starting from the top-left corner `(0, 0)` to the bottom-right corner `(29, 29)`.

4. Close the window to exit the program.

## Keyboard Controls
- **Space**: Start the BFS algorithm and reset the grid.
- **Close Button**: Exit the application.

## Customization
- Adjust the grid size by modifying `ROWS` and `COLS` in `main.py`.
- Change the algorithms being used by modifying the initialization of the algorithm class (`DFS`, `BFS`, `AStar`).
- Customize colors by changing the RGB tuples in `main.py`.

## Example Output
The program visualizes the BFS traversal across the grid, highlighting the cells as they are visited.

## Video Demo

You can view the demo video of the project below:
<figure class="video_container">
  <iframe src="https://github.com/Rahul20037237/Optimial_path_finding_viz/blob/0bf258393fedb4128b0148c7eab30d74c1e5cb14/video/Astar.mp4" frameborder="0" allowfullscreen="true"> 
</iframe>
</figure>


## Author
Developed by **RAHUL A**. Contributions are welcome!

