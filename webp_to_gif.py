''' 
Converts files in the directory with extention webp to gif
'''

#import os
import glob
from PIL import Image

#path = os.getcwd() + '/*webp'
#print(path)
files = glob.glob('*webp')
#print(files)

# create list of files
for file in files:
  print(file)

# get user input
user_input = input('Would you like to convert these files? Y/n: ')
print(user_input.lower())

# convert animated webp files
if user_input.lower() == 'y':
  for file in files:
    im = Image.open(file)
    print(file)
    if im.is_animated == True:
      new_name = file.replace('.webp','.gif')
      print(new_name)
      #im.save(str(new_name)+'.gif', 'gif', save_all=True, optimize=True, background=0)
    #else: print(file + ' is not an animation')
elif user_input.lower() == 'n': 
  print('Good bye')
  exit()
else:
  print('Please enter either Y or N')
