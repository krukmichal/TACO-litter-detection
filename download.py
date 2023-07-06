'''
This script downloads TACO's images from Flickr given an annotation json file
Code written by Pedro F. Proenza, 2019
'''

import os.path
import argparse
import json
from PIL import Image
import requests
from io import BytesIO
import sys
import cv2

parser = argparse.ArgumentParser(description='')
parser.add_argument('--dataset_path', required=False, default= './data/annotations.json', help='Path to annotations')
args = parser.parse_args()

dataset_dir = os.path.dirname(args.dataset_path)

print('Note. If for any reason the connection is broken. Just call me again and I will start where I left.')

# Load annotations
with open(args.dataset_path, 'r') as f:
    annotations = json.loads(f.read())

    nr_images = len(annotations['images'])
    for i in range(nr_images):

        image = annotations['images'][i]

        file_name = image['file_name']
        url_original = image['flickr_url']
        url_resized = image['flickr_640_url']

        file_path = os.path.join(dataset_dir, file_name)

        # Create subdir if necessary
        subdir = os.path.dirname(file_path)
        if not os.path.isdir(subdir):
            os.mkdir(subdir)

        if not os.path.isfile(file_path):
            # Load and Save Image
            if_need_resizing=False
            response = None
            if url_resized != None:
                response = requests.get(url_resized)
            else:
                if_need_resizing=True
                response = requests.get(url_original)

            #img = Image.open(BytesIO(response.content))
            #if img._getexif():
            #    img.save(file_path, exif=img.info["exif"])
            #else:
            #    img.save(file_path)

            if response.status_code == 200:
                with open(file_path, "wb") as img:
                    img.write(response.content)
            else:
                print("response error")

            if if_need_resizing:
                img = cv2.imread(file_path)
                print("original dimensions: ", img.shape)
                scale = 640/max(img.shape[0], img.shape[1])
                width = int(img.shape[1]*scale)
                height = int(img.shape[0]*scale)
                dim = (width,height)

                resized = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)

                print("resized dimensions : ", resized.shape)
                cv2.imwrite(file_path, resized)
                print("resized: ", file_path)

        # Show loading bar
        bar_size = 30
        x = int(bar_size * i / nr_images)
        sys.stdout.write("%s[%s%s] - %i/%i\r" % ('Loading: ', "=" * x, "." * (bar_size - x), i, nr_images))
        sys.stdout.flush()
        i+=1

    sys.stdout.write('Finished\n')
