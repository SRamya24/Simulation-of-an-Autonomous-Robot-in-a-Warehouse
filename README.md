# Simulation of an Autonomous Robot in a Warehouse

## Overview
This project simulates an autonomous robot navigating a rectangular warehouse of dimensions 10 meters by 10 meters. The robot starts at the coordinates (0, 0) and must navigate to the destination at (7, 9). The simulation considers the robot’s movement behavior, including speed, stopping conditions, and obstacle avoidance (if applicable).

The robot follows a set of constraints that define its movement and stops every 0.1 seconds for 2 seconds. The project is implemented using Python and visualized using `matplotlib` to represent the robot's movement.

## Objective
The goal of the simulation is to develop a Python program that accurately models the movement of an autonomous robot in a confined environment, taking into account the following:
- Robot's movement between two points.
- Time-based stopping behavior.
- Obstacle avoidance (optional).
- Proper boundary checks.

## Features
- **Robot Movement:** The robot moves towards the destination by covering a specific distance over a set period.
- **Speed Control:** The robot moves at 0.1 meters per second.
- **Stop and Go Behavior:** After every 0.1 seconds of movement, the robot pauses for 2 seconds.
- **Boundary Control:** The robot remains within the warehouse boundaries.
- **Visualization:** The robot's movement is visualized using `matplotlib`, displaying its path from the starting point to the destination.

## Prerequisites
To run the simulation, you’ll need to have the following Python packages installed:
- `matplotlib` (for visualizing the robot's movement)
- `time` (for managing movement and stopping intervals)

You can install the required packages by running:
```
pip install matplotlib
```

## How to Run the Simulation
1. Clone the repository to your local machine:
    ```
    git clone https://github.com/SRamya24/Simulation-of-an-Autonomous-Robot-in-a-Warehouse.git
    cd robot-simulation
    ```

2. Run the simulation script:
    ```
    python robot_simulation.py
    ```

3. The simulation will start, and a window will pop up showing the robot's movement from `(0, 0)` to `(7, 9)`, with stops at regular intervals.

4. The robot will be represented as a red dot and the destination as a green dot. You will be able to observe the robot stopping every 0.1 seconds and moving towards the destination after each pause.

## Code Explanation
- **Robot Movement:** The robot moves in steps based on the distance to the destination and the defined speed. Each movement lasts for 0.1 seconds, followed by a 2-second stop.
- **Visualization:** The robot’s position is tracked and updated on a `matplotlib` plot. The movement is animated using `FuncAnimation`, updating the robot’s position step-by-step.
  
## Evaluation Criteria
- **Programming Efficiency:** The code is well-organized and efficient, following clean coding practices.
- **Simulation Accuracy:** The robot's movement matches the specified constraints (speed, stopping intervals, boundary control).
- **Creativity:** The simulation can be enhanced with additional features, such as obstacle avoidance or more complex pathfinding algorithms.

## Expected Output
- A visual representation of the robot navigating the warehouse, with stopping and moving behavior clearly visible in the animation.
- A series of screenshots or GIFs demonstrating the robot's path from start to finish, including its stop-and-go behavior.

## Future Improvements
- **Obstacle Avoidance:** Implementing dynamic obstacle handling where the robot can detect and navigate around obstacles within the warehouse.
- **Pathfinding Algorithm:** Integrating pathfinding algorithms like A* or Dijkstra’s to allow the robot to find an optimal path around obstacles.

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests. Contributions for enhancements such as better visualizations or new features are always welcome!

# OUTPUT
![image](https://github.com/user-attachments/assets/11a2d723-2af8-4f83-9bbd-d8d93076285e)
