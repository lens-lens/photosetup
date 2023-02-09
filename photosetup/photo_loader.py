import imghdr
from loguru import logger
from PIL import Image, ExifTags

def is_file_image(file_path: str) -> bool:
    logger.debug(f'Dostałam ściezkę {file_path}')
    detected_image_type = imghdr.what(file_path)
    logger.debug(f'Wykryty typ obrazka to {detected_image_type}')
    if detected_image_type is None:
        logger.warning('Plik nie jest obrazkiem')
        return False
    if type(detected_image_type) == str:
        return True

def show_iso(file_path: str) -> int:
    img = Image.open("/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/Jacek_red-9 75dpi.jpg")
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    return exif["ISOSpeedRatings"]

# ponizszy kod nie wykona się w nowym .py przy importowaniu tego pliku .py
if __name__ ==  "__main__":
    a = '/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/Jacek_red-9 75dpi.jpg' 
    result = is_file_image(a)
    print(result)
    show = show_iso(a)
    print(show)