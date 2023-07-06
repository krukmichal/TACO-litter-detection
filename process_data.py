from  data_processing.to_yolo import move_files_and_create_labels
from data_processing.split_data import split_data
from data_processing.swap_labels import swap_labels
import shutil


if __name__ == "__main__":
    print("start")
    shutil.rmtree("output")
    shutil.rmtree("tacodataset_small_official_yolo_format")
    move_files_and_create_labels("data/annotations.json", "official")
    swap_labels()
    split_data()
    shutil.make_archive("tacodataset_small_official_yolo_format", 'zip','tacodataset_small_official_yolo_format')

