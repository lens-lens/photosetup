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
    expected_result = {'ImageWidth': 1365, 'ImageLength': 2048, 'BitsPerSample': (16, 16, 16), 'Compression': 1, 'PhotometricInterpretation': 2, 'ResolutionUnit': 2, 'ExifOffset': 296, 'Make': 'SONY', 'Model': 'ILCE-7M3', 'Software': 'Adobe Photoshop 24.1 (Macintosh)', 'Orientation': 1, 'DateTime': '2023:01:18 18:04:33', 'SamplesPerPixel': 3, 'XResolution': 75.0, 'YResolution': 75.0, 'PlanarConfiguration': 1, 'ExifVersion': b'0231', 'ShutterSpeedValue': 5.906891, 'ApertureValue': 2.970854, 'DateTimeOriginal': '2023:01:15 20:56:46', 'DateTimeDigitized': '2023:01:15 20:56:46', 'BrightnessValue': 2.8609375, 'ExposureBiasValue': 0.0, 'MaxApertureValue': 2.96875, 'MeteringMode': 1, 'LightSource': 0, 'Flash': 16, 'FocalLength': 69.0, 'ColorSpace': 1, 'ExifImageWidth': 1365, 'FocalPlaneXResolution': 1677.41796875, 'FocalPlaneYResolution': 1677.41796875, 'OffsetTime': '+01:00', 'OffsetTimeOriginal': '+02:00', 'OffsetTimeDigitized': '+02:00', 'ExifImageHeight': 2048, 'FocalPlaneResolutionUnit': 3, 'FileSource': b'\x03', 'ExposureTime': 0.016666666666666666, 'FNumber': 2.8, 'SceneType': b'\x01', 'ExposureProgram': 1, 'CustomRendered': 0, 'ISOSpeedRatings': 100, 'ExposureMode': 1, 'SensitivityType': 2, 'WhiteBalance': 0, 'RecommendedExposureIndex': 100, 'LensSpecification': (24.0, 70.0, 2.8, 2.8), 'LensModel': 'FE 24-70mm F2.8 GM II', 'DigitalZoomRatio': 1.0, 'FocalLengthIn35mmFilm': 69, 'SceneCaptureType': 0, 'Contrast': 0, 'Saturation': 0, 'Sharpness': 0}
    result = photo_loader.show_metadatas(test_file)
    assert(result == expected_result)