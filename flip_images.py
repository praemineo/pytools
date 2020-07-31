from glob import glob
from tqdm import tqdm
import cv2
import argparse
from random import random


parser = argparse.ArgumentParser(
    description='Flip images in given directory and all its subdirectories.')
parser.add_argument("--base_path", "-bp",
                    help="Base path of images directory", required=True)
parser.add_argument("--flip_probability", "--fp", type=float,
                    help="Probability value for flipping images, must between 0 and 1", default=0.5)
args = parser.parse_args()


flip_probability = args.flip_probability
base_path = args.base_path
extentions = ['.png', '.jpg', '.jpeg']


for ext in extentions:
    glob_query = f"{base_path}/**/*{ext}"
    print(f"Searching for {glob_query}")

    img_paths = glob(glob_query, recursive=True)
    img_paths_len = len(img_paths)

    if(img_paths_len == 0):
        continue

    print(f"Found {img_paths_len} images")

    flip_counter = 0
    skip_counter = 0

    for img_path in tqdm(img_paths):
        # Randomness
        if(random() > flip_probability):
            skip_counter += 1
            continue

        flip_counter += 1

        img = cv2.imread(img_path)
        img = cv2.flip(img, 1)
        new_img_path = img_path.replace(ext, f"_flipped{ext}")
        cv2.imwrite(new_img_path, img)

    print(f"Flipped {flip_counter} images & Skipped {skip_counter} images")
