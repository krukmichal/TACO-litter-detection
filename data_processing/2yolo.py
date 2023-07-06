import os
import shutil
import json

def coco2yolo(category,bbox,size):
    a,b,width,height = bbox
    img_width,img_height = size

    x = (a+width/2)/img_width 
    y = (b+height/2)/img_height

    new_width = width/img_width
    new_height = height/img_height

    return [category,x,y,new_width,new_height]


def move_files_and_create_labels(annotations_file_name, prefix):
    
    new_img_path = "output/images/"
    new_ano_path = "output/labels/"
    path = "output/"

    directories = [path, new_img_path, new_ano_path]

    for directory in directories:
        if not os.path.exists(directory):
            os.mkdir(directory)

    with open(annotations_file_name) as annotations_file:
        annotations = json.load(annotations_file)
        sizes = dict()
         
        for data in annotations["images"]:
            id = data['id']
            source = data['file_name']
            destination = new_img_path + prefix + "_" + str(id)+".jpg"
            width = data['width']
            height = data['height']
            sizes[id] = (width, height)
            shutil.copy("data/" + source, destination)
            
        for data in annotations["annotations"]:
            image_id = data['image_id']
            category_id = data['category_id']
            output = new_ano_path + prefix + "_" + str(image_id) + ".txt"
            bbox = data["bbox"]

            lst = coco2yolo(category_id, bbox, sizes[image_id])
            newline = ""

            for l in lst:
                newline+=str(l)+" "
            newline+= "\n"

            with open(output, "a") as f:
                f.write(newline)

if __name__ == "__main__":
    print("test")
    move_files_and_create_labels("data/annotations.json", "official")