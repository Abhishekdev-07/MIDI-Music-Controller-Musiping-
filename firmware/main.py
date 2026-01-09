# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# --- ABHISHEK'S ADDITION: Import MIDI Support ---
# This tells KMK we want to send Music Notes, not just Letters
from kmk.modules.midi import MidiKeys 

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension (from the guide)
macros = Macros()
keyboard.modules.append(macros)

# --- ABHISHEK'S ADDITION: Enable MIDI ---
# We turn on the "Music Engine" here
midi = MidiKeys()
keyboard.modules.append(midi)

# Define your pins here! 
# (These are placeholders from the guide, we will fix them 
# to match your specific D0, D1, D2, D3 pins later!)
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix (we are using direct pins)
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# I have changed the keys to send MIDI NOTES instead of letters!
keyboard.keymap = [
    [
        KC.MIDI_NOTE_C4,  # Button 1 plays Middle C
        KC.MIDI_NOTE_D4,  # Button 2 plays D
        KC.MIDI_NOTE_E4,  # Button 3 plays E
        KC.MIDI_NOTE_F4,  # Button 4 plays F
    ]
]

if __name__ == '__main__':
    keyboard.go()
