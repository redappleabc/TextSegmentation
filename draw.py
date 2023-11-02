import cv2
import numpy as np
import os
import json
import shutil

src_path = "./images"
rect_path = "./ocr"
save_path = "./results"

if os.path.exists(save_path):
    shutil.rmtree(save_path)
os.mkdir(save_path)

files = os.listdir(src_path)
files.sort()

for file in files:
    path = os.path.join(src_path, file)
    image = cv2.imread(path)
    rect_file_path = os.path.join(rect_path, file + '.json')
    rect_data = []
    with open(rect_file_path, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        rect_data = data['readResult']['pages'][0]['lines']

    # Define the color of the rectangle (in BGR format)
    color = (0, 0, 255)  # Red in BGR

    # Define the thickness of the rectangle border (use -1 to fill the rectangle)
    thickness = 1

    for rect in rect_data:
        points = rect['boundingBox']
        top_left = (round(points[0]), round(points[1]))  # (x, y) of the top-left corner
        bottom_right = (round(points[4]), round(points[5]))  # (x, y) of the bottom-right corner

        # print(top_left, bottom_right)
        # Draw the rectangle on the image
        image = cv2.rectangle(image, top_left, bottom_right, color, thickness)

    # Save the modified image
    save_file_path = os.path.join(save_path, file)
    cv2.imwrite(save_file_path, image)
