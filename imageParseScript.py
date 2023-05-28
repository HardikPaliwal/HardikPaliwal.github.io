import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import json
import pathlib
import subprocess



directory = 'G:/My Drive/ai art/finished'
outputDirectory = "./images/"
pathlib.Path(outputDirectory).mkdir(parents=True, exist_ok=True) 
pathlib.Path(outputDirectory+ "thumbnails\\").mkdir(parents=True, exist_ok=True) 
pathlib.Path(outputDirectory+ "raw\\").mkdir(parents=True, exist_ok=True) 

manualPrompt = {
    "gog" : {
        "Model" : "midjourney-v4",
        "Prompt": "The fire magician attending magic school",
        "Negative Prompt" : "--",
        "Title": "The fire mage attending magic school"
    },
    "gog1" : {
        "Model" : "midjourney-v5",
        "Prompt": "Transparent ghost, salvador dali, mystery, swirls, small glitters, hyperrealism, high resolution, very sharp, highly detailed, fantasy, surreal --v 5",
        "Negative Prompt" : "--",
        "Title" : "The future seen in the past"
    }, 
    "gog3" : {
        "Model" : "midjourney-v5",
        "Prompt": "Man walking through a fantastical death valley near a river, in the style of james gilleard, stone sculptures, alex andreev, faceted forms, becky cloonan, impressive panoramas, gigantic scale --v 5 -- ar 9:16",
        "Negative Prompt" : "--",
        "Title" : "The Shattered Plains in 1000 years"
    },
    "gog4" : {
        "Model" : "midjourney-v5",
        "Prompt": "Colorized massive tower of Babel at night, slight waves, night sky in the style of graphic novel inspired illustrations, intricate landscapes, guatemalan art, # pixelart, poster art, sublime wilderness, high - contrast shading --ar 9:16 --v 5",
        "Negative Prompt" : "--",
        "Title" : "Ominous City by Night"
    },
    "gog_Surrealist_anime_illustrated_starry_night_painting_transorm_b48b9d77-5198-4587-b39f-9dccd92db4a4": {
        "Model" : "midjourney-v5",
        "Prompt": "Surrealist anime illustrated starry night painting transorming into reality cinematic shot, volumetric lighting, hayao miyazaki art style, studio ghibli style --ar 2:3 -q 2",
        "Negative Prompt": "--",
        "Title": "Start of an adventure 2"
    },
    "gog_Surrealist_anime_illustrated_starry_night_painting_transorm_3a2320d7-c289-4b29-b263-da19c191a48d": {
        "Model" : "midjourney-v4",
        "Prompt": "Surrealist anime illustrated starry night painting transorming into reality cinematic shot, volumetric lighting, hayao miyazaki art style, studio ghibli style --ar 2:3 --q 2",
        "Negative Prompt": "--",
        "Title": "Start of an adventure 1"
    },
    "gog_illustration_of_jupiter_clouds_by_dan_mumford_alien_landsca_38b12d18-bbd2-430e-b105-fba6c75e1cc5": {
        "Model" : "midjourney-v5",
        "Prompt": "Illustration of jupiter clouds by dan mumford, alien landscape and vegetation, epic scene, a lot of swirling clouds, high exposure, realistic, vibrant blue and orange tinted colors, uhd  --ar 9:16 --v 5",
        "Negative Prompt": "--",
        "Title": "In an alternate universe..."
    },
    "gog_Cyberpunk_city_view_from_afar_across_a_lake_Massive_city._E_5bd9746b-d0fc-404c-9328-e083cec149f7": {
        "Model" : "midjourney-v5",
        "Prompt": "Cyberpunk city view from afar across a lake, Massive city. Endless skyscrapers, Beautiful, bright and clear, futuristic, night time, large signage, cyberpunk colors, sky scrapers, without people, --ar 16:9 --v 5",
        "Negative Prompt": "--",
        "Title": "Chicago in 50 years"
    },
    "gog_Dreaming_the_cloudy_night_sky_dark_colors_fire_in_sky_illus_ad7ced97-126a-4819-b399-4e462d5233e5": {
        "Model" : "midjourney-v4",
        "Prompt": "Dreaming, the cloudy night sky, dark colors, fire in sky, illustration, artistic, background",
        "Negative Prompt": "--",
        "Title": "The Felon or the Victim?"
    },
    "gog_The_Magic_of_the_winter_solstice_magical_moment_Snow_cloudy_b3607336-cfa7-40e1-bf46-a4aec8c7d981": {
        "Model" : "midjourney",
        "Prompt": "The Magic of the winter solstice, magical moment, Snow, cloudy starry night, old oil painting, Rococo style, hunting atmosphere, fantasy, Dark fantasy, cinematic lighting, romantic atmosphere, divine, Ultra realistic, 4k, --ar 2:3",
        "Negative Prompt": "--",
        "Title": "Waiting"
    },
    "gog_road_leading_to_the_distance_artstation_night_dark_horror_a_bac2e4e4-0517-430d-bc45-433d7ab2cd9c": {
        "Model" : "midjourney-v5",
        "Prompt": "Road leading to the distance, artstation, night, dark horror, atmosphere, artgerm, greg rutkowski, red moon in the distance --v 5 --ar 2:3",
        "Negative Prompt": "--",
        "Title": "A Road better left untravelled"
    },
    "gog_Low_angle_image_of_magneto_in_a_tense_action_-_packed_scene_456bf1ce-43f5-4ad5-a619-18db9d3b17e0": {
        "Model" : "midjourney-v5",
        "Prompt": "Low angle image of magneto in a tense, action - packed scene, with explosive energy and bold dynamic composition, in the style of Ross Tran --ar 2:3 --v 5",
        "Negative Prompt": "--",
        "Title": "Magneto if he wasn't always catching L's"
    },
    "gog_Balrog_rushes_towards_the_viewer_fire_spitting_thick_black__6fa04709-eedb-46b5-8e17-a327059c9f9f": {
        "Model" : "midjourney-v5",
        "Prompt": "Balrog rushes towards the viewer, fire spitting, thick black smoke, dark fantasy style, in the style of ross tran --v 5 --ar 2:3",
        "Negative Prompt": "--",
        "Title": "Fire Mage Gladiator"
    },
    "gog_superman_shooting_lasers_from_his_eyes_in_the_style_of_ross_bd9b2132-5c6f-4136-8cdb-3c58372fe986": {
        "Model" : "midjourney-v5",
        "Prompt": "Superman shooting lasers from his eyes in the style of ross tran --ar 2:3 --v 5",
        "Negative Prompt": "--",
        "Title": "Homelander if he wasn't always catching L's"
    },
    "gog_Creepy_woman_with_the_venom_symbiote_dark_fantasy_in_the_st_e8e67085-75fe-4ba1-aaa5-128c7c92eda8": {
        "Model" : "midjourney-v5",
        "Prompt": "Man made up of lightning in the style Hajime Isayama& Alex Horley& Sergio Toppi --ar 2:3 --v 5",
        "Negative Prompt": "--",
        "Title": "Main Character Vibes"
    },
    "gog_a_blood_devil_in_the_style_Hajime_Isayama_Alex_Horley_Sergi_e758bfb5-51ae-4c36-9b8a-8e1cbfc539d0": {
        "Model" : "midjourney-v5",
        "Prompt": "Creepy woman with the venom symbiote, dark fantasy, in the style of ross tran --ar 1:2 --v 5",
        "Negative Prompt": "--",
        "Title": "Elizabeth holmes staring in venom"
    },
    "gog_man_made_up_of_lightning_in_the_style_Hajime_Isayama_Alex_H_f09529b1-e8ee-4328-8243-907cd94cd119": {
        "Model" : "midjourney-v5",
        "Prompt": "A blood devil in the style Hajime Isayama& Alex Horley& Sergio Toppi --ar 2:3 --v 5",
        "Negative Prompt": "--",
        "Title": "Blood and Dark"
    },
    "gog_God_in_the_style_of_Hajime_Isayama_Alex_Horley_Sergio_Toppi_5dea9f30-00e0-4706-bf5f-3ec63fab6703": {
        "Model" : "midjourney-v5",
        "Prompt": "God in the style of Hajime Isayama& Alex Horley& Sergio Toppi --ar 2:3 --v 5",
        "Negative Prompt": "--",
        "Title": "Hell's Pilgrim"
    },
    "gog_God_ascending_in_an_ethereal_gas_cloud_nebula_tarot_card_pa_a63377f0-8093-4dc6-a3d5-77405b8a8e99": {
        "Model" : "midjourney-v5",
        "Prompt": "God ascending in an ethereal gas cloud nebula, tarot card painted by yoann lossel and peter mohrbacher and with multiple matte black boarders on black paper background, gold foil accents --ar 2:3 --v 5",
        "Negative Prompt": "--",
        "Title": "Tarot 1"
    },
    "00052": {
        "Model" : "dreamshaperv4",
        "Prompt": "night festival, magical scene <lora:ruinsAndLight_v10:1>",
        "Negative Prompt": "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, blurry, draft, grainy",
        "Title": "A King's Dream"
    },
    "gog_Lithography_colourful_art_by_Michelangelo_god_of_wrath_stro_255f383e-f448-4850-aca7-5bb8fbfcecfc": {
        "Model" : "midjourney-v4",
        "Prompt": "Lithography colourful art by Michelangelo god of wrath, strom coming, huge waves, terrifying god of death judging in esoteric tantric hell Temple, huge mirror reflecting the past Concept art, wide angle shot, oriental fantasy, insanely detailed and intricate, golden ratio, hypermaximalist, matte painting, cinematic, cgsociety, moebius strip --ar 1:2 --q 2",
        "Negative Prompt": "--",
        "Title": "Something cool"
    },
    "gog_Lithography_colourful_art_by_Michelangelo_god_of_wrath_stro_e5425161-af6f-4154-b3e5-4a968ba181ca": {
        "Model" : "midjourney-v4",
        "Prompt": "Lithography colourful art by Michelangelo god of wrath, strom coming, huge waves, terrifying god of death judging in esoteric tantric hell Temple, huge mirror reflecting the past Concept art, wide angle shot, oriental fantasy, insanely detailed and intricate, golden ratio, hypermaximalist, matte painting, cinematic, cgsociety, moebius strip --ar 1:2 --q 2",
        "Negative Prompt": "--",
        "Title": "The pilgrim"
    },
    "gog_Shimmering_crystalline_man_by_bujbal--v_5_95517778-fd76-49d2-822d-f11eedadf498": {
        "Model" : "midjourney-v5",
        "Prompt": "Shimmering crystalline man by bujbal",
        "Negative Prompt": "--",
        "Title": "Mankind's Reckoning"
    },
    "gog_A_painting_on_black_paper_showing_a_beautiful_night_sky_and_9136bf3a-0f42-4964-9952-6cf20e6d9dc1": {
        "Model" : "midjourney-v5",
        "Prompt": "A painting on black paper showing a beautiful night sky and a village, in the style of art nouveau organic flowing lines, futuristic chromatic waves, intricate and bizarre illustrations, swirling vortexes, detailed character illustrations, colorful turbulence, high resolution",
        "Negative Prompt": "--",
        "Title": "Fate Mechanics"
    },

}

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
        fileName = imagePath.split(os.sep)[-1][0:-4]
        image = Image.open(imagePath)
        metadata = {"Model" : "--", "Prompt": "--", "Negative Prompt": "--", "Steps": "--", "Sampler": "--", "CFG scale": "--", "Seed": "--", "Model": "--", "Date": os.path.getmtime(imagePath)}
        commandToThumbnail = "magick \"" + imagePath + "\" -thumbnail 400x400^ -gravity center -extent 400x400 -strip -quality 80  -interlace JPEG \"" + outputDirectory + "thumbnails\\" + fileName +".jpg\""
        commandToJpg = "magick \"" + imagePath + "\"  \"" + outputDirectory + "raw\\" + fileName +".jpg\""
        run(commandToThumbnail)
        run(commandToJpg)

        imagesMetaData[fileName+".jpg"] = metadata

        if (len(fileName) > 3 and fileName[0:3] == "gog"):
            metadata["Model"] = "midjourney"
            metadata["Prompt"] = manualPrompt[fileName]["Prompt"]
            metadata["Title"] = manualPrompt[fileName]["Title"]
            continue
        if (not "parameters" in image.text):
            print(fileName)
            metadata["Model"] = manualPrompt[fileName]["Model"]
            metadata["Prompt"] = manualPrompt[fileName]["Prompt"]
            metadata["Title"] = manualPrompt[fileName]["Title"]
            continue

        toParse = image.text["parameters"]
        if (len(toParse.split('\n')) > 1):
            metadata["Prompt"] = toParse.split('\n')[0]
            metadata["Negative Prompt"] = toParse.split('\n')[1][16:]
        metadata["Steps"] = toParse.split('Steps: ')[1].split(',')[0]
        metadata["Sampler"] = toParse.split('Sampler: ')[1].split(',')[0]
        metadata["CFG scale"] = toParse.split('CFG scale: ')[1].split(',')[0]
        metadata["Seed"] = toParse.split('Seed: ')[1].split(',')[0]
        metadata["Model"] = toParse.split('Model: ')[1].split(',')[0]

    except Exception as e:
        # print(fileName)
        # print(image.text)
        # break
        # print(e)
        pass

json_object = json.dumps(imagesMetaData, indent=4)
with open(outputDirectory + "images_metadata.json", "w") as outfile:
    outfile.write(json_object)