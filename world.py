import os
from config import width, height

#包含生物
class World:
    # 基本属性
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = [] 
        self.grid = [['░' for _ in range(width)] for _ in range(height)]

    def add_entity(self, entity):
        self.entities.append(entity)

   #渲染地图
    def render(self):
        #过去位置
        prev_positions = set() 
        
        for entity in self.entities:
            
            if entity.x != entity.prev_x or entity.y != entity.prev_y:
          
                prev_positions.add((entity.prev_x, entity.prev_y))
            
        
       
        for prev_x, prev_y in prev_positions:
            self.grid[prev_y][prev_x] = '░'

        
      #打印新的符号
        for entity in self.entities:
           self.grid[entity.y][entity.x] = entity.symbol
        entity.prev_x = entity.x
        entity.prev_y = entity.y

    #打印地图
    def print_world(self):
     
        os.system('cls') 
        for row in self.grid:
            print("".join(row))