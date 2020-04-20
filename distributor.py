#! /usr/bin/env python3
import os, re
def process_destination():
    file = open("file_addresses.txt")
    place_pattern = r"\s?:\s?([a-zA-Z/_])"
    places = []
    for line in file:
        place = re.search(place_pattern, line)
        places.append(place)
    file.close()
    return places

def move(places):
    text, python, bash, image = places
    text = text.group()
    python = python.group()
    image = image.group()
    # check that the pattern is right or not
    # Try from here :)
    # search for "how to find the type of file in python3"
    for file in os.listdir():
        if ".txt" in file and os.path.exists(text):
            os.system("mv {} {}".format(file, text))
        elif ".py" in file and os.path.exists(python):
            os.system("mv {} {}".format(file, python))
        elif ".sh" in file and os.path.exists(bash):
            os.system("mv {} {}".format(file, bash))
        elif (".jpg" in file or "png" in file or ".jpeg" in file) and os.path.exists(image):
            os.system("mv {} {}".format(file, image))

def main():
    move(process_destination())

main()