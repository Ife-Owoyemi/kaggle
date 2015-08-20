# Finding the OS Type
import pandas as pd
import gzip
import math
import platform
import os.path
import time
from datetime import date
if( platform.system() == "Windows"):
    SLASH = "\\"
else:
    SLASH = "/"

# Class Definition
class MLPipelineManager:
    'Common Base Class for all Project Predictions' # ClassName._doc_
    # Class Static Variables
    INPUT_PATH = ".." + SLASH + " data" + SLASH + " input" + SLASH
    TRAIN_DATA = "train.csv.zip"
    TEST_DATA = "test.csv.zip" 
    OUTPUT_PATH = ".." + SLASH + " data" + SLASH + " output" + SLASH
    INTERMEDIARY_PATH = ".." + SLASH + " data" + SLASH + " intermediary" + SLASH
    REPORT_PATH = "." + SLASH + "reports" + SLASH
    Y_COL = 0 ## keep in mind in case it moves
    def _init_(self, name)):
        self.percent_train = 80  # THE REST WILL BE USED FOR CROSS VALIDATION SET
        self.name = name
        self.method_id_array = [];
        self.load_report()
        self.report_array = {
        project.submit = False
        self.method_counter = 0;
        self.version = -1
    def load_raw_as_featured(self):
        self.labeled_xy = pd.read_csv(INPUT_PATH+TRAIN_DATA)
        self.unlabeled_x = pd.read_csv(INPUT_PATH+TEST_DATA)
        self.num_features = labeled_xy.shape[1]
        self.num_examples = labeled_xy.shape[0]
        self.split_train_csv()
        self.x_test = unlabeled_x.values
        self.y_test = unlabeled_x.values
    def write_compressed_submission(self):
        pd.DataFrame({self.label1: range(1,len(self.y_test)+1), self.label2: self.y_test}).to_csv(OUTPUT_PATH + self.name+'.csv', index=False, header=True)
        f_in = open(OUTPUT_PATH +self.name+'.csv', 'rb')
        f_out = gzip.open(OUTPUT_PATH +self.name + '.csv'+'.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
