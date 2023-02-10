from photosetup import photo_loader

def test_is_file_image_true():
    test_file = "/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/Jacek_red-9 75dpi.jpg"
    expected_result = True
    result = photo_loader.is_file_image(test_file)
    assert(result == expected_result)

def test_is_file_image_false():
    test_file = "/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/text.txt"
    expected_result = False
    result = photo_loader.is_file_image(test_file)
    assert(result == expected_result)

def test_show_metadata():
    test_file = "/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/Jacek_red-9 75dpi.jpg"
    expected_result = {'Iso': 100, 'Exposure': 1, 'Shutter_speed': 5.906891, 'Apperture': 2.970854}
    result = photo_loader.show_metadata(test_file)
    assert(result == expected_result)

#TODO test dla show_metadata, jeśli plik nie ma metadanych
#uyć image, oczekiwany rezultat, rezultat, assert

#TODO usunąc z foty tylko iso i zrobić test dla funkcji show_metadata bez iso