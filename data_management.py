from pathlib import Path
from shutil import copy
import os


class DataManagement:
    project_path = os.getenv("APPDATA") + "/MSoftware/Invoice_generator/"
    seller_file_path = project_path + "Sellers/"
    buyer_file_path = project_path + "Buyers/"
    languages_file_path = project_path + "Languages/"

    def __init__(self):
        if Path(self.project_path).is_dir() is False:
            os.mkdir(self.project_path)
            copy("../utils/defaults.txt", self.project_path)

        if Path(self.seller_file_path).is_dir() is False:
            os.mkdir(self.seller_file_path)

        if Path(self.buyer_file_path).is_dir() is False:
            os.mkdir(self.buyer_file_path)

        if Path(self.languages_file_path).is_dir() is False:
            os.mkdir(self.languages_file_path)
            copy("../utils/english.txt", self.languages_file_path)
            copy("../utils/polish.txt", self.languages_file_path)
