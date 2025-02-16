import arcade
from utils.solvers import AStarSolver

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE


# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

class SimGrid(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "A* Grid Interaction")
        self.grid = _GridStateManager()
        self.target_cell_color = arcade.color.GREEN
        self.path_color = arcade.color.RED 

        self.grid.set_start_cell(0, 0)
        self.grid.set_target_cell(10, 10)

        self.solver = AStarSolver(self.grid)
        self.solved_path = None  # Store the final path

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * CELL_SIZE
                y = row * CELL_SIZE

                if self.grid.is_target_cell(row, col):
                    color = self.target_cell_color
                elif self.solved_path and (row, col) in self.solved_path:
                    color = self.path_color 
                else:
                    color = arcade.color.BLACK if self.grid[row][col] == 0 else arcade.color.BLUE

                arcade.draw_rectangle_filled(
                    x + CELL_SIZE / 2, y + CELL_SIZE / 2, CELL_SIZE, CELL_SIZE, color
                )

                arcade.draw_rectangle_outline(
                    x + CELL_SIZE / 2, y + CELL_SIZE / 2, CELL_SIZE, CELL_SIZE, arcade.color.WHITE
                )

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse clicks to toggle cells."""
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            self.grid.set_cell_state(row, col)

    def on_key_press(self, key, modifiers):
        """Handle key presses."""
        if key == arcade.key.SPACE:
            result = self.solver.step()  
            print("Stepped")
            if isinstance(result, list):  # If A* is complete, store the path
                self.solved_path = result
                print(self.solver.path)
            self.clear()
            self.on_draw()


class _GridStateManager:
    
    def __init__(self):
        self.grid_state = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.GRID_SIZE = GRID_SIZE
        self.target_cells = []
        self.start_cell = None

    def __getitem__(self, index):
        return self.grid_state[index]
    
    def __setitem__(self, index, value):
        self.grid_state[index] = value

    def get_grid_state(self):
        return self.grid_state
    
    def set_cell_state(self, row, column):
        """Toggles the state of a cell (wall/block or empty)."""
        if 0 <= row < GRID_SIZE and 0 <= column < GRID_SIZE:
            self.grid_state[row][column] = 1 if self.grid_state[row][column] == 0 else 0

    def get_neighbors(self, cell):
        """Returns the valid neighboring cells (up, down, left, right)."""
        row, col = cell
        neighbors = []

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.GRID_SIZE and 0 <= new_col < self.GRID_SIZE:
                neighbors.append((new_row, new_col))
        
        return neighbors

    def set_target_cell(self, row, column):
        """Adds a target cell to the list."""
        if (row, column) not in self.target_cells:
            self.target_cells.append((row, column))

    def is_target_cell(self, row, column):
        """Checks if a cell is a target cell."""
        return (row, column) in self.target_cells
    
    def set_start_cell(self, row, column):
        """Sets the start cell."""
        self.start_cell = (row, column)

    def get_start_cell(self):
        """Returns the start cell."""
        return self.start_cell
    
    def get_target_cell(self):
        """Returns the first target cell if it exists, otherwise None."""
        return self.target_cells[0] if self.target_cells else None



