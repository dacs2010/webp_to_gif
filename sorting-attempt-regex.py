from operator import itemgetter

def heyo(frames):
    '''
    Sorts file names by splitting the string with regex, then turns the num strs into ints, then sorts, then concats the list and outputs final list. This was an interesting process to attempt, but in the end overly complicated.
    '''
    new_frames = []

    for frame in frames:
        exploded_frame = re.split(r'([0-9]+)', frame)
        int_frame = [int(i) if i.isdigit() else i for i in exploded_frame]
        new_frames.append(int_frame)

    # sorting with itemgetter over lambda for performance
    new_frames.sort(key=itemgetter(1))
    # new_frames = sorted(new_frames, key=lambda x: x[1])
    final_frames = [''.join(map(str, i)) for i in new_frames]
    print(final_frames)

# start2 = time.time()
# heyo(frames)
# print(time.time() - start2)