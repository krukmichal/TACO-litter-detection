import json
import sys



def find_filenames_by_class(class_number):
    with open("data/annotations.json") as file:
        annotations = json.load(file)
        for data in annotations["annotations"]:
            category_id = data["category_id"]
            if int(category_id) == int(class_number):
                print("official_" + str(data["image_id"]) + ".txt")


if __name__ == "__main__":
    find_filenames_by_class(sys.argv[1])