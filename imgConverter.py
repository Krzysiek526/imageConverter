import sys
import os
from PIL import Image, ImageFilter

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
#print(image_folder, output_folder) #checking if they run




#chceck if new\ exist, if not create
# print(os.path.exists(output_folder)) #check if they exist - must get False
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


#loop through Pokedex #new
# for filename in os.listdir(image_folder):
# 	img = Image.open(f'{image_folder}{filename}')
# 	clean_name = os.path.splitext(filename)[0] #cleaning image with jpg extension
# 	###convert imgaes to png save to the new folder
# 	img.save(f'{output_folder}{clean_name}.png', 'png')
# 	print('all done!')

## edition with size #new2
# for filename in os.listdir(image_folder):
# 	img = Image.open(f'{image_folder}{filename}')
# 	clean_name = os.path.splitext(filename)[0]
# 	img.thumbnail((200,200))
# 	img.save(f'{output_folder}{clean_name}.png', 'png')
# 	print('all done!')

###edition with size and filter (grey image) #new3
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.thumbnail((200,200))
	filtered = img.convert('L')
	filtered.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')
