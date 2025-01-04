import os
import logging


class FileReader:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.info("FileReader initialized")

    def load_dir(self, dir_path):
        self.files = []
        if not os.path.isdir(dir_path):
            if not os.path.isfile(dir_path):
                raise Exception
            elif os.path.isfile(dir_path):
                self.files = [dir_path]

        if os.path.isdir(dir_path):
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    self.files.append(os.path.join(root, file))

        return self.files

    def import_files(self, loader):
        self.data = []
        for file in self.files:
            self.data.append(loader(file))
        return self.data
