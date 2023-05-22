import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import json

directory = 'G:/My Drive/ai art/finished'
outputDirectory = "./testImages/images"
images = []
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file[-4:] == ".jpg" or file[-4:] == ".png":
            images.append(os.path.join(subdir, file))
    # read the image data using PIL

imagesMetaData= {}
for imagePath in images:
    try:
        image = Image.open(imagePath)
        metadata = {}
        toParse = image.text["parameters"]
        metadata["Prompt"] = toParse.split('\n')[0]
        metadata["Negative Prompt"] = toParse.split('\n')[1][16:]
        lastRow = toParse.split('\n')[2]
        metadata["Steps"] = lastRow.split(': ')[1].split(',')[0]
        metadata["Sampler"] = lastRow.split(': ')[2].split(',')[0]
        metadata["CFG scale"] = lastRow.split(': ')[3].split(',')[0]
        metadata["Seed"] = lastRow.split(': ')[4].split(',')[0]
        metadata["Model"] = lastRow.split(': ')[7].split(',')[0]
        metadata["Denoising strength"] = lastRow.split(': ')[8].split(',')[0]

        print(json.dumps(metadata))
    except:
        pass
