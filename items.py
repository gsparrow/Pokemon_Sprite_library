# -*- coding: utf-8 -*-
# vim: nu cursorline foldmethod=marker maxmem=10000000
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent ttyfast

import pygame
from sprites import my_sprite

class Pokeball (my_sprite): # {{{
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color1, color2, color3, screen):

    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.screen          = screen

#default colors for Poké Ball
#    self.color_1 = (25,16,16)
#    self.color_2 = (255,255,255) #white
#    self.color_3 = (255,123,23)
    self.color_1 = color1
    self.color_2 = color2
    self.color_3 = color3

  def get_Name(self):
    return u"Poké Ball"

  def get_Pokedex_Message(self):
    return "Allows the player to catch wild Pokémon."

  def get_front_height(self):
    return 12*self.size

  def get_front_width(self):
    return 12*self.size

  def draw(self): # {{{
    ###  0 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y +  0*self.size,  4*self.size, 1*self.size])
    # }}}
    ###  1 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y +  1*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  4*self.size,  self.my_y +  1*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y +  1*self.size,  2*self.size, 1*self.size])
    # }}}
    ###  2 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  1*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  2*self.size,  self.my_y +  2*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  5*self.size,  self.my_y +  2*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  7*self.size,  self.my_y +  2*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    # }}}
    ###  3 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  1*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  2*self.size,  self.my_y +  3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  5*self.size,  self.my_y +  3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  7*self.size,  self.my_y +  3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    # }}}
    ###  4 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  0*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  1*self.size,  self.my_y +  4*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    # }}}
    ###  5 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  0*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  1*self.size,  self.my_y +  5*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    # }}}
    ###  6 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  0*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  1*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  3*self.size,  self.my_y +  6*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  9*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    # }}}
    ###  7 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  0*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  1*self.size,  self.my_y +  7*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    # }}}
    ###  8 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  1*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  2*self.size,  self.my_y +  8*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    # }}}
    ###  9 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  1*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  2*self.size,  self.my_y +  9*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 10 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y + 10*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  4*self.size,  self.my_y + 10*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y + 10*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 11 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y + 11*self.size,  4*self.size, 1*self.size])
    # }}} }}}
# }}}

