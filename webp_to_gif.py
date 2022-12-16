''' 
Converts files in the current directory with extention webp to gif
'''

import glob
from PIL import Image


# create list of files
files = glob.glob('*webp')


def webp_to_gif(files):
  '''
  convert animated webp files
  '''
  for file in files:  
    print(file)
  
  user_input = input('Would you like to convert these files? Y/n: ')

  if user_input.lower() == 'y':
    for file in files:
      im = Image.open(file)
      if im.is_animated == True:
        new_name = file.replace('.webp','.gif')
        im.save(str(new_name), 'gif', save_all=True, optimize=True, background=0)
        # os.remove(file)
      else: print(file + ' is not an animation')
    return files
  elif user_input.lower() == 'n': 
    print('OK, bye bye -_-!')
    # exit()
  else:
    print('Please enter either Y or N')
    # roadmap: rerun code


webp_to_gif(files)