import os
import glob
from tqdm.auto import tqdm
from PIL import Image, ImageOps

data_folder = r'data'
resized_folder = r'images'
if not os.path.exists(resized_folder):
    os.makedirs(resized_folder)

image_files = glob.glob(os.path.join(data_folder, '*.png'))
for image_file in tqdm(image_files):
    image = Image.open(image_file)
    image = ImageOps.fit(image, (256, 256), method=Image.Resampling.LANCZOS)
    resized_image_path = os.path.join(resized_folder, os.path.basename(image_file))
    image.save(resized_image_path)
