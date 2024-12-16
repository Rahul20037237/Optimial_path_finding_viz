# DFS, BFS, and A* Pathfinding Visualization using Pygame

Welcome to the **Pathfinding Visualization** project! This project provides a visual representation of popular pathfinding algorithms such as **DFS (Depth First Search)**, **BFS (Breadth First Search)**, and ***A* (A-Star)**** using Python and the Pygame library.

## 🚀 Features
- **Grid-based visualization** of pathfinding algorithms.
- **Interactive animations** for DFS and BFS algorithms.
- **Real-time control** using keyboard for starting and resetting the algorithm.

## 📋 Requirements
To run this project, you need the following:

- **Python 3.x**
- **Pygame library**

## 🛠️ Installation

Follow these simple steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Rahul20037237/Optimial_path_finding_viz.git
   cd Optimial_path_finding_viz
2.Install the required dependencies:
   ```bash
      pip install pygame

## 📁 Files Overview
main.py: Entry point of the project that runs the pathfinding algorithm.
Grid_making.py: Contains the Grid class responsible for creating and managing the grid.
DFS.py: Implements the DFS algorithm for pathfinding.
BFS.py: Implements the BFS algorithm for pathfinding.
A_star.py: Implements the A* algorithm for pathfinding (if implemented).
## ⚙️ Usage
Run the main script:

bash
Copy code
python main.py
The grid will be displayed on the screen.

Press the Space key to visualize BFS starting from the top-left corner (0, 0) to the bottom-right corner (29, 29).

To exit the program, simply close the window.

## ⌨️ Keyboard Controls
Space: Start the BFS algorithm and reset the grid.
Close Button: Exit the application.
## 🎨 Customization
Grid Size: Adjust the grid size by modifying ROWS and COLS in main.py.
Algorithms: Change the algorithm used by modifying the initialization of the algorithm class (DFS, BFS, AStar).
Colors: Customize the grid and algorithm colors by changing the RGB tuples in main.py.
🖼️ Example Output
The program visualizes the BFS traversal across the grid, highlighting the cells as they are visited.

🎬 Video Demo
You can view the demo video of the project below:



Watch the demo to see how the pathfinding algorithms work in real-time!

📧 Author
Developed by RAHUL A.
