# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

from kmk.extensions.RGB import RGB

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GP3, board.GP4, board.GP2, board.GP1, board.GP0, board.GP7]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.TG(1), KC.TILDE, KC.AT, KC.HASH, KC.DOLLAR, KC.PERCENT],

    [KC.TG(0),KC.F15,KC.F17,KC.F14,KC.F16,KC.F13]
]

class LayerRGB(RGB):
    def on_layer_change(self, layer):
        if layer == 0:
            self.set_hsv_fill(0, self.sat_default, self.val_default)   # red
        elif layer == 1:
            self.set_hsv_fill(170, self.sat_default, self.val_default) # blue
        # update the LEDs manually if no animation is active:
        self.show()


rgb = LayerRGB(pixel_pin=board.GP6, # GPIO pin of the status LED, or background RGB light
        num_pixels=2,                # one if status LED, more if background RGB light
        hue_default=0,               # in range 0-255: 0/255-red, 85-green, 170-blue
        sat_default=255,
        val_default=255,
        )
keyboard.extensions.append(rgb)


class RGBLayers(Layers):
    def activate_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx)
        rgb.on_layer_change(layer)

    def deactivate_layer(self, keyboard, layer):
        super().deactivate_layer(keyboard, layer)
        rgb.on_layer_change(keyboard.active_layers[0])


keyboard.modules.append(RGBLayers())

# Start kmk!
if __name__ == '__main__':
    keyboard.go()