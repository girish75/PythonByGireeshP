import os
import sys
from PIL import Image

# grab first folder and second (new) folder argument
# check if new folder  exist, if not create
# loop through first folder
# Convert images to png
# save images to the new folder.
class InvalidArgument(Exception):
    pass

#if __name__ == "__main__":
try:
    first_folder_path = sys.argv[1]
    second_folder_path = sys.argv[2]
    if not os.path.exists(second_folder_path):
        print("Second argument does not exist..creating directory..")
        os.mkdir(second_folder_path)
    elif os.path.isfile(second_folder_path):
        print("Second argument is a file, it should be a folder of all the images required to be converted")
    # else:
    # isfolder2 = os.path.isdir(second_folder_path)
    # if isfolder2:
    #     print("Second argument is a folder")
    # else:
    #     print("Second argument is a file, it should be a folder of all the images required to be converted")
except IndexError as err:
    raise InvalidArgument("No folder name given, require source and destination folders")

for filename in os.listdir(first_folder_path):
    # print("first_folder_path =", first_folder_path)
    # print("File name",filename)
    img: object
    with Image.open(f'{first_folder_path}{filename}') as img:
        clean_name = os.path.splitext(filename)[0]
        #print(clean_name)
        img.save(f'{second_folder_path}{filename}.png', 'png')
        print(f"File converted and saved to the {second_folder_path}\\")
