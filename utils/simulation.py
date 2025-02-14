import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

class SimGrid(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "A* Grid Interaction")
        # Initialize grid as a 2D list of zeros (empty cells)
        self.grid = _GridStateManager()
        self.target_cell_color = arcade.color.GREEN
        self.grid.set_target_cell(0, 0)
        self.grid.set_target_cell(10, 0)
    
    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        # Draw the grid
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                if self.grid.is_target_cell(row, col):
                    color = self.target_cell_color
                else:
                    color = arcade.color.BLACK if self.grid[row][col] == 0 else arcade.color.BLUE
                arcade.draw_rectangle_filled(
                    x + CELL_SIZE / 2, y + CELL_SIZE / 2, CELL_SIZE, CELL_SIZE, color
                )
                # Draw grid lines
                arcade.draw_rectangle_outline(
                    x + CELL_SIZE / 2, y + CELL_SIZE / 2, CELL_SIZE, CELL_SIZE, arcade.color.WHITE
                )

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse clicks to toggle cells."""
        # Convert screen coordinates to grid coordinates
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            # Toggle the cell's state
            self.grid.set_cell_state(row, col)




class _GridStateManager():
    
    def __init__(self):
        self.grid_state = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.GRID_SIZE = GRID_SIZE
        self.target_cell = (None, None)
        self.start_cell = (None, None)

    def __getitem__(self, index):
        return self.grid_state[index]
    
    def __setitem__(self, index, value):
        self.grid_state[index] = value

    def get_grid_state(self):
        return self.grid_state
    
    def set_cell_state(self, row, column):
        
        if 0 <= row < GRID_SIZE and 0 <= column < GRID_SIZE:
            self.grid_state[row][column] = 1 if self.grid_state[row][column] == 0 else 0

    def get_neighbors(self, row, column):
        row, col = cell
        neighbors = []

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.GRID_SIZE and 0 <= new_col < self.GRID_SIZE:
                neighbors.append((new_row, new_col))
        
        return neighbors

    def set_target_cell(self, row, column):
        self.target_cell = (row, column)

    def is_target_cell(self, row, column):
        return True if row == self.target_cell[0] and column == self.target_cell[1] else False
    
    def set_start_cell(self, row, column):
        self.start_cell = (row, column)

    def get_start_cell(self):
        return self.start_cell



