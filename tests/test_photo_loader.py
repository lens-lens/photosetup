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

def test_show_metadatas():
    test_file = "/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/Jacek_red-9 75dpi.jpg"
    expected_result = {'Iso': 100, 'Exposure': 1, 'Shutter_speed': 5.906891, 'Apperture': 2.970854}
    result = photo_loader.show_metadatas(test_file)
    assert(result == expected_result)

#TODO test dla show_metadatas, jeśli plik nie ma metadanych
