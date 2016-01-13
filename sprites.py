# vim: nu
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent
# vim: cursorline foldmethod=marker

import pygame

class my_sprite: # {{{
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier):
    self.my_x = x
    self.my_y = y
    self.my_velocity_x = velocity_x
    self.my_velocity_y = velocity_y
    if size_multiplier < 2:
      self.size = 2
    else:
      self.size = size_multiplier

  def get_x (self):
    return self.my_x
  def get_y (self):
    return self.my_x
  def get_velocity_x (self):
    return self.my_velocity_x
  def get_velocity_y (self):
    return self.my_velocity_y
  def get_size_multiplier (self):
    return self.size

  def set_x (self, x):
    self.my_x = x
  def set_y (self, y):
    self.my_y = y
  def set_velocity_x (self, velocity_x):
    self.my_velocity_x = velocity_x
  def set_velocity_y (self, velocity_y):
    self.my_velocity_y = velocity_y
  def set_size_multiplier (self, size):
    self.size = size
# }}}

class Bulbasaur (my_sprite): # {{{
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color1, color2, color3, color4, screen):

    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.screen          = screen

#default colors for bulbasaur
#    self.color_1 = (25,16,16)
#    self.color_2 = (74,165,90)
#    self.color_3 = (165,214,132)
#    self.color_4 = (255,255,255) #white
    self.color_1 = color1
    self.color_2 = color2
    self.color_3 = color3
    self.color_4 = color4

  def __str__(self):
    return "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokemon."

  def draw(self):
    ### 0 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 26*self.size,  self.my_y +  0*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 1 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 26*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 27*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 2 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 24*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 25*self.size,  self.my_y +  2*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 28*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 3 ### {{{
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 20*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 24*self.size,  self.my_y +  3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 26*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 28*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 4 ### {{{
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  4*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 20*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 22*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 23*self.size,  self.my_y +  4*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 26*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 28*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 5 ### {{{
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 14*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y +  5*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 16*self.size,  self.my_y +  5*self.size, 4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 21*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 22*self.size,  self.my_y +  5*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 24*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 26*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 28*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 6 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 14*self.size,  self.my_y +  6*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 19*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 20*self.size,  self.my_y +  6*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 23*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 26*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 28*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 7 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 13*self.size,  self.my_y +  7*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 16*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 17*self.size,  self.my_y +  7*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 21*self.size,  self.my_y +  7*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 24*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 26*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 28*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 8 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 12*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 16*self.size,  self.my_y +  8*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 19*self.size,  self.my_y +  8*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 22*self.size,  self.my_y +  8*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 26*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 27*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y +  8*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 9 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 11*self.size,  self.my_y +  9*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 14*self.size,  self.my_y +  9*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 16*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 17*self.size,  self.my_y +  9*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 20*self.size,  self.my_y +  9*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 24*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 26*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 27*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 10 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  5*self.size,  self.my_y +  10*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 11*self.size,  self.my_y +  10*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 14*self.size,  self.my_y +  10*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 17*self.size,  self.my_y + 10*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 19*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  10*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 24*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 26*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 27*self.size,  self.my_y + 10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 29*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 31*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  10*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 11 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  5*self.size,  self.my_y + 11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y +  11*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  11*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 16*self.size,  self.my_y + 11*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 18*self.size,  self.my_y +  11*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 20*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 22*self.size,  self.my_y +  11*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 24*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 26*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 27*self.size,  self.my_y + 11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 29*self.size,  self.my_y + 11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 31*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  11*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 12 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  5*self.size,  self.my_y + 12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  7*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y +  12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y +  12*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 16*self.size,  self.my_y +  12*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 19*self.size,  self.my_y +  12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 22*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 24*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 25*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 26*self.size,  self.my_y + 12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  12*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 13 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  5*self.size,  self.my_y + 13*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y +  13*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 17*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 18*self.size,  self.my_y +  13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 23*self.size,  self.my_y +  13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 25*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 26*self.size,  self.my_y + 13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 29*self.size,  self.my_y +  13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  13*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 14 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  5*self.size,  self.my_y +  14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  6*self.size,  self.my_y + 14*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y +  14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y +  14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 14*self.size,  self.my_y +  14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 16*self.size,  self.my_y +  14*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 23*self.size,  self.my_y +  14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 24*self.size,  self.my_y +  14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 25*self.size,  self.my_y + 14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 29*self.size,  self.my_y +  14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y +  14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  14*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 15 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y +  15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  5*self.size,  self.my_y + 15*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y +  15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  15*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  15*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y +  15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y +  15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y +  15*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y +  15*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 24*self.size,  self.my_y +  15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 25*self.size,  self.my_y +  15*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 28*self.size,  self.my_y +  15*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 32*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  15*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 16 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y +  16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  4*self.size,  self.my_y + 16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  6*self.size,  self.my_y +  16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  7*self.size,  self.my_y + 16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  9*self.size,  self.my_y +  16*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 14*self.size,  self.my_y +  16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y +  16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y +  16*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y +  16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  16*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 31*self.size,  self.my_y +  16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 32*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  16*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 17 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  4*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  5*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  6*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  7*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y +  17*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 13*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 15*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 16*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 17*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 18*self.size,  self.my_y +  17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 22*self.size,  self.my_y +  17*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 26*self.size,  self.my_y +  17*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 31*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  17*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 18 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y +  18*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  5*self.size,  self.my_y +  18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  6*self.size,  self.my_y +  18*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y +  18*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 13*self.size,  self.my_y +  18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  18*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 16*self.size,  self.my_y +  18*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 19*self.size,  self.my_y +  18*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 26*self.size,  self.my_y +  18*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 29*self.size,  self.my_y +  18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 30*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 31*self.size,  self.my_y +  18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 32*self.size,  self.my_y +  18*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 19 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  3*self.size,  self.my_y + 19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  5*self.size,  self.my_y + 19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  6*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  7*self.size,  self.my_y +  19*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  19*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 16*self.size,  self.my_y + 19*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 19*self.size,  self.my_y +  19*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 24*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  19*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 28*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 29*self.size,  self.my_y +  19*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 31*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  19*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 20 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y +  20*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  3*self.size,  self.my_y +  20*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y +  20*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y +  20*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 19*self.size,  self.my_y +  20*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y +  20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y +  20*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 28*self.size,  self.my_y +  20*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  20*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 21 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  1*self.size,  self.my_y +  21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  2*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  3*self.size,  self.my_y +  21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y +  21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  5*self.size,  self.my_y +  21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  6*self.size,  self.my_y +  21*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 14*self.size,  self.my_y +  21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y +  21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 16*self.size,  self.my_y + 21*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 19*self.size,  self.my_y +  21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 20*self.size,  self.my_y +  21*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y +  21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y +  21*self.size,  4*self.size, 1*self.size])
    # }}}
    ### 22 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y +  22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  3*self.size,  self.my_y + 22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  4*self.size,  self.my_y +  22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  5*self.size,  self.my_y +  22*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 15*self.size,  self.my_y + 22*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 19*self.size,  self.my_y +  22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  22*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 28*self.size,  self.my_y +  22*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 23 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  0*self.size,  self.my_y +  23*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  2*self.size,  self.my_y + 23*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y +  23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  7*self.size,  self.my_y +  23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y +  23*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 15*self.size,  self.my_y + 23*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 19*self.size,  self.my_y +  23*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y +  23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 23*self.size,  self.my_y +  23*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  23*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 27*self.size,  self.my_y +  23*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y +  23*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 24 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  1*self.size,  self.my_y +  24*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  2*self.size,  self.my_y + 24*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  7*self.size,  self.my_y +  24*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 15*self.size,  self.my_y + 24*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 18*self.size,  self.my_y +  24*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  24*self.size,  9*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  24*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 25 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y +  25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  3*self.size,  self.my_y + 25*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y +  25*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y +  25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x +  9*self.size,  self.my_y + 25*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y +  25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 16*self.size,  self.my_y + 25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 17*self.size,  self.my_y +  25*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 20*self.size,  self.my_y +  25*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 24*self.size,  self.my_y +  25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 25*self.size,  self.my_y +  25*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 27*self.size,  self.my_y +  25*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  25*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 26 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  4*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  5*self.size,  self.my_y +  26*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  7*self.size,  self.my_y +  26*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  9*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 10*self.size,  self.my_y + 26*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 14*self.size,  self.my_y +  26*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 16*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 17*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 18*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 19*self.size,  self.my_y +  26*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 22*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 24*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 25*self.size,  self.my_y + 26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 26*self.size,  self.my_y +  26*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 29*self.size,  self.my_y +  26*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  26*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 27 ### {{{
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  5*self.size,  self.my_y +  27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  6*self.size,  self.my_y +  27*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  9*self.size,  self.my_y +  27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y +  27*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  27*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  27*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y +  27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 24*self.size,  self.my_y +  27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 25*self.size,  self.my_y + 27*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  27*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  27*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 28 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  9*self.size,  self.my_y +  28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 10*self.size,  self.my_y + 28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 11*self.size,  self.my_y +  28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y +  28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  28*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y +  28*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y +  28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 23*self.size,  self.my_y +  28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 24*self.size,  self.my_y + 28*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  28*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  28*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  28*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 29 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  9*self.size,  self.my_y +  29*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 10*self.size,  self.my_y + 29*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 12*self.size,  self.my_y +  29*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 13*self.size,  self.my_y +  29*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  29*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 16*self.size,  self.my_y +  29*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y +  29*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 23*self.size,  self.my_y +  29*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 24*self.size,  self.my_y + 29*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  29*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  29*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  29*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 30 ### {{{
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  9*self.size,  self.my_y +  30*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 10*self.size,  self.my_y + 30*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  30*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y +  30*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y +  30*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 23*self.size,  self.my_y +  30*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 24*self.size,  self.my_y +  30*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 25*self.size,  self.my_y + 30*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  30*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  30*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  30*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 31 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y +  31*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 11*self.size,  self.my_y + 31*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  31*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 16*self.size,  self.my_y +  31*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  31*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y +  31*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 24*self.size,  self.my_y +  31*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 25*self.size,  self.my_y +  31*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_4, [self.my_x + 26*self.size,  self.my_y + 31*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y +  31*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 29*self.size,  self.my_y +  31*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  31*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 32 ### {{{
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 11*self.size,  self.my_y +  32*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y +  32*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  32*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y +  32*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 19*self.size,  self.my_y +  32*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 20*self.size,  self.my_y +  32*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  32*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y +  32*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y +  32*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  32*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 33 ### {{{
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 13*self.size,  self.my_y +  33*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  33*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 18*self.size,  self.my_y +  33*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y +  33*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  33*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 28*self.size,  self.my_y +  33*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  33*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 34 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 17*self.size,  self.my_y +  34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 18*self.size,  self.my_y +  34*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y +  34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 26*self.size,  self.my_y +  34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 27*self.size,  self.my_y +  34*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  34*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 35 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  35*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y +  35*self.size,  3*self.size, 1*self.size])
    # }}}
# }}}

