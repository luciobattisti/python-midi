from collections import deque
from midiutil import MIDIFile


import my_utils
import os

output_dir = "midi_files"

array_of_notes = [
    ("C", 4), ("G", 4), ("C", 5), ("C", 4), 
    ("G", 4), ("C", 5), ("C", 4), ("G", 4), 
    ("D", 5), ("C", 4), ("G", 4), ("C", 5), 
    ("C", 4), ("G", 4), ("C", 5), ("G", 4),
    ("C", 4), ("F", 4), ("C", 5), ("C", 4), 
    ("F", 4), ("C", 5), ("C", 4), ("G", 4), 
    ("D", 5), ("C", 4), ("F", 4), ("C", 5), 
    ("C", 4), ("F", 4), ("C", 5), ("F", 4)
]

array_of_note_numbers = []
array_of_notes_numbers_shifted = []

for i in range(1, 5):

    for note in array_of_notes:
        array_of_note_numbers.append(my_utils.note_to_number(note[0], note[1]))
        
    array_of_notes_shifted = deque(array_of_notes)
    array_of_notes_shifted.rotate(-i)
    array_of_notes_shifted = list(array_of_notes_shifted)
        
    for note in array_of_notes_shifted:
        array_of_notes_numbers_shifted.append(my_utils.note_to_number(note[0], note[1]))

track = 0
channel = 0
time = 0  # In beats
duration = 0.5  # In beats
tempo = 120  # In BPM
volume = 100  # 0-127, as per the MIDI standard

# One track, defaults to format 1 (tempo track is created automatically)
MyMIDI = MIDIFile(1)  
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(array_of_note_numbers):
    MyMIDI.addNote(track, channel, pitch, time + i/2, duration, volume)

os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "phase-shifting-f-g-0.mid"), "wb") as fp:
    MyMIDI.writeFile(fp)

# One track, defaults to format 1 (tempo track is created automatically)
MyMIDI = MIDIFile(1)  
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(array_of_notes_numbers_shifted):
    MyMIDI.addNote(track, channel, pitch, time + i/2, duration, volume)

os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "phase-shifting-f-g-1.mid"), "wb") as fp:
    MyMIDI.writeFile(fp)
