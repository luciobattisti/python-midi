from collections import deque
from midiutil import MIDIFile
from mingus.core import chords


import my_utils
import os

chord_progression = ["Cmaj7", "Cmaj7", "Cmaj7", "Cmaj7", 
                     "Fmaj7", "Fmaj7", "Fmaj7", "Fmaj7",
                     "Gdom7", "Gdom7", "Gdom7", "Gdom7",
                     "Amin7", "Amin7", "Amin7", "Amin7"]
output_dir = "midi_files"

array_of_notes = []
array_of_notes_shifted_1 = []
array_of_notes_shifted_2 = []

count = 0
for chord in chord_progression:
    chords_notes = chords.from_shorthand(chord)
    
    chords_notes_shifted_1 = deque(chords.from_shorthand(chord))
    chords_notes_shifted_1.rotate(-(count % 4))

    chords_notes_shifted_2 = deque(chords.from_shorthand(chord))
    chords_notes_shifted_2.rotate(count % 4)

    array_of_notes.extend(chords_notes)
    array_of_notes_shifted_1.extend(list(chords_notes_shifted_1))
    array_of_notes_shifted_2.extend(list(chords_notes_shifted_2))

    count += 1

array_of_note_numbers = []
for note in array_of_notes:
    OCTAVE = 4
    array_of_note_numbers.append(my_utils.note_to_number(note, OCTAVE))

array_of_note_numbers_shifted_1 = []
for note in array_of_notes_shifted_1:
    OCTAVE = 4
    array_of_note_numbers_shifted_1.append(my_utils.note_to_number(note, OCTAVE))

array_of_note_numbers_shifted_2 = []
for note in array_of_notes_shifted_2:
    OCTAVE = 4
    array_of_note_numbers_shifted_2.append(my_utils.note_to_number(note, OCTAVE))

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
with open(os.path.join(output_dir, "phase-shifting-0.mid"), "wb") as fp:
    MyMIDI.writeFile(fp)

# One track, defaults to format 1 (tempo track is created automatically)
MyMIDI = MIDIFile(1)  
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(array_of_note_numbers_shifted_1):
    MyMIDI.addNote(track, channel, pitch, time + i/2, duration, volume)

os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "phase-shifting-1.mid"), "wb") as fp:
    MyMIDI.writeFile(fp)

# One track, defaults to format 1 (tempo track is created automatically)
MyMIDI = MIDIFile(1)  
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(array_of_note_numbers_shifted_2):
    MyMIDI.addNote(track, channel, pitch, time + i/2, duration, volume)

os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "phase-shifting-2.mid"), "wb") as fp:
    MyMIDI.writeFile(fp)
