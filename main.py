import os  
import random
import time


width = 50;#地图高度
height = 20;#地图宽度
initial_mobs = 15;#初始生物数量
initial_food = 40;#初始事物数量
move_energy_cost = 1#移动能量消耗
stay_energy_cost = 0.1;#静止能量消耗
time_per_step = 0.1;#时间流动速度

    
class World:
    #初始化世界基本的这些变量
    def __init__(self,width,height,ini_mobs,ini_food,
                 mec,sec):
        self.grid = [['░' for _ in range(width)] for _ in range(height)]
        self.initial_mobs = ini_mobs
        self.initial_food = ini_food
        self.move_energy_cost = mec
        self.stay_energy_cost = sec
    #打印地图
    def print_world(self):
        os.system('cls')
        for row in self.grid:
            for i in row:
                print(i,end="")
            print()
    #替换某个对象（类列表）坐标到地图上
    def print_objects(self,objects):
        for obj in objects:
            self.grid[obj.y][obj.x] = obj.symbol
        #把之前的地方改成空地(用hasattr避免grass没有prev_x属性报错)
            if hasattr(obj,'prev_x') and hasattr(obj,'prev_y'):
                self.grid[obj.prev_y][obj.prev_x] = '░'




class Grass:# growthstate(int)和能量有换算公式 现在先不计算
    def __init__(self,x,y,growthState):
        self.x = x
        self.y = y
        self.growthState = growthState
        self.symbol = '♣'
        self.energy = growthState

#一只最基本的羊
#实现功能：移动，吃草
class Sheep:
    def __init__(self,ini_x,ini_y):
        self.x = ini_x
        self.y = ini_y
        self.prev_x = ini_x
        self.prev_y = ini_y
        #  direction = 'up','down','left','right'
        self.symbol = 'S'
    def move(self,direction,steps):
        #定义基础移动方法
        self.prev_x = self.x
        self.prev_y = self.y
        if direction == 'up':
            self.y -= steps
        elif direction == 'down':
            self.y += steps
        elif direction == 'left':
            self.x -= steps
        elif direction == 'right':
            self.x += steps
        #边界检测
        if self.x < 0:
            self.x = 0
        if self.x >= width:
            self.x = width - 1
        if self.y < 0:
            self.y = 0
        if self.y >= height:
            self.y = height - 1
    def eat(self,grass_x,grass_y,grass_energy,sheep_x,sheep_y,sheep_energy):
        #定义吃草方法
        #如果当前位置有草，则吃掉草，增加能量
        if(grass_x == sheep_x and grass_y == sheep_y):
            sheep_energy += grass_energy
            grass_energy = 0
        return sheep_energy,grass_energy
    
    # 羊的随机移动
    def random_move(self):
        import random
        direction = random.choice(['up','down','left','right'])
        self.move(direction,1)

        
    
    
    
test = World(width,height,initial_mobs,initial_food,move_energy_cost,stay_energy_cost)
test_grass = Grass(10,10,5)
test_sheep = Sheep(5,5)
#🐏随机走动 看看能不能吃到草
#逐步显示
for _ in range(20):
    test_sheep.random_move()
    sheep_energy,grass_energy = test_sheep.eat(test_grass.x,test_grass.y,
                                               test_grass.energy,
                                               test_sheep.x,test_sheep.y,10)
    test_grass.energy = grass_energy
    test.print_objects([test_grass,test_sheep])
    test.print_world()
    time.sleep(0.1)
