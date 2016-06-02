from glob import glob


class Generator(object):
    def __init__(self):
        pass

    def list_files(self, source_path):
        return glob.glob(source_path)
