import pygame
import numpy as np
import time

#initializing pygame
pygame.init()
 
#initializing surface
surface = pygame.display.set_mode((800,600))

class minicube:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class face:
    def __init__(self, cubes):
        self.cubes = cubes

class cube:
    def __init__(self, faces):
        self.faces = faces
    
    def draw(self):
        #orange
        pygame.draw.rect(surface, self.faces[0].cubes[0].color, pygame.Rect(self.faces[0].cubes[0].x, self.faces[0].cubes[0].y, 60, 60))
        # print(self.faces[0].cubes[0].x)
        # print(self.faces[0].cubes[0].y)
        # print(surface.get_at((self.faces[0].cubes[0].x, self.faces[0].cubes[0].y)))
        pygame.draw.rect(surface, self.faces[0].cubes[1].color, pygame.Rect(self.faces[0].cubes[1].x, self.faces[0].cubes[1].y, 60, 60))
        # print(self.faces[0].cubes[1].x)
        # print(self.faces[0].cubes[1].y)
        # print(surface.get_at((self.faces[0].cubes[1].x, self.faces[0].cubes[1].y)))
        pygame.draw.rect(surface, self.faces[0].cubes[2].color, pygame.Rect(self.faces[0].cubes[2].x, self.faces[0].cubes[2].y, 60, 60))
        # print(self.faces[0].cubes[2].x)
        # print(self.faces[0].cubes[2].y)
        # print(surface.get_at((self.faces[0].cubes[2].x, self.faces[0].cubes[2].y)))
        
        pygame.draw.rect(surface, self.faces[0].cubes[3].color, pygame.Rect(self.faces[0].cubes[3].x, self.faces[0].cubes[3].y, 60, 60))
        # print(self.faces[0].cubes[3].x)
        # print(self.faces[0].cubes[3].y)
        # print(surface.get_at((self.faces[0].cubes[3].x, self.faces[0].cubes[3].y)))
        pygame.draw.rect(surface, self.faces[0].cubes[4].color, pygame.Rect(self.faces[0].cubes[4].x, self.faces[0].cubes[4].y, 60, 60))
        # print(self.faces[0].cubes[4].x)
        # print(self.faces[0].cubes[4].y)
        # print(surface.get_at((self.faces[0].cubes[4].x, self.faces[0].cubes[4].y)))
        pygame.draw.rect(surface, self.faces[0].cubes[5].color, pygame.Rect(self.faces[0].cubes[5].x, self.faces[0].cubes[5].y, 60, 60))
        # print(self.faces[0].cubes[5].x)
        # print(self.faces[0].cubes[5].y)
        # print(surface.get_at((self.faces[0].cubes[5].x, self.faces[0].cubes[5].y)))
        
        pygame.draw.rect(surface, self.faces[0].cubes[6].color, pygame.Rect(self.faces[0].cubes[6].x, self.faces[0].cubes[6].y, 60, 60))
        # print(self.faces[0].cubes[6].x)
        # print(self.faces[0].cubes[6].y)
        # print(surface.get_at((self.faces[0].cubes[6].x, self.faces[0].cubes[6].y)))
        pygame.draw.rect(surface, self.faces[0].cubes[7].color, pygame.Rect(self.faces[0].cubes[7].x, self.faces[0].cubes[7].y, 60, 60))
        # print(self.faces[0].cubes[6].x)
        # print(self.faces[0].cubes[6].y)
        # print(surface.get_at((self.faces[0].cubes[6].x, self.faces[0].cubes[6].y)))
        pygame.draw.rect(surface, self.faces[0].cubes[8].color, pygame.Rect(self.faces[0].cubes[8].x, self.faces[0].cubes[8].y, 60, 60))
        # print(self.faces[0].cubes[6].x)
        # print(self.faces[0].cubes[6].y)
        # print(surface.get_at((self.faces[0].cubes[6].x, self.faces[0].cubes[6].y)))
        
        #green
        pygame.draw.rect(surface, self.faces[1].cubes[0].color, pygame.Rect(self.faces[1].cubes[0].x, self.faces[1].cubes[0].y, 60, 60))
        pygame.draw.rect(surface, self.faces[1].cubes[1].color, pygame.Rect(self.faces[1].cubes[1].x, self.faces[1].cubes[1].y, 60, 60))
        pygame.draw.rect(surface, self.faces[1].cubes[2].color, pygame.Rect(self.faces[1].cubes[2].x, self.faces[1].cubes[2].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[1].cubes[3].color, pygame.Rect(self.faces[1].cubes[3].x, self.faces[1].cubes[3].y, 60, 60))
        pygame.draw.rect(surface, self.faces[1].cubes[4].color, pygame.Rect(self.faces[1].cubes[4].x, self.faces[1].cubes[4].y, 60, 60))
        pygame.draw.rect(surface, self.faces[1].cubes[5].color, pygame.Rect(self.faces[1].cubes[5].x, self.faces[1].cubes[5].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[1].cubes[6].color, pygame.Rect(self.faces[1].cubes[6].x, self.faces[1].cubes[6].y, 60, 60))
        pygame.draw.rect(surface, self.faces[1].cubes[7].color, pygame.Rect(self.faces[1].cubes[7].x, self.faces[1].cubes[7].y, 60, 60))
        pygame.draw.rect(surface, self.faces[1].cubes[8].color, pygame.Rect(self.faces[1].cubes[8].x, self.faces[1].cubes[8].y, 60, 60))
        
        #red
        pygame.draw.rect(surface, self.faces[2].cubes[0].color, pygame.Rect(self.faces[2].cubes[0].x, self.faces[2].cubes[0].y, 60, 60))
        pygame.draw.rect(surface, self.faces[2].cubes[1].color, pygame.Rect(self.faces[2].cubes[1].x, self.faces[2].cubes[1].y, 60, 60))
        pygame.draw.rect(surface, self.faces[2].cubes[2].color, pygame.Rect(self.faces[2].cubes[2].x, self.faces[2].cubes[2].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[2].cubes[3].color, pygame.Rect(self.faces[2].cubes[3].x, self.faces[2].cubes[3].y, 60, 60))
        pygame.draw.rect(surface, self.faces[2].cubes[4].color, pygame.Rect(self.faces[2].cubes[4].x, self.faces[2].cubes[4].y, 60, 60))
        pygame.draw.rect(surface, self.faces[2].cubes[5].color, pygame.Rect(self.faces[2].cubes[5].x, self.faces[2].cubes[5].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[2].cubes[6].color, pygame.Rect(self.faces[2].cubes[6].x, self.faces[2].cubes[6].y, 60, 60))
        pygame.draw.rect(surface, self.faces[2].cubes[7].color, pygame.Rect(self.faces[2].cubes[7].x, self.faces[2].cubes[7].y, 60, 60))
        pygame.draw.rect(surface, self.faces[2].cubes[8].color, pygame.Rect(self.faces[2].cubes[8].x, self.faces[2].cubes[8].y, 60, 60))

        #blue
        pygame.draw.rect(surface, self.faces[3].cubes[0].color, pygame.Rect(self.faces[3].cubes[0].x, self.faces[3].cubes[0].y, 60, 60))
        pygame.draw.rect(surface, self.faces[3].cubes[1].color, pygame.Rect(self.faces[3].cubes[1].x, self.faces[3].cubes[1].y, 60, 60))
        pygame.draw.rect(surface, self.faces[3].cubes[2].color, pygame.Rect(self.faces[3].cubes[2].x, self.faces[3].cubes[2].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[3].cubes[3].color, pygame.Rect(self.faces[3].cubes[3].x, self.faces[3].cubes[3].y, 60, 60))
        pygame.draw.rect(surface, self.faces[3].cubes[4].color, pygame.Rect(self.faces[3].cubes[4].x, self.faces[3].cubes[4].y, 60, 60))
        pygame.draw.rect(surface, self.faces[3].cubes[5].color, pygame.Rect(self.faces[3].cubes[5].x, self.faces[3].cubes[5].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[3].cubes[6].color, pygame.Rect(self.faces[3].cubes[6].x, self.faces[3].cubes[6].y, 60, 60))
        pygame.draw.rect(surface, self.faces[3].cubes[7].color, pygame.Rect(self.faces[3].cubes[7].x, self.faces[3].cubes[7].y, 60, 60))
        pygame.draw.rect(surface, self.faces[3].cubes[8].color, pygame.Rect(self.faces[3].cubes[8].x, self.faces[3].cubes[8].y, 60, 60))
        
        #white
        pygame.draw.rect(surface, self.faces[4].cubes[0].color, pygame.Rect(self.faces[4].cubes[0].x, self.faces[4].cubes[0].y, 60, 60))
        pygame.draw.rect(surface, self.faces[4].cubes[1].color, pygame.Rect(self.faces[4].cubes[1].x, self.faces[4].cubes[1].y, 60, 60))
        pygame.draw.rect(surface, self.faces[4].cubes[2].color, pygame.Rect(self.faces[4].cubes[2].x, self.faces[4].cubes[2].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[4].cubes[3].color, pygame.Rect(self.faces[4].cubes[3].x, self.faces[4].cubes[3].y, 60, 60))
        pygame.draw.rect(surface, self.faces[4].cubes[4].color, pygame.Rect(self.faces[4].cubes[4].x, self.faces[4].cubes[4].y, 60, 60))
        pygame.draw.rect(surface, self.faces[4].cubes[5].color, pygame.Rect(self.faces[4].cubes[5].x, self.faces[4].cubes[5].y, 60, 60))

        pygame.draw.rect(surface, self.faces[4].cubes[6].color, pygame.Rect(self.faces[4].cubes[6].x, self.faces[4].cubes[6].y, 60, 60))
        pygame.draw.rect(surface, self.faces[4].cubes[7].color, pygame.Rect(self.faces[4].cubes[7].x, self.faces[4].cubes[7].y, 60, 60))
        pygame.draw.rect(surface, self.faces[4].cubes[8].color, pygame.Rect(self.faces[4].cubes[8].x, self.faces[4].cubes[8].y, 60, 60))
        
        #yellow
        pygame.draw.rect(surface, self.faces[5].cubes[0].color, pygame.Rect(self.faces[5].cubes[0].x, self.faces[5].cubes[0].y, 60, 60))
        pygame.draw.rect(surface, self.faces[5].cubes[1].color, pygame.Rect(self.faces[5].cubes[1].x, self.faces[5].cubes[1].y, 60, 60))
        pygame.draw.rect(surface, self.faces[5].cubes[2].color, pygame.Rect(self.faces[5].cubes[2].x, self.faces[5].cubes[2].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[5].cubes[3].color, pygame.Rect(self.faces[5].cubes[3].x, self.faces[5].cubes[3].y, 60, 60))
        pygame.draw.rect(surface, self.faces[5].cubes[4].color, pygame.Rect(self.faces[5].cubes[4].x, self.faces[5].cubes[4].y, 60, 60))
        pygame.draw.rect(surface, self.faces[5].cubes[5].color, pygame.Rect(self.faces[5].cubes[5].x, self.faces[5].cubes[5].y, 60, 60))
        
        pygame.draw.rect(surface, self.faces[5].cubes[6].color, pygame.Rect(self.faces[5].cubes[6].x, self.faces[5].cubes[6].y, 60, 60))
        pygame.draw.rect(surface, self.faces[5].cubes[7].color, pygame.Rect(self.faces[5].cubes[7].x, self.faces[5].cubes[7].y, 60, 60))
        pygame.draw.rect(surface, self.faces[5].cubes[8].color, pygame.Rect(self.faces[5].cubes[8].x, self.faces[5].cubes[8].y, 60, 60))
    
    def printCubeColour(self):
        for face in self.faces:
            for cube in face.cubes:
                print(cube.color)
                break
                
    def moveTC(self):
        orange = self.faces[0].cubes[0:3]
        green = self.faces[1].cubes[0:3]
        red = self.faces[2].cubes[0:3]
        blue = self.faces[3].cubes[0:3]
        for i in range(3):
            self.faces[2].cubes[i].x, green[i].x = green[i].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, green[i].y = green[i].y, self.faces[2].cubes[i].y
        for i in range(3):
            self.faces[3].cubes[i].x, red[i].x = red[i].x, self.faces[3].cubes[i].x
            self.faces[3].cubes[i].y, red[i].y = red[i].y, self.faces[3].cubes[i].y
        for i in range(3):
            self.faces[0].cubes[i].x, blue[i].x = blue[i].x, self.faces[0].cubes[i].x
            self.faces[0].cubes[i].y, blue[i].y = blue[i].y, self.faces[0].cubes[i].y
        
    def moveTA(self):    
        orange = self.faces[0].cubes[0:3]
        green = self.faces[1].cubes[0:3]
        red = self.faces[2].cubes[0:3]
        blue = self.faces[3].cubes[0:3]
        
        for i in range(3):
            self.faces[2].cubes[i].x, blue[i].x = blue[i].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, blue[i].y = blue[i].y, self.faces[2].cubes[i].y
        for i in range(3):
            self.faces[3].cubes[i].x, orange[i].x = orange[i].x, self.faces[3].cubes[i].x
            self.faces[3].cubes[i].y, orange[i].y = orange[i].y, self.faces[3].cubes[i].y
        for i in range(3):
            self.faces[0].cubes[i].x, green[i].x = green[i].x, self.faces[0].cubes[i].x
            self.faces[0].cubes[i].y, green[i].y = green[i].y, self.faces[0].cubes[i].y
        for i in range(3):
            self.faces[0].cubes[i].x, self.faces[2].cubes[i].x = self.faces[2].cubes[i].x, self.faces[0].cubes[i].x
            self.faces[0].cubes[i].y, self.faces[2].cubes[i].y = self.faces[2].cubes[i].y, self.faces[0].cubes[i].y
            self.faces[3].cubes[i].x, self.faces[1].cubes[i].x = self.faces[1].cubes[i].x, self.faces[3].cubes[i].x
            self.faces[3].cubes[i].y, self.faces[1].cubes[i].y = self.faces[1].cubes[i].y, self.faces[3].cubes[i].y

    def moveFC(self):
        yellow = self.faces[5].cubes[6::]
        green = self.faces[1].cubes[6::]
        white = self.faces[4].cubes[6::]
        blue = self.faces[3].cubes[6::]
        
        for i in range(3):
            self.faces[5].cubes[6 + i].x, blue[i].x = blue[i].x, self.faces[5].cubes[6 + i].x
            self.faces[5].cubes[6 + i].y, blue[i].y = blue[i].y, self.faces[5].cubes[6 + i].y
        for i in range(3):
            self.faces[1].cubes[6 + i].x, yellow[i].x = yellow[i].x, self.faces[1].cubes[6 + i].x
            self.faces[1].cubes[6 + i].y, yellow[i].y = yellow[i].y, self.faces[1].cubes[6 + i].y
        for i in range(3):
            self.faces[4].cubes[6 + i].x, green[i].x = green[i].x, self.faces[4].cubes[6 + i].x
            self.faces[4].cubes[6 + i].y, green[i].y = green[i].y, self.faces[4].cubes[6 + i].y
    
    def moveFA(self):
        yellow = self.faces[5].cubes[6::]
        green = self.faces[1].cubes[6::]
        white = self.faces[4].cubes[6::]
        blue = self.faces[3].cubes[6::]
        
        for i in range(3):
            self.faces[5].cubes[6 + i].x, blue[i].x = blue[i].x, self.faces[5].cubes[6 + i].x
            self.faces[5].cubes[6 + i].y, blue[i].y = blue[i].y, self.faces[5].cubes[6 + i].y
        for i in range(3):
            self.faces[1].cubes[6 + i].x, yellow[i].x = yellow[i].x, self.faces[1].cubes[6 + i].x
            self.faces[1].cubes[6 + i].y, yellow[i].y = yellow[i].y, self.faces[1].cubes[6 + i].y
        for i in range(3):
            self.faces[4].cubes[6 + i].x, green[i].x = green[i].x, self.faces[4].cubes[6 + i].x
            self.faces[4].cubes[6 + i].y, green[i].y = green[i].y, self.faces[4].cubes[6 + i].y
        for i in range(3):
            self.faces[4].cubes[6 + i].x, self.faces[5].cubes[6 + i].x = self.faces[5].cubes[6 + i].x, self.faces[4].cubes[6 + i].x
            self.faces[4].cubes[6 + i].y, self.faces[5].cubes[6 + i].y = self.faces[5].cubes[6 + i].y, self.faces[4].cubes[6 + i].y
            self.faces[3].cubes[6 + i].x, self.faces[1].cubes[6 + i].x = self.faces[1].cubes[6 + i].x, self.faces[3].cubes[6 + i].x
            self.faces[3].cubes[6 + i].y, self.faces[1].cubes[6 + i].y = self.faces[1].cubes[6 + i].y, self.faces[3].cubes[6 + i].y
    
    def moveBC(self):
        orange = self.faces[0].cubes[6::]
        green = self.faces[1].cubes[6::]
        red = self.faces[2].cubes[6::]
        blue = self.faces[3].cubes[6::]
        for i in range(3):
            self.faces[2].cubes[6 + i].x, green[i].x = green[i].x, self.faces[2].cubes[6 + i].x
            self.faces[2].cubes[6 + i].y, green[i].y = green[i].y, self.faces[2].cubes[6 + i].y
        for i in range(3):
            self.faces[3].cubes[6 + i].x, red[i].x = red[i].x, self.faces[3].cubes[6 + i].x
            self.faces[3].cubes[6 + i].y, red[i].y = red[i].y, self.faces[3].cubes[6 + i].y
        for i in range(3):
            self.faces[0].cubes[6 + i].x, blue[i].x = blue[i].x, self.faces[0].cubes[6 + i].x
            self.faces[0].cubes[6 + i].y, blue[i].y = blue[i].y, self.faces[0].cubes[6 + i].y
    
    def moveBA(self):    
        orange = self.faces[0].cubes[6::]
        green = self.faces[1].cubes[6::]
        red = self.faces[2].cubes[6::]
        blue = self.faces[3].cubes[6::]
        
        for i in range(3):
            self.faces[2].cubes[6 + i].x, blue[i].x = blue[i].x, self.faces[2].cubes[6 + i].x
            self.faces[2].cubes[6 + i].y, blue[i].y = blue[i].y, self.faces[2].cubes[6 + i].y
        for i in range(3):
            self.faces[3].cubes[6 + i].x, orange[i].x = orange[i].x, self.faces[3].cubes[6 + i].x
            self.faces[3].cubes[6 + i].y, orange[i].y = orange[i].y, self.faces[3].cubes[6 + i].y
        for i in range(3):
            self.faces[0].cubes[6 + i].x, green[i].x = green[i].x, self.faces[0].cubes[6 + i].x
            self.faces[0].cubes[6 + i].y, green[i].y = green[i].y, self.faces[0].cubes[6 + i].y
        for i in range(3):
            self.faces[0].cubes[6 + i].x, self.faces[2].cubes[6 + i].x = self.faces[2].cubes[6 + i].x, self.faces[0].cubes[6 + i].x
            self.faces[0].cubes[6 + i].y, self.faces[2].cubes[6 + i].y = self.faces[2].cubes[6 + i].y, self.faces[0].cubes[6 + i].y
            self.faces[3].cubes[6 + i].x, self.faces[1].cubes[6 + i].x = self.faces[1].cubes[6 + i].x, self.faces[3].cubes[6 + i].x
            self.faces[3].cubes[6 + i].y, self.faces[1].cubes[6 + i].y = self.faces[1].cubes[6 + i].y, self.faces[3].cubes[6 + i].y
   
    def moveAC(self):
        yellow = self.faces[5].cubes[0:3]
        green = self.faces[1].cubes[0:3]
        white = self.faces[4].cubes[0:3]
        blue = self.faces[3].cubes[0:3]
        
        for i in range(3):
            self.faces[5].cubes[i].x, blue[i].x = blue[i].x, self.faces[5].cubes[i].x
            self.faces[5].cubes[i].y, blue[i].y = blue[i].y, self.faces[5].cubes[i].y
        for i in range(3):
            self.faces[1].cubes[i].x, yellow[i].x = yellow[i].x, self.faces[1].cubes[i].x
            self.faces[1].cubes[i].y, yellow[i].y = yellow[i].y, self.faces[1].cubes[i].y
        for i in range(3):
            self.faces[4].cubes[i].x, green[i].x = green[i].x, self.faces[4].cubes[i].x
            self.faces[4].cubes[i].y, green[i].y = green[i].y, self.faces[4].cubes[i].y
    
    def moveAA(self):
        yellow = self.faces[5].cubes[0:3]
        green = self.faces[1].cubes[0:3]
        white = self.faces[4].cubes[0:3]
        blue = self.faces[3].cubes[0:3]
        
        for i in range(3):
            self.faces[5].cubes[i].x, blue[i].x = blue[i].x, self.faces[5].cubes[i].x
            self.faces[5].cubes[i].y, blue[i].y = blue[i].y, self.faces[5].cubes[i].y
        for i in range(3):
            self.faces[1].cubes[i].x, yellow[i].x = yellow[i].x, self.faces[1].cubes[i].x
            self.faces[1].cubes[i].y, yellow[i].y = yellow[i].y, self.faces[1].cubes[i].y
        for i in range(3):
            self.faces[4].cubes[i].x, green[i].x = green[i].x, self.faces[4].cubes[i].x
            self.faces[4].cubes[i].y, green[i].y = green[i].y, self.faces[4].cubes[i].y
        for i in range(3):
            self.faces[4].cubes[i].x, self.faces[5].cubes[i].x = self.faces[5].cubes[i].x, self.faces[4].cubes[i].x
            self.faces[4].cubes[i].y, self.faces[5].cubes[i].y = self.faces[5].cubes[i].y, self.faces[4].cubes[i].y
            self.faces[3].cubes[i].x, self.faces[1].cubes[i].x = self.faces[1].cubes[i].x, self.faces[3].cubes[i].x
            self.faces[3].cubes[i].y, self.faces[1].cubes[i].y = self.faces[1].cubes[i].y, self.faces[3].cubes[i].y
    
    def moveRA(self):
        red = [self.faces[2].cubes[2], self.faces[2].cubes[5], self.faces[2].cubes[8]]
        yellow = [self.faces[5].cubes[2], self.faces[5].cubes[5], self.faces[5].cubes[8]]
        orange = [self.faces[0].cubes[2], self.faces[0].cubes[5], self.faces[0].cubes[8]]
        white = [self.faces[4].cubes[2], self.faces[4].cubes[5], self.faces[4].cubes[8]]
        indices = [2, 5, 8]
        
        for i in indices:
            self.faces[2].cubes[i].x, white[indices.index(i)].x = white[indices.index(i)].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, white[indices.index(i)].y = white[indices.index(i)].y, self.faces[2].cubes[i].y
        for i in indices:
            self.faces[5].cubes[i].x, red[indices.index(i)].x = red[indices.index(i)].x, self.faces[5].cubes[i].x
            self.faces[5].cubes[i].y, red[indices.index(i)].y = red[indices.index(i)].y, self.faces[5].cubes[i].y
        for i in indices:
            self.faces[0].cubes[i].x, yellow[indices.index(i)].x = yellow[indices.index(i)].x, self.faces[0].cubes[i].x
            self.faces[0].cubes[i].y, yellow[indices.index(i)].y = yellow[indices.index(i)].y, self.faces[0].cubes[i].y
        
        for i in indices:
            self.faces[4].cubes[i].x, self.faces[5].cubes[i].x = self.faces[5].cubes[i].x, self.faces[4].cubes[i].x
            self.faces[4].cubes[i].y, self.faces[5].cubes[i].y = self.faces[5].cubes[i].y, self.faces[4].cubes[i].y
            self.faces[2].cubes[i].x, self.faces[0].cubes[i].x = self.faces[0].cubes[i].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, self.faces[0].cubes[i].y = self.faces[0].cubes[i].y, self.faces[2].cubes[i].y
        
    def moveRC(self):
        red = [self.faces[2].cubes[2], self.faces[2].cubes[5], self.faces[2].cubes[8]]
        yellow = [self.faces[5].cubes[2], self.faces[5].cubes[5], self.faces[5].cubes[8]]
        orange = [self.faces[0].cubes[2], self.faces[0].cubes[5], self.faces[0].cubes[8]]
        white = [self.faces[4].cubes[2], self.faces[4].cubes[5], self.faces[4].cubes[8]]
        indices = [2, 5, 8]
        
        for i in indices:
            self.faces[2].cubes[i].x, white[indices.index(i)].x = white[indices.index(i)].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, white[indices.index(i)].y = white[indices.index(i)].y, self.faces[2].cubes[i].y
        for i in indices:
            self.faces[5].cubes[i].x, red[indices.index(i)].x = red[indices.index(i)].x, self.faces[5].cubes[i].x
            self.faces[5].cubes[i].y, red[indices.index(i)].y = red[indices.index(i)].y, self.faces[5].cubes[i].y
        for i in indices:
            self.faces[0].cubes[i].x, yellow[indices.index(i)].x = yellow[indices.index(i)].x, self.faces[0].cubes[i].x
            self.faces[0].cubes[i].y, yellow[indices.index(i)].y = yellow[indices.index(i)].y, self.faces[0].cubes[i].y
    
    def moveLC(self):
        red = [self.faces[2].cubes[0], self.faces[2].cubes[3], self.faces[2].cubes[6]]
        yellow = [self.faces[5].cubes[0], self.faces[5].cubes[3], self.faces[5].cubes[6]]
        orange = [self.faces[0].cubes[0], self.faces[0].cubes[3], self.faces[0].cubes[6]]
        white = [self.faces[4].cubes[0], self.faces[4].cubes[3], self.faces[4].cubes[6]]
        indices = [0, 3, 6]
        
        for i in indices:
            self.faces[2].cubes[i].x, yellow[indices.index(i)].x = yellow[indices.index(i)].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, yellow[indices.index(i)].y = yellow[indices.index(i)].y, self.faces[2].cubes[i].y
        for i in indices:
            self.faces[5].cubes[i].x, orange[indices.index(i)].x = orange[indices.index(i)].x, self.faces[5].cubes[i].x
            self.faces[5].cubes[i].y, orange[indices.index(i)].y = orange[indices.index(i)].y, self.faces[5].cubes[i].y
        for i in indices:
            self.faces[0].cubes[i].x, white[indices.index(i)].x = white[indices.index(i)].x, self.faces[0].cubes[i].x
            self.faces[0].cubes[i].y, white[indices.index(i)].y = white[indices.index(i)].y, self.faces[0].cubes[i].y
        
        for i in indices:
            self.faces[4].cubes[i].x, self.faces[5].cubes[i].x = self.faces[5].cubes[i].x, self.faces[4].cubes[i].x
            self.faces[4].cubes[i].y, self.faces[5].cubes[i].y = self.faces[5].cubes[i].y, self.faces[4].cubes[i].y
            self.faces[2].cubes[i].x, self.faces[0].cubes[i].x = self.faces[0].cubes[i].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, self.faces[0].cubes[i].y = self.faces[0].cubes[i].y, self.faces[2].cubes[i].y
    
    def moveLA(self):
        red = [self.faces[2].cubes[0], self.faces[2].cubes[3], self.faces[2].cubes[6]]
        yellow = [self.faces[5].cubes[0], self.faces[5].cubes[3], self.faces[5].cubes[6]]
        orange = [self.faces[0].cubes[0], self.faces[0].cubes[3], self.faces[0].cubes[6]]
        white = [self.faces[4].cubes[0], self.faces[4].cubes[3], self.faces[4].cubes[6]]
        indices = [0, 3, 6]
        
        for i in indices:
            self.faces[2].cubes[i].x, white[indices.index(i)].x = white[indices.index(i)].x, self.faces[2].cubes[i].x
            self.faces[2].cubes[i].y, white[indices.index(i)].y = white[indices.index(i)].y, self.faces[2].cubes[i].y
        for i in indices:
            self.faces[5].cubes[i].x, red[indices.index(i)].x = red[indices.index(i)].x, self.faces[5].cubes[i].x
            self.faces[5].cubes[i].y, red[indices.index(i)].y = red[indices.index(i)].y, self.faces[5].cubes[i].y
        for i in indices:
            self.faces[0].cubes[i].x, yellow[indices.index(i)].x = yellow[indices.index(i)].x, self.faces[0].cubes[i].x
            self.faces[0].cubes[i].y, yellow[indices.index(i)].y = yellow[indices.index(i)].y, self.faces[0].cubes[i].y
    
    def scramble(self):
        file = open("scramble.txt", "r")
        movesText = file.read()
        moves = movesText.split(" ")
        print(moves)
        for move in moves:
            if (move == "TC"):
                self.moveTC()
            elif (move == "TA"):
                self.moveTA()
            elif (move == "FC"):
                self.moveFC()
            elif(move == "FA"):
                self.moveFA()
            elif(move == "BC"):
                self.moveBC()
            elif(move == "BA"):
                self.moveBA()
            elif(move == "AC"):
                self.moveAC()
            elif(move == "AA"):
                self.moveAA()
            elif(move == "RA"):
                self.moveRA()
            elif(move == "RC"):
                self.moveRC()
            elif(move == "LC"):
                self.moveLC()
            elif(move == "LA"):
                self.moveLA()
    
    def getCurrentState(self):
        state = ""
        face1X = [30, 91, 152]
        face1Y = [183, 244, 305]
        for y in face1Y:
            for x in face1X:
                color = surface.get_at((x,y))
                if(color == (255, 165, 0, 255)): #orange
                    state += "O"
                elif(color == (0, 255, 0, 255)): #green
                    state += "G"
                elif(color == (255, 0, 0, 255)): #red
                    state += "R"
                elif(color == (0, 0, 255, 255)): #blue
                    state += "B"
                elif(color == (255, 255, 255, 255)): #white
                    state += "W"
                elif(color == (255, 255, 0, 255)): #yellow
                    state += "Y"
        face2X = [213, 274, 335]
        face2Y = [183, 244, 305]
        for y in face2Y:
            for x in face2X:
                color = surface.get_at((x,y))
                if(color == (255, 165, 0, 255)): #orange
                    state += "O"
                elif(color == (0, 255, 0, 255)): #green
                    state += "G"
                elif(color == (255, 0, 0, 255)): #red
                    state += "R"
                elif(color == (0, 0, 255, 255)): #blue
                    state += "B"
                elif(color == (255, 255, 255, 255)): #white
                    state += "W"
                elif(color == (255, 255, 0, 255)): #yellow
                    state += "Y"
        face3X = [396, 457, 518]
        face3Y = [183, 244, 305]
        for y in face3Y:
            for x in face3X:
                color = surface.get_at((x,y))
                if(color == (255, 165, 0, 255)): #orange
                    state += "O"
                elif(color == (0, 255, 0, 255)): #green
                    state += "G"
                elif(color == (255, 0, 0, 255)): #red
                    state += "R"
                elif(color == (0, 0, 255, 255)): #blue
                    state += "B"
                elif(color == (255, 255, 255, 255)): #white
                    state += "W"
                elif(color == (255, 255, 0, 255)): #yellow
                    state += "Y"
        face4X = [579, 640, 701]
        face4Y = [183, 244, 305]
        for y in face4Y:
            for x in face4X:
                color = surface.get_at((x,y))
                if(color == (255, 165, 0, 255)): #orange
                    state += "O"
                elif(color == (0, 255, 0, 255)): #green
                    state += "G"
                elif(color == (255, 0, 0, 255)): #red
                    state += "R"
                elif(color == (0, 0, 255, 255)): #blue
                    state += "B"
                elif(color == (255, 255, 255, 255)): #white
                    state += "W"
                elif(color == (255, 255, 0, 255)): #yellow
                    state += "Y"
        face5X = [213, 274, 335]
        face5Y = [122, 61, 0]
        for y in face5Y:
            for x in face5X:
                color = surface.get_at((x,y))
                if(color == (255, 165, 0, 255)): #orange
                    state += "O"
                elif(color == (0, 255, 0, 255)): #green
                    state += "G"
                elif(color == (255, 0, 0, 255)): #red
                    state += "R"
                elif(color == (0, 0, 255, 255)): #blue
                    state += "B"
                elif(color == (255, 255, 255, 255)): #white
                    state += "W"
                elif(color == (255, 255, 0, 255)): #yellow
                    state += "Y"
        face6X = [213, 274, 335]
        face6Y = [366, 427, 488]
        for y in face6Y:
            for x in face6X:
                color = surface.get_at((x,y))
                if(color == (255, 165, 0, 255)): #orange
                    state += "O"
                elif(color == (0, 255, 0, 255)): #green
                    state += "G"
                elif(color == (255, 0, 0, 255)): #red
                    state += "R"
                elif(color == (0, 0, 255, 255)): #blue
                    state += "B"
                elif(color == (255, 255, 255, 255)): #white
                    state += "W"
                elif(color == (255, 255, 0, 255)): #yellow
                    state += "Y"
        return state          
    def heuristicScore(self):
        score = 0
        #orange
        orangeX = [30, 91, 152]
        orangeY = [183, 244, 305]
        for y in orangeY:
            for x in orangeX:
                color = surface.get_at((x,y))
                if(color == (255, 165, 0, 255)):
                    score += 1
        greenX = [213, 274, 335]
        greenY = [183, 244, 305]
        for y in greenY:
            for x in greenX:
                color = surface.get_at((x, y))
                if(color == (0, 255, 0, 255)):
                    score += 1
        redX = [396, 457, 518]
        redY = [183, 244, 305]
        for y in redY:
            for x in redX:
                color = surface.get_at((x, y))
                if(color == (255, 0, 0, 255)):
                    score += 1
        blueX = [579, 640, 701]
        blueY = [183, 244, 305]
        for y in blueY:
            for x in blueX:
                color = surface.get_at((x, y))
                if(color == (0, 0, 255, 255)):
                    score += 1
        whiteX = [213, 274, 335]
        whiteY = [122, 61, 0]
        for y in whiteY:
            for x in whiteX:
                color = surface.get_at((x, y))
                if(color == (255, 255, 255, 255)):
                    score += 1
        yellowX = [213, 274, 335]
        yellowY = [366, 427, 488]
        for y in yellowY:
            for x in yellowX:
                color = surface.get_at((x, y))
                if(color == (255, 255, 0, 255)):
                    score += 1
        return score
    
    def a_starCube(self):
        moves = []
        statesEncountered = []
        statesEncountered.append(self.getCurrentState())
        while self.heuristicScore() != 54:
            scores = []
            oldScores = []
            prospectiveMoves = [] #finding neighbouring nodes
            self.moveAA()#
            self.draw()
            prospectiveMoves.append("AA")
            scores.append(self.heuristicScore())
            self.moveAC()
            self.draw()
            self.moveAC()#
            self.draw()
            prospectiveMoves.append("AC")
            scores.append(self.heuristicScore())
            self.moveAA()
            self.draw()
            self.moveBA()#
            self.draw()
            prospectiveMoves.append("BA")
            scores.append(self.heuristicScore())
            self.moveBC()
            self.draw()
            self.moveBC()#
            self.draw()
            prospectiveMoves.append("BC")
            scores.append(self.heuristicScore())
            self.moveBA()
            self.draw()
            self.moveFC()#
            self.draw()
            prospectiveMoves.append("FC")
            scores.append(self.heuristicScore())
            self.moveFA()
            self.draw()
            self.moveFA()#
            self.draw()
            prospectiveMoves.append("FA")
            scores.append(self.heuristicScore())
            self.moveFC()
            self.draw()
            self.moveLC()#
            self.draw()
            prospectiveMoves.append("LC")
            scores.append(self.heuristicScore())
            self.moveLA()
            self.draw()
            self.moveLA()#
            self.draw()
            prospectiveMoves.append("LA")
            scores.append(self.heuristicScore())
            self.moveLC()
            self.draw()
            self.moveRC()#
            self.draw()
            prospectiveMoves.append("RC")
            scores.append(self.heuristicScore())
            self.moveRA()
            self.draw()
            self.moveRA()#
            self.draw()
            prospectiveMoves.append("RA")
            scores.append(self.heuristicScore())
            self.moveRC()
            self.draw()
            self.moveTC()#
            self.draw()
            prospectiveMoves.append("TC")
            scores.append(self.heuristicScore())
            self.moveTA()
            self.draw()
            self.moveTA()#
            self.draw()
            prospectiveMoves.append("TA")
            scores.append(self.heuristicScore())
            self.moveTC()
            self.draw()
            oldScores = scores
            scores = np.array(scores)
            max_Score = scores.max()
            indexMax = oldScores.index(max_Score)
            move = prospectiveMoves[indexMax]
            print(scores)
            print(prospectiveMoves)
            print(len(scores))
            print("Max: "+ str(max_Score))
            if (move == "TC"):
                self.moveTC()
                print("Moved TC 1")
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                        print("Moved TA rev")
                    elif (move == "TA"):
                        self.moveTC()
                        print("Moved TC rev")
                    elif (move == "FC"):
                        self.moveFA()
                        print("Moved FA rev")
                    elif(move == "FA"):
                        self.moveFC()
                        print("Moved FC rev")
                    elif(move == "BC"):
                        self.moveBA()
                        print("Moved BA rev")
                    elif(move == "BA"):
                        self.moveBC()
                        print("Moved BC rev")
                    elif(move == "AC"):
                        self.moveAA()
                        print("Moved AA rev")
                    elif(move == "AA"):
                        self.moveAC()
                        print("Moved AC rev")
                    elif(move == "RA"):
                        self.moveRC()
                        print("Moved RC rev")
                    elif(move == "RC"):
                        self.moveRA()
                        print("Moved RA rev")
                    elif(move == "LC"):
                        self.moveLA()
                        print("Moved LA rev")
                    elif(move == "LA"):
                        self.moveLC()
                        print("Moved LC rev")
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                        print("Moved TC 2")
                    elif (move == "TA"):
                        self.moveTA()
                        print("Moved TA 2")
                    elif (move == "FC"):
                        self.moveFC()
                        print("Moved FC 2")
                    elif(move == "FA"):
                        self.moveFA()
                        print("Moved FA 2")
                    elif(move == "BC"):
                        self.moveBC()
                        print("Moved BC 2")
                    elif(move == "BA"):
                        self.moveBA()
                        print("Moved BA 2")
                    elif(move == "AC"):
                        self.moveAC()
                        print("Moved AC 2")
                    elif(move == "AA"):
                        self.moveAA()
                        print("Moved AA 2")
                    elif(move == "RA"):
                        self.moveRA()
                        print("Moved RA 2")
                    elif(move == "RC"):
                        self.moveRC()
                        print("Moved RC 2")
                    elif(move == "LC"):
                        self.moveLC()
                        print("Moved LC 2")
                    elif(move == "LA"):
                        self.moveLA()
                        print("Moved LA 2")
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved TC")
                self.draw()
                pygame.display.update()
                time.sleep(5)
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif (move == "TA"):
                self.moveTA()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif (move == "FC"):
                self.moveFC()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "FA"):
                self.moveFA()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "BC"):
                self.moveBC()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "BA"):
                self.moveBA()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    print("OldScores: ", oldScores)
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    max_Score = max_Score2
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "AC"):
                self.moveAC()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    max_Score = max_Score2
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "AA"):
                self.moveAA()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    print(scores)
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    max_Score = max_Score2
                    print(max_Score2)
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    print(move)
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "RA"):
                self.moveRA()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    max_Score = max_Score2
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "RC"):
                self.moveRC()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    max_Score = max_Score2
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "LC"):
                self.moveLC()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    max_Score = max_Score2
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            elif(move == "LA"):
                self.moveLA()
                self.draw()
                pygame.display.update()
                time.sleep(5)
                state = self.getCurrentState()
                while state in statesEncountered:
                    if (move == "TC"): #reversing move
                        self.moveTA()
                    elif (move == "TA"):
                        self.moveTC()
                    elif (move == "FC"):
                        self.moveFA()
                    elif(move == "FA"):
                        self.moveFC()
                    elif(move == "BC"):
                        self.moveBA()
                    elif(move == "BA"):
                        self.moveBC()
                    elif(move == "AC"):
                        self.moveAA()
                    elif(move == "AA"):
                        self.moveAC()
                    elif(move == "RA"):
                        self.moveRC()
                    elif(move == "RC"):
                        self.moveRA()
                    elif(move == "LC"):
                        self.moveLA()
                    elif(move == "LA"):
                        self.moveLC()
                    self.draw()
                    pygame.display.update()
                    oldScores.remove(max_Score)
                    oldScores2 = oldScores
                    oldScores = np.array(oldScores)
                    max_Score2 = oldScores.max()
                    max_Score = max_Score2
                    oldScores = oldScores.tolist()
                    indexMax2 = oldScores2.index(max_Score2)
                    move = prospectiveMoves[indexMax2]
                    if (move == "TC"): #makingMove
                        self.moveTC()
                    elif (move == "TA"):
                        self.moveTA()
                    elif (move == "FC"):
                        self.moveFC()
                    elif(move == "FA"):
                        self.moveFA()
                    elif(move == "BC"):
                        self.moveBC()
                    elif(move == "BA"):
                        self.moveBA()
                    elif(move == "AC"):
                        self.moveAC()
                    elif(move == "AA"):
                        self.moveAA()
                    elif(move == "RA"):
                        self.moveRA()
                    elif(move == "RC"):
                        self.moveRC()
                    elif(move == "LC"):
                        self.moveLC()
                    elif(move == "LA"):
                        self.moveLA()
                    self.draw()
                    pygame.display.update()
                    state = self.getCurrentState()
                print("Moved")
                self.draw()
                pygame.display.update()
                statesEncountered.append(self.getCurrentState())
                moves.append(move)
            self.draw()
            pygame.display.update()
        return moves
    
    # def a_starCube(self):
    #     moves = []
    #     statesEncountered = []
    #     statesEncountered.append(self.getCurrentState())

    #     while self.heuristicScore() != 54:
    #         scores = []
    #         prospectiveMoves = []
            
    #         # Define all possible moves
    #         move_functions = [
    #             ("AA", self.moveAA),
    #             ("AC", self.moveAC),
    #             ("BA", self.moveBA),
    #             ("BC", self.moveBC),
    #             ("FC", self.moveFC),
    #             ("FA", self.moveFA),
    #             ("LC", self.moveLC),
    #             ("LA", self.moveLA),
    #             ("RC", self.moveRC),
    #             ("RA", self.moveRA),
    #             ("TC", self.moveTC),
    #             ("TA", self.moveTA)
    #         ]

    #         # Apply each move and calculate the heuristic score
    #         for move_name, move_func in move_functions:
    #             move_func()
    #             self.draw()
    #             pygame.display.update()
    #             score = self.heuristicScore()
    #             scores.append(score)
    #             prospectiveMoves.append(move_name)
    #             # Reverse the move to return to the original state
    #             if move_name.endswith("C"):
    #                 move_func()  # Reverse the move
    #             else:
    #                 move_func()  # Reverse the move

    #         # Find the move with the maximum score
    #         max_score = max(scores)
    #         index_max = scores.index(max_score)
    #         move = prospectiveMoves[index_max]

    #         # Apply the selected move
    #         move_func = dict(move_functions)[move]
    #         move_func()

    #         # Check if the new state has already been encountered
    #         new_state = self.getCurrentState()
    #         if new_state in statesEncountered:
    #             # If the state has been encountered, reverse the move and try the next best move
    #             move_func()  # Reverse the move
    #             scores[index_max] = -1  # Mark this move as invalid
    #             continue

    #         # If the state is new, add it to the list of encountered states
    #         statesEncountered.append(new_state)
    #         moves.append(move)

    #         # Update the display
    #         self.draw()
    #         pygame.display.update()

    #     return moves
            
        
