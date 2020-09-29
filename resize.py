from tinify import tinify


SCALE_METHOD='scale'
FIT_METHOD='fit'
COVER_METHOD='cover'
THUMB_METHOD='thumb'
METHODS=[SCALE_METHOD, FIT_METHOD, COVER_METHOD, THUMB_METHOD]

def resize(API, image_path, new_image_path, width, height, method=SCALE_METHOD):
    tinify.key = API
    tinify.validate()
    source = tinify.from_file(image_path)
    resized = source.resize(
                method=method,
                width=width, 
                height=height
            )
    resized.to_file(new_image_path)
