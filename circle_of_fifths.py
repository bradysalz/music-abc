from music import NOTES, NUM_NOTES
from music import MajorKey, MinorKey, MusicKey


def rotate(l, n):
    """Right rotate a list by n elements"""
    return l[n:] + l[:n]


Cmaj = MajorKey('C ')
Cmaj.generate_scale()

Gmaj = MajorKey('G ')
Gmaj.generate_scale()

Dmaj = MajorKey('D ')
Dmaj.generate_scale()


def print_scale_rotations():
    print(Gmaj.scale, "- Gmaj")
    for rot in range(len(Cmaj.scale)):
        rotated_scale = rotate(Cmaj.scale, rot)
        print(f"{rotated_scale} - Cmaj start on Note {rot+1}")


def print_next_rotations():
    print(Dmaj.scale, "- Dmaj")
    rot_Gmaj = rotate(Gmaj.scale, 4)
    print(f"{rot_Gmaj} - Gmaj start on Note {4+1}")


def recursive_scales(scale, desired_note):
    """Recursively generates the scale for desired_note"""
    if scale[0] == desired_note:
        return scale
    else:
        scale = rotate(scale, 4)
        last_note_idx = (NOTES.index(scale[6]) + 1) % NUM_NOTES
        scale[6] = NOTES[last_note_idx]
        return recursive_scales(scale, desired_note)


def recursive_test():
    """Does this recursive thing even work?"""
    Bmaj = MajorKey('B ')
    Bmaj.generate_scale()
    print(Bmaj.scale)

    scale = recursive_scales(Cmaj.scale, 'B ')
    print(scale)


def recursive_loop():
    """Can we make it all the way around the loop?"""
    scale = recursive_scales(Gmaj.scale, 'C ')
    print(scale)


def minorify_scale(scale):
    """Turns a major scale into a minor scale"""
    return rotate(scale, 5)


if __name__ == "__main__":
    Amin = MinorKey('A ')
    Amin.generate_scale()
    print(Cmaj.scale)
    print(minorify_scale(Cmaj.scale))
    print(Amin.scale)