#initializing colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)

#face Arrays
faces = []
rubiks = cube(faces)
orangeCubes = []
greenCubes = []
redCubes = []
blueCubes = []
whiteCubes = []
yellowCubes = []

#creation of Cubes

#orange
m1 = minicube(30, 183, orange)
m2 = minicube(91, 183, orange)
m3 = minicube(152, 183, orange)
    
m4 = minicube(30, 244, orange)
m5 = minicube(91, 244, orange)
m6 = minicube(152, 244, orange)

m7 = minicube(30, 305, orange)
m8 = minicube(91, 305, orange)
m9 = minicube(152, 305, orange)

orangeCubes.append(m1)
orangeCubes.append(m2)
orangeCubes.append(m3)
orangeCubes.append(m4)
orangeCubes.append(m5)
orangeCubes.append(m6)
orangeCubes.append(m7)
orangeCubes.append(m8)
orangeCubes.append(m9)

orangeFace = face(orangeCubes)
faces.append(orangeFace)

#green
m10 = minicube(213, 183, green)
m11 = minicube(274, 183, green)
m12 = minicube(335, 183, green)

m13 = minicube(213, 244, green)
m14 = minicube(274, 244, green)
m15 = minicube(335, 244, green)

m16 = minicube(213, 305, green)
m17 = minicube(274, 305, green)
m18 = minicube(335, 305, green)

