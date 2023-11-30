import glob
import math
from pathlib import Path
from PIL import Image
import os

input_path = 'original_tiffs'
#output_path = 'test/jpg_samples/'
output_path = 'repaginated_tiffs/'

#output_file_ext = 'jpg'
output_file_ext = 'tif'

def repaginate_notebook(nb_base_path=None, nb_params=None):
    nb_dir = Path(nb_params['directory'])
    nb_base_path = Path(nb_base_path)
    nb_dir_path = nb_base_path.joinpath(nb_dir)
    images = glob.glob(str(nb_dir_path) + '/' + '*.tif')
    images.sort()
    pad = nb_params.get('pad')

    if pad:
        pad_l = pad
        pad_r = pad
    else:
        pad_l = nb_params['pad_l']
        pad_r = nb_params['pad_r']        
    page_counter = 0
    spread_width_min = nb_params['spread_width_min']
    for image_path in images:
        image_path = Path(image_path)
        image_name = image_path.stem
        page_sep = image_name.find('_')
        notebook_ID = image_name[:page_sep]
        print(image_name, notebook_ID)
        
        spread = Image.open(image_path)
        spread_width, height = spread.size
        #notebook_dir = Path(notebook_ID)
        image_out_path = Path(output_path) / notebook_ID
        image_out_path.mkdir(parents=True, exist_ok=True)
        print('image_out_path:', image_out_path)
        if spread_width > spread_width_min:
            page_width = math.floor(spread_width/2)
            
            # Crop left page
            page_width_l = page_width + (page_width * pad_l) # padding to crop past center of images
            #print('page_width_l:', page_width_l, 'pad_l:', pad_l)
            left = spread.crop((0,0,page_width_l,height))

            image_out_name = notebook_ID + '_' + str(page_counter).zfill(3) + '.' + output_file_ext
            print(image_out_path / image_out_name)

            left.save(image_out_path / image_out_name)
            page_counter +=1

            # Crop right page
            page_width_r = page_width + (page_width * pad_r)
            #print('page_width_r:', page_width_r, 'pad_r:', pad_r)
            right = spread.crop((spread_width - page_width_r,0,spread_width,height))
            image_out_name = notebook_ID + '_' + str(page_counter).zfill(3) + '.' + output_file_ext
            print(image_out_path / image_out_name)
            right.save(image_out_path / image_out_name)
            page_counter +=1
        else:
            #image is narrow, probably front or back cover
            image_out_name = notebook_ID + '_' + str(page_counter).zfill(3) + '.' + output_file_ext
            print(image_out_path / image_out_name)
            spread.save(image_out_path / image_out_name)
            page_counter +=1

# Each notebook is configurable due to different sizes and layouts
FN01 = {'directory':'FieldNotebook1_(BRIT-A-AR003-FN01)_1-646', 'spread_width_min':2800, 'pad':0.07}
FN02 = {'directory':'FieldNotebook2_(BRIT-A-AR003-FN02)_845-1103', 'spread_width_min':2400, 'pad':0.03}
FN03 = {'directory':'FieldNotebook3_(BRIT-A-AR003-FN03)_1117-1400', 'spread_width_min':2700, 'pad':0.02}
#FN04 cropping not needed
#FN05 cropping not needed
FN06 = {'directory':'FieldNotebook6(BRIT-A-AR003-FN06)_2379-2427', 'spread_width_min':2700, 'pad':0.05}
FN07 = {'directory':'FieldNotebook7(BRIT-A-AR003-FN07)_2774-3118', 'spread_width_min':2500, 'pad_l':0.15, 'pad_r':0.00}
FN08 = {'directory':'FieldNotebook8(BRIT-A-AR003-FN08)_3119-3693', 'spread_width_min':2500, 'pad_l':0.12, 'pad_r':0.02}
FN09 = {'directory':'FieldNotebook9(BRIT-A-AR003-FN09)_3694-4049', 'spread_width_min':2500, 'pad_l':0.1, 'pad_r':0.00}
FN10 = {'directory':'FieldNotebook10(BRIT-A-AR003-FN10)_4050-4374', 'spread_width_min':2500, 'pad_l':0.08, 'pad_r':0.05}
FN11 = {'directory':'FieldNotebook11(BRIT-A-AR003-FN11)_4375-4956', 'spread_width_min':2500, 'pad_l':0.05, 'pad_r':0.05}
FN12 = {'directory':'FieldNotebook12(BRIT-A-AR003-FN12)_4957-5133', 'spread_width_min':2400, 'pad_l':0.05, 'pad_r':0.05}
FN13 = {'directory':'FieldNotebook13(BRIT-A-AR003-FN13)_5134-6102', 'spread_width_min':2400, 'pad_l':0.05, 'pad_r':0.05}
FN14 = {'directory':'FieldNotebook14(BRIT-A-AR003-FN14)_8000-8218', 'spread_width_min':2600, 'pad_l':0.05, 'pad_r':0.02}
FN15 = {'directory':'FieldNotebook15(BRIT-A-AR003-FN15)_15134-15380', 'spread_width_min':2600, 'pad_l':0.05, 'pad_r':0.05}
FN16 = {'directory':'FieldNotebook16(BRIT-A-AR003-FN16)_15381-15481', 'spread_width_min':2600, 'pad_l':0.05, 'pad_r':0.05}
FN17 = {'directory':'FieldNotebook17(BRIT-A-AR003-FN17)_15482-15616', 'spread_width_min':2400, 'pad_l':0.05, 'pad_r':0.05}
FN18 = {'directory':'FieldNotebook18(BRIT-A-AR003-FN18)_15617-15725', 'spread_width_min':2400, 'pad_l':0.05, 'pad_r':0.05}
FN19 = {'directory':'FieldNotebook19(BRIT-A-AR003-FN19)_15726-15950', 'spread_width_min':2400, 'pad_l':0.05, 'pad_r':0.05}

fn_list = [FN01,FN02,FN03,FN06,FN07,FN08,FN09,FN10,FN11,FN12,FN13,FN14,FN15,FN16,FN17,FN18,FN19]
#fn_list = [FN01,FN02]

for notebook in fn_list:
    repaginate_notebook(nb_base_path=input_path, nb_params=notebook)