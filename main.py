# vim: nu
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent

#!/usr/bin/python

import sys
import pygame
import sprites

pygame.init()
WIDTH = 700										# arbitrary values for now
HEIGHT = 700
size = WIDTH, HEIGHT
WHITE = (255, 255, 255)									#a few predefined constant colors
BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
ORANGE= (255, 165,   0)
    
    

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Gotta Catch 'Em All")

done = False
clock = pygame.time.Clock()

#pokemon  = sprites.Bulbasaur(  0, 0, 0, 0, 1, (25,16,16), (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Ivysaur(  0, 0, 0, 0, 1, (25,16,16), (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Venasaur(  0, 0, 0, 0, 1, (25,16,16), (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Squirtle(  0, 0, 0, 0, 1, (25,16,16), (115,156,206), (173,206,239), WHITE, screen)
#pokemon  = sprites.Wartortle(  0, 0, 0, 0, 1, (25,16,16), (115,156,206), (173,206,239), WHITE, screen)
pokemon  = sprites.Blastoise(  0, 0, 0, 0, 1, (25,16,16), (115,156,206), (173,206,239), WHITE, screen)
											#set sprite at location x,y, with velocity x,y,
											#with size multiplier 1,  with the following four colors
											#on the main screen
print pokemon
while not done:

  #limit the clock to ten loops per second
  clock.tick(3)

  for event in pygame.event.get():							#allows you to exit by clicking x
    if event.type == pygame.QUIT:
      done =True

  screen.fill(RED)									#arbitrary color, good for spotting mistakes in the sprite

  pokemon.draw()

  pygame.display.flip()

pygame.quit()
