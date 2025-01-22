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
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        # Draw the grid
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
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
            self.grid[row][col] = 1 if self.grid[row][col] == 0 else 0
