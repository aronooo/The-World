# world.py
import random
from cell import Cell

class World:
    """Manages the grid of cells and the simulation logic.
    
    
    """

    def __init__(self, config):
        self.height, self.width = config["world_size"]
        self.config = config
        self.grid = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]

    def run_day_phase(self):
        """Runs the logic for a single day cycle."""
        print("Day phase.")

        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]

                cell.dry_off()

                is_sunny = random.random() < self.config["sun_chance"]
                cell.set_sun(is_sunny)

                current_rain_chance = self.config["rain_chance"]
                if cell.is_sunny:
                    current_rain_chance *= (1.0 - self.config["sun_rain_reduction"])
                
                if random.random() < current_rain_chance:
                    cell.become_wet()

    def run_night_phase(self):
        """Runs the logic for a single night cycle."""
        print("Night phase.")
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x].set_sun(False)

    def get_neighbors_of(self, cell):
        """Finds and returns the neighbor Cell objects of a given cell."""
        neighbors = {}
        moves = [("top", cell.y - 1, cell.x), ("bottom", cell.y + 1, cell.x),
                 ("left", cell.y, cell.x - 1), ("right", cell.y, cell.x + 1)]

        for name, ny, nx in moves:
            if 0 <= ny < self.height and 0 <= nx < self.width:
                neighbors[name] = self.grid[ny][nx]
        
        return neighbors

    def display(self):
        """Prints the current state of the world to the console."""
        print("_-----: World View :-----_")
        for y in range(self.height):
            row_string = ""
            for x in range(self.width):
                row_string += self.grid[y][x].get_char()
            print(row_string)
        print("------------------")