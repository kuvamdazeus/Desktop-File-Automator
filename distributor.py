#! /usr/bin/env python3
import re, os
def process_destination():
    file = open("file_addresses.txt")
    place_pattern = r"\s?:\s?([a-zA-Z/_~]+)"
    string_places = []
    places = []
    for line in file:
        place = re.search(place_pattern, line)
        places.append(place.group(1))
    file.close()
    print(places)
    return places

def move(places):
    text, python, bash, image = places
    print(text, python, bash, image)
    # check that the pattern is right or not
    # Try from here :)
    # search for "how to find the type of file in python3"
    os.chdir("./Distributor")
    files = os.listdir()
    os.chdir("..")
    print(files)
    for file in files:
        print(file)
        if file == "distributor.py" or file == "file_addresses.txt" or file == "setup.sh":
            continue
        if ".txt" in file and os.path.exists(text):
            os.system("mv ./Distributor/{} {}".format(file, text))
        elif ".py" in file and os.path.exists(python):
            os.system("mv ./Distributor/{} {}".format(file, python))
        elif ".sh" in file and os.path.exists(bash):
            os.system("mv ./Distributor/{} {}".format(file, bash))
        elif (".jpg" in file or "png" in file or ".jpeg" in file) and os.path.exists(image):
            os.system("mv ./Distributor/{} {}".format(file, image))

def main():
    move(process_destination())

main()