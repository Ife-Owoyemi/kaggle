# Finding the OS Type
import pandas as pd
import gzip
import math
import platform
import os.path
import personalLibrary
import time
from datetime import date
if( platform.system() == "Windows"):
    SLASH = "\\"
else:
    SLASH = "/"

# Class Definition
class PipelineManager:
    'Common Base Class for all Project Predictions' # ClassName._doc_
    # Class Static Variables
    INPUT_PATH = ".." + SLASH + "data" + SLASH + "input" + SLASH
    TRAIN_DATA = "train.csv"
    TEST_DATA = "test.csv" 
    OUTPUT_PATH = ".." + SLASH + "data" + SLASH + "output" + SLASH
    INTERMEDIARY_PATH = ".." + SLASH + "data" + SLASH + "intermediary" + SLASH
    REPORT_PATH = "." + SLASH + "reports" + SLASH
    Y_COL = 0 ## keep in mind in case it moves
    def __init__(self, name):
        self.name = name
    def load_featured_data(self):
        # Check if the file for csv
        self.labeled_xy = pd.read_csv(personalLibrary.find_data_filename(PipelineManager.INPUT_PATH + PipelineManager.TRAIN_DATA))
        self.unlabeled_x = pd.read_csv(personalLibrary.find_data_filename(PipelineManager.INPUT_PATH + PipelineManager.TEST_DATA))
        self.num_features = self.labeled_xy.shape[1] - 1
        self.num_examples = self.labeled_xy.shape[0] 
