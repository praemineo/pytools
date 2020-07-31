from glob import glob
from tqdm import tqdm
import cv2

from random import random

flip_probability = 0.5
base_path = "images"
extentions = ['.png', '.jpg', '.jpeg']


for ext in extentions:
    glob_query = f"{base_path}/**/*{ext}"
    print(f"Searching for {glob_query}")

    img_paths = glob(glob_query, recursive=True)
    print(f"Found {len(img_paths)} images")

    flip_counter = 0
    skip_counter = 0

    for img_path in tqdm(img_paths):
        # Randomness
        if(flip_probability > random()):
            skip_counter += 1
            continue

        flip_counter += 1

        img = cv2.imread(img_path)
        img = cv2.flip(img, 1)
        new_img_path = img_path.replace(ext, f"_flipped{ext}")
        cv2.imwrite(new_img_path, img)

    print(f"Flipped {flip_counter} images & Skipped {skip_counter} images")
