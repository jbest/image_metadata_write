import exiftool

#files = ["SamTest_1_0055-AP.tif"]
#files = ['write_test.tif']
#files = ['carlquist_meta.tif']
#files = ['carlquist_meta_slack.tif']
files = ['/media/jbest/data21/Carlquist_notebooks_repaginate/metadata_tests/test1/BRIT-A-AR003-FN01_000.jpg']
with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(files)
    for d in metadata:
        for item in d:
            print(item, d[item])