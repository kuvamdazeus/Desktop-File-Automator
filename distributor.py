#! /usr/bin/env python3
import re, os, sys
def process_destination():
    file = open("file_addresses.txt")
    place_pattern = r"\s?:\s?([a-zA-Z0-9\-/_]+)" # pattern to extract the file name from file_addresses.txt
    places = []
    for line in file:
        place = re.search(place_pattern, line)
        if place != None:
            places.append(place.group(1)) # extract and append in places list
    print(places)
    file.close()
    print(places)
    return places

def move(places): # places is the list of destinations provided in the file_addresses.txt
    try:
        text, python, bash, image = places
    except Exception:
        print("File file_addresses.txt was edited or is corrupted")
        sys.exit(1)
    # print(text, python, bash, image)
    # Try from here :)
    os.chdir("./Distributor")
    files = os.listdir()
    os.chdir("..")
    for file in files: # Extensions are most important, file which do not has extension will be left in distributor
        if file == "distributor.py" or file == "file_addresses.txt" or file == "setup.sh":
            continue
        if ".txt" in file and os.path.exists(text): # check the extension of file and then check if the given destination exists or not
            os.system("mv ./Distributor/{} {}".format(file, text))
        elif ".py" in file and os.path.exists(python):
            os.system("mv ./Distributor/{} {}".format(file, python))
        elif ".sh" in file and os.path.exists(bash):
            os.system("mv ./Distributor/{} {}".format(file, bash))
        elif (".jpg" in file or "png" in file or ".jpeg" in file) and os.path.exists(image):
            os.system("mv ./Distributor/{} {}".format(file, image))
    os.chdir("./Distributor")
    if len(os.listdir()) is 0:
        print("{} Files transfered successfully".format(len(files)))
    else:
        print("Remaining files: ")
        count = 0
        for file in os.listdir():
            count += 1
            print("{}. {}".format(count, file))
    os.chdir("..")

def main():
    move(process_destination())

main()