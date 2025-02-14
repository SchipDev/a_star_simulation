import math
import heapq as hq
from utils.simulation import _GridStateManager

class AStarSolver:
    
    
    def __init__(self, grid: _GridStateManager):
        self.grid = grid
        self.start_cell = self.grid.get_start_cell()
        self.target_cell = self.grid.get_target_cell()

        # Priority queue for A* search (min-heap)
        self.open_set = []
        hq.heappush(self.open_set, (0, self.start_cell))  # Push start cell with f-score 0

        # Closed set (nodes already evaluated)
        self.closed_set = set()

        # Cost from start to each node
        self.g_scores = {self.start_cell: 0}
        self.f_scores = {self.start_cell: self.manhattan_distance(self.start_cell, self.target_cell)}
        
        # Path reconstruction
        self.came_from = {}

        # Initialize g and f scores for all other cells
        for row in range(self.grid.GRID_SIZE):
            for col in range(self.grid.GRID_SIZE):
                cell = (row, col)
                if cell != self.start_cell:
                    self.g_scores[cell] = float('inf')
                    self.f_scores[cell] = float('inf')


    @staticmethod
    def manhattan_distance(cell_1, cell_2):
        """Compute Manhattan distance heuristic."""
        return abs(cell_2[0] - cell_1[0]) + abs(cell_2[1] - cell_1[1])

    def step(self):
        """Runs one step of the A* algorithm for visualization."""
        if not self.open_set:
            return None  # No path found

        # Get the node with the lowest f_score
        _, current = hq.heappop(self.open_set)
        
        # If we reached the goal, reconstruct and return the path
        if current == self.target_cell:
            return self.reconstruct_path()

        self.closed_set.add(current)  # Mark as evaluated

        # Iterate through neighbors (now using grid's built-in function)
        for neighbor in self.grid.get_neighbors(current):
            if neighbor in self.closed_set:
                continue  # Ignore nodes already evaluated

            tentative_g_score = self.g_scores[current] + 1  # Uniform movement cost

            # If new path to neighbor is shorter OR neighbor is not in open_set
            open_set_cells = {cell for _, cell in self.open_set}  # Set for quick lookup
            if neighbor not in open_set_cells or tentative_g_score < self.g_scores[neighbor]:
                self.g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + self.manhattan_distance(neighbor, self.target_cell)
                self.f_scores[neighbor] = f_score
                hq.heappush(self.open_set, (f_score, neighbor))
                self.came_from[neighbor] = current  # Store path

        return current  # Return the current node for visualization


    def reconstruct_path(self):
        """Reconstructs the shortest path by backtracking from the goal."""
        path = []
        current = self.target_cell

        while current in self.came_from:
            path.append(current)
            current = self.came_from[current]

        path.append(self.start_cell)  # Include start cell
        path.reverse()  # Reverse to get path from start → goal

        return path
    

