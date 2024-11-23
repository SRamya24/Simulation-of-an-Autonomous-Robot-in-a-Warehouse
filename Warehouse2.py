import matplotlib.pyplot as plt
import time

class Warehouse:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def add_obstacle(self, x, y):
        self.grid[y][x] = 1

class Robot:
    def __init__(self, warehouse, start=(0, 0), destination=(7, 9)):
        self.warehouse = warehouse
        self.position = start
        self.destination = destination
        self.path = [start]

    def move(self):
        while self.position != self.destination:
            new_x, new_y = self.position
            if new_x < self.destination[0]:
                new_x += 1
            elif new_y < self.destination[1]:
                new_y += 1

            if self.warehouse.grid[new_y][new_x] == 1:
                print(f"Obstacle encountered at ({new_x}, {new_y})!")
                return

            self.position = (new_x, new_y)
            self.path.append(self.position)

            self.visualize_step()
            time.sleep(0.1)
            time.sleep(2)

    def visualize_step(self):
        plt.imshow(self.warehouse.grid, cmap="gray_r")
        plt.scatter(*zip(*self.path), c='blue')
        plt.scatter(*self.position, c='red', marker='o')
        plt.scatter(*self.destination, c='green', marker='x')
        plt.pause(0.1)


warehouse = Warehouse()
warehouse.add_obstacle(5, 5)

robot = Robot(warehouse)
robot.move()

plt.show()
