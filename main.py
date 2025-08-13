import sys
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables,)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateables, drawables)
  # print("Starting Asteroids!")
   # print (f"Screen width: {constants.SCREEN_WIDTH}")
   # print (f"Screen height: {constants.SCREEN_HEIGHT}")
    while True:
       screen.fill("black")
       dt =  clock.tick(60)/1000

       updateables.update(dt)

       for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                   asteroids.add(*asteroid.split())
                   shot.kill()

       for asteroid in asteroids:
              if player.collision(asteroid):
                 print("Game Over!")
                 sys.exit()


       for item in drawables:
           item.draw(screen)

       pygame.display.flip()


       for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return

if __name__ == "__main__":
    main()
