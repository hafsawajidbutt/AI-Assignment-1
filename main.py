import pygame

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
    