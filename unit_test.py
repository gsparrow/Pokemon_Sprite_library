# -*- coding: utf-8 -*-
# vim: nu foldmethod=marker maxmem=10000000 
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent ttyfast

import sys
import pygame
import unittest
import pokemon

pygame.init()
WIDTH = 700										# arbitrary values for now
HEIGHT = 700
size = WIDTH, HEIGHT
WHITE      = (255, 255, 255)			      					#a few predefined constant colors
BLACK      = (  0,   0,   0)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)
NEAR_BLACK = ( 25,  16,  16)                                                            #appears to be used rather than black
    

#screen = pygame.display.set_mode(size)
screen = pygame.Surface(size)

done = False
clock = pygame.time.Clock()

class test_Bulbasaur(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Bulbasaur( 0, 0, 0, 0, 1, pokemon.Bulbasaur.get_default_color_0(), pokemon.Bulbasaur.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Bulbasaur')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '001')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Seed Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 28)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 15.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.9)
# }}}

class test_Ivysaur(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Ivysaur( 0, 0, 0, 0, 1, pokemon.Ivysaur.get_default_color_0(), pokemon.Ivysaur.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Ivysaur')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '002')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Seed Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 28.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 13.0)
# }}}

class test_Venasaur(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Venasaur( 0, 0, 0, 0, 1, pokemon.Venasaur.get_default_color_0(), pokemon.Venasaur.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Venasaur')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '003')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Seed Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 79)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 220.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 100.0)
# }}}

class test_Charmander(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Charmander( 0, 0, 0, 0, 1, pokemon.Charmander.get_default_color_0(), pokemon.Charmander.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Charmander')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '004')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Lizard Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 18.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 8.5)
# }}}

class test_Charmeleon(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Charmeleon( 0, 0, 0, 0, 1, pokemon.Charmeleon.get_default_color_0(), pokemon.Charmeleon.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Charmeleon')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '005')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When it swings its burning tail, it elevates the temperature to unbearably high levels.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flame Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 41.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 19.0)
# }}}

class test_Charizard(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Charizard( 0, 0, 0, 0, 1, pokemon.Charizard.get_default_color_0(), pokemon.Charizard.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Charizard')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '006')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flame Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 67)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 199.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 90.5)
# }}}

class test_Squirtle(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Squirtle   (  0, 0, 0, 0, 1, pokemon.Squirtle.get_default_color_0(), pokemon.Squirtle.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Squirtle')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '007')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Tiny Turtle Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 20)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 19.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 9.0)
# }}}

class test_Wartortle(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Wartortle   (  0, 0, 0, 0, 1, pokemon.Wartortle.get_default_color_0(), pokemon.Wartortle.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Wartortle')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '008')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Often hides in water to stalk unwary prey. For swimming fast, it moves its ears to maintain balance.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Turtle Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 49.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 22.5)
# }}}

class test_Blastoise(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Blastoise   (  0, 0, 0, 0, 1, pokemon.Blastoise.get_default_color_0(), pokemon.Blastoise.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Blastoise')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '009')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A brutal Pokémon with pressurized water jets on its shell. They are used for high speed tackles.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Shellfish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 188.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 85.5)
# }}}

class test_Caterpie(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Caterpie( 0, 0, 0, 0, 1, pokemon.Caterpie.get_default_color_0(), pokemon.Caterpie.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Caterpie')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '010')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its short feet are tipped with suction pads that enable it to tirelessly climb slopes and walls.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Worm Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 6.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 2.9)
# }}}

class test_Metapod(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Metapod( 0, 0, 0, 0, 1, pokemon.Metapod.get_default_color_0(), pokemon.Metapod.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Metapod')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '011')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"This Pokémon is vulnerable to attack while its shell is soft, exposing its weak and tender body.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Cocoon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 28)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 21.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 9.9)
# }}}

class test_Butterfree(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Butterfree (  0, 0, 0, 0, 1, pokemon.Butterfree.get_default_color_0(), pokemon.Butterfree.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Butterfree')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '012')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "In battle, it flaps its wings at high speed to release highly toxic dust into the air.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Butterfly Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 70.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 32.0)
# }}}

class test_Weedle(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Weedle( 0, 0, 0, 0, 1, pokemon.Weedle.get_default_color_0(), pokemon.Weedle.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Weedle')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '013')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Often found in forests, eating leaves. It has a sharp venomous stinger on its head.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Hairy Bug Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 7.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 3.2)
# }}}

class test_Kakuna(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Kakuna     (  0, 0, 0, 0, 1, pokemon.Kakuna.get_default_color_0(), pokemon.Kakuna.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Kakuna')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '014')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Almost incapable of moving, this Pokémon can only harden its shell to protect itself from predators.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Cocoon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 22.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 10.0)
# }}}

class test_Beedrill(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Beedrill( 0, 0, 0, 0, 1, pokemon.Beedrill.get_default_color_0(), pokemon.Beedrill.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Beedrill')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '015')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Flies at high speed and attacks using its large venomous stingers on its forelegs and tail.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Bee Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 65.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 29.5)
# }}}

class test_Pidgey(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Pidgey     (  0, 0, 0, 0, 1, pokemon.Pidgey.get_default_color_0(), pokemon.Pidgey.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Pidgey')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '016')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "A common sight in forests and woods. It flaps its wings at ground level to kick up blinding sand.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Tiny Bird Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 4.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 1.8)
# }}}

class test_Pidgeotto(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Pidgeotto     (  0, 0, 0, 0, 1, pokemon.Pidgeotto.get_default_color_0(), pokemon.Pidgeotto.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Pidgeotto')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '017')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Very protective of its sprawling territorial area, this Pokémon will fiercely peck at any intruder.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bird Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 66.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 30.0)
# }}}

class test_Pidgeot(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Pidgeot     (  0, 0, 0, 0, 1, pokemon.Pidgeot.get_default_color_0(), pokemon.Pidgeot.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Pidgeot')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '018')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When hunting, it skims the surface of water at high speed to pick off unwary prey such as Magikarp.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bird Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 87.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 39.5)
# }}}

class test_Rattata(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Rattata    (  0, 0, 0, 0, 1, pokemon.Rattata.get_default_color_0(), pokemon.Rattata.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Rattata')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '019')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Bites anything when it attacks. Small and very quick, it is a common sight in many places.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mouse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 7.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 3.5)
# }}}

class test_Raticate(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Raticate    (  0, 0, 0, 0, 1, pokemon.Raticate.get_default_color_0(), pokemon.Raticate.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Raticate')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '020')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It uses its whiskers to maintain its balance. It apparently slows down if they are cut off.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mouse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 28)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 40.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 18.5)
# }}}

class test_Spearow(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Spearow    (  0, 0, 0, 0, 1, pokemon.Spearow.get_default_color_0(), pokemon.Spearow.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Spearow')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '021')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Eats bugs in grassy areas. It has to flap its short wings at high speed to stay airborne.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Tiny Bird Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 4.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 2.0)
# }}}

class test_Fearow(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Fearow    (  0, 0, 0, 0, 1, pokemon.Fearow.get_default_color_0(), pokemon.Fearow.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Fearow')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '022')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "With its huge and magnificent wings, it can keep aloft without ever having to land for rest.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Beak Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 83.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 38.0)
# }}}

class test_Ekans(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Ekans      (  0, 0, 0, 0, 1, pokemon.Ekans.get_default_color_0(), pokemon.Ekans.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Ekans')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '023')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Moves silently and stealthily. Eats the eggs of birds, such as Pidgey and Spearow, whole.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Snake Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 79)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 15.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.9)
# }}}

class test_Arbok(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Arbok      (  0, 0, 0, 0, 1, pokemon.Arbok.get_default_color_0(), pokemon.Arbok.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Arbok')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '024')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It is rumored that the ferocious warning markings on its belly differ from area to area.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Cobra Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 138)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 3.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 143.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 65.0)
# }}}

class test_Pikachu(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Pikachu    (  0, 0, 0, 0, 1, pokemon.Pikachu.get_default_color_0(), pokemon.Pikachu.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Pikachu')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '025')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"When several of these Pokémon gather, their electricity could build and cause lightning storms.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mouse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 13.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.0)
# }}}

class test_Raichu(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Raichu    (  0, 0, 0, 0, 1, pokemon.Raichu.get_default_color_0(), pokemon.Raichu.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Raichu')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '026')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its long tail serves as a ground to protect itself from its own high voltage power.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mouse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 66.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 30.0)
# }}}

class test_Sandshrew(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Sandshrew  (  0, 0, 0, 0, 1, pokemon.Sandshrew.get_default_color_0(), pokemon.Sandshrew.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Sandshrew')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '027')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Burrows deep underground in arid locations far from water. It only emerges to hunt for food.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mouse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 26.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 12.0)
# }}}

class test_Sandslash(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Sandslash  (  0, 0, 0, 0, 1, pokemon.Sandslash.get_default_color_0(), pokemon.Sandslash.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Sandslash')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '028')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Curls up into a spiny ball when threatened. It can roll while curled up to attack or escape.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mouse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 65.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 29.5)
# }}}

class test_NidoranF(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.NidoranF   (  0, 0, 0, 0, 1, pokemon.NidoranF.get_default_color_0(), pokemon.NidoranF.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), u'Nidoran♀')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '029')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Although small, its venomous barbs render this Pokémon dangerous. The female has smaller horns.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Pin Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 15.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 7.0)
# }}}

class test_Nidorina(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Nidorina   (  0, 0, 0, 0, 1, pokemon.Nidorina.get_default_color_0(), pokemon.Nidorina.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Nidorina')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '030')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The female's horn develops slowly. Prefers physical attacks such as clawing and biting.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Pin Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 44.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 20.0)
# }}}

class test_Nidoqueen(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Nidoqueen  (  0, 0, 0, 0, 1, pokemon.Nidoqueen.get_default_color_0(), pokemon.Nidoqueen.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Nidoqueen')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '031')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its hard scales provide strong protection. It uses its hefty bulk to execute powerful moves.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Drill Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 132.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 60.0)
# }}}

class test_NidoranM(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.NidoranM   (  0, 0, 0, 0, 1, pokemon.NidoranM.get_default_color_0(), pokemon.NidoranM.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), u'Nidoran♂')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '032')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Stiffens its ears to sense danger. The larger its horns, the more powerful its secreted venom.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Pin Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 20)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 19.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 9.0)
# }}}

class test_Nidorino(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Nidorino   (  0, 0, 0, 0, 1, pokemon.Nidorino.get_default_color_0(), pokemon.Nidorino.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Nidorino')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '033')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"An aggressive Pokémon that is quick to attack. The horn on its head secretes a powerful venom.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Pin Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 35)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 43.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 19.5)
# }}}

class test_Nidoking(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Nidoking   (  0, 0, 0, 0, 1, pokemon.Nidoking.get_default_color_0(), pokemon.Nidoking.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Nidoking')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '034')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It uses its powerful tail in battle to smash, constrict, then break the prey's bones.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Drill Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 55)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 136.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 62.0)
# }}}

class test_Clefairy(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Clefairy   (  0, 0, 0, 0, 1, pokemon.Clefairy.get_default_color_0(), pokemon.Clefairy.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Clefairy')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '035')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its magical and cute appeal has many admirers. It is rare and found only in certain areas.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fairy Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 16.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 7.5)
# }}}

class test_Clefable(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Clefable   (  0, 0, 0, 0, 1, pokemon.Clefable.get_default_color_0(), pokemon.Clefable.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Clefable')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '036')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A timid fairy Pokémon that is rarely seen. It will run and hide the moment it senses people.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fairy Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 88.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 40.0)
# }}}

class test_Vulpix(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Vulpix( 0, 0, 0, 0, 1, pokemon.Vulpix.get_default_color_0(), pokemon.Vulpix.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Vulpix')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '037')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "At the time of birth, it has just one tail. The tail splits from its tip as it grows older.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fox Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 21.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 9.9)
# }}}

class test_Ninetails(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Ninetails  (  0, 0, 0, 0, 1, pokemon.Ninetails.get_default_color_0(), pokemon.Ninetails.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Ninetails')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '038')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Very smart and very vengeful. Grabbing one of its many tails could result in a 1000-year curse.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fox Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 43.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 19.9)
# }}}

class test_Jigglypuff(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Jigglypuff (  0, 0, 0, 0, 1, pokemon.Jigglypuff.get_default_color_0(), pokemon.Jigglypuff.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Jigglypuff')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '039')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When its huge eyes light up, it sings a mysteriously soothing melody that lulls its enemies to sleep.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Balloon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 20)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 12.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 5.5)
# }}}

class test_Wigglytuff(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Wigglytuff (  0, 0, 0, 0, 1, pokemon.Wigglytuff.get_default_color_0(), pokemon.Wigglytuff.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Wigglytuff')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '040')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The body is soft and rubbery. When angered, it will suck in air and inflate itself to an enormous size.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Balloon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 26.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 12.0)
# }}}

class test_Zubat(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Zubat      (  0, 0, 0, 0, 1, pokemon.Zubat.get_default_color_0(), pokemon.Zubat.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Zubat')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '041')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Forms colonies in perpetually dark places. Uses ultrasonic waves to identify and approach targets.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bat Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 16.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 7.5)
# }}}

class test_Golbat(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Golbat     (  0, 0, 0, 0, 1, pokemon.Golbat.get_default_color_0(), pokemon.Golbat.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Golbat')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '042')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Once it strikes, it will not stop draining energy from the victim even if it gets too heavy to fly.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bat Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 121.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 55.0)
# }}}

class test_Oddish(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Oddish(  0, 0, 0, 0, 1, pokemon.Oddish.get_default_color_0(), pokemon.Oddish.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Oddish')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '043')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "During the day, it keeps its face buried in the ground. At night, it wanders around sowing its seeds.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Weed Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 20)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 11.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 5.4)
# }}}

class test_Gloom(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Gloom      (  0, 0, 0, 0, 1, pokemon.Gloom.get_default_color_0(), pokemon.Gloom.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Gloom')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '044')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The fluid that oozes from its mouth isn't drool. It is a nectar that is used to attract prey.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Weed Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 19.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 8.6)
# }}}

class test_Vileplume(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Vileplume  (  0, 0, 0, 0, 1, pokemon.Vileplume.get_default_color_0(), pokemon.Vileplume.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Vileplume')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '045')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The larger its petals, the more toxic pollen it contains. Its big head is heavy and hard to hold up.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flower Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 41.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 18.6)
# }}}

class test_Paras(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Paras      (  0, 0, 0, 0, 1, pokemon.Paras.get_default_color_0(), pokemon.Paras.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Paras')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '046')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Burrows to suck tree roots. The mushrooms on its back grow by drawing nutrients from the bug host.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mushroom Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 11.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 5.4)
# }}}

class test_Parasect(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Parasect   (  0, 0, 0, 0, 1, pokemon.Parasect.get_default_color_0(), pokemon.Parasect.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Parasect')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '047')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "A host-parasite pair in which the parasite mushroom has taken over the host bug. Prefers damp places.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mushroom Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 65.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 29.5)
# }}}

class test_Venonat(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Venonat    (  0, 0, 0, 0, 1, pokemon.Venonat.get_default_color_0(), pokemon.Venonat.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Venonat')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '048')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Lives in the shadows of tall trees where it eats insects. It is attracted by light at night.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Insect Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 66.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 30.0)
# }}}

class test_Venomoth(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Venomoth   (  0, 0, 0, 0, 1, pokemon.Venomoth.get_default_color_0(), pokemon.Venomoth.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Venomoth')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '049')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The dust-like scales covering its wings are color coded to indicate the kinds of poison it has.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Moth Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 27.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 12.5)
# }}}

class test_Diglet(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Diglet     (  0, 0, 0, 0, 1, pokemon.Diglet.get_default_color_0(), pokemon.Diglet.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Diglet')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '050')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Lives about one yard underground where it feeds on plant roots. It sometimes appears above ground.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mole Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 8)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 1.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 0.8)
# }}}

class test_Dugtrio(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Dugtrio    (  0, 0, 0, 0, 1, pokemon.Dugtrio.get_default_color_0(), pokemon.Dugtrio.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Dugtrio')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '051')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "A team of Diglett triplets. It triggers huge earthquakes by burrowing 60 miles underground.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mole Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 28)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 73.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 33.3)
# }}}

class test_Meowth(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Meowth     (  0, 0, 0, 0, 1, pokemon.Meowth.get_default_color_0(), pokemon.Meowth.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Meowth')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '052')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Adores circular objects. Wanders the streets on a nightly basis to look for dropped loose change.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Scratch Cat Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 9.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 4.2)
# }}}

class test_Persian(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Persian    (  0, 0, 0, 0, 1, pokemon.Persian.get_default_color_0(), pokemon.Persian.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Persian')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '053')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Although its fur has many admirers, it is tough to raise as a pet because of its fickle meanness.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Classy Cat Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 70.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 32.0)
# }}}

class test_Psyduck(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Psyduck( 0, 0, 0, 0, 1, pokemon.Psyduck.get_default_color_0(), pokemon.Psyduck.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Psyduck')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '054')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "While lulling its enemies with its vacant look, this wily Pokémon will use psychokinetic powers.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Duck Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 43.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 19.6)
# }}}

class test_Golduck(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Golduck    (  0, 0, 0, 0, 1, pokemon.Golduck.get_default_color_0(), pokemon.Golduck.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Golduck')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '055')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Often seen swimming elegantly by lake shores. It is often mistaken for the Japanese monster, Kappa.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Duck Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 67)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 168.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 76.6)
# }}}

class test_Mankey(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Mankey     (  0, 0, 0, 0, 1, pokemon.Mankey.get_default_color_0(), pokemon.Mankey.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Mankey')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '056')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Extremely quick to anger. It could be docile one moment then thrashing away the next instant.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Pig Monkey Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 20)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 61.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 28.0)
# }}}

class test_Primeape(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Primeape   (  0, 0, 0, 0, 1, pokemon.Primeape.get_default_color_0(), pokemon.Primeape.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Primeape')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '057')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Always furious and tenacious to boot. It will not abandon chasing its quarry until it is caught.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Pig Monkey Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 70.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 32.0)
# }}}

class test_Growlithe(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Growlithe  (  0, 0, 0, 0, 1, pokemon.Growlithe.get_default_color_0(), pokemon.Growlithe.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Growlithe')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '058')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Very protective of its territory. It will bark and bite to repel intruders from its space.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Puppy Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 28)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 41.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 19.0)
# }}}

class test_Arcanine(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Arcanine   (  0, 0, 0, 0, 1, pokemon.Arcanine.get_default_color_0(), pokemon.Arcanine.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Arcanine')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '059')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A Pokémon that has been admired since the past for its beauty. It runs agilely as if on wings.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Legendary Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 75)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 341.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 155.0)
# }}}

class test_Poliwag(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Poliwag    (  0, 0, 0, 0, 1, pokemon.Poliwag.get_default_color_0(), pokemon.Poliwag.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Poliwag')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '060')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its newly grown legs prevent it from running. It appears to prefer swimming than trying to stand.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Tadpole Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 27.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 12.4)
# }}}

class test_Poliwhirl(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Poliwhirl  (  0, 0, 0, 0, 1, pokemon.Poliwhirl.get_default_color_0(), pokemon.Poliwhirl.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Poliwhirl')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '061')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Capable of living in or out of water. When out of water, it sweats to keep its body slimy.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Tadpole Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 44.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 20.0)
# }}}

class test_Poliwrath(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Poliwrath  (  0, 0, 0, 0, 1, pokemon.Poliwrath.get_default_color_0(), pokemon.Poliwrath.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Poliwrath')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '062')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "An adept swimmer at both the front crawl and breast stroke. Easily overtakes the best human swimmers.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Tadpole Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 119.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 54.0)
# }}}

class test_Abra(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Abra( 0, 0, 0, 0, 1, pokemon.Abra.get_default_color_0(), pokemon.Abra.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Abra')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '063')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Using its ability to read minds, it will identify impending danger and Teleport to safety.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Psi Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 35)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 43.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 19.5)
# }}}

class test_Kadabra(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Kadabra( 0, 0, 0, 0, 1, pokemon.Kadabra.get_default_color_0(), pokemon.Kadabra.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Kadabra')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '064')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It emits special alpha waves from its body that induce headaches just by being close by.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Psi Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 124.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 56.5)
# }}}

class test_Alakazam(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Alakazam( 0, 0, 0, 0, 1, pokemon.Alakazam.get_default_color_0(), pokemon.Alakazam.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Alakazam')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '065')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its brain can outperform a super-computer. Its intelligence quotient is said to be 5,000.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Psi Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 105.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 48.0)
# }}}

class test_Machop(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Machop     (  0, 0, 0, 0, 1, pokemon.Machop.get_default_color_0(), pokemon.Machop.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Machop')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '066')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Loves to build its muscles. It trains in all styles of martial arts to become even stronger.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Superpower Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 43.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 19.5)
# }}}zo

class test_Machoke(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Machoke    (  0, 0, 0, 0, 1, pokemon.Machoke.get_default_color_0(), pokemon.Machoke.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Machoke')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '067')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its muscular body is so powerful, it must wear a power save belt to be able to regulate its motions.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Superpower Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 155.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 70.5)
# }}}

class test_Machamp(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Machamp    (  0, 0, 0, 0, 1, pokemon.Machamp.get_default_color_0(), pokemon.Machamp.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Machamp')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '068')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Using its heavy muscles, it throws powerful punches that can send the victim clear over the horizon.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Superpower Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 286.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 130.0)
# }}}

class test_Bellsprout(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Bellsprout( 0, 0, 0, 0, 1, pokemon.Bellsprout.get_default_color_0(), pokemon.Bellsprout.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Bellsprout')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '069')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A carnivorous Pokémon that traps and eats bugs. It uses its root feet to soak up needed moisture.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flower Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 28)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 8.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 4.0)
# }}}

class test_Weepinbell(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Weepinbell( 0, 0, 0, 0, 1, pokemon.Weepinbell.get_default_color_0(), pokemon.Weepinbell.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Weepinbell')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '070')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It spits out PoisonPowder to immobilize the enemy and then finishes it with a spray of Acid.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flycatcher Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 14.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.4)
# }}}

class test_Victreebel(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Victreebel( 0, 0, 0, 0, 1, pokemon.Victreebel.get_default_color_0(), pokemon.Victreebel.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Victreebel')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '071')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Said to live in huge colonies deep in jungles, although no one has ever returned from there.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flycatcher Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 67)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 34.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 15.5)
# }}}

class test_Tentacool(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Tentacool  (  0, 0, 0, 0, 1, pokemon.Tentacool.get_default_color_0(), pokemon.Tentacool.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Tentacool')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '072')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Drifts in shallow seas. Anglers who hook them by accident are often punished by its stinging acid.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Jellyfish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 35)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 100.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 45.5)
# }}}

class test_Tentacruel(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Tentacruel (  0, 0, 0, 0, 1, pokemon.Tentacruel.get_default_color_0(), pokemon.Tentacruel.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Tentacruel')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '073')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The tentacles are normally kept short. On hunts, they are extended to ensnare and immobilize prey.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Jellyfish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 121.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 55.0)
# }}}

class test_Geodude(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Geodude    (  0, 0, 0, 0, 1, pokemon.Geodude.get_default_color_0(), pokemon.Geodude.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Geodude')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '074')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Found in fields and mountains. Mistaking them for boulders, people often step or trip on them.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Rock Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 44.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 20.0)
# }}}

class test_Graveler(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Graveler   (  0, 0, 0, 0, 1, pokemon.Graveler.get_default_color_0(), pokemon.Graveler.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Graveler')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '075')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Rolls down slopes to move. It rolls over any obstacle without slowing or changing its direction.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Rock Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 231.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 105.0)
# }}}

class test_Golem(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Golem      (  0, 0, 0, 0, 1, pokemon.Golem.get_default_color_0(), pokemon.Golem.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Golem')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '076')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Megaton Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 55)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 661.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 300.0)
# }}}

class test_Ponyta(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Ponyta( 0, 0, 0, 0, 1, pokemon.Ponyta.get_default_color_0(), pokemon.Ponyta.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Ponyta')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '077')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its hooves are 10 times harder than diamonds. It can trample anything completely flat in little time.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fire Horse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 66.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 30.0)
# }}}

class test_Rapidash(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Rapidash( 0, 0, 0, 0, 1, pokemon.Rapidash.get_default_color_0(), pokemon.Rapidash.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Rapidash')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '078')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Very competitive, this Pokémon will chase anything that moves fast in the hopes of racing it.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fire Horse Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 67)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 209.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 95.0)
# }}}

class test_Slowpoke(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Slowpoke   (  0, 0, 0, 0, 1, pokemon.Slowpoke.get_default_color_0(), pokemon.Slowpoke.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Slowpoke')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '079')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Incredibly slow and dopey. It takes 5 seconds for it to feel pain when under attack.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Dopey Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 79.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 36.0)
# }}}

class test_Slowbro(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Slowbro    (  0, 0, 0, 0, 1, pokemon.Slowbro.get_default_color_0(), pokemon.Slowbro.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Slowbro')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '080')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The Shellder that is latched onto Slowpoke's tail is said to feed on the host's left over scraps.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Hermit Crab Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 173.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 78.5)
# }}}

class test_Magnemite(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Magnemite  (  0, 0, 0, 0, 1, pokemon.Magnemite.get_default_color_0(), pokemon.Magnemite.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Magnemite')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '081')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Uses anti-gravity to stay suspended. Appears without warning and uses Thunder Wave and similar moves.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Magnet Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 13.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.0)
# }}}

class test_Magneton(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Magneton   (  0, 0, 0, 0, 1, pokemon.Magneton.get_default_color_0(), pokemon.Magneton.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Magneton')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '082')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Formed by several Magnemites linked together. They frequently appear when sunspots flare up.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Magnet Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 132.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 60.0)
# }}}

class test_Farfetchd(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Farfetchd  (  0, 0, 0, 0, 1, pokemon.Farfetchd.get_default_color_0(), pokemon.Farfetchd.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Farfetch\'d')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '083')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The sprig of green onions it holds is its weapon. It is used much like a metal sword.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Wild Duck Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 33.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 15.0)
# }}}

class test_Doduo(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Doduo      (  0, 0, 0, 0, 1, pokemon.Doduo.get_default_color_0(), pokemon.Doduo.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Doduo')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '084')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "A bird that makes up for its poor flying with its fast foot speed. Leaves giant footprints.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Twin Bird Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 55)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 86.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 39.2)
# }}}

class test_Dodrio(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Dodrio     (  0, 0, 0, 0, 1, pokemon.Dodrio.get_default_color_0(), pokemon.Dodrio.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Dodrio')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '085')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Uses its three brains to execute complex plans. While two heads sleep, one head stays awake.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Triple Bird Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 71)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 187.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 85.2)
# }}}

class test_Seel(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Seel       (  0, 0, 0, 0, 1, pokemon.Seel.get_default_color_0(), pokemon.Seel.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Seel')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '086')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The protruding horn on its head is very hard. It is used for bashing through thick ice.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Sea Lion Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 198.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 90.0)
# }}}

class test_Dewgong(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Dewgong    (  0, 0, 0, 0, 1, pokemon.Dewgong.get_default_color_0(), pokemon.Dewgong.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Dewgong')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '087')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Stores thermal energy in its body. Swims at a steady 8 knots even in intensely cold waters.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Sea Lion Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 67)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 264.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 120.0)
# }}}

class test_Grimer(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Grimer     (  0, 0, 0, 0, 1, pokemon.Grimer.get_default_color_0(), pokemon.Grimer.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Grimer')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '088')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Appears in filthy areas. Thrives by sucking up polluted sludge that is pumped out of factories.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Sludge Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 35)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 66.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 30.0)
# }}}

class test_Muk(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Muk        (  0, 0, 0, 0, 1, pokemon.Muk.get_default_color_0(), pokemon.Muk.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Muk')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '089')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Thickly covered with a filthy, vile sludge. It is so toxic, even its footprints contain poison.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Sludge Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 66.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 30.0)
# }}}

class test_Shellder(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Shellder   (  0, 0, 0, 0, 1, pokemon.Shellder.get_default_color_0(), pokemon.Shellder.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Shellder')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '090')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its hard shell repels any kind of attack. It is vulnerable only when its shell is open.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bivalve Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 8.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 4.0)
# }}}

class test_Cloyster(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Cloyster   (  0, 0, 0, 0, 1, pokemon.Cloyster.get_default_color_0(), pokemon.Cloyster.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Cloyster')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '091')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When attacked, it launches its horns in quick volleys. Its innards have never been seen.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bivalve Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 292.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 132.5)
# }}}

class test_Gastly(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Gastly     (  0, 0, 0, 0, 1, pokemon.Gastly.get_default_color_0(), pokemon.Gastly.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Gastly')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '092')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Almost invisible, this gaseous Pokémon cloaks the target and puts it to sleep without notice.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Gas Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 0.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 0.1)
# }}}

class test_Haunter(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Haunter    (  0, 0, 0, 0, 1, pokemon.Haunter.get_default_color_0(), pokemon.Haunter.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Haunter')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '093')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Because of its ability to slip through block walls, it is said to be from another dimension.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Gas Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 0.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 0.1)
# }}}

class test_Gengar(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Gengar     (  0, 0, 0, 0, 1, pokemon.Gengar.get_default_color_0(), pokemon.Gengar.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Gengar')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '094')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Under a full moon, this Pokémon likes to mimic the shadows of people and laugh at their fright.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Shadow Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 89.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 40.5)
# }}}

class test_Onix(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Onix       (  0, 0, 0, 0, 1, pokemon.Onix.get_default_color_0(), pokemon.Onix.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Onix')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '095')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "As it grows, the stone portions of its body harden to become similar to a diamond, but colored black.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Rock Snake Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 346)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 8.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 463.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 210.0)
# }}}

class test_Drowzee(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Drowzee( 0, 0, 0, 0, 1, pokemon.Drowzee.get_default_color_0(), pokemon.Drowzee.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Drowzee')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '096')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Puts enemies to sleep then eats their dreams. Occasionally gets sick from eating bad dreams.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Hypnosis Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 71.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 32.4)
# }}}

class test_Hypno(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Hypno( 0, 0, 0, 0, 1, pokemon.Hypno.get_default_color_0(), pokemon.Hypno.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Hypno')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '097')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When it locks eyes with an enemy, it will use a mix of PSI moves such as Hypnosis and Confusion.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Hypnosis Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 166.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 75.6)
# }}}

class test_Krabby(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Krabby     (  0, 0, 0, 0, 1, pokemon.Krabby.get_default_color_0(), pokemon.Krabby.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Krabby')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '098')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its pincers are not only powerful weapons, they are used for balance when walking sideways.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"River Crab Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 14.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.5)
# }}}

class test_Kingler(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Kingler    (  0, 0, 0, 0, 1, pokemon.Kingler.get_default_color_0(), pokemon.Kingler.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Kingler')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '099')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The large pincer has 10000 hp of crushing power. However, its huge size makes it unwieldy to use.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Pincer Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 132.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 60.0)
# }}}

class test_Voltorb(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Voltorb( 0, 0, 0, 0, 1, pokemon.Voltorb.get_default_color_0(), pokemon.Voltorb.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Voltorb')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '100')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Usually found in power plants. Easily mistaken for a Poké Ball, they have zapped many people.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Ball Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 20)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 22.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 10.4)
# }}}

class test_Electrode(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Electrode( 0, 0, 0, 0, 1, pokemon.Electrode.get_default_color_0(), pokemon.Electrode.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Electrode')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '101')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It stores electric energy under very high pressure. It often explodes with little or no provocation.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Ball Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 146.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 66.6)
# }}}

class test_Exeggcute(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Exeggcute  (  0, 0, 0, 0, 1, pokemon.Exeggcute.get_default_color_0(), pokemon.Exeggcute.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Exeggcute')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '102')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Often mistaken for eggs. When disturbed, they quickly gather and attack in swarms.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Egg Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 5.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 2.5)
# }}}

class test_Exeggutor(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Exeggutor( 0, 0, 0, 0, 1, pokemon.Exeggutor.get_default_color_0(), pokemon.Exeggutor.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Exeggutor')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '103')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Legend has it that on rare occasions, one of its heads will drop off and continue on as an Exeggcute.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Coconut Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 79)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 264.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 120.0)
# }}}

class test_Cubone(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Cubone     (  0, 0, 0, 0, 1, pokemon.Cubone.get_default_color_0(), pokemon.Cubone.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Cubone')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '104')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Because it never removes its skull helmet, no one has ever seen this Pokémon's real face.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Lonely Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 14.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.5)
# }}}

class test_Marowak(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Marowak    (  0, 0, 0, 0, 1, pokemon.Marowak.get_default_color_0(), pokemon.Marowak.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Marowak')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '105')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The bone it holds is its key weapon. It throws the bone skillfully like a boomerang to KO targets.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bone Keeper Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 99.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 45.0)
# }}}

class test_Hitmonlee(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Hitmonlee  (  0, 0, 0, 0, 1, pokemon.Hitmonlee.get_default_color_0(), pokemon.Hitmonlee.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Hitmonlee')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '106')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When in a hurry, its legs lengthen progressively. It runs smoothly with extra long, loping strides.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Kicking Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 109.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 49.8)
# }}}

class test_Hitmonchan(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Hitmonchan (  0, 0, 0, 0, 1, pokemon.Hitmonchan.get_default_color_0(), pokemon.Hitmonchan.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Hitmonchan')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '107')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "While apparently doing nothing, it fires punches in lightning fast volleys that are impossible to see.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Punching Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 55)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 110.7)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 50.2)
# }}}

class test_Lickitung(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Lickitung  (  0, 0, 0, 0, 1, pokemon.Lickitung.get_default_color_0(), pokemon.Lickitung.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Lickitung')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '108')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its tongue can be extended like a chameleon's. It leaves a tingling sensation when it licks enemies.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Licking Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 144.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 65.5)
# }}}

class test_Koffing(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Koffing    (  0, 0, 0, 0, 1, pokemon.Koffing.get_default_color_0(), pokemon.Koffing.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Koffing')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '109')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Because it stores several kinds of toxic gases in its body, it is prone to exploding without warning.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Gas Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 2.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 1.0)
# }}}

class test_Weezing(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Weezing    (  0, 0, 0, 0, 1, pokemon.Weezing.get_default_color_0(), pokemon.Weezing.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (222,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Weezing')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '110')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Where two kinds of poison gases meet, 2 Koffings can fuse into a Weezing over many years.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Poison Gas Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 20.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 9.5)
# }}}

class test_Rhyhorn(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Rhyhorn    (  0, 0, 0, 0, 1, pokemon.Rhyhorn.get_default_color_0(), pokemon.Rhyhorn.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Rhyhorn')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '111')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its massive bones are 1000 times harder than human bones. It can easily knock a trailer flying.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Spikes Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 253.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 115.0)
# }}}

class test_Rhydon(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Rhydon     (  0, 0, 0, 0, 1, pokemon.Rhydon.get_default_color_0(), pokemon.Rhydon.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Rhydon')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '112')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Protected by an armor-like hide, it is capable of living in molten lava of 3,600 degrees.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Drill Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 75)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 264.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 120.0)
# }}}

class test_Chansey(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Chansey    (  0, 0, 0, 0, 1, pokemon.Chansey.get_default_color_0(), pokemon.Chansey.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Chansey')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '113')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A rare and elusive Pokémon that is said to bring happiness to those who manage to get it.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Egg Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 76.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 34.6)
# }}}

class test_Tangela(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Tangela    (  0, 0, 0, 0, 1, pokemon.Tangela.get_default_color_0(), pokemon.Tangela.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Tangela')

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '114')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The whole body is swathed with wide vines that are similar to seaweed. Its vines shake as it walks.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Vine Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 77.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 35.0)
# }}}

class test_Kangaskhan(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Kangaskhan (  0, 0, 0, 0, 1, pokemon.Kangaskhan.get_default_color_0(), pokemon.Kangaskhan.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Kangaskhan')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '115')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "The infant rarely ventures out of its mother's protective pouch until it is 3 years old.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Parent Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 87)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 176.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 80.0)
# }}}

class test_Horsea(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Horsea     (  0, 0, 0, 0, 1, pokemon.Horsea.get_default_color_0(), pokemon.Horsea.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Horsea')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '116')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Known to shoot down flying bugs with precision blasts of ink from the surface of the water.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Dragon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 17.6)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 8.0)
# }}}

class test_Seadra(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Seadra     (  0, 0, 0, 0, 1, pokemon.Seadra.get_default_color_0(), pokemon.Seadra.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Seadra')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '117')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Capable of swimming backwards by rapidly flapping its wing-like pectoral fins and stout tail.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Dragon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 47)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 55.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 25.0)
# }}}

class test_Goldeen(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Goldeen    (  0, 0, 0, 0, 1, pokemon.Goldeen.get_default_color_0(), pokemon.Goldeen.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Goldeen')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '118')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its tail fin billows like an elegant ballroom dress, giving it the nickname of the Water Queen.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Goldfish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 24)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 33.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 15.0)
# }}}

class test_Seaking(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Seaking    (  0, 0, 0, 0, 1, pokemon.Seaking.get_default_color_0(), pokemon.Seaking.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Seaking')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '119')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "In the autumn spawning season, they can be seen swimming powerfully up rivers and creeks.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Goldfish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 86.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 39.0)
# }}}

class test_Staryu(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Staryu     (  0, 0, 0, 0, 1, pokemon.Staryu.get_default_color_0(), pokemon.Staryu.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Staryu')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '120')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"An enigmatic Pokémon that can effortlessly regenerate any appendage it loses in battle.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Star Shape Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 76.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 34.5)
# }}}

class test_Starmie(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Starmie    (  0, 0, 0, 0, 1, pokemon.Starmie.get_default_color_0(), pokemon.Starmie.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Starmie')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '121')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its central core glows with the seven colors of the rainbow. Some people value the core as a gem.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mysterious Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 176.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 80.0)
# }}}

class test_Mr_Mime(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Mr_Mime    (  0, 0, 0, 0, 1, pokemon.Mr_Mime.get_default_color_0(), pokemon.Mr_Mime.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Mr. Mime')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '122')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "If interrupted while it is miming, it will slap around the offender with its broad hands.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Barrier Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 120.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 54.5)
# }}}

class test_Scyther(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Scyther( 0, 0, 0, 0, 1, pokemon.Scyther.get_default_color_0(), pokemon.Scyther.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (165,214,132))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (74,165,90))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Scyther')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '123')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "With ninja-like agility and speed, it can create the illusion that there is more than one.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Mantis Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 123.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 56.0)
# }}}

class test_Jynx(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Jynx       (  0, 0, 0, 0, 1, pokemon.Jynx.get_default_color_0(), pokemon.Jynx.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,140))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (132,115,156))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Jynx')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '124')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It seductively wiggles its hips as it walks. It can cause people to dance in unison with it.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Human Shape Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 55)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 89.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 40.6)
# }}}

class test_Electabuzz(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Electabuzz( 0, 0, 0, 0, 1, pokemon.Electabuzz.get_default_color_0(), pokemon.Electabuzz.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Electabuzz')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '125')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Normally found near power plants, they can wander away and cause major blackouts in cities.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Electric Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 43)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 66.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 30.0)
# }}}

class test_Magmar(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Magmar( 0, 0, 0, 0, 1, pokemon.Magmar.get_default_color_0(), pokemon.Magmar.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Magmar')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '126')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its body always burns with an orange glow that enables it to hide perfectly among flames.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Spitfire Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 98.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 44.5)
# }}}

class test_Pinsir(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Pinsir     (  0, 0, 0, 0, 1, pokemon.Pinsir.get_default_color_0(), pokemon.Pinsir.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Pinsir')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '127')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "If it fails to crush the victim in its pincers, it will swing it around and toss it hard.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Stag Beetle Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 59)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 121.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 55.0)
# }}}

class test_Tauros(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Tauros     (  0, 0, 0, 0, 1, pokemon.Tauros.get_default_color_0(), pokemon.Tauros.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Tauros')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '128')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When it targets an enemy, it charges furiously while whipping its body with its long tails.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Wild Bull Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 55)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 194.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 88.4)
# }}}

class test_Magikarp(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Magikarp   (  0, 0, 0, 0, 1, pokemon.Magikarp.get_default_color_0(), pokemon.Magikarp.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,165,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Magikarp')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '129')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "In the distant past, it was somewhat stronger than the horribly weak descendants that exist today.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 35)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 22.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 10.0)
# }}}

class test_Gyrados(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Gyrados    (  0, 0, 0, 0, 1, pokemon.Gyrados.get_default_color_0(), pokemon.Gyrados.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Gyrados')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '130')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Rarely seen in the wild. Huge and vicious, it is capable of destroying entire cities in a rage.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Atrocious Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 256)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 6.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 518.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 235.0)
# }}}

class test_Lapras(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Lapras     (  0, 0, 0, 0, 1, pokemon.Lapras.get_default_color_0(), pokemon.Lapras.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Lapras')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '131')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A Pokémon that has been overhunted almost to extinction. It can ferry people across the water.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Transport Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 98)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 485.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 220.0)
# }}}

class test_Ditto(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Ditto      (  0, 0, 0, 0, 1, pokemon.Ditto.get_default_color_0(), pokemon.Ditto.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Ditto')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '132')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Capable of copying an enemy's genetic code to instantly transform itself into a duplicate of the enemy.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Transform Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 8.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 4.0)
# }}}

class test_Eevee(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Eevee      (  0, 0, 0, 0, 1, pokemon.Eevee.get_default_color_0(), pokemon.Eevee.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Eevee')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '133')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its genetic code is irregular. It may mutate if it is exposed to radiation from element Stones.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Evolution Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 12)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 14.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 6.5)
# }}}

class test_Vaporeon(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Vaporeon   (  0, 0, 0, 0, 1, pokemon.Vaporeon.get_default_color_0(), pokemon.Vaporeon.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (173,206,239))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (115,156,206))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Vaporeon')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '134')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Lives close to water. Its long tail is ridged with a fin which is often mistaken for a mermaid's.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Bubble Jet Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 63.9)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 29.0)
# }}}

class test_Jolteon(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Jolteon( 0, 0, 0, 0, 1, pokemon.Jolteon.get_default_color_0(), pokemon.Jolteon.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Jolteon')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '135')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It accumulates negative ions in the atmosphere to blast out 10000-volt lightning bolts.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Lightning Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 54.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 24.5)
# }}}

class test_Flareon(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Flareon( 0, 0, 0, 0, 1, pokemon.Flareon.get_default_color_0(), pokemon.Flareon.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Flareon')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '136')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "When storing thermal energy in its body, its temperature could soar to over 1600 degrees.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flame Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 35)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.9)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 55.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 25.0)
# }}}

class test_Porygon(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Porygon    (  0, 0, 0, 0, 1, pokemon.Porygon.get_default_color_0(), pokemon.Porygon.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Porygon')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '137')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A Pokémon that consists entirely of programming code. Capable of moving freely in cyberspace.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Virtual Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 31)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 80.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 36.5)
# }}}

class test_Omanyte(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Omanyte    (  0, 0, 0, 0, 1, pokemon.Omanyte.get_default_color_0(), pokemon.Omanyte.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Omanyte')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '138')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Although long extinct, in rare cases, it can be genetically resurrected from fossils.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Spiral Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 16.5)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 7.5)
# }}}

class test_Omastar(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Omastar    (  0, 0, 0, 0, 1, pokemon.Omastar.get_default_color_0(), pokemon.Omastar.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Omastar')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '139')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A prehistoric Pokémon that died out when its heavy shell made it impossible to catch prey.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Spiral Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 39)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 77.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 35.0)
# }}}

class test_Kabuto(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Kabuto     (  0, 0, 0, 0, 1, pokemon.Kabuto.get_default_color_0(), pokemon.Kabuto.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Kabuto')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '140')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A Pokémon that was resurrected from a fossil found in what was once the ocean floor eons ago.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Shellfish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 20)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.5)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 25.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 11.5)
# }}}

class test_Kabutops(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Kabutops   (  0, 0, 0, 0, 1, pokemon.Kabutops.get_default_color_0(), pokemon.Kabutops.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Kabutops')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '141')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Its sleek shape is perfect for swimming. It slashes prey with its claws and drains the body fluids.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Shellfish Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 51)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 89.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 40.5)
# }}}

class test_Aerodactyl(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Aerodactyl (  0, 0, 0, 0, 1, pokemon.Aerodactyl.get_default_color_0(), pokemon.Aerodactyl.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Aerodactyl')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '142')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A ferocious, prehistoric Pokémon that goes for the enemy's throat with its serrated saw-like fangs.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Fossil Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 71)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 130.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 59.0)
# }}}

class test_Snorlax(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Snorlax    (  0, 0, 0, 0, 1, pokemon.Snorlax.get_default_color_0(), pokemon.Snorlax.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,197))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (230,123,173))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Snorlax')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '143')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Very lazy. Just eats and sleeps. As its rotund bulk builds, it becomes steadily more slothful.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Sleeping Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 83)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.1)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 1014.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 460.0)
# }}}

class test_Articuno(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Articuno   (  0, 0, 0, 0, 1, pokemon.Articuno.get_default_color_0(), pokemon.Articuno.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Articuno')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '144')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A legendary bird Pokémon that is said to appear to doomed people who are lost in icy mountains.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Freeze Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 67)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.7)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 122.1)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 55.4)
# }}}

class test_Zapdos(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Zapdos( 0, 0, 0, 0, 1, pokemon.Zapdos.get_default_color_0(), pokemon.Zapdos.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,230,115))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,165,0))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Zapdos')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '145')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A legendary bird Pokémon that is said to appear from clouds while dropping enormous lightning bolts.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Electric Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 63)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.6)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 116.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 52.6)
# }}}

class test_Moltres(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon = pokemon.Moltres( 0, 0, 0, 0, 1, pokemon.Moltres.get_default_color_0(), pokemon.Moltres.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (255,162,82))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (214,82,49))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Moltres')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '146')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "Known as the legendary bird of fire. Every flap of its wings creates a dazzling flash of flames.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Flame Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 79)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 132.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 60.0)
# }}}

class test_Dratini(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Dratini    (  0, 0, 0, 0, 1, pokemon.Dratini.get_default_color_0(), pokemon.Dratini.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (214,173,181))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (123,123,148))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Dratini')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '147')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"Long considered a mythical Pokémon until recently when a small colony was found living underwater.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Dragon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 71)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 1.8)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 7.3)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 3.3)
# }}}

class test_Dragonair(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Dragonair  (  0, 0, 0, 0, 1, pokemon.Dragonair.get_default_color_0(), pokemon.Dragonair.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (148,165,222))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (90,123,189))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Dragonair')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '148')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"A mystical Pokémon that exudes a gentle aura. Has the ability to change climate conditions.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Dragon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 157)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 4.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 36.4)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 16.5)
# }}}

class test_Dragonite(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Dragonite  (  0, 0, 0, 0, 1, pokemon.Dragonite.get_default_color_0(), pokemon.Dragonite.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (230,165,123))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (173,115,74))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Dragonite')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '149')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), u"An extremely rarely seen marine Pokémon. Its intelligence is said to match that of humans.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Dragon Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 87)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.2)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 463.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 210.0)
# }}}

class test_Mewtwo(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Mewtwo     (  0, 0, 0, 0, 1, pokemon.Mewtwo.get_default_color_0(), pokemon.Mewtwo.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,140))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (132,115,156))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Mewtwo')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '150')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "It was created by a scientist after years of horrific gene splicing and DNA engineering experiments.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"Genetic Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 79)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 2.0)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 269.0)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 122.0)
# }}}

class test_Mew(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Mew        (  0, 0, 0, 0, 1, pokemon.Mew.get_default_color_0(), pokemon.Mew.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (247,181,140))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (132,115,156))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (25,16,16))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'Mew')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '151')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "So rare that it is still said to be a mirage by many experts. Only a few people have seen it worldwide.")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u"New Species Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 16)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 0.4)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 8.8)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 4.0)
# }}}

class test_Missingno(unittest.TestCase): # {{{
  def setUp(self):
    self.my_pokemon  = pokemon.Missingno  (  0, 0, 0, 0, 1, pokemon.Missingno.get_default_color_0(), pokemon.Missingno.get_default_color_1(), screen)

  def test_default_color_0(self):
    self.assertEqual(self.my_pokemon.get_default_color_0(), (238,168,126))

  def test_default_color_1(self):
    self.assertEqual(self.my_pokemon.get_default_color_1(), (117,101,142))

  def test_default_color_2(self):
    self.assertEqual(self.my_pokemon.get_default_color_2(), (255,255,255))

  def test_default_color_3(self):
    self.assertEqual(self.my_pokemon.get_default_color_3(), (18,11,11))

  def test_Name(self):
    self.assertEqual(self.my_pokemon.get_Name(), 'MISSINGNO.')

  def test_Pokedex_Number(self):
    self.assertEqual(str(self.my_pokemon.get_Number()).zfill(3), '000')

  def test_Pokedex_Message(self):
    self.assertEqual(self.my_pokemon.get_Pokedex_Message(), "")

  def test_Pokemon_Category(self):
    self.assertEqual(self.my_pokemon.get_Pokemon_Category(), u" ??? Pokémon")

  def test_Pokemon_Height_US(self):
    self.assertEqual(self.my_pokemon.get_Height_US(), 120)

  def test_Pokemon_Height_SI(self):
    self.assertEqual(self.my_pokemon.get_Height_SI(), 3.3)

  def test_Pokemon_Weight_US(self):
    self.assertEqual(self.my_pokemon.get_Weight_US(), 3507.2)

  def test_Pokemon_Weight_SI(self):
    self.assertEqual(self.my_pokemon.get_Weight_SI(), 1590.8)
# }}}

if __name__=='__main__':
  unittest.main()

