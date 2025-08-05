import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
   # print("Starting Asteroids!")
   # print (f"Screen width: {constants.SCREEN_WIDTH}")
   # print (f"Screen height: {constants.SCREEN_HEIGHT}")
    while True:
       screen.fill("black", rect=None, special_flags=0)
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return

if __name__ == "__main__":
    main()
