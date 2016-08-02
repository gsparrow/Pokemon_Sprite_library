# -*- coding: utf-8 -*-
# vim: nu foldmethod=marker
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent

#!/usr/bin/python

import sys
import pygame
import items

#below are the imports of every individual pokemon from pokemon.py # {{{
from pokemon import Bulbasaur
from pokemon import Ivysaur
from pokemon import Venasaur
from pokemon import Charmander
from pokemon import Charmeleon
from pokemon import Charizard
from pokemon import Squirtle
from pokemon import Wartortle
from pokemon import Blastoise
from pokemon import Caterpie
from pokemon import Metapod
from pokemon import Butterfree
from pokemon import Weedle
from pokemon import Kakuna
from pokemon import Beedrill
from pokemon import Pidgey
from pokemon import Pidgeotto
from pokemon import Pidgeot
from pokemon import Rattata
from pokemon import Raticate
from pokemon import Spearow
from pokemon import Fearow
from pokemon import Ekans
from pokemon import Arbok
from pokemon import Pikachu
from pokemon import Raichu
from pokemon import Sandshrew
from pokemon import Sandslash
from pokemon import NidoranF
from pokemon import Nidorina
from pokemon import Nidoqueen
from pokemon import NidoranM
from pokemon import Nidorino
from pokemon import Nidoking
from pokemon import Clefairy
from pokemon import Clefable
from pokemon import Vulpix
from pokemon import Ninetails
from pokemon import Jigglypuff
from pokemon import Wigglytuff
from pokemon import Zubat
from pokemon import Golbat
from pokemon import Oddish
from pokemon import Gloom
from pokemon import Vileplume
from pokemon import Paras
from pokemon import Parasect
from pokemon import Venonat
from pokemon import Venomoth
from pokemon import Diglet
from pokemon import Dugtrio
from pokemon import Meowth
from pokemon import Persian
from pokemon import Psyduck
from pokemon import Golduck
from pokemon import Mankey
from pokemon import Primeape
from pokemon import Growlithe
from pokemon import Arcanine
from pokemon import Poliwag
from pokemon import Poliwhirl
from pokemon import Poliwrath
from pokemon import Abra
from pokemon import Kadabra
from pokemon import Alakazam
from pokemon import Machop
from pokemon import Machoke
from pokemon import Machamp
from pokemon import Bellsprout
from pokemon import Weepinbell
from pokemon import Victreebel
from pokemon import Tentacool
from pokemon import Tentacruel
from pokemon import Geodude
from pokemon import Graveler
from pokemon import Golem
from pokemon import Ponyta
from pokemon import Rapidash
from pokemon import Slowpoke
from pokemon import Slowbro
from pokemon import Magnemite
from pokemon import Magneton
from pokemon import Farfetchd
from pokemon import Doduo
from pokemon import Dodrio
from pokemon import Seel
from pokemon import Dewgong
from pokemon import Grimer
from pokemon import Muk
from pokemon import Shellder
from pokemon import Cloyster
from pokemon import Gastly
from pokemon import Haunter
from pokemon import Gengar
from pokemon import Onix
from pokemon import Drowzee
from pokemon import Hypno
from pokemon import Krabby
from pokemon import Kingler
from pokemon import Voltorb
from pokemon import Electrode
from pokemon import Exeggcute
from pokemon import Exeggutor
from pokemon import Cubone
from pokemon import Marowak
from pokemon import Hitmonlee
from pokemon import Hitmonchan
from pokemon import Lickitung
from pokemon import Koffing
from pokemon import Weezing
from pokemon import Rhyhorn
from pokemon import Rhydon
from pokemon import Chansey
from pokemon import Tangela
from pokemon import Kangaskhan
from pokemon import Horsea
from pokemon import Seadra
from pokemon import Goldeen
from pokemon import Seaking
from pokemon import Staryu
from pokemon import Starmie
from pokemon import Mr_Mime
from pokemon import Scyther
from pokemon import Jynx
from pokemon import Electabuzz
from pokemon import Magmar
from pokemon import Pinsir
from pokemon import Tauros
from pokemon import Magikarp
from pokemon import Gyrados
from pokemon import Lapras
from pokemon import Ditto
from pokemon import Eevee
from pokemon import Vaporeon
from pokemon import Jolteon
from pokemon import Flareon
from pokemon import Porygon
from pokemon import Omanyte
from pokemon import Omastar
from pokemon import Kabuto
from pokemon import Kabutops
from pokemon import Aerodactyl
from pokemon import Snorlax
from pokemon import Articuno
from pokemon import Zapdos
from pokemon import Moltres
from pokemon import Dratini
from pokemon import Dragonair
from pokemon import Dragonite
from pokemon import Mewtwo
from pokemon import Mew
from pokemon import Missingno
# }}}


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
#my_pokemon  = Bulbasaur  (  0, 0, 0, 0, 1, Bulbasaur.get_default_color_0(), Bulbasaur.get_default_color_1(), screen)
#my_pokemon  = Ivysaur    (  0, 0, 0, 0, 1, Ivysaur.get_default_color_0(),   Ivysaur.get_default_color_1(),   screen)
#my_pokemon  = Venasaur   (  0, 0, 0, 0, 1, Venasaur.get_default_color_0(),  Venasaur.get_default_color_1(),  screen)
#my_pokemon  = Charmander (  0, 0, 0, 0, 1, Charmander.get_default_color_0(), Charmander.get_default_color_1(), screen)
#my_pokemon  = Charmeleon (  0, 0, 0, 0, 1, Charmeleon.get_default_color_0(), Charmeleon.get_default_color_1(), screen)
#my_pokemon  = Charizard  (  0, 0, 0, 0, 1, Charizard.get_default_color_0(), Charizard.get_default_color_1(), screen)
#my_pokemon  = Squirtle   (  0, 0, 0, 0, 1, Squirtle.get_default_color_0(), Squirtle.get_default_color_1(), screen)
#my_pokemon  = Wartortle  (  0, 0, 0, 0, 1, Wartortle.get_default_color_0(), Wartortle.get_default_color_1(), screen)
#my_pokemon  = Blastoise  (  0, 0, 0, 0, 1, Blastoise.get_default_color_0(), Blastoise.get_default_color_1(), screen)
#my_pokemon  = Caterpie   (  0, 0, 0, 0, 1, Caterpie.get_default_color_0(), Caterpie.get_default_color_1(), screen)
#my_pokemon  = Metapod    (  0, 0, 0, 0, 1, Metapod.get_default_color_0(), Metapod.get_default_color_1(), screen)
#my_pokemon  = Butterfree (  0, 0, 0, 0, 1, Butterfree.get_default_color_0(), Butterfree.get_default_color_1(), screen)
#my_pokemon  = Weedle     (  0, 0, 0, 0, 1, Weedle.get_default_color_0(), Weedle.get_default_color_1(), screen)
#my_pokemon  = Kakuna     (  0, 0, 0, 0, 1, Kakuna.get_default_color_0(), Kakuna.get_default_color_1(), screen)
#my_pokemon  = Beedrill   (  0, 0, 0, 0, 1, Beedrill.get_default_color_0(), Beedrill.get_default_color_1(), screen)
#my_pokemon  = Pidgey     (  0, 0, 0, 0, 1, Pidgey.get_default_color_0(), Pidgey.get_default_color_1(), screen)
#my_pokemon  = Pidgeotto  (  0, 0, 0, 0, 1, Pidgeotto.get_default_color_0(), Pidgeotto.get_default_color_1(), screen)
#my_pokemon  = Pidgeot    (  0, 0, 0, 0, 1, Pidgeot.get_default_color_0(), Pidgeot.get_default_color_1(), screen)
#my_pokemon  = Rattata    (  0, 0, 0, 0, 1, Rattata.get_default_color_0(), Rattata.get_default_color_1(), screen)
#my_pokemon  = Raticate   (  0, 0, 0, 0, 1, Raticate.get_default_color_0(), Raticate.get_default_color_1(), screen)
#my_pokemon  = Spearow    (  0, 0, 0, 0, 1, Spearow.get_default_color_0(), Spearow.get_default_color_1(), screen)
#my_pokemon  = Fearow     (  0, 0, 0, 0, 1, Fearow.get_default_color_0(), Fearow.get_default_color_1(), screen)
#my_pokemon  = Ekans      (  0, 0, 0, 0, 1, Ekans.get_default_color_0(), Ekans.get_default_color_1(), screen)
#my_pokemon  = Arbok      (  0, 0, 0, 0, 1, Arbok.get_default_color_0(), Arbok.get_default_color_1(), screen)
#my_pokemon  = Pikachu    (  0, 0, 0, 0, 1, Pikachu.get_default_color_0(), Pikachu.get_default_color_1(), screen)
#my_pokemon  = Raichu     (  0, 0, 0, 0, 1, Raichu.get_default_color_0(), Raichu.get_default_color_1(), screen)
#my_pokemon  = Sandshrew  (  0, 0, 0, 0, 1, Sandshrew.get_default_color_0(), Sandshrew.get_default_color_1(), screen)
#my_pokemon  = Sandslash  (  0, 0, 0, 0, 1, Sandslash.get_default_color_0(), Sandslash.get_default_color_1(), screen)
#my_pokemon  = NidoranF   (  0, 0, 0, 0, 1, NidoranF.get_default_color_0(), NidoranF.get_default_color_1(), screen)
#my_pokemon  = Nidorina   (  0, 0, 0, 0, 1, Nidorina.get_default_color_0(), Nidorina.get_default_color_1(), screen)
#my_pokemon  = Nidoqueen  (  0, 0, 0, 0, 1, Nidoqueen.get_default_color_0(), Nidoqueen.get_default_color_1(), screen)
#my_pokemon  = NidoranM   (  0, 0, 0, 0, 1, NidoranM.get_default_color_0(), NidoranM.get_default_color_1(), screen)
#my_pokemon  = Nidorino   (  0, 0, 0, 0, 1, Nidorino.get_default_color_0(), Nidorino.get_default_color_1(), screen)
#my_pokemon  = Nidoking   (  0, 0, 0, 0, 1, Nidoking.get_default_color_0(), Nidoking.get_default_color_1(), screen)
#my_pokemon  = Clefairy   (  0, 0, 0, 0, 1, Clefairy.get_default_color_0(), Clefairy.get_default_color_1(), screen)
#my_pokemon  = Clefable   (  0, 0, 0, 0, 1, Clefable.get_default_color_0(), Clefable.get_default_color_1(), screen)
#my_pokemon  = Vulpix     (  0, 0, 0, 0, 1, Vulpix.get_default_color_0(), Vulpix.get_default_color_1(), screen)
#my_pokemon  = Ninetails  (  0, 0, 0, 0, 1, Ninetails.get_default_color_0(), Ninetails.get_default_color_1(), screen)
#my_pokemon  = Jigglypuff (  0, 0, 0, 0, 1, Jigglypuff.get_default_color_0(), Jigglypuff.get_default_color_1(), screen)
#my_pokemon  = Wigglytuff (  0, 0, 0, 0, 1, Wigglytuff.get_default_color_0(), Wigglytuff.get_default_color_1(), screen)
#my_pokemon  = Zubat      (  0, 0, 0, 0, 1, Zubat.get_default_color_0(), Zubat.get_default_color_1(), screen)
#my_pokemon  = Golbat     (  0, 0, 0, 0, 1, Golbat.get_default_color_0(), Golbat.get_default_color_1(), screen)
#my_pokemon  = Oddish     (  0, 0, 0, 0, 1, Oddish.get_default_color_0(), Oddish.get_default_color_1(), screen)
#my_pokemon  = Gloom      (  0, 0, 0, 0, 1, Gloom.get_default_color_0(), Gloom.get_default_color_1(), screen)
#my_pokemon  = Vileplume  (  0, 0, 0, 0, 1, Vileplume.get_default_color_0(), Vileplume.get_default_color_1(), screen)
#my_pokemon  = Paras      (  0, 0, 0, 0, 1, Paras.get_default_color_0(), Paras.get_default_color_1(), screen)
#my_pokemon  = Parasect   (  0, 0, 0, 0, 1, Parasect.get_default_color_0(), Parasect.get_default_color_1(), screen)
#my_pokemon  = Venonat    (  0, 0, 0, 0, 1, Venonat.get_default_color_0(), Venonat.get_default_color_1(), screen)
#my_pokemon  = Venomoth   (  0, 0, 0, 0, 1, Venomoth.get_default_color_0(), Venomoth.get_default_color_1(), screen)
#my_pokemon  = Diglet     (  0, 0, 0, 0, 1, Diglet.get_default_color_0(), Diglet.get_default_color_1(), screen)
#my_pokemon  = Dugtrio    (  0, 0, 0, 0, 1, Dugtrio.get_default_color_0(), Dugtrio.get_default_color_1(), screen)
#my_pokemon  = Meowth     (  0, 0, 0, 0, 12, Meowth.get_default_color_0(), Meowth.get_default_color_1(), screen)
#my_pokemon  = Persian    (  0, 0, 0, 0, 1, Persian.get_default_color_0(), Persian.get_default_color_1(), screen)
#my_pokemon  = Psyduck    (  0, 0, 0, 0, 1, Psyduck.get_default_color_0(), Psyduck.get_default_color_1(), screen)
#my_pokemon  = Golduck    (  0, 0, 0, 0, 1, Golduck.get_default_color_0(), Golduck.get_default_color_1(), screen)
#my_pokemon  = Mankey     (  0, 0, 0, 0, 1, Mankey.get_default_color_0(), Mankey.get_default_color_1(), screen)
#my_pokemon  = Primeape   (  0, 0, 0, 0, 1, Primeape.get_default_color_0(), Primeape.get_default_color_1(), screen)
#my_pokemon  = Growlithe  (  0, 0, 0, 0, 1, Growlithe.get_default_color_0(), Growlithe.get_default_color_1(), screen)
#my_pokemon  = Arcanine   (  0, 0, 0, 0, 1, Arcanine.get_default_color_0(), Arcanine.get_default_color_1(), screen)
#my_pokemon  = Poliwag    (  0, 0, 0, 0, 1, Poliwag.get_default_color_0(), Poliwag.get_default_color_1(), screen)
#my_pokemon  = Poliwhirl  (  0, 0, 0, 0, 1, Poliwhirl.get_default_color_0(), Poliwhirl.get_default_color_1(), screen)
#my_pokemon  = Poliwrath  (  0, 0, 0, 0, 1, Poliwrath.get_default_color_0(), Poliwrath.get_default_color_1(), screen)
#my_pokemon  = Abra       (  0, 0, 0, 0, 1, Abra.get_default_color_0(), Abra.get_default_color_1(), screen)
#my_pokemon  = Kadabra    (  0, 0, 0, 0, 1, Kadabra.get_default_color_0(), Kadabra.get_default_color_1(), screen)
#my_pokemon  = Alakazam   (  0, 0, 0, 0, 1, Alakazam.get_default_color_0(), Alakazam.get_default_color_1(), screen)
#my_pokemon  = Machop     (  0, 0, 0, 0, 1, Machop.get_default_color_0(), Machop.get_default_color_1(), screen)
#my_pokemon  = Machoke    (  0, 0, 0, 0, 1, Machoke.get_default_color_0(), Machoke.get_default_color_1(), screen)
#my_pokemon  = Machamp    (  0, 0, 0, 0, 1, Machamp.get_default_color_0(), Machamp.get_default_color_1(), screen)
#my_pokemon  = Bellsprout (  0, 0, 0, 0, 1, Bellsprout.get_default_color_0(), Bellsprout.get_default_color_1(), screen)
#my_pokemon  = Weepinbell (  0, 0, 0, 0, 1, Weepinbell.get_default_color_0(), Weepinbell.get_default_color_1(), screen)
#my_pokemon  = Victreebel (  0, 0, 0, 0, 1, Victreebel.get_default_color_0(), Victreebel.get_default_color_1(), screen)
#my_pokemon  = Tentacool  (  0, 0, 0, 0, 1, Tentacool.get_default_color_0(), Tentacool.get_default_color_1(), screen)
#my_pokemon  = Tentacruel (  0, 0, 0, 0, 1, Tentacruel.get_default_color_0(), Tentacruel.get_default_color_1(), screen)
#my_pokemon  = Geodude    (  0, 0, 0, 0, 1, Geodude.get_default_color_0(), Geodude.get_default_color_1(), screen)
#my_pokemon  = Graveler   (  0, 0, 0, 0, 1, Graveler.get_default_color_0(), Graveler.get_default_color_1(), screen)
#my_pokemon  = Golem      (  0, 0, 0, 0, 1, Golem.get_default_color_0(), Golem.get_default_color_1(), screen)
#my_pokemon  = Ponyta     (  0, 0, 0, 0, 1, Ponyta.get_default_color_0(), Ponyta.get_default_color_1(), screen)
#my_pokemon  = Rapidash   (  0, 0, 0, 0, 1, Rapidash.get_default_color_0(), Rapidash.get_default_color_1(), screen)
#my_pokemon  = Slowpoke   (  0, 0, 0, 0, 1, Slowpoke.get_default_color_0(), Slowpoke.get_default_color_1(), screen)
#my_pokemon  = Slowbro    (  0, 0, 0, 0, 1, Slowbro.get_default_color_0(), Slowbro.get_default_color_1(), screen)
#my_pokemon  = Magnemite  (  0, 0, 0, 0, 1, Magnemite.get_default_color_0(), Magnemite.get_default_color_1(), screen)
#my_pokemon  = Magneton   (  0, 0, 0, 0, 1, Magneton.get_default_color_0(), Magneton.get_default_color_1(), screen)
#my_pokemon  = Farfetchd  (  0, 0, 0, 0, 1, Farfetchd.get_default_color_0(), Farfetchd.get_default_color_1(), screen)
#my_pokemon  = Doduo      (  0, 0, 0, 0, 1, Doduo.get_default_color_0(), Doduo.get_default_color_1(), screen)
#my_pokemon  = Dodrio     (  0, 0, 0, 0, 1, Dodrio.get_default_color_0(), Dodrio.get_default_color_1(), screen)
#my_pokemon  = Seel       (  0, 0, 0, 0, 1, Seel.get_default_color_0(), Seel.get_default_color_1(), screen)
#my_pokemon  = Dewgong    (  0, 0, 0, 0, 1, Dewgong.get_default_color_0(), Dewgong.get_default_color_1(), screen)
#my_pokemon  = Grimer     (  0, 0, 0, 0, 1, Grimer.get_default_color_0(), Grimer.get_default_color_1(), screen)
#my_pokemon  = Muk        (  0, 0, 0, 0, 1, Muk.get_default_color_0(), Muk.get_default_color_1(), screen)
#my_pokemon  = Shellder   (  0, 0, 0, 0, 1, Shellder.get_default_color_0(), Shellder.get_default_color_1(), screen)
#my_pokemon  = Cloyster   (  0, 0, 0, 0, 1, Cloyster.get_default_color_0(), Cloyster.get_default_color_1(), screen)
#my_pokemon  = Gastly     (  0, 0, 0, 0, 1, Gastly.get_default_color_0(), Gastly.get_default_color_1(), screen)
#my_pokemon  = Haunter    (  0, 0, 0, 0, 1, Haunter.get_default_color_0(), Haunter.get_default_color_1(), screen)
#my_pokemon  = Gengar     (  0, 0, 0, 0, 1, Gengar.get_default_color_0(), Gengar.get_default_color_1(), screen)
#my_pokemon  = Onix       (  0, 0, 0, 0, 1, Onix.get_default_color_0(), Onix.get_default_color_1(), screen)
#my_pokemon  = Drowzee    (  0, 0, 0, 0, 1, Drowzee.get_default_color_0(), Drowzee.get_default_color_1(), screen)
#my_pokemon  = Hypno      (  0, 0, 0, 0, 1, Hypno.get_default_color_0(), Hypno.get_default_color_1(), screen)
#my_pokemon  = Krabby     (  0, 0, 0, 0, 1, Krabby.get_default_color_0(), Krabby.get_default_color_1(), screen)
#my_pokemon  = Kingler    (  0, 0, 0, 0, 1, Kingler.get_default_color_0(), Kingler.get_default_color_1(), screen)
#my_pokemon  = Voltorb    (  0, 0, 0, 0, 1, Voltorb.get_default_color_0(), Voltorb.get_default_color_1(), screen)
#my_pokemon  = Electrode  (  0, 0, 0, 0, 1, Electrode.get_default_color_0(), Electrode.get_default_color_1(), screen)
#my_pokemon  = Exeggcute  (  0, 0, 0, 0, 1, Exeggcute.get_default_color_0(), Exeggcute.get_default_color_1(), screen)
#my_pokemon  = Exeggutor  (  0, 0, 0, 0, 1, Exeggutor.get_default_color_0(), Exeggutor.get_default_color_1(), screen)
#my_pokemon  = Cubone     (  0, 0, 0, 0, 1, Cubone.get_default_color_0(), Cubone.get_default_color_1(), screen)
#my_pokemon  = Marowak    (  0, 0, 0, 0, 1, Marowak.get_default_color_0(), Marowak.get_default_color_1(), screen)
#my_pokemon  = Hitmonlee  (  0, 0, 0, 0, 1, Hitmonlee.get_default_color_0(), Hitmonlee.get_default_color_1(), screen)
#my_pokemon  = Hitmonchan (  0, 0, 0, 0, 1, Hitmonchan.get_default_color_0(), Hitmonchan.get_default_color_1(), screen)
#my_pokemon  = Lickitung  (  0, 0, 0, 0, 1, Lickitung.get_default_color_0(), Lickitung.get_default_color_1(), screen)
#my_pokemon  = Koffing    (  0, 0, 0, 0, 1, Koffing.get_default_color_0(), Koffing.get_default_color_1(), screen)
#my_pokemon  = Weezing    (  0, 0, 0, 0, 1, Weezing.get_default_color_0(), Weezing.get_default_color_1(), screen)
#my_pokemon  = Rhyhorn    (  0, 0, 0, 0, 1, Rhyhorn.get_default_color_0(), Rhyhorn.get_default_color_1(), screen)
#my_pokemon  = Rhydon     (  0, 0, 0, 0, 1, Rhydon.get_default_color_0(), Rhydon.get_default_color_1(), screen)
#my_pokemon  = Chansey    (  0, 0, 0, 0, 1, Chansey.get_default_color_0(), Chansey.get_default_color_1(), screen)
#my_pokemon  = Tangela    (  0, 0, 0, 0, 1, Tangela.get_default_color_0(), Tangela.get_default_color_1(), screen)
#my_pokemon  = Kangaskhan (  0, 0, 0, 0, 1, Kangaskhan.get_default_color_0(), Kangaskhan.get_default_color_1(), screen)
#my_pokemon  = Horsea     (  0, 0, 0, 0, 1, Horsea.get_default_color_0(), Horsea.get_default_color_1(), screen)
#my_pokemon  = Seadra     (  0, 0, 0, 0, 1, Seadra.get_default_color_0(), Seadra.get_default_color_1(), screen)
#my_pokemon  = Goldeen    (  0, 0, 0, 0, 1, Goldeen.get_default_color_0(), Goldeen.get_default_color_1(), screen)
#my_pokemon  = Seaking    (  0, 0, 0, 0, 1, Seaking.get_default_color_0(), Seaking.get_default_color_1(), screen)
#my_pokemon  = Staryu     (  0, 0, 0, 0, 1, Staryu.get_default_color_0(), Staryu.get_default_color_1(), screen)
#my_pokemon  = Starmie    (  0, 0, 0, 0, 1, Starmie.get_default_color_0(), Starmie.get_default_color_1(), screen)
#my_pokemon  = Mr_Mime    (  0, 0, 0, 0, 1, Mr_Mime.get_default_color_0(), Mr_Mime.get_default_color_1(), screen)
#my_pokemon  = Scyther    (  0, 0, 0, 0, 1, Scyther.get_default_color_0(), Scyther.get_default_color_1(), screen)
#my_pokemon  = Jynx       (  0, 0, 0, 0, 1, Jynx.get_default_color_0(), Jynx.get_default_color_1(), screen)
#my_pokemon  = Electabuzz (  0, 0, 0, 0, 1, Electabuzz.get_default_color_0(), Electabuzz.get_default_color_1(), screen)
#my_pokemon  = Magmar     (  0, 0, 0, 0, 1, Magmar.get_default_color_0(), Magmar.get_default_color_1(), screen)
#my_pokemon  = Pinsir     (  0, 0, 0, 0, 1, Pinsir.get_default_color_0(), Pinsir.get_default_color_1(), screen)
#my_pokemon  = Tauros     (  0, 0, 0, 0, 1, Tauros.get_default_color_0(), Tauros.get_default_color_1(), screen)
#my_pokemon  = Magikarp   (  0, 0, 0, 0, 1, Magikarp.get_default_color_0(), Magikarp.get_default_color_1(), screen)
#my_pokemon  = Gyrados    (  0, 0, 0, 0, 1, Gyrados.get_default_color_0(), Gyrados.get_default_color_1(), screen)
#my_pokemon  = Lapras     (  0, 0, 0, 0, 1, Lapras.get_default_color_0(), Lapras.get_default_color_1(), screen)
#my_pokemon  = Ditto      (  0, 0, 0, 0, 1, Ditto.get_default_color_0(), Ditto.get_default_color_1(), screen)
#my_pokemon  = Eevee      (  0, 0, 0, 0, 1, Eevee.get_default_color_0(), Eevee.get_default_color_1(), screen)
#my_pokemon  = Vaporeon   (  0, 0, 0, 0, 1, Vaporeon.get_default_color_0(), Vaporeon.get_default_color_1(), screen)
#my_pokemon  = Jolteon    (  0, 0, 0, 0, 1, Jolteon.get_default_color_0(), Jolteon.get_default_color_1(), screen)
#my_pokemon  = Flareon    (  0, 0, 0, 0, 1, Flareon.get_default_color_0(), Flareon.get_default_color_1(), screen)
#my_pokemon  = Porygon    (  0, 0, 0, 0, 1, Porygon.get_default_color_0(), Porygon.get_default_color_1(), screen)
#my_pokemon  = Omanyte    (  0, 0, 0, 0, 1, Omanyte.get_default_color_0(), Omanyte.get_default_color_1(), screen)
#my_pokemon  = Omastar    (  0, 0, 0, 0, 1, Omastar.get_default_color_0(), Omastar.get_default_color_1(), screen)
#my_pokemon  = Kabuto     (  0, 0, 0, 0, 1, Kabuto.get_default_color_0(), Kabuto.get_default_color_1(), screen)
#my_pokemon  = Kabutops   (  0, 0, 0, 0, 1, Kabutops.get_default_color_0(), Kabutops.get_default_color_1(), screen)
#my_pokemon  = Aerodactyl (  0, 0, 0, 0, 1, Aerodactyl.get_default_color_0(), Aerodactyl.get_default_color_1(), screen)
#my_pokemon  = Snorlax    (  0, 0, 0, 0, 1, Snorlax.get_default_color_0(), Snorlax.get_default_color_1(), screen)
#my_pokemon  = Articuno   (  0, 0, 0, 0, 1, Articuno.get_default_color_0(), Articuno.get_default_color_1(), screen)
#my_pokemon  = Zapdos     (  0, 0, 0, 0, 1, Zapdos.get_default_color_0(), Zapdos.get_default_color_1(), screen)
#my_pokemon  = Moltres    (  0, 0, 0, 0, 1, Moltres.get_default_color_0(), Moltres.get_default_color_1(), screen)
#my_pokemon  = Dratini    (  0, 0, 0, 0, 1, Dratini.get_default_color_0(), Dratini.get_default_color_1(), screen)
#my_pokemon  = Dragonair  (  0, 0, 0, 0, 1, Dragonair.get_default_color_0(), Dragonair.get_default_color_1(), screen)
#my_pokemon  = Dragonite  (  0, 0, 0, 0, 1, Dragonite.get_default_color_0(), Dragonite.get_default_color_1(), screen)
#my_pokemon  = Mewtwo     (  0, 0, 0, 0, 1, Mewtwo.get_default_color_0(), Mewtwo.get_default_color_1(), screen)
#my_pokemon  = Mew        (  0, 0, 0, 0, 1, Mew.get_default_color_0(), Mew.get_default_color_1(), screen)
my_pokemon  = Missingno  (  0, 0, 0, 0, 1, Missingno.get_default_color_0(), Missingno.get_default_color_1(), screen)
											#set sprite at location x,y, with velocity x,y,
											#with size multiplier 1,  with the following four colors
											#on the main screen
print my_pokemon.get_Name()
print str(my_pokemon.get_Number()).zfill(3)
print my_pokemon.get_Pokedex_Message()
print str(my_pokemon.get_Height_US()) + "in"
print str(my_pokemon.get_Height_SI()) + "m"
print str(my_pokemon.get_Weight_US()) + "lbs"
print str(my_pokemon.get_Weight_SI()) + "kg"
while not done:

  #limit the clock to ten loops per second
  clock.tick(3)

  for event in pygame.event.get():					       	    #allows you to exit by clicking x
    if event.type == pygame.QUIT:
      done =True
    elif event.type == pygame.MOUSEBUTTONUP:
      None 
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_F10:
        pygame.image.save(screen, (str(my_pokemon.get_Number()).zfill(3) + ".bmp"))

  screen.fill(RED)								    #arbitrary color, good for spotting mistakes in the sprite

  my_pokemon.draw()

  pygame.display.flip()

pygame.quit()
