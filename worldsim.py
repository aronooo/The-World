import numpy as np

'''
A world simulation with day and night cycles, sunshine, and rain.
The world is represented as a grid where each cell can be sunny or cloudy,
and rainy, (and steamy). The simulation runs for a specified number of rounds.


my first intuition was to complete it with classes, but I got stuck, so i went with numpy which I am more familiar with.
'''




# config for world
CONFIG = {
    "world_size": (10, 20),  # (height, width) - like rows and columns
    "num_rounds": 5,         # How many full day/night cycles to run
    "sun_chance": 0.4,       # 40% chance a cell will be sunny
    "rain_chance": 0.3,      # 30% base chance of rain
    "sun_rain_reduction": 0.8 # 80% - if it's sunny, rain is much less likely
}


# --------------------------------------------------------------------------
# The visuals
# -------------------------------------------------------------------------

def display_world(world_state):
    print("_-----: World View :-----_")
    
    # extracting initialized layers.
    sun_layer = world_state['sun']
    water_layer = world_state['water']  
    
    height, width = sun_layer.shape

    # row by row printing out the world
    for y in range(height):
        row_string = ""
        for x in range(width):
            # We check the state of each cell and pick a character
            is_sunny = sun_layer[y, x] == 1
            is_wet = water_layer[y, x] == 1

            if is_sunny and is_wet:
                row_string += "♨ " # ground steaM???
            elif is_sunny:
                row_string += "☀ " # sun
            elif is_wet:
                row_string += "🌧 " # wet and cloudy
            elif not is_wet and not is_sunny:
                row_string += "☁ " # Dry and cloudy
            # elif smth:
            #     row_string += "?? " # future states- apocalypse, meteor, zombies, idk        
        
        print(row_string)
    print("------------------")


# --------------------------------------------------------------------------
# 3. the phases - day and night
# --------------------------------------------------------------------------

def run_day_phase(world_state, config):
    print("The sun is rising! Wake up!!.")
    
    height, width = config["world_size"]
    
    # 1. reggel száraz
    world_state['water'].fill(0)
    
    # sunshine
    random_values = np.random.rand(height, width)
    sun_layer = (random_values < config["sun_chance"]).astype(int) # wherever random is less than sun_change it is sunny.
    world_state['sun'] = sun_layer
    
    # Rain....
    rain_prob_grid = np.full((height, width), config["rain_chance"]) #grid of base prob
    # reduce rain prob in sunny locations
    sunny_locations = (sun_layer == 1)
    reduction = 1.0 - config["sun_rain_reduction"]
    rain_prob_grid[sunny_locations] *= reduction
    # see rain areas by comparison with rand values
    random_values_for_rain = np.random.rand(height, width)
    rain_occurs = (random_values_for_rain < rain_prob_grid)
    # update water layer!
    world_state['water'][rain_occurs] = 1


# NIght phase
def run_night_phase(world_state):
    print("The sun sets....... (go sleep)")
    world_state['sun'].fill(0) #no sun
    #water remains

# neighbor function is a bit weird
# should be changed so it can be used during the phases maybe.
def get_neighbors(world_state, y, x):
    height, width = world_state['sun'].shape
    neighbors = {}
    
    
    moves = [("top", y - 1, x), ("bottom", y + 1, x), #all possible moves (dir, y, x)
             ("left", y, x - 1), ("right", y, x + 1)]
    
    for name, ny, nx in moves:
        # Check if the neighbor is inside the world borders
        if 0 <= ny < height and 0 <= nx < width:

            neighbors[name] = {            # if yes, get state
                "is_sunny": world_state['sun'][ny, nx] == 1,
                "is_wet": world_state['water'][ny, nx] == 1
            }
            
    return neighbors

# --------------------------------------------------------------------------
# The main simulation loop
# --------------------------------------------------------------------------

def main():
    print("🙏 Welcome to Project God-Complex 🙏")
    
    height, width = CONFIG["world_size"]

    # Initialize the world state
    world_state = {
        "sun": np.zeros((height, width), dtype=int),
        "water": np.zeros((height, width), dtype=int)
    }

    print("World initialized! Let's begin the simulation.")
    display_world(world_state)

    # The main loop of universe generation
    for i in range(CONFIG["num_rounds"]):
        print(f"\n======= ROUND {i + 1} / {CONFIG['num_rounds']} =======")
        
        # Run Day
        input("Press Enter to start the Day phase...")
        run_day_phase(world_state, CONFIG)
        display_world(world_state)

        # Run Night
        input("Press Enter to start the Night phase...")
        run_night_phase(world_state)
        display_world(world_state)
    
    print("\nSimulation complete. The world is at rest.")


    # neighbor cell testing for show (not very useful yet, will amend)

    print("\nLet's inspect the neighbors of cell (2, 2):")
    neighbors_of_cell = get_neighbors(world_state, 2, 2)
    for direction, state in neighbors_of_cell.items():
        print(f" The cell to the {direction} is {'wet' if state['is_wet'] else 'dry'}.")

if __name__ == "__main__":
    main()