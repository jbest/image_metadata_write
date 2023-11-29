import glob
import math
from PIL import Image


#input_path = 'test/FieldNotebook1_(BRIT-A-AR003-FN01)_1-646/'
input_path = 'test/small_batch/'
images = glob.glob(input_path + '*.tif')

#print(images)

"""
test = ['a','x', '4', '003', 'A']
print(test)
test.sort()
print(test)
"""

page_counter = 0
spread_width_min = 0
for image_path in images:
	# TODO skip first file (front cover)
	
	spread = Image.open(image_path)
	spread_width, height = spread.size
	#spread.show()
	# Crop left page
	page_width = math.floor(spread_width/2)
	left = spread.crop((0,0,page_width,height))
	print(spread_width)
	left.show()



	# Crop right page
	right = spread.crop((spread_width - page_width,0,spread_width,height))
	right.show()
	print(str(page_counter).zfill(3))
	page_counter +=1