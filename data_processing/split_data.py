import os
import shutil
import random


def filename_jpg2txt(filename):
    return os.path.basename(filename[:filename.find(".")]+".txt")

def create_directories(path):
    splitted_datasets = ["train/", "val/", "test/"]
    datatypes = ["images/", "labels/"]

    for datatype in datatypes:
        for dataset in splitted_datasets:
                os.makedirs(path+datatype+dataset, exist_ok=True)


def split_data():
    path = "tacodataset_small_offcial_yolo_format/"
    create_directories(path)

    images = os.listdir("output/images")
    random.shuffle(images)
    
    for i in range(len(images)):
        image = images[i]
        label = filename_jpg2txt(image)

        if i % 10 == 1:
            shutil.copy("output/images/"+image, path+"images/test/"+ image)
            shutil.copy("output/labels/"+label, path+"labels/test/"+ label)
        
        elif i % 10 == 2:
            shutil.copy("output/images/"+image, path+"images/val/"+ image)
            shutil.copy("output/labels/"+label, path+"labels/val/"+ label)
        
        else:
            shutil.copy("output/images/"+image, path+"images/train/"+ image)
            shutil.copy("output/labels/"+label, path+"labels/train/"+ label)

if __name__ == "__main__":
    split_data()