import glob
import math
from pathlib import Path
from PIL import Image


#input_path = 'test/FieldNotebook1_(BRIT-A-AR003-FN01)_1-646/'
#input_path = 'test/small_batch/'
input_path = 'original_tiffs/**/'
#output_path = 'test/out/'
output_path = 'test/jpg_samples/'
output_file_ext = 'jpg'
print(input_path)
images = glob.glob(input_path + '*.tif', recursive=True)
print('images', images)

# TODO - Make sure sort is correct
images.sort()

page_counter = 0
spread_width_min = 2800 # full spreads seem to all be 2855
for image_path in images:
    image_path = Path(image_path)
    image_name = image_path.stem
    page_sep = image_name.find('_')
    notebook_ID = image_name[:page_sep]
    #print(image_name, notebook_ID)
    
    spread = Image.open(image_path)
    spread_width, height = spread.size
    if spread_width > spread_width_min:
        #spread.show()
        # Crop left page
        page_width = math.floor(spread_width/2)
        page_width = page_width + (page_width *.07) # padding to crop past center of images
        left = spread.crop((0,0,page_width,height))
        #print(spread_width)
        #left.show()
        image_out_path = Path(output_path)
        image_out_name = notebook_ID + '_' + str(page_counter).zfill(3) + '.' + output_file_ext
        image_out_path = image_out_path / image_out_name
        print(image_out_path)
        left.save(image_out_path)
        page_counter +=1

        # Crop right page
        right = spread.crop((spread_width - page_width,0,spread_width,height))
        #right.show()
        image_out_path = Path(output_path)
        image_out_name = notebook_ID + '_' + str(page_counter).zfill(3) + '.' + output_file_ext
        image_out_path = image_out_path / image_out_name
        print(image_out_path)
        right.save(image_out_path)
        page_counter +=1
    else:
        #image is narrow, probably front or back cover
        #spread.show()
        image_out_path = Path(output_path)
        image_out_name = notebook_ID + '_' + str(page_counter).zfill(3) + '.' + output_file_ext
        image_out_path = image_out_path / image_out_name
        print(image_out_path)
        spread.save(image_out_path)
        page_counter +=1