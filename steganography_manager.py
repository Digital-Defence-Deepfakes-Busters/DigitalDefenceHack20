import glob
from stegano import lsb
import os
import concurrent.futures
from PIL import Image

input_locations = [r"D:\ML Study Workspace\Hackathon - Data\data_sets\data_sets\hotel/" ,
r"D:\ML Study Workspace\Hackathon - Data\data_sets\data_sets\sea/", 
r"D:\ML Study Workspace\Hackathon - Data\data_sets\data_sets\tree/",
r"D:\ML Study Workspace\Hackathon - Data\data_sets\data_sets\mountain/"]

lookup = {
  "tree" : "sdfjksdj3234234s",
  "mountain" : "oio243234nsdf443",
  "sea" : "lopwrpw23834i445",
  "hotel" : "mnh876ertpow45bn"
}

def add_image_steganography(image_file):
    #print(image_file)

    try:
        key = ''
        if "tree" in image_file:
            key = 'tree'
        elif "mountain" in image_file:
            key = 'mountain'
        elif "sea" in image_file:
            key = 'sea'
        elif "hotel" in image_file:
            key = 'hotel'
    
        #print(lookup[key])
        if ".jpg"  in image_file.lower():
            #print(image_file)
            img = Image.open(image_file)
            img1 = img.convert("RGB")
            secret = lsb.hide(img1, lookup[key])
            secret.save("./valid_data/" + key + "/" + os.path.basename(image_file))

    except:
        print(" Error in processing the file ")    


    return True

def process_images(input_locations):
    for folder_location in input_locations:        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            image_files = glob.glob(folder_location + "*.*")
            for image_files, process_status in zip(image_files, executor.map(add_image_steganography, image_files)):
                #print(f"A Steganography for {image_files} was processed with status as {process_status}")
                str = "temp"


process_images(input_locations)

