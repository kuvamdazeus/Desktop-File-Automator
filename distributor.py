#! /usr/bin/env python3
import re, os, sys
def process_destination():
    try:
      file = open("file_addresses.txt")
    except Exception:
      print("File file_addresses.txt was not found, make sure it is in the same directory as the distributor.py is")
      sys.exit(1)
    place_pattern = r"\s?:\s?([a-zA-Z0-9\-/_]+)" # pattern to extract the file name from file_addresses.txt
    places = []
    for line in file:
        place = re.search(place_pattern, line)
        if place != None:
            places.append(place.group(1)) # extract and append in places list
    file.close()
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
    if len(files) is 0:
      print("Searching...")
    os.chdir("..")
    for file in files: # Extensions are most important, file which do not has extension will be left in distributor
        if file == "distributor.py" or file == "file_addresses.txt" or file == "setup.sh":
            continue
        if ".txt" in file and os.path.exists(text): # check the extension of file and then check if the given destination exists or not
            os.system("mv ./Distributor/{} {}".format(file, text))
            print("{} was transferred".format(file))
        elif ".py" in file and os.path.exists(python):
            os.system("mv ./Distributor/{} {}".format(file, python))
            print("{} was transferred".format(file))
        elif ".sh" in file and os.path.exists(bash):
            os.system("mv ./Distributor/{} {}".format(file, bash))
            print("{} was transferred".format(file))
        elif (".jpg" in file or "png" in file or ".jpeg" in file) and os.path.exists(image):
            os.system("mv ./Distributor/{} {}".format(file, image))
            print("{} was transferred".format(file))
    os.chdir("./Distributor")
    if len(os.listdir()) is 0:
        print("{} Files transfered successfully".format(len(files)))
        sys.exit(0)
    else:
        print("Remaining files: ")
        count = 0
        for file in os.listdir():
            count += 1
            print("{}. {}".format(file))
        sys.exit(0)

def main():
    move(process_destination())

while True:
  main()
