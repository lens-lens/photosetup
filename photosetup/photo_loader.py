import imghdr
from loguru import logger

def is_file_image(file_path: str) -> bool:
    logger.debug(f'Dostałam ściezkę {file_path}')
    detected_image_type = imghdr.what(file_path)
    logger.debug(f'Wykryty typ obrazka to {detected_image_type}')
    if detected_image_type is None:
        logger.warning('Plik nie jest obrazkiem')
        return False
    if type(detected_image_type) == str:
        return True

# ponizszy kod nie wykona się przy importowaniu tego pliku
if __name__ ==  "__main__":
    a = '/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/image.png' 
    result = is_file_image(a)
    print(is_file_image)


