
import time
from config import width, height, initial_mobs, initial_food, time_per_step
from world import World
from manager import SimulationManager

def run_simulation():
    world = World(width, height)
    manager = SimulationManager(world, initial_mobs, initial_food)
    step_count = 0
    while True:
        print(f"Step {step_count + 1}:")
        step_count += 1
        continue_simulation = manager.update_simulation()
        time.sleep(time_per_step)
        if not continue_simulation:
            break
        if step_count >= 100: 
          
            break


if __name__ == "__main__":
    run_simulation()