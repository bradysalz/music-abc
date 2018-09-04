NOTES = [
    'C ', 'C#', 'D ', 'D#', 'E ', 'F ', 'F#', 'G ', 'G#', 'A ', 'A#', 'B '
]
NUM_NOTES = len(NOTES)


class MusicKey:
    def __init__(self, root: str):
        self.root = root
        self._set_idx()
        self.scale = []
        self.chords = []
        self.chord_labels = []

    def _set_idx(self):
        """Sets the starting index based on the root note"""
        self._idx = NOTES.index(self.root)

    def half_step(self) -> int:
        """Increments by a half step"""
        self._idx = (self._idx + 1) % NUM_NOTES
        return self._idx

    def whole_step(self) -> int:
        """Increments by a whole step"""
        self._idx = (self._idx + 2) % NUM_NOTES
        return self._idx

    def generate_scale(self):
        raise NotImplementedError

    def generate_chords(self):
        """Creates all chords in the scale"""
        for note in self.scale:
            chord_root_idx = self.scale.index(note)
            first_note = note
            third_note = self.scale[(chord_root_idx + 2) % 7]
            fifth_note = self.scale[(chord_root_idx + 4) % 7]
            self.chords.append([first_note, third_note, fifth_note])

    def label_chords(self):
        """Categorizes all chords in the scale"""
        for chord in self.chords:
            first_dist = NOTES.index(chord[1]) - NOTES.index(chord[0])
            if first_dist < 0:
                first_dist += NUM_NOTES

            second_dist = NOTES.index(chord[2]) - NOTES.index(chord[1])
            if second_dist < 0:
                second_dist += NUM_NOTES

            if (first_dist == 4) and (second_dist == 3):
                self.chord_labels.append('Major')
            elif (first_dist == 3) and (second_dist == 4):
                self.chord_labels.append('Minor')
            elif (first_dist == 3) and (second_dist == 3):
                self.chord_labels.append('Diminished')


class MajorKey(MusicKey):
    def generate_scale(self):
        """Creates the major scale for a root note"""
        self.scale.append(NOTES[self._idx])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.half_step()])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.whole_step()])


class MinorKey(MusicKey):
    def generate_scale(self):
        """Creates the minor scale for a root note"""
        self.scale.append(NOTES[self._idx])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.half_step()])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.half_step()])
        self.scale.append(NOTES[self.whole_step()])


class BluesScale(MusicKey):
    def generate_scale(self):
        """Creates the blues scale for a root note"""
        self.scale.append(NOTES[self._idx])
        self.whole_step()
        self.scale.append(NOTES[self.half_step()])
        self.scale.append(NOTES[self.whole_step()])
        self.scale.append(NOTES[self.half_step()])
        self.scale.append(NOTES[self.half_step()])
        self.whole_step()
        self.scale.append(NOTES[self.half_step()])
        self.scale.append(NOTES[self.whole_step()])


if __name__ == "__main__":
    Cmaj = MajorKey('C')
    Cmaj.generate_scale()
    Cmaj.generate_chords()
    Cmaj.label_chords()
    for label, ch in zip(Cmaj.chord_labels, Cmaj.chords):
        print(f"{label}: {ch}")

    Gmaj = MajorKey('G')
    Gmaj.generate_scale()
    Gmaj.generate_chords()
    Gmaj.label_chords()
    for label, ch in zip(Gmaj.chord_labels, Gmaj.chords):
        print(f"{label}: {ch}")

    Emin = MinorKey('E')
    Emin.generate_scale()
    Emin.generate_chords()
    Emin.label_chords()
    for label, ch in zip(Emin.chord_labels, Emin.chords):
        print(f"{label}: {ch}")
