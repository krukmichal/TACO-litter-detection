from  data_processing.to_yolo import move_files_and_create_yolo_boxes
from data_processing.split_data import split_data
from data_processing.swap_labels import swap_labels
from test_src.draw_bbox import draw_bbox_for_all_images
from utilities.change_images_size import change_size_all_images
import shutil
import os

def remove_recursively(name):
    if os.path.exists(name):
        shutil.rmtree(name)


if __name__ == "__main__":
    print("removing dirs")

    remove_recursively("output")
    remove_recursively("tacodataset_small_official_yolo_format")

    print("moving files")
    move_files_and_create_yolo_boxes("data/annotations.json", "official")

    print("resizing images")
    change_size_all_images()

    print("swaping labels")
    swap_labels()
    print("drawing bboxes for all images")
    draw_bbox_for_all_images() # for tests
    print("splitting data")
    split_data()

    shutil.copy("config.yaml", "tacodataset_small_official_yolo_format")

    print("making archive")
    shutil.make_archive("tacodataset_small_official_yolo_format", 'zip','tacodataset_small_official_yolo_format')

