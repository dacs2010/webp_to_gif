from PIL import Image, ImageSequence
import glob
import time
import os


files = glob.glob('*webp')
# print(files)


def pull_frames(files):
    '''
    with help from the PIL docs sample, get all the frames from an animated webp
    https://pillow.readthedocs.io/en/stable/reference/ImageSequence.html 

    Sorts files by removing '.png' portion of the string, sorting numerically, then adding '.png' back to the end of the file name.

    currently creates a gif but the quality loss is still there. I will be looking for other ways to create the animation.
    '''
    for file in files:
        im = Image.open(file)
        print(file)
        print(im.is_animated)
        print(im.n_frames)
        if im.is_animated:
            index = 0
            for frame in ImageSequence.Iterator(im):
                frame.save(f"{index}.png")
                index += 1
            frames = glob.glob('*.png')
            #need to open png's then add them to a list and then save as gif, that's why this isn't working
            new_frames = [frame.replace('.png', '') for frame in frames]
            new_frames.sort(key=float)
            rename_frames = [frame+'.png' for frame in new_frames]
            final_frames = []
            for frame in rename_frames:
                fr = Image.open(frame)
                final_frames.append(fr)
            new_name = file.replace('.webp','.gif')
            print(final_frames)
            final_frames[0].save(str(new_name),save_all=True, append_images=final_frames[1:], loop=0)
        else: im


start0 = time.time()
pull_frames(files)
print(time.time() - start0)

frames = glob.glob('*.png')


def rename_frames(frames):
    '''
    Sorts files by removing '.png' portion of the string, sorting numerically, then adding '.png' back to the end of the file name.
    '''
    new_frames = [frame.replace('.png', '') for frame in frames]
    new_frames.sort(key=float)
    final_frames = [frame +'.png' for frame in new_frames]
    print(final_frames)

# start1 = time.time()
# rename_frames(frames)
# print(time.time() - start1)



