import imghdr

def is_file_image(file_path: str) -> bool:
    # 1. Load a file from a file_path
    # file_image = open(file_path)
    # 2. Check file type
    detected_image_type = imghdr.what(file_path)
    if detected_image_type is None:
        return False
    if type(detected_image_type) == str:
        return True
    # 3. If type == image return True else return False

