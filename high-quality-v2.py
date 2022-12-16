from PIL import Image, ImageSequence
import glob
import time
import imageio.v3 as iio
from pathlib import Path

path = Path('.')
files = glob.glob('*webp')
frames = glob.glob('*.png')


def pull_frames(files):
    '''Pull the frames from an animated webp file.

    With help from the PIL docs sample, get all the frames from an animated webp
    https://pillow.readthedocs.io/en/stable/reference/ImageSequence.html 

    Sorts files by removing '.png' portion of the string, sorting numerically, then adding '.png' back to the end of the file name. Creating a PNG image from each animation frame.

    '''
    for file in files:
        im = Image.open(file)
        print(file)
        print(im.info)
        if im.is_animated:
            index = 0
            frames = []
            for frame in ImageSequence.Iterator(im):
                frame.save(f"{index}.png")
                index += 1
                frames.append(frame)
            
            print(str(len(frames)) + ' frames')
        else: im


def make_gif(frames):
    '''Assemble PNG images into a gif.

    It turns out that the quality issue is due to the fact that the GIF format can only handle 256 colors per frame. 

    '''
    
    print(frames)
    imframes = []
    for frame in frames:
        imframe = iio.imread(frame)
        imframes.append(imframe)
    iio.imwrite('test.gif', imframes)
    


# start0 = time.time()
pull_frames(files)
# print(str(time.time() - start0) + ' seconds')

# make_gif(frames)