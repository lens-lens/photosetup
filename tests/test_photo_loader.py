from photosetup import photo_loader


def test_is_file_image_true():
    test_file = "/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/image.png"
    expected_result = True
    result = photo_loader.is_file_image(test_file)
    assert(result == expected_result)


def test_is_file_image_false():
    test_file = "/Users/milenanapierala/Desktop/PROJECTS/photosetup/tests/text.txt"
    expected_result = False
    result = photo_loader.is_file_image(test_file)
    assert(result == expected_result)


    


