
import random
import time
from config import width, height, move_energy_cost, stay_energy_cost
from entity import Sheep, Grass
#无时间间隔
class SimulationManager:
    def __init__(self, world, initial_mobs, initial_food):
        self.world = world
        self.mobs = [] # 存放生物
        self.food = [] # 存放地图资源
        self._initialize_entities(initial_mobs, initial_food)

    def _initialize_entities(self, ini_mobs, ini_food):
        
        # 初始化羊
        for _ in range(ini_mobs):
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            sheep = Sheep(x, y)
            self.mobs.append(sheep)
            self.world.add_entity(sheep)
            
        # 初始化草
        for _ in range(ini_food):
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            grass = Grass(x, y, growthState=5)
            self.food.append(grass)
            self.world.add_entity(grass)

    #处理所有类型的行为和交互
    def update_simulation(self):
        eaten_grass = []
        dead_sheep = []
        for sheep in self.mobs:
            #走不动了   
            if not sheep.consume_energy(move_energy_cost):
                dead_sheep.append(sheep)
                continue 
            sheep.random_move()
            
            for grass in self.food:
                if grass not in eaten_grass and sheep.x == grass.x and sheep.y == grass.y:
                    if sheep.eat(grass):
                        eaten_grass.append(grass)
                      
                        break 
        if eaten_grass:
            self.food = [g for g in self.food if g not in eaten_grass]
            
     
        if dead_sheep:
            self.mobs = [s for s in self.mobs if s not in dead_sheep]
            
      
        self.world.entities = self.mobs + self.food
        self.world.render()
        self.world.print_world()
        
        return len(self.mobs) > 0 and len(self.food) > 0 