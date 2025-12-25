# Taglia's Gaming Pad

Taglia's Gaming Pad is a 6 key macropad with 2 SK6812MINI RGB Leds that uses KMK software

It was made for the Hackpad YSWS on Hack Club

## Features:
- 3D printed case (color to be defined)
- 2 SK6812MINI RGB LEDs. Both for aesthetics, and also to indicate which layer the keyboard is on
- 6 Keys, with one to swap between 2 layers, making for a total of 10 different key inputs!

## CAD Model:
Everything fits together using 4 M3 Bolts and heatset inserts.

Case
<img src=assets/case.png alt="case" width="500"/>

Complete CAD
<img src=assets/cad.png alt="Schematic" width="500"/>

All made in Autocad Fusion (former Fusion360)


## PCB
Here is the PCB of my Pad! it was made in KiCad 9.0. Some little easter eggs have been added to the board as text, like a couple of memes, a phrase in my native language and my Pad's name

Schematic

<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB

<img src=assets/pcb.png alt="Schematic" width="300"/>

The keyswitch footprints used are Cherry MX1 switches

## Firmware Overview
This hackpad uses [KMK](https://github.com/KMKfw/kmk_firmware) firmware.

- The three keys in the upper row and the first two keys (from the left) on the bottom input either: A ASCII US character or Function Keys F13 through F17
- The bottom right key alternates between the two layers, and changes the LED color!

## BOM:
Here Is everything needed to realise this Pad:

- 6x Cherry MX Switches
- 6x DSA Keycaps (white)
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm Screws
- 2x SK6812 MINI-E LEDs
- 1x Seeed XIAO RP2040 microcontroller
- 1x Case (2 printed parts)

