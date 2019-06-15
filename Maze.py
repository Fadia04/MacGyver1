
import pygame
from pygame.locals import *
from constantes import *
pygame.init()

class Maze:

    def __init__(self): # lef chemin vers notre fichier struct
        self.file = "Maze.txt"
        self.structure = 0
        

    def generate(self):
        with open(self.file, "r") as file:
            structure_maze = []
            for line in file:
                line_maze = []
                for letter in line:
                    if letter != "\n":
                        line_maze.append(letter)
                structure_maze.append(line_maze)
                self.structure = structure_maze
            print(structure_maze)
    def display(self):
        window = pygame.display.set_mode((450, 450))
        wall = pygame.image.load("wall.png").convert()
        start = pygame.image.load("macgyver.png").convert_alpha()
        goal = pygame.image.load("gardian.png").convert_alpha()
        floor = pygame.image.load("floor.png").convert()
        num_line = 0
        for line in self.structure:
            num_col = 0
            for letter in line:
                x = num_col * letter_size
                y = num_line * letter_size
                if letter == 'x':
                    window.blit(wall, (x,y))
                elif letter == 'p':
                    window.blit(start, (x,y))
                elif letter == 'g':
                    window.blit(goal, (x,y))
                elif letter == "o":
                    window.blit(floor, (x,y))
                num_col += 1
            num_line += 1
        pygame.display.flip() 
        continuer = 1
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    continuer = 0 
        

class Items:
    def __init(self, structure):
        self.structure = structure
        self.pos_x = 0
        self.pos_y = 0
        self.x = 0
        self.y = 0
        ether = pygame.image.load("ether.png").convert_alpha()
        needle = pygame.image.load("needle.png").convert_alpha()
        pipe = pygame.image.load("pipe.png").convert_alpha()
    def randomize(self):
        pos_x = 0
        pos_y = 0
        while self.structure[self.pos_y][self.pos_x]!= "x":
            self.pos_x = random.randint(0,14)
            self.pos_y = random.randint(0,14)
        self.x = self.pos_x*letter_size
        self.y = self.pos_y*letter_size

maze = Maze()
maze.generate()
maze.display()
item = Items()
item.randomize()
          
          


                
    



