import os
from PIL import Image
from PIL.ExifTags import TAGS
import json

directory = './'

outputDirectory = "./testImages/images"
images = []
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file[-4:] == ".jpg" or file[-4:] == ".png":
            images.append(os.path.join(subdir, file))
    # read the image data using PIL


for imagePath in images:
    image = Image.open(imagePath)

    # extract EXIF data
    exifdata = image.getexif()

    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id).decode("utf-16")
        print(f"{tag:25}: {data}")  