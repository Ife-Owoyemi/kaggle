# Finding the OS Type
import pandas as pd
import gzip
import math
import platform
import os.path
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
    def _init_(name)):
        self.percent_train = 80  # THE REST WILL BE USED FOR CROSS VALIDATION SET
        self.name = name
        load_project_details()
    def load_project_details():
        fo = open(OUTPUT_PATH + "sample.csv", "rw+")
        line = fo.readline()
        labels = line.split(",",2)
        self.ouput_label1 = labels[0]
        self.output_label2 = labels[1]
### Should we have unfeatured data we will deal with it then.
    def load_raw_as_featured():
        self.labeled_xy = pd.read_csv(INPUT_PATH+TRAIN_DATA)
        self.unlabeled_x = pd.read_csv(INPUT_PATH+TEST_DATA)
        self.num_features = labeled_xy.shape[1]
        self.num_examples = labeled_xy.shape[0]
        self.split_train_csv()
        self.x_test = unlabeled_x.values
        self.y_test = unlabeled_x.values  # just a placeholder
    def split_train_csv()
        self.num_train_rows = math.floor(self.num_examples*self.percent_train)
        self.num_cross_val_rows = self.num_examples - self.num_train_rows
        self.x_train = labeled_xy.values[0:self.num_train_rows, 1:]
        self.x_cross_val = labeled_xy.values[self.num_train_rows:, 1:]
        self.y_train = labeled_xy.values[0:self.num_train_rows, MLPipelineManagerY_COL]
        self.y_cross_val = labeled_xy.values[self.num_train_rows:, MLPipeLineManagerY_COL]
    def add_to_log(section,string):
        self.log_array[section].append(string)
    def load_report():
        self.log_array = {"FG": [], "FS":[], "PA": [], "E": []}            
        if(os.path.exists(REPORT_PATH+self.name+".txt")):
            with open(OUTPUT_PATH + self.name + ".txt", "r") as file:
                for line in file:
                    if(line[0:2] == "FG"):
                        key == 0
                    else if (line[0:2] == "FS"):
                        key == 1
                    else if (line[0:2] == "PA"):
                        key == 2
                    else if (line[0:2] == "E "):
                        key == 3
                    else: 
                        self.log_array[pipe_options[key]].append(line)
    def compile_report():
        target = open(REPORT_PATH + self.name + ".txt", "w")
        for key in self.log_array:
            for entry in self.log_array(key):
                target.write(entry)
                target.write("\n")
        target.close()
    def write_compressed_submission():
        pd.DataFrame({self.label1: range(1,len(self.y_test)+1), self.label2: self.y_test}).to_csv(OUTPUT_PATH + self.name+'.csv', index=False, header=True)
        f_in = open(OUTPUT_PATH +self.name+'.csv', 'rb')
        f_out = gzip.open(OUTPUT_PATH +self.name + '.csv'+'.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()

