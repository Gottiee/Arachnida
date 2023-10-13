#!/usr/bin/env python3

from sys import argv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def error(err:str):
    print(err)
    exit(1)

def scorpion(path:str):
    try:
        image = Image.open(path)
    except FileNotFoundError:
        error("File not found")
    except Exception as e:
        error(e)
    print("Format:", image.format)
    shape = list(image.size)
    shape.append(image.mode)
    print("The shape of image is:", shape)

    exif_data = image.getexif()
    if len(exif_data) == 0:
        print("No EXIF data")
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name}: {value}")
    

    if 'GPSInfo' in exif_data:
        gps_info = exif_data['GPSInfo']
        for key in gps_info.keys():
            tag_name = GPSTAGS.get(key, key)
            print(f"GPS {tag_name}: {gps_info[key]}")
    else:
        print("No GPSInfo")
    image.show()


def main():
    """
Scorpion display basic attributes such as the creation date, as well as EXIF data.

usage : ./scorpion FILE1 [FILE2 ...]
    """
    if len(argv) < 2:
        error(main.__doc__)
    ar = argv[1:]
    for arg in ar:
        print(f"Analyse of {arg}")
        scorpion(arg)
        print("---")

if __name__ == "__main__":
    main()