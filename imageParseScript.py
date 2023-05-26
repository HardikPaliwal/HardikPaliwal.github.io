import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import json
import pathlib
import subprocess

directory = 'G:/My Drive/ai art/finished'
outputDirectory = "./images/"
pathlib.Path(outputDirectory).mkdir(parents=True, exist_ok=True) 

def run(cmd):
    subprocess.run(["powershell", "-Command", cmd])

images = []
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file[-4:] == ".jpg" or file[-4:] == ".png":
            images.append(os.path.join(subdir, file))

imagesMetaData= {}
for imagePath in images:
    try:
        fileName = imagePath.split(os.sep)[-1][0:-3]
        image = Image.open(imagePath)
        metadata = {}
        imagesMetaData[fileName+"jpg"] = {}
        commandToThumbnail = "magick \"" + imagePath + "\" -thumbnail 400x400^ -gravity center -extent 400x400 \"" + outputDirectory + "THUMBNAIL-" + fileName +"jpg\""
        commandToJpg = "magick \"" + imagePath + "\"  \"" + outputDirectory + fileName +"jpg\""
        run(commandToThumbnail)
        run(commandToJpg)

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

        imagesMetaData[fileName+"jpg"] = metadata

    except Exception as e:
        print(fileName)
        print(e)
        pass

json_object = json.dumps(imagesMetaData, indent=4)
with open(outputDirectory + "images_metadata.json", "w") as outfile:
    outfile.write(json_object)