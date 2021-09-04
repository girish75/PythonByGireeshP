import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo (1).jpg',
    'photo (2).jpg',
    'photo (3).jpg',
    'photo (4).jpg',
    'photo (5).jpg',
    'photo (6).jpg',
]

def process_image(img_name):
    size = (1200, 1200)
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

if __name__ == "__main__":

    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)


    end_time = time.perf_counter()

    print(f'Finished in {end_time-start_time} seconds')