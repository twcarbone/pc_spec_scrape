import json
import pprint


def get_amd_data():
   
    with open("tableExport.json") as js:
        d = json.load(js)

    for value in d.values():
        for item in value:
            for k, v in item.items():
                print("%s: %s" % (k, v))

            print("\n")

if __name__ == "__main__":
    get_amd_data()    
