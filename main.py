import os  



width = 50;#地图高度
height = 20;#地图宽度
initial_mobs = 15;#初始生物数量
initial_food = 40;#初始事物数量
move_energy_cost = 1#移动能量消耗
stay_energy_cost = 0.1;#静止能量消耗

    
class World:
    #初始化世界基本的这些变量
    def __init__(self,width,height,ini_mobs,ini_food,
                 mec,sec):
        self.grid = [['░' for _ in range(width)] for _ in range(height)]
        self.initial_mobs = ini_mobs
        self.initial_food = ini_food
        self.move_energy_cost = mec
        self.stay_energy_cost = sec
        
    def print_world(self):
        os.system('cls')
        for row in self.grid:
            for i in row:
                print(i,end="")
            print()

class Grass:
    def __init__(self,x,y,growthState):
        self.x = x
        self.y = y
        self.growthState = growthState
        self.symbol = '♣'
        
        
    
    
    
test = World(width,height,initial_mobs,initial_food,move_energy_cost,stay_energy_cost)

test.print_world()