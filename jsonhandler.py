##For Handling JSON data
import json

def jsonloader(inputfile):
    with open(inputfile, "r") as file:
        data = json.load(file)
        return data
        print(data)