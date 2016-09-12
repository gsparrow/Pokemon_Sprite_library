# -*- coding: utf-8 -*-
# vim: nu foldmethod=marker maxmem=10000000 
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent ttyfast


import pygame
from sprites import my_sprite

class Drowzee (my_sprite):
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color0, color1, screen):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.screen = screen
    self.color_0 = color0
    self.color_1 = color1
    self.color_2 = self.get_default_color_2()
    self.color_3 = self.get_default_color_3()
  
  @staticmethod
  def get_default_color_0():
    return (255,230,115)

  @staticmethod
  def get_default_color_1():
    return (214,165,0)

  @staticmethod
  def get_default_color_2():
    return(255,255,255)

  @staticmethod
  def get_default_color_3():
    return(25,16,16)

  def get_color_0(self):
    return self.color_0

  def get_color_1(self):
    return self.color_1

  def get_color_2(self):
    return self.color_2

  def get_color_3(self):
    return self.color_3

  def set_color_0(self, color):
    self.color_0 = color

  def set_color_1(self, color):
    self.color_1 = color

  def set_color_2(self, color):
    self.color_2 = color

  def set_color_3(self, color):
    self.color_3 = color

  def get_Name(self):
    return u"Drowzee"

  def get_Number(self):
    return 96

  def get_Pokedex_Message(self):
    return "Puts enemies to sleep then eats their dreams. Occasionally gets sick from eating bad dreams."
    
  def get_Pokemon_Category(self):
    return u"Hypnosis Pokémon"

  def get_Height_US(self):
    return 39

  def get_Height_SI(self):
    return 1.0

  def get_Weight_US(self):
    return 71.4

  def get_Weight_SI(self):
    return 32.4

  def get_Type_0(self):
    return "Psychic"

  def get_Type_1(self):
    return "Psychic"

  def get_front_height(self):
    return 48*self.size

  def get_front_width(self):
    return 48*self.size

  def draw_front(self): # {{{
    ### 0 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y +  0*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y +  0*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 34*self.size,  self.my_y +  0*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 1 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 14*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 15*self.size,  self.my_y +  1*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 17*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y +  1*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 34*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 35*self.size,  self.my_y +  1*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 2 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y +  2*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 17*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 30*self.size,  self.my_y +  2*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 32*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 33*self.size,  self.my_y +  2*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 3 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y +  3*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 19*self.size,  self.my_y +  3*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 29*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 30*self.size,  self.my_y +  3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 33*self.size,  self.my_y +  3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 35*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 4 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y +  4*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 17*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 19*self.size,  self.my_y +  4*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y +  4*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 29*self.size,  self.my_y +  4*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 31*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y +  4*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y +  4*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 5 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 12*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 16*self.size,  self.my_y +  5*self.size, 11*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 28*self.size,  self.my_y +  5*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 31*self.size,  self.my_y +  5*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y +  5*self.size,  3*self.size, 1*self.size])
    # }}}
    ### 6 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y +  6*self.size, 16*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 31*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 7 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 12*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y +  7*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 19*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 20*self.size,  self.my_y +  7*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 30*self.size,  self.my_y +  7*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  7*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 8 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y +  8*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 18*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 19*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 20*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 21*self.size,  self.my_y +  8*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  8*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 9 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y +  9*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 18*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 19*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 20*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 21*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 22*self.size,  self.my_y +  9*self.size, 11*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y +  9*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 10 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y + 10*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 10*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 18*self.size,  self.my_y + 10*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 21*self.size,  self.my_y + 10*self.size, 13*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y + 10*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 37*self.size,  self.my_y + 10*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 11 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y + 11*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 11*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y + 11*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 20*self.size,  self.my_y + 11*self.size, 14*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y + 11*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 37*self.size,  self.my_y + 11*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 12 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 12*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 15*self.size,  self.my_y + 12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 17*self.size,  self.my_y + 12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 19*self.size,  self.my_y + 12*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y + 12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 24*self.size,  self.my_y + 12*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 29*self.size,  self.my_y + 12*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 35*self.size,  self.my_y + 12*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 38*self.size,  self.my_y + 12*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 13 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 11*self.size,  self.my_y + 13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 16*self.size,  self.my_y + 13*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 22*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 23*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 24*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 25*self.size,  self.my_y + 13*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 29*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 30*self.size,  self.my_y + 13*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 38*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 40*self.size,  self.my_y + 13*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 14 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  5*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y + 14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 14*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 15*self.size,  self.my_y + 14*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y + 14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 23*self.size,  self.my_y + 14*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 29*self.size,  self.my_y + 14*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 34*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 35*self.size,  self.my_y + 14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 37*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 38*self.size,  self.my_y + 14*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 40*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 41*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 42*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 15 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  3*self.size,  self.my_y + 15*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  5*self.size,  self.my_y + 15*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  7*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 15*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y + 15*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 18*self.size,  self.my_y + 15*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y + 15*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 25*self.size,  self.my_y + 15*self.size,  9*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 34*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 35*self.size,  self.my_y + 15*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 38*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 39*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 40*self.size,  self.my_y + 15*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 42*self.size,  self.my_y + 15*self.size,  3*self.size, 1*self.size])
    # }}}
    ### 16 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  1*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  2*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  3*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  4*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  5*self.size,  self.my_y + 16*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  9*self.size,  self.my_y + 16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 16*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 19*self.size,  self.my_y + 16*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 30*self.size,  self.my_y + 16*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 16*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 39*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 40*self.size,  self.my_y + 16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 42*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 43*self.size,  self.my_y + 16*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 45*self.size,  self.my_y + 16*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 17 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  1*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  2*self.size,  self.my_y + 17*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  5*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  6*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  7*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  9*self.size,  self.my_y + 17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y + 17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 16*self.size,  self.my_y + 17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 18*self.size,  self.my_y + 17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y + 17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 22*self.size,  self.my_y + 17*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 29*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 30*self.size,  self.my_y + 17*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 17*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 39*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 40*self.size,  self.my_y + 17*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 42*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 43*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 44*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 45*self.size,  self.my_y + 17*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 18 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  0*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  1*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  2*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y + 18*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  7*self.size,  self.my_y + 18*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  9*self.size,  self.my_y + 18*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 18*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y + 18*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 18*self.size,  self.my_y + 18*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 23*self.size,  self.my_y + 18*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 29*self.size,  self.my_y + 18*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 18*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 42*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 43*self.size,  self.my_y + 18*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 45*self.size,  self.my_y + 18*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 19 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  0*self.size,  self.my_y + 19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  1*self.size,  self.my_y + 19*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  3*self.size,  self.my_y + 19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y + 19*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  9*self.size,  self.my_y + 19*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y + 19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 19*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y + 19*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 17*self.size,  self.my_y + 19*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 23*self.size,  self.my_y + 19*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 28*self.size,  self.my_y + 19*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 31*self.size,  self.my_y + 19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 32*self.size,  self.my_y + 19*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y + 19*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 19*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 44*self.size,  self.my_y + 19*self.size,  3*self.size, 1*self.size])
    # }}}
    ### 20 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  1*self.size,  self.my_y + 20*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  4*self.size,  self.my_y + 20*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  9*self.size,  self.my_y + 20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y + 20*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 12*self.size,  self.my_y + 20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 20*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 18*self.size,  self.my_y + 20*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 22*self.size,  self.my_y + 20*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y + 20*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 26*self.size,  self.my_y + 20*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 29*self.size,  self.my_y + 20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 31*self.size,  self.my_y + 20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 33*self.size,  self.my_y + 20*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 20*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 37*self.size,  self.my_y + 20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 39*self.size,  self.my_y + 20*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 44*self.size,  self.my_y + 20*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 45*self.size,  self.my_y + 20*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 47*self.size,  self.my_y + 20*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 21 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  0*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  1*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y + 21*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  9*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 12*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 17*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 19*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 20*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 21*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 25*self.size,  self.my_y + 21*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 30*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 33*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 35*self.size,  self.my_y + 21*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 40*self.size,  self.my_y + 21*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 45*self.size,  self.my_y + 21*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 47*self.size,  self.my_y + 21*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 22 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  0*self.size,  self.my_y + 22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x +  1*self.size,  self.my_y + 22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  2*self.size,  self.my_y + 22*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 22*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y + 22*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y + 22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 16*self.size,  self.my_y + 22*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y + 22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 22*self.size,  self.my_y + 22*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 25*self.size,  self.my_y + 22*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 28*self.size,  self.my_y + 22*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y + 22*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 33*self.size,  self.my_y + 22*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 41*self.size,  self.my_y + 22*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 46*self.size,  self.my_y + 22*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 23 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  1*self.size,  self.my_y + 23*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y + 23*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 23*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y + 23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y + 23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 15*self.size,  self.my_y + 23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 16*self.size,  self.my_y + 23*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y + 23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 21*self.size,  self.my_y + 23*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y + 23*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 27*self.size,  self.my_y + 23*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 33*self.size,  self.my_y + 23*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 23*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 38*self.size,  self.my_y + 23*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 41*self.size,  self.my_y + 23*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 45*self.size,  self.my_y + 23*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 24 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  3*self.size,  self.my_y + 24*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  4*self.size,  self.my_y + 24*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  6*self.size,  self.my_y + 24*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y + 24*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y + 24*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 12*self.size,  self.my_y + 24*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y + 24*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y + 24*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 19*self.size,  self.my_y + 24*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 21*self.size,  self.my_y + 24*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y + 24*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 25*self.size,  self.my_y + 24*self.size, 11*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y + 24*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 24*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 43*self.size,  self.my_y + 24*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 45*self.size,  self.my_y + 24*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 25 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  5*self.size,  self.my_y + 25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y + 25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  7*self.size,  self.my_y + 25*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y + 25*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y + 25*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 23*self.size,  self.my_y + 25*self.size, 11*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y + 25*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 35*self.size,  self.my_y + 25*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 37*self.size,  self.my_y + 25*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 41*self.size,  self.my_y + 25*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 45*self.size,  self.my_y + 25*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 26 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y + 26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  7*self.size,  self.my_y + 26*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 14*self.size,  self.my_y + 26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y + 26*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 22*self.size,  self.my_y + 26*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y + 26*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 35*self.size,  self.my_y + 26*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 26*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 45*self.size,  self.my_y + 26*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 27 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  6*self.size,  self.my_y + 27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  7*self.size,  self.my_y + 27*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y + 27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 27*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 21*self.size,  self.my_y + 27*self.size, 14*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 35*self.size,  self.my_y + 27*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 36*self.size,  self.my_y + 27*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 38*self.size,  self.my_y + 27*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 44*self.size,  self.my_y + 27*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 28 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  7*self.size,  self.my_y + 28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y + 28*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y + 28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 28*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 21*self.size,  self.my_y + 28*self.size, 13*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y + 28*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y + 28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 38*self.size,  self.my_y + 28*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 39*self.size,  self.my_y + 28*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 42*self.size,  self.my_y + 28*self.size,  2*self.size, 1*self.size])
    # }}}
    ### 29 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y + 29*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y + 29*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y + 29*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 17*self.size,  self.my_y + 29*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 20*self.size,  self.my_y + 29*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 23*self.size,  self.my_y + 29*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 28*self.size,  self.my_y + 29*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y + 29*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 34*self.size,  self.my_y + 29*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 38*self.size,  self.my_y + 29*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 39*self.size,  self.my_y + 29*self.size,  5*self.size, 1*self.size])
    # }}}
    ### 30 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 30*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 18*self.size,  self.my_y + 30*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 20*self.size,  self.my_y + 30*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 22*self.size,  self.my_y + 30*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 23*self.size,  self.my_y + 30*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 28*self.size,  self.my_y + 30*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 29*self.size,  self.my_y + 30*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 32*self.size,  self.my_y + 30*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 33*self.size,  self.my_y + 30*self.size, 11*self.size, 1*self.size])
    # }}}
    ### 31 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y + 31*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 13*self.size,  self.my_y + 31*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 19*self.size,  self.my_y + 31*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 21*self.size,  self.my_y + 31*self.size,  8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 29*self.size,  self.my_y + 31*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 32*self.size,  self.my_y + 31*self.size, 12*self.size, 1*self.size])
    # }}}
    ### 32 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 12*self.size,  self.my_y + 32*self.size, 32*self.size, 1*self.size])
    # }}}
    ### 33 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y + 33*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 14*self.size,  self.my_y + 33*self.size, 23*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 33*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 38*self.size,  self.my_y + 33*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 41*self.size,  self.my_y + 33*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 42*self.size,  self.my_y + 33*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 44*self.size,  self.my_y + 33*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 34 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 11*self.size,  self.my_y + 34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 12*self.size,  self.my_y + 34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 13*self.size,  self.my_y + 34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 14*self.size,  self.my_y + 34*self.size, 22*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 37*self.size,  self.my_y + 34*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 42*self.size,  self.my_y + 34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 43*self.size,  self.my_y + 34*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 44*self.size,  self.my_y + 34*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 35 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y + 35*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y + 35*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y + 35*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 35*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y + 35*self.size, 20*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 35*self.size,  self.my_y + 35*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y + 35*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 38*self.size,  self.my_y + 35*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 39*self.size,  self.my_y + 35*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 43*self.size,  self.my_y + 35*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 44*self.size,  self.my_y + 35*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 36 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 36*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y + 36*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 36*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y + 36*self.size, 20*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 35*self.size,  self.my_y + 36*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y + 36*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 36*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 38*self.size,  self.my_y + 36*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 39*self.size,  self.my_y + 36*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 40*self.size,  self.my_y + 36*self.size,  5*self.size, 1*self.size])
    # }}}
    ### 37 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  9*self.size,  self.my_y + 37*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 37*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 13*self.size,  self.my_y + 37*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 37*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y + 37*self.size, 19*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y + 37*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 37*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 37*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 37*self.size,  self.my_y + 37*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 40*self.size,  self.my_y + 37*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 41*self.size,  self.my_y + 37*self.size,  4*self.size, 1*self.size])
    # }}}
    ### 38 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  9*self.size,  self.my_y + 38*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y + 38*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y + 38*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 16*self.size,  self.my_y + 38*self.size, 18*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 34*self.size,  self.my_y + 38*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 38*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 38*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 38*self.size,  self.my_y + 38*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 39*self.size,  self.my_y + 38*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 40*self.size,  self.my_y + 38*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 45*self.size,  self.my_y + 38*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 39 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  9*self.size,  self.my_y + 39*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 39*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 14*self.size,  self.my_y + 39*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 15*self.size,  self.my_y + 39*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 16*self.size,  self.my_y + 39*self.size, 18*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 34*self.size,  self.my_y + 39*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 39*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 38*self.size,  self.my_y + 39*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 39*self.size,  self.my_y + 39*self.size,  7*self.size, 1*self.size])
    # }}}
    ### 40 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 40*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 15*self.size,  self.my_y + 40*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 16*self.size,  self.my_y + 40*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 17*self.size,  self.my_y + 40*self.size, 17*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 34*self.size,  self.my_y + 40*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 40*self.size, 11*self.size, 1*self.size])
    # }}}
    ### 41 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y + 41*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y + 41*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 16*self.size,  self.my_y + 41*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 17*self.size,  self.my_y + 41*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 19*self.size,  self.my_y + 41*self.size, 15*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 34*self.size,  self.my_y + 41*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 41*self.size, 11*self.size, 1*self.size])
    # }}}
    ### 42 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y + 42*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 17*self.size,  self.my_y + 42*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 19*self.size,  self.my_y + 42*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 21*self.size,  self.my_y + 42*self.size, 14*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 35*self.size,  self.my_y + 42*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 36*self.size,  self.my_y + 42*self.size, 10*self.size, 1*self.size])
    # }}}
    ### 43 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 43*self.size,  9*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 19*self.size,  self.my_y + 43*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 21*self.size,  self.my_y + 43*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 24*self.size,  self.my_y + 43*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 43*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 37*self.size,  self.my_y + 43*self.size,  9*self.size, 1*self.size])
    # }}}
    ### 44 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  9*self.size,  self.my_y + 44*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 10*self.size,  self.my_y + 44*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 11*self.size,  self.my_y + 44*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 12*self.size,  self.my_y + 44*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 14*self.size,  self.my_y + 44*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 21*self.size,  self.my_y + 44*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 24*self.size,  self.my_y + 44*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 27*self.size,  self.my_y + 44*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 37*self.size,  self.my_y + 44*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 40*self.size,  self.my_y + 44*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 41*self.size,  self.my_y + 44*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 45*self.size,  self.my_y + 44*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 46*self.size,  self.my_y + 44*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 45 ### {{{
    pygame.draw.rect(self.screen, self.color_1, [self.my_x +  8*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  9*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 11*self.size,  self.my_y + 45*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y + 45*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y + 45*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 30*self.size,  self.my_y + 45*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 45*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 38*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 39*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 40*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 41*self.size,  self.my_y + 45*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 44*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 45*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 46*self.size,  self.my_y + 45*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 46 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x +  9*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 10*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 11*self.size,  self.my_y + 46*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 14*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 15*self.size,  self.my_y + 46*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 27*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 28*self.size,  self.my_y + 46*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 33*self.size,  self.my_y + 46*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 36*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 37*self.size,  self.my_y + 46*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 39*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 40*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_2, [self.my_x + 41*self.size,  self.my_y + 46*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_0, [self.my_x + 45*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 46*self.size,  self.my_y + 46*self.size,  1*self.size, 1*self.size])
    # }}}
    ### 47 ### {{{
    pygame.draw.rect(self.screen, self.color_3, [self.my_x +  8*self.size,  self.my_y + 47*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_1, [self.my_x + 20*self.size,  self.my_y + 47*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.color_3, [self.my_x + 35*self.size,  self.my_y + 47*self.size, 12*self.size, 1*self.size])
    # }}} }}}