greenCubes.append(m10)
greenCubes.append(m11)
greenCubes.append(m12)
greenCubes.append(m13)
greenCubes.append(m14)
greenCubes.append(m15)
greenCubes.append(m16)
greenCubes.append(m17)
greenCubes.append(m18)

greenFace = face(greenCubes)
faces.append(greenFace)

#red
m19 = minicube(396, 183, red)
m20 = minicube(457, 183, red)
m21 = minicube(518, 183, red)

m22 = minicube(396, 244, red)
m23 = minicube(457, 244, red)
m24 = minicube(518, 244, red)

m25 = minicube(396, 305, red)
m26 = minicube(457, 305, red)
m27 = minicube(518, 305, red)

redCubes.append(m19)
redCubes.append(m20)
redCubes.append(m21)
redCubes.append(m22)
redCubes.append(m23)
redCubes.append(m24)
redCubes.append(m25)
redCubes.append(m26)
redCubes.append(m27)

redFace = face(redCubes)
faces.append(redFace)

#blue
m25 = minicube(579, 183, blue)
m26 = minicube(640, 183, blue)
m27 = minicube(701, 183, blue)

m28 = minicube(579, 244, blue)
m29 = minicube(640, 244, blue)
m30 = minicube(701, 244, blue)

m31 = minicube(579, 305, blue)
m32 = minicube(640, 305, blue)
m33 = minicube(701, 305, blue)

