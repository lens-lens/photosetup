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

def show_metadata(file_path: str) -> int: 
    img = Image.open(file_path)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    if exif is None:
        logger.warning('Obrazek nie ma podanych metadanych')
        return None
    # iso = exif.get('ISOSpeedRatings', 'Brak ISO')
    # exposure = exif.get('ExposureProgram', 'Brak ekspozycji')
    # shutter_speed = exif.get('ShutterSpeedValue', 'Brak czasu migawki')
    # apperture = exif.get('ApertureValue', 'Brak przysłony')
    
    metadata = {
    'Iso' : exif.get('ISOSpeedRatings', 'Brak ISO'),
    'Exposure' : exif.get('ExposureProgram', 'Brak ekspozycji'),
    'Shutter_speed' : exif.get('ShutterSpeedValue', 'Brak czasu migawki'),
    'Apperture' : exif.get('ApertureValue', 'Brak przysłony'),
    }
    return metadata

# ponizszy kod nie wykona się w nowym .py przy importowaniu tego pliku .py
if __name__ ==  "__main__":
    a = '/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/Jacek_red-9 75dpi.jpg' 
    result = is_file_image(a)
    print(result)
    show = show_metadata(a)
    print(show)