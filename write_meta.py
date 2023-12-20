from pathlib import Path
import glob

from exiftool import ExifToolHelper
#input_path = '/media/jbest/data21/Carlquist_notebooks_repaginate/metadata_tests/test1/'
input_path = '/media/jbest/data21/Carlquist_notebooks_repaginate/paginated_tiffs/'



#output_directory = Path(input_path)
#output_directory = Path(input_path)
#images = glob.glob(input_path + '**/*.jpg', recursive = True)
images = glob.glob(input_path + '**/*.tif', recursive = True)

for image in images:
    image_path = Path(image)
    image_id = image_path.stem
    print(image_path)

    with ExifToolHelper() as et:
        et.set_tags(image,
            tags={
                'XMP:Creator': 'Sherwin Carlquist',
                'EXIF:Artist': 'Sherwin Carlquist',
                'EXIF:Copyright': '© Botanical Research Institute of Texas',
                'IPTC:CopyrightNotice': '© Botanical Research Institute of Texas',
                'XMP:Rights': '© Botanical Research Institute of Texas',
                'EXIF:DocumentName': image_id,
                'XMP:Title': image_id,
                'IPTC:ObjectName': image_id,
                'XMP:Source': 'Botanical Research Institute of Texas Library',
                'IPTC:Source': 'Botanical Research Inst. of Tx',
                'XMP:WebStatement': 'https://creativecommons.org/licenses/by/4.0/',
                'Photoshop:URL': 'https://creativecommons.org/licenses/by/4.0/',
                'XMP:UsageTerms': 'This work is licensed under CC BY 4.0.',

                
            },
            params=["-P", "-overwrite_original"]
        )
