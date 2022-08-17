''' 
Get all files in a directory with the webp ext and convert them to gif.

This currently works, however it will convert ANY webp to gif. The next step is to loop through and test to see if the webp is animated or not, if so then convert it.

A possible next step is to remove the original image and replace it with the new file, however this might be bad practice.
'''

import os
import glob
from PIL import Image

path = os.getcwd() + '/*webp'
print(path)
files = glob.glob(path)
print(files)

for file in files:
  im = Image.open(file)
  new_name = file.replace('.webp','')
  print(new_name)
  im.save(str(new_name)+'.gif', 'gif', save_all=True, optimize=True, background=0)
