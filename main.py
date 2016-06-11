# -*- coding: utf-8 -*-
# vim: nu
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent

#!/usr/bin/python

import sys
import pygame
import pokemon
import items

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
    

icon = pygame.Surface((24,24))
icon.fill(BLUE)
my_icon = items.Pokeball (0, 0, 0, 0, 1, NEAR_BLACK, WHITE, (255,123,123), icon)
my_icon.draw()
pygame.display.set_icon(icon)
pygame.display.set_caption("Gotta Catch 'Em All")
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

#my_pokemon  = items.Pokeball     (  0, 0, 0, 0, 1, NEAR_BLACK, WHITE,         (255,123,123),        screen)
#my_pokemon  = pokemon.Bulbasaur  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Ivysaur    (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Venasaur   (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Charmander (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#my_pokemon  = pokemon.Charmeleon (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#my_pokemon  = pokemon.Charizard  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#my_pokemon  = pokemon.Squirtle   (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#my_pokemon  = pokemon.Wartortle  (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#my_pokemon  = pokemon.Blastoise  (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#my_pokemon  = pokemon.Caterpie   (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Metapod    (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Butterfree (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#my_pokemon  = pokemon.Weedle     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Kakuna     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Beedrill   (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Pidgey     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Pidgeotto  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Pidgeot    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Rattata    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Raticate   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Spearow    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Fearow     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Ekans      (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Arbok      (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Pikachu    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Raichu     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Sandshrew  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Sandslash  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.NidoranF   (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.Nidorina   (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.Nidoqueen  (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.NidoranM   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Nidorino   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Nidoking   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Clefairy   (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197), WHITE, screen)
#my_pokemon  = pokemon.Clefable   (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197), WHITE, screen)
#my_pokemon  = pokemon.Vulpix     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#my_pokemon  = pokemon.Ninetails  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Jigglypuff (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197), WHITE, screen)
#my_pokemon  = pokemon.Wigglytuff (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197), WHITE, screen)
#my_pokemon  = pokemon.Zubat      (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.Golbat     (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.Oddish     (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Gloom      (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,165,82),  WHITE, screen)
#my_pokemon  = pokemon.Vileplume  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,165,82),  WHITE, screen)
#my_pokemon  = pokemon.Paras      (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,165,82),  WHITE, screen)
#my_pokemon  = pokemon.Parasect   (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,165,82),  WHITE, screen)
#my_pokemon  = pokemon.Venonat    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Venomoth   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Diglet     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Dugtrio    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Meowth     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Persian    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Psyduck    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Golduck    (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#my_pokemon  = pokemon.Mankey     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Primeape   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Growlithe  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Arcanine   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (255,165,82),  WHITE, screen)
#my_pokemon  = pokemon.Poliwag    (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.Poliwhirl  (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.Poliwrath  (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#my_pokemon  = pokemon.Abra       (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Kadabra    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Alakazam   (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Machop     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Machoke    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Machamp    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Bellsprout (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Weepinbell (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Victreebel (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#my_pokemon  = pokemon.Tentacool  (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#my_pokemon  = pokemon.Tentacruel (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#my_pokemon  = pokemon.Geodude    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Graveler   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Golem      (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Ponyta     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#my_pokemon  = pokemon.Rapidash   (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#my_pokemon  = pokemon.Slowpoke   (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197), WHITE, screen)
#my_pokemon  = pokemon.Slowbro    (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197),  WHITE, screen)
#my_pokemon  = pokemon.Magnemite  (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Magneton   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Farfetchd  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Doduo      (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Dodrio     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#my_pokemon  = pokemon.Seel       (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
my_pokemon  = pokemon.Dewgong    (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
# TODO  88 - Grimer
# TODO  89 - Muk
# TODO  90 - Shellder
# TODO  91 - Cloyster
#my_pokemon  = pokemon.Gastly     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Haunter    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Gengar     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Onix       (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO  96 - Drowzee
# TODO  97 - Hypno
# TODO  98 - Krabby
# TODO  99 - Kingler
#my_pokemon  = pokemon.Voltorb    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#my_pokemon  = pokemon.Electrode  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
# TODO 102 - Exeggcute
# TODO 103 - Exeggutor
#my_pokemon  = pokemon.Cubone     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Marowak    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO 106 - Hitmonlee
# TODO 107 - Hitmonchan
# TODO 108 - Lickitung
#my_pokemon  = pokemon.Koffing    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#my_pokemon  = pokemon.Weezing    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
# TODO 111 - Rhyhorn
# TODO 112 - Rhydon
# TODO 113 - Chansey
#my_pokemon  = pokemon.Tangela    (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189), (148,165,222), WHITE, screen)
# TODO 115 - Kangaskhan
# TODO 116 - Horsea
# TODO 117 - Seadra
# TODO 118 - Goldeen
# TODO 119 - Seaking
#my_pokemon  = pokemon.Staryu    (  0, 0, 0, 0, 1, NEAR_BLACK, (255,165,82), (214,82,49), WHITE, screen)
#my_pokemon  = pokemon.Starmie   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#my_pokemon  = pokemon.Mr_Mime   (  0, 0, 0, 0, 1, NEAR_BLACK, (247,181,197), (230,123,173), WHITE, screen)
# TODO 123 - Scyther
# TODO 124 - Jynx
# TODO 125 - Electabuzz
# TODO 126 - Magmar
# TODO 127 - Pinsir
#my_pokemon  = pokemon.Tauros    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO 129 - Magikarp
# TODO 130 - Gyrados
# TODO 131 - Lapras
#my_pokemon  = pokemon.Ditto     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
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
#my_pokemon  = pokemon.Mewtwo     (  0, 0, 0, 0, 1, NEAR_BLACK, (132,115,156), (247,181,140), WHITE, screen)
#my_pokemon  = pokemon.Mew        (  0, 0, 0, 0, 1, NEAR_BLACK, (132,115,156), (247,181,140), WHITE, screen)
#my_pokemon  = pokemon.Missingno  (  0, 0, 0, 0, 1, NEAR_BLACK, WHITE, screen)
											#set sprite at location x,y, with velocity x,y,
											#with size multiplier 1,  with the following four colors
											#on the main screen
print my_pokemon.get_Name()
print str(my_pokemon.get_Number()).zfill(3)
print my_pokemon.get_Pokedex_Message()
while not done:

  #limit the clock to ten loops per second
  clock.tick(3)

  for event in pygame.event.get():							#allows you to exit by clicking x
    if event.type == pygame.QUIT:
      done =True

  screen.fill(RED)									#arbitrary color, good for spotting mistakes in the sprite

  my_pokemon.draw()

  pygame.display.flip()

pygame.quit()