blueCubes.append(m25)
blueCubes.append(m26)
blueCubes.append(m27)
blueCubes.append(m28)
blueCubes.append(m29)
blueCubes.append(m30)
blueCubes.append(m31)
blueCubes.append(m32)
blueCubes.append(m33)

blueFace = face(blueCubes)
faces.append(blueFace)

#white
m31 = minicube(213, 122, white)
m32 = minicube(274, 122, white)
m33 = minicube(335, 122, white)

m34 = minicube(213, 61, white)
m35 = minicube(274, 61, white)
m36 = minicube(335, 61, white)

m37 = minicube(213, 0, white)
m38 = minicube(274, 0, white)
m39 = minicube(335, 0, white)

whiteCubes.append(m31)
whiteCubes.append(m32)
whiteCubes.append(m33)
whiteCubes.append(m34)
whiteCubes.append(m35)
whiteCubes.append(m36)
whiteCubes.append(m37)
whiteCubes.append(m38)
whiteCubes.append(m39)

whiteFace = face(whiteCubes)
faces.append(whiteFace)

#yellow
m40 = minicube(213, 366, yellow)
m41 = minicube(274, 366, yellow)
m42 = minicube(335, 366, yellow)

m43 = minicube(213, 427, yellow)
m44 = minicube(274, 427, yellow)
m45 = minicube(335, 427, yellow)

m46 = minicube(213, 488, yellow)
m47 = minicube(274, 488, yellow)
m48 = minicube(335, 488, yellow)

yellowCubes.append(m40)
yellowCubes.append(m41)
yellowCubes.append(m42)
yellowCubes.append(m43)
yellowCubes.append(m44)
yellowCubes.append(m45)
yellowCubes.append(m46)
yellowCubes.append(m47)
yellowCubes.append(m48)

yellowFace = face(yellowCubes)
faces.append(yellowFace)
done = False
running = True
# Drawing Rectangle
rubiks.scramble()
#rubiks.heuristicScore()
#rubiks.draw()
while running:
    for event in pygame.event.get():  # Get all events
        if event.type == pygame.QUIT:  # Check if the QUIT event occurorange
            running = False
    rubiks.draw()
    pygame.display.update()
    print(rubiks.a_starCube())
    break

#OOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBWWWWWWWWWYYYYYYYYY