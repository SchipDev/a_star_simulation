import math
import numpy as np
from utils.simulation import _GridStateManager

class AStarSolver():

    def __init__(self, grid: _GridStateManager):
        self.open_set = []
        self.closed_set = []
        self.grid = grid
        self.start_cell = self.grid.get_start_cell()
        self.target_cell = self.grid.get_target_cell()
        
        # Initialize G Scores and F Scores
        self.g_scores = {self.grid.get_start_cell(): 0}
        self.f_scores = {self.grid.get_start_cell(): self.manhattan_distance(self.start_cell, self.target_cell)}
        for row in range(self.grid.GRID_SIZE):
            for col in range(self.grid.GRID_SIZE):
                if (row, col) != self.grid.get_start_cell():
                    self.g_scores[(row, col)] = float('inf')
                    self.f_scores{(row, col)} = float('inf')


    @staticmethod
    def manhattan_distance(cell_1, cell_2):
        return abs(cell_2[0] - cell_1[0])) + abs(cell_2[1] - cell_1[1]))
    
    @staticmethod
    def g_score(current_node, neighbor_note, g_scores):
        return 
    

