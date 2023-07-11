import cv2
import matplotlib.pyplot as plt
import os

class_names = {
    0: "metal&plastic",
    1: "paper",
    2: "electronic",
    3: "glass",
    4: "bio",
    5: "other"
}

def yolo2xyxy(yolo_data, img_size):
    #print(yolo_data)
    center_x,center_y,width,height=yolo_data
    x1 = (center_x-width/2)*img_size[0]; 
    x1 = int(x1)
    y1 = (center_y-height/2)*img_size[1]; y1 = int(y1)
    x2 = x1 + width*img_size[0]; x2=int(x2)
    y2 = y1 + height*img_size[1]; y2=int(y2)
    
    return x1,y1,x2,y2

def filename_jpg2txt(filename):
    return os.path.basename(filename[:filename.find(".")]+".txt")

def get_boxes_from_txt(filename):
    boxes = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(" ")
            for i in range(len(data)):
                data[i] = float(data[i].strip("\n"))
            boxes.append(data)
    return boxes

def print_image_bbox(path, filename):
    print(path+filename)
    img = cv2.imread(path + filename)
    yolo_boxes = get_boxes_from_txt(filename_jpg2txt(filename))
    for yolo_box in yolo_boxes:
        box = yolo2xyxy(yolo_box[1:], [img.shape[1], img.shape[0]])
        start_point = (box[0],box[1])
        end_point= (box[2],box[3])
        cv2.rectangle(img, start_point, end_point, color=(0,255,0), thickness=1)
     
    plt.figure(figsize=(12,12))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
def save_image_bbox(input_path, filename, output_path):
    img = cv2.imread(input_path + "images/" + filename)
    label_name = input_path + "labels/" + filename_jpg2txt(filename)
    yolo_boxes = get_boxes_from_txt(label_name)
    for yolo_box in yolo_boxes:
        box = yolo2xyxy(yolo_box[1:], [img.shape[1], img.shape[0]])
        class_name = class_names[int(yolo_box[0])]
        start_point = (box[0],box[1])
        end_point= (box[2],box[3])
        cv2.rectangle(img, start_point, end_point, color=(0,255,0), thickness=1)
        cv2.putText(
            img,
            class_name,
            (box[0],box[3]),
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
            1,
            (255,0,0),
            1,
            cv2.LINE_AA)
        #cv2.rectangle(img, (400,0), end_point(700,200),color=(0,255,0), thickness=4)
     
    #plt.figure(figsize=(12,12))
    #plt.imsave(output_path + filename)
    cv2.imwrite(output_path+filename, img)

def draw_bbox_for_all_images():
    input_path = "output/"
    output_path = "output/test/"
    images = os.listdir(input_path+"images")
    os.makedirs("output/test", exist_ok=True)

    for image in images:
        save_image_bbox(input_path,image,output_path)
