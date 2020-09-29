from tinify import tinify
import os


def tiny(API, src_path, dst_path, level):
    tinify.key = API
    tinify.validate()
    current_dir = os.curdir
    prev_path = src_path
    for l in range(1, level+1):
        dst_level_dir = os.path.join(dst_path, f"level-{l}")
        os.mkdir(dst_level_dir)
        for file in os.listdir(prev_path):
            filename = f"{str(file)}"
            src_filepath = os.path.join(prev_path, filename)
            dst_filepath = os.path.join(dst_level_dir, filename)
            source = tinify.from_file(src_filepath)
            source.to_file(path=dst_filepath)
            print(f"{src_filepath} => {dst_filepath}")
        prev_path = dst_level_dir
