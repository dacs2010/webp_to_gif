''' 
Converts files in the directory with extention webp to gif
'''

#import os
import glob
from PIL import Image

#path = os.getcwd() + '/*webp'
#print(path)
files = glob.glob('*webp')
print(files)

for file in files:
  im = Image.open(file)
  print(file)
  if im.is_animated == True:
    new_name = file.replace('.webp','.gif')
    print(new_name)
    #im.save(str(new_name)+'.gif', 'gif', save_all=True, optimize=True, background=0)
  else: print(file + ' is not an animation')
