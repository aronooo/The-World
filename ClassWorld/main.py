# main.py
from world import World
from config import CONFIG

def main():
    """Initializes and runs the world simulation."""
    print("🙏 Welcome to Project God-Complex 🙏")
    my_world = World(CONFIG)

    print("World initialized. Starting simulation.")
    my_world.display()

    for i in range(CONFIG["num_rounds"]):
        print(f"\n======= ROUND {i + 1} / {CONFIG['num_rounds']} =======")

        input("Press Enter to start the Day phase...")
        my_world.run_day_phase()
        my_world.display()

        input("Press Enter to start the Night phase...")
        my_world.run_night_phase()
        my_world.display()

    print("\nSimulation complete.")

    # Test the neighbor function
    print("\nInspecting cell (2, 2) and its neighbors:")
    target_cell = my_world.grid[2][2]
    print(f"  - Target Cell (2,2) is {'wet' if target_cell.is_wet else 'dry'}.")
    
    neighbors = my_world.get_neighbors_of(target_cell)
    for direction, neighbor_cell in neighbors.items():
        print(f"  - The cell to the {direction} is {'wet' if neighbor_cell.is_wet else 'dry'}.")


if __name__ == "__main__":
    main()