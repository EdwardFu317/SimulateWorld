
import random
from config import width, height

# 实体基类
class Entity:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.prev_x = x # 用于地图清理
        self.prev_y = y
        self.symbol = symbol
        
    def get_position(self):
        return (self.x, self.y)

# 草类
class Grass(Entity):
    def __init__(self, x, y, growthState=5):
        super().__init__(x, y, '♣')
        self.energy = growthState
        self.is_alive = True

# 羊类
class Sheep(Entity):
    def __init__(self, x, y, energy=10):
        super().__init__(x, y, 'S')
        self.energy = energy
        self.max_energy = 20
        self.min_energy_to_survive = 0

    # 移动方法，包含边界检测
    def random_move(self):
        #移动之前先保存
        self.prev_x, self.prev_y = self.x, self.y
        
        direction = random.choice(['up','down','left','right','stay'])
        
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        
        # 边界检测优化
        self.x = max(0, min(self.x, width - 1))
        self.y = max(0, min(self.y, height - 1))

    # 羊与草的交互逻辑
    def eat(self, grass):
        
        if self.x == grass.x and self.y == grass.y:
            # 用min简化数值比较
            self.energy = min(self.max_energy, self.energy + grass.energy)
            return True
        return False
    
    # 模拟能量消耗和存活判定
    def consume_energy(self, cost):
        self.energy -= cost
        if self.energy <= self.min_energy_to_survive:
            return False 
        return True 