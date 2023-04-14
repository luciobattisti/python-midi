from midiutil import MIDIFile
from mingus.core import chords

import my_utils
import os

chord_progression = ["Cmaj7", "Cmaj7", "Fmaj7", "Gdom7"]
output_dir = "midi_files"

array_of_notes = []
for chord in chord_progression:
    array_of_notes.extend(chords.from_shorthand(chord)[0])


array_of_note_numbers = []
for note in array_of_notes:
    OCTAVE = 3
    array_of_note_numbers.append(my_utils.note_to_number(note, OCTAVE))

track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 120  # In BPM
volume = 100  # 0-127, as per the MIDI standard

# One track, defaults to format 1 (tempo track is created automatically)
MyMIDI = MIDIFile(1)  
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(array_of_note_numbers):
    MyMIDI.addNote(track, channel, pitch, time + (i*4), duration, volume)

os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "pure-edm-fire-bass.mid"), "wb") as fp:
    MyMIDI.writeFile(fp)
