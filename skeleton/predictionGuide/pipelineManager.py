# Finding the OS Typeimport hashlib
import pandas as pd
import gzip
import math
import platform
import os.path
import personalLibrary
import time
import xml.etree.ElementTree as ET
from datetime import date
from abc import ABCMeta, abstractmethod
from sklearn.decomposition import PCA, KernelPCA
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import hashlib
# Class Definition
class PipelineManager:
    'Common Base Class for all Project Predictions' # ClassName._doc_
    # Class Static Variables
    PROJECT_ROOT_DIR = ".."
    INPUT_DIR = os.path.join(PROJECT_ROOT_DIR, "data", "input")
    INTERMEDIARY_DIR = os.path.join(PROJECT_ROOT_DIR, "data", "intermediary")
    OUTPUT_DIR = os.path.join(PROJECT_ROOT_DIR,"data","output")
    SUBMISSION_FILE_SUFFIX = "submission"
    TRAIN_DATA = "train.csv"
    TEST_DATA = "test.csv"
    SAMPLE_SUBMISSION = "sample_submission.csv"
    FULL_SAMPLE_SUBMISSION_PATH = os.path.join(OUTPUT_DIR, SAMPLE_SUBMISSION)
    FULL_TRAIN_DATA_PATH = os.path.join(INPUT_DIR, TRAIN_DATA)
    FULL_TEST_DATA_PATH = os.path.join(INPUT_DIR, TEST_DATA)
    REPORTS_PATH = os.path.join(PROJECT_ROOT_DIR,"reports")
    CONFIG_FILE = "config.xml"
    FULL_CONFIG_FILE_PATH = os.path.join(PROJECT_ROOT_DIR,CONFIG_FILE)
    Y_COL = 0 # Assume that the the first column is the y label
    FULL_SUBMISSION_PATH = os.path.join(OUTPUT_DIR)
    def __init__(self, name, cross_percentage = .3):
        # This is used in writing the output so it cannot have spaces
        self.name = name.replace(" ", "_")
        self.load_config_file()
        self.submit = True
        self.cross_percentage = cross_percentage
        self.log = {"FG": [], "FM":[], "PA": [], "E": []}            
        self.event_count = 0
    def load_featured_data(self):
        # Check if the file for csv
        self.labeled_xy = pd.read_csv(personalLibrary.find_data_filename(PipelineManager.FULL_TRAIN_DATA_PATH))
        self.x_test = pd.read_csv(personalLibrary.find_data_filename(PipelineManager.FULL_TEST_DATA_PATH))
        self.num_features = self.labeled_xy.shape[1] - 1
        self.num_examples = self.labeled_xy.shape[0]
        self.split_train_csv()
    def split_train_csv(self):
        self.num_train_rows = math.floor(self.num_examples*(1 - self.cross_percentage))
        self.num_cross_val_rows = self.num_examples - self.num_train_rows
        self.x_train = self.labeled_xy.values[0:self.num_train_rows, 1:]
        self.x_cross_val = self.labeled_xy.values[self.num_train_rows:, 1:]
        self.y_train = self.labeled_xy.values[0:self.num_train_rows, self.Y_COL]
        self.y_cross_val = self.labeled_xy.values[self.num_train_rows:, self.Y_COL]
    def write_submission(self):
        self.compile_report()
        self.sample_submission = pd.read_csv(personalLibrary.find_data_filename(PipelineManager.FULL_SAMPLE_SUBMISSION_PATH))
        # Then see how many headers it has
        columns = self.sample_submission.columns.values.tolist()
        pd.DataFrame({columns[self.pred_index]: self.y_test}).to_csv(self.get_submission_path(), index=False, header=self.header)
        self.FULL_SUBMISSION_PATH = self.get_submission_path()
    def write_compressed_submission(self):
        self.write_submission()
        f_in = open(self.FULL_SUBMISSION_PATH, 'rb')
        f_out = gzip.open(self.FULL_SUBMISSION_PATH + '.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        os.remove(self.FULL_SUBMISSION_PATH)
        self.FULL_SUBMISSION_PATH = self.get_submission_path() + '.gz'
    def get_submission_path(self):
        return os.path.join(self.OUTPUT_DIR,self.name + self.SUBMISSION_FILE_SUFFIX + '.csv')
    def load_config_file(self):
        config_tree = ET.parse(self.FULL_CONFIG_FILE_PATH)
        config_root = config_tree.getroot()
        header = config_root.find('data').find('output').find('header').text
        if(header == 'True'):
            self.header = True
        elif(header == 'False'):
            self.header = False
        else:
            raise ValueError("config.xml header field incorrectly configured")
        pred_index = config_root.find('data').find('output').find('predIndex').text
        self.pred_index = int(pred_index)
    def FMMethod(self, object):
        stage = "FM"
        self.runAndLogMethod(object, stage)
    def PAMethod(self, object):
        stage = "PA"
        self.runAndLogMethod(object, stage)
    def runAndLogMethod(self, object,stage):
        if(object.STAGENAME != stage):
            # Return with error
            print function + object.name + " is not a valid parameter for the " + stage + "method because it is of stage " + object.stage + "\n"
        else:
            object.run(self)
            if(self.submit):
#                self.log_event(object)
                object.event_count = self.event_count
                self.event_count += 1
                self.log[stage].append(object)
            # Refactored
            '''if(self.new_method || !self.check_method(object.generate_id)):
                # Param nows what to do.
                object.run(self.train_x, self.train_y, self.test_x)
                if(self.submit):
                    self.log_event(object)
            else:
                # These parameters exist in the xml file, find them
                self.load_interm_data(self.name + "_" + self.version + "_" + object.name)'''
    def compile_report(self):
        root = ET.Element("pipeline")
        name = ET.SubElement(root, "pipelineName")
        name.text = "Process Name"
        version = ET.SubElement(root, "pipelineVersion")
        version.text = "0"
        for key in self.log.keys():
            stage = ET.SubElement(root, "stage"+ key)
            for entry in self.log[key]:
                entry.log(stage)
        tree = ET.ElementTree(root)
        tree.write(os.path.join(PipelineManager.REPORTS_PATH, self.name + ".xml"))
class Event:
    'General Class for logging behavior'
    __metaclass__ = ABCMeta
    def __init__(self, stage, funcname,  method_notes, user_id):
        self.user_id = user_id
        self.stage = stage
        self.name = funcname
        if not method_notes:
            self.method_notes = []
        self.date = date.today()
        self.event_count = None
    @abstractmethod
    def generate_id(self):
        self.method_id = self.stage + self.name 
        return self.method_id    
    @abstractmethod
    def gen_imp_id(self):
        raise NotImplementedError, "Event.gen_imp_id() is an abstract methdod"
    def add_defaults(self, params, defaults):
        if not params:
            self.params = defaults
        else:
            self.params = params
            for key in defaults:
                if key not in self.params:
                    self.params[key] = defaults[key]
    def log(self, stage):
        method = ET.SubElement(stage, "method")
        #method.set("eventCount", str(self.event_count))
        method.set("method_id", self.gen_imp_id())
        method_name = ET.SubElement(method, "methodName")
        method_name.text = self.name
        method_notes = ET.SubElement(method, "methodNotes")
        method_notes.text = ';'.join(self.method_notes)
        user_id = ET.SubElement(method, "userId")
        user_id.text = self.user_id
        date = ET.SubElement(method, "date")
        # date.text = self.date.strftime("%B %d, %Y")
        # This may need to be implemented separately
        params = ET.SubElement(method, "params")
        for param_name in self.params.keys():
            p = ET.SubElement(params, str(param_name))
            p.text = self.params[param_name]


class FeatureGenerator(Event):
    'Takes Raw Data and Produces Features' # ClassName._doc_
    __metaclass__ = ABCMeta
    STAGENAME = "FM"
    def __init__(self, funcname, method_notes, user_id):
        super(FeatureGenerator, self).__init__(FeatureGenerator.STAGENAME, funcname, method_notes, user_id)
    @abstractmethod
    def run(self):
        raise NotImplementedError, "FeatureGenerator.run() is an abstract methdod"
class PCAWrapper(FeatureGenerator):
    'Wrapper for scikit-learn pca function'
    FUNCTIONNAME = "scikit-PCA"
    DEFAULTPARAMS = {"n_components": .8, "copy": False, "whiten":False}
    def __init__(self,user_id, method_notes=None, params=None, parameter_notes=None):
        super(PCAWrapper, self).__init__(PCAWrapper.FUNCTIONNAME, method_notes, user_id)
        self.add_defaults(params,PCAWrapper.DEFAULTPARAMS)        
        if not parameter_notes:
            self.parameter_notes = []
    def generate_id(self):
        self.method_id = self.stage + self.name + self.gen_imp_id()
        return self.method_id
    def gen_imp_id(self):
        h = hashlib.md5(''.join('{}{}'.format(key, val) for key, val in sorted(self.params.items())))
        return h.hexdigest()
    def run(self,po):
        pca = PCA(n_components = self.params["n_components"],copy = self.params["copy"], whiten = self.params["whiten"])
        po.x_train = pca.fit_transform(po.x_train)
        po.x_test = pca.transform(po.x_test)
class PredictionAlgorithm(Event):
    'Takes Feature Data and Produces a Prediction' # ClassName._doc_
    STAGENAME = "PA"
    __metaclass__ = ABCMeta
    def __init__(self, funcname, method_notes, user_id):
        super(PredictionAlgorithm, self).__init__(PredictionAlgorithm.STAGENAME, funcname, method_notes, user_id)
    @abstractmethod
    def run(self):
        raise NotImplementedError, "PredictionAlgorithm.run() is an abstract methdod"
class KNNWrapper(PredictionAlgorithm):
    'Wrapper for scikit-learn pca function'
    FUNCTIONNAME = "scikit-K Nearest Neighbors"
    DEFAULTPARAMS = {"n_neighbors": 5, "weights": "uniform", "algorithm":"auto", "leaf_size": 30, "metric": "minkowski", "p": 2, "metric_params":None}
    def __init__(self, user_id, method_notes = None, params = None, parameter_notes = None):
        super(KNNWrapper, self).__init__(KNNWrapper.FUNCTIONNAME, method_notes, user_id)
        self.add_defaults(params, self.DEFAULTPARAMS)
        if not parameter_notes:
            self.parameter_notes = []
    def generate_id(self):
        self.method_id = self.stage + self.name + self.gen_imp_id()
        return self.method_id
    def gen_imp_id(self):
        h = hashlib.md5(''.join('{}{}'.format(key, val) for key, val in sorted(self.params.items())))
        return h.hexdigest()
    def run(self,po):
        if po.num_examples < 5:
            self.params["n_neighbors"] = po.num_examples - 1            
        # Makes the object with the parameters
        neigh = KNeighborsClassifier(n_neighbors = self.params["n_neighbors"], weights = self.params["weights"], algorithm = self.params["algorithm"], leaf_size = self.params["leaf_size"], metric = self.params["metric"], metric_params = self.params["metric_params"])
        neigh.fit(po.x_train,po.y_train)
        po.y_test = neigh.predict(po.x_test)
