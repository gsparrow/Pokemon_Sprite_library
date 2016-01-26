# -*- coding: utf-8 -*-
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
WHITE      = (255, 255, 255)			      					#a few predefined constant colors
BLACK      = (  0,   0,   0)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)
NEAR_BLACK = ( 25,  16,  16)                                                            #appears to be used rather than black
    

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Gotta Catch 'Em All")

done = False
clock = pygame.time.Clock()

#pokemon  = sprites.Bulbasaur  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Ivysaur    (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Venasaur   (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Charmander (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49), (255,162,82), WHITE, screen)
#pokemon  = sprites.Charmeleon (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49), (255,162,82), WHITE, screen)
#pokemon  = sprites.Charizard  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49), (255,162,82), WHITE, screen)
#pokemon  = sprites.Squirtle   (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#pokemon  = sprites.Wartortle  (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#pokemon  = sprites.Blastoise  (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
# TODO  10 - Caterpie
# TODO  11 - Metapod
# TODO  12 - Butterfree
# TODO  13 - Weedle
# TODO  14 - Kakuna
# TODO  15 - Beedrill
# TODO  16 - Pidgey
# TODO  17 - Pidgeotto
# TODO  18 - Pidgeot
# TODO  19 - Rattata
# TODO  20 - Raticate
# TODO  21 - Spearow
# TODO  22 - Fearow
# TODO  23 - Ekans
# TODO  24 - Arbok
#pokemon  = sprites.Pikachu  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#pokemon  = sprites.Raichu  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
# TODO  27 - Sandshrew
# TODO  28 - Sandslash
# TODO  29 - Nidoran♀
# TODO  30 - Nidorina
# TODO  31 - Nidoqueen
# TODO  32 - Nidoran♂
# TODO  33 - Nidorino
# TODO  34 - Nidoking
# TODO  35 - Clefairy
# TODO  36 - Clefable
# TODO  37 - Vulpix
# TODO  38 - Ninetails
# TODO  39 - Jigglypuff
# TODO  40 - Wigglytuff
# TODO  41 - Zubat
# TODO  42 - Golbat
#pokemon  = sprites.Oddish    (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Gloom     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49), (255,165,82), WHITE, screen)
#pokemon  = sprites.Vileplume (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49), (255,165,82), WHITE, screen)
# TODO  46 - Paras
# TODO  47 - Parasect
#pokemon  = sprites.Venonat   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Venomoth  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
# TODO  50 - Diglet
# TODO  51 - Dugtrio
# TODO  52 - Meowth
# TODO  53 - Persian
# TODO  54 - Psyduck
# TODO  55 - Golduck
# TODO  56 - Mankey
# TODO  57 - Primeape
# TODO  58 - Growlithe
# TODO  59 - Arcanine
# TODO  60 - Poliwag
# TODO  61 - Poliwhirl
# TODO  62 - Poliwrath
#pokemon  = sprites.Abra     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#pokemon  = sprites.Kadabra  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#pokemon  = sprites.Alakazam (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
# TODO  66 - Machop
# TODO  67 - Machoke
# TODO  68 - Machamp
# TODO  69 - Bellsprout
#pokemon  = sprites.Bellsprout  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Weepinbell  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Victreebel  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
# TODO  72 - Tentacool
# TODO  73 - Tentacruel
#pokemon  = sprites.Geodude   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Graveler  (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Golem     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO  77 - Ponyta
# TODO  78 - Rapidash
# TODO  79 - Slowpoke
# TODO  80 - Slowbro
# TODO  81 - Magnemite
# TODO  82 - Magneton
# TODO  83 - Farfetch'd
# TODO  84 - Doduo
# TODO  85 - Dodrio
# TODO  86 - Seel
# TODO  87 - Dewgong
# TODO  88 - Grimer
# TODO  89 - Muk
# TODO  90 - Shellder
# TODO  91 - Cloyster
# TODO  92 - Ghastly
# TODO  93 - Haunter
# TODO  94 - Gengar
#pokemon  = sprites.Onix       (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO  96 - Drowzee
# TODO  97 - Hypno
# TODO  98 - Krabby
# TODO  99 - Kingler
#pokemon  = sprites.Voltorb    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#pokemon  = sprites.Electrode  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
# TODO 102 - Exeggcute
# TODO 103 - Exeggutor
#pokemon  = sprites.Cubone     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Marowak    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO 106 - Hitmonlee
# TODO 107 - Hitmonchan
# TODO 108 - Lickitung
pokemon  = sprites.Koffing    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
# TODO 110 - Weezing
# TODO 111 - Rhyhorn
# TODO 112 - Rhydon
# TODO 113 - Chansey
#pokemon  = sprites.Tangela    (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189), (148,165,222), WHITE, screen)
# TODO 115 - Kangaskhan
# TODO 116 - Horsea
# TODO 117 - Seadra
# TODO 118 - Goldeen
# TODO 119 - Seaking
# TODO 120 - Staryu
#pokemon  = sprites.Staryu    (  0, 0, 0, 0, 1, NEAR_BLACK, (255,165,82), (214,82,49), WHITE, screen)
#pokemon  = sprites.Starmie   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Mr_Mime     (  0, 0, 0, 0, 1, NEAR_BLACK, (247,181,197), (230,123,173), WHITE, screen)
# TODO 123 - Scyther
# TODO 124 - Jynx
# TODO 125 - Electabuzz
# TODO 126 - Magmar
# TODO 127 - Pinsir
# TODO 128 - Tauros
# TODO 129 - Magikarp
# TODO 130 - Gyrados
# TODO 131 - Lapras
#pokemon  = sprites.Ditto      (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO 133 - Evee
# TODO 134 - Vaporeon
# TODO 135 - Jolteon
# TODO 136 - Flareon
# TODO 137 - Porygon
# TODO 138 - Omanyte
# TODO 139 - Omastar
# TODO 140 - Kabuto
# TODO 141 - Kabutops
# TODO 142 - Aerodactyl
# TODO 143 - Snorlax
# TODO 144 - Articuno
# TODO 145 - Zapdos
# TODO 146 - Moltres
# TODO 147 - Dratini
# TODO 148 - Dragonair
# TODO 149 - Dragonite
#pokemon  = sprites.Mewtwo     (  0, 0, 0, 0, 1, NEAR_BLACK, (132,115,156), (247,181,140), WHITE, screen)
#pokemon  = sprites.Mew        (  0, 0, 0, 0, 1, NEAR_BLACK, (132,115,156), (247,181,140), WHITE, screen)
# TODO Missingno
											#set sprite at location x,y, with velocity x,y,
											#with size multiplier 1,  with the following four colors
											#on the main screen
print pokemon.get_Name()
print str(pokemon.get_Number()).zfill(3)
print pokemon.get_Pokedex_Message()
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
