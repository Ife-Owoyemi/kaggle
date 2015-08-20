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
# Methods for handling XML Logging
def xmlOpenTag(string):
    return "<" + string ">"
def xmlCloseTag(string):
    return "</" + string + ">"
def xmlBody(tag_array, body_array):
    xmlList = []
    for indx, entry in enumerate(tag_array):
        xmlList[indx] = xmlOpenTag(entry) + body_array[indx] + xmlCloseTag(entry) + "\n"
    return xmlList
def stringXmlBody(array):
    string = ""
    for entry in array:
        string += entry
    return string
# Class for all methods to inherit their loggin behavior. Preset
class Event:
    'General Class for logging behavior'
    def _init_(self):
        self.name = ""
        self.method_notes = ""
        self.user_id = ""
        self.date = ""
        self.parameter_notes = ""        
        self.stage = ""
        self.method_id = ""

    def generate_id(self):
        self.method_id = self.stage + self.name + self.parameter_names
        return self.method_id
    def log(self,MLPM_object):
        parameter_string = stringXmlBody(xmlBody(self.parameter_names, self.parameter_values))
        method_name
        message_body_tags =["methodName", "notes", "userId", "date", "params", "parameterNotes"]
        message_body = [self.name, self.method_notes, self.user_id , self.date , parameter_string , self.parameter_notes] 
        MLPM_object.log_body(xmlOpenTag("method") + message_body + xmlCloseTag("method"), self.stage)

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
        # Why do we have a load report?
        # The real thing we want to do is to check against an existing run of this file.
        # If there exists one by name then we should run it method by method to see where the discrepency is.
        # That is what the load report it.
        # It should then when its running.  Check against the previous report for changes, no code should run unless there is a change.
        self.method_id_array = [];
        self.load_report()
        # Create the dictionary with empty arrays and the appropriate keys
        self.report_array = {
        "FG": [],"FM": [], "PA":[], "E":[]
        }
        project.submit = False
        #  The log manager should deal with this 
        #    self.competition_name = ## need to do some file traversal here
        self.method_counter = 0;
        self.version = -1
    def check_method(self, method_id):
        if(self.method_id_array[self.method_counter] == method_id):
            self.method_counter+= 1
            self.new_method = False
            return False
        else: 
            self.new_method = True
            self.version += 1
            return True
    def get_submission_format(self):
        # Add a line that checks if there is a sample submission in the outputfile
        fo = open(OUTPUT_PATH + "sample.csv", "rw+")
        line = fo.readline()
        labels = line.split(",",2)
        self.ouput_label1 = labels[0]
        self.output_label2 = labels[1]
### Should we have unfeatured data we will deal with it then.
    def load_raw_as_featured(self):
        self.labeled_xy = pd.read_csv(INPUT_PATH+TRAIN_DATA)
        self.unlabeled_x = pd.read_csv(INPUT_PATH+TEST_DATA)
        self.num_features = labeled_xy.shape[1]
        self.num_examples = labeled_xy.shape[0]
        self.split_train_csv()
        self.x_test = unlabeled_x.values
        self.y_test = unlabeled_x.values  # just a placeholder
    # There are different ways to do cross validation.
    # K-fold cross-validation, K = 5, 10
    # leave out one cross validation # Very computationally expensive
    # Generalized Cross validation Method.
    def load_interm_data(self, filename):
        self.labeled_xy = pd.read_csv(INTERMEDIARY_PATH+filename+TRAIN_DATA)
        self.unlabeled_x = pd.read_csv(INTERMEDIARY_PATH+filename + TEST_DATA)
        self.num_features = labeled_xy.shape[1]
        self.num_examples = labeled_xy.shape[0]
        self.split_train_csv()
        self.x_test = unlabeled_x.values
        self.y_test = unlabeled_x.values  # just a placeholder
    def split_train_csv(self):
        self.num_train_rows = math.floor(self.num_examples*self.percent_train)
        self.num_cross_val_rows = self.num_examples - self.num_train_rows
        self.x_train = labeled_xy.values[0:self.num_train_rows, 1:]
        self.x_cross_val = labeled_xy.values[self.num_train_rows:, 1:]
        self.y_train = labeled_xy.values[0:self.num_train_rows, MLPipelineManager.Y_COL]
        self.y_cross_val = labeled_xy.values[self.num_train_rows:, MLPipeLineManager.Y_COL]
    def log_event(self,section,string):
        self.
    def load_report(self):
        # Reads the existing xml file to 
        #   method_id_array
        #   get version( version will be incremented if there is a difference in the method inputs)
        #       if there is no file, version is 0
        '''
        Outdated
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
        '''
    def compile_report(self):
        target = open(REPORT_PATH + self.name + ".txt", "w")
        for key in self.log_array:
            for entry in self.log_array(key):
                target.write(entry)
                target.write("\n")
        target.close()
    def write_compressed_submission(self):
        pd.DataFrame({self.label1: range(1,len(self.y_test)+1), self.label2: self.y_test}).to_csv(OUTPUT_PATH + self.name+'.csv', index=False, header=True)
        f_in = open(OUTPUT_PATH +self.name+'.csv', 'rb')
        f_out = gzip.open(OUTPUT_PATH +self.name + '.csv'+'.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
    # train_x, train_y, test_x for self
    def FGmethod(self, object):
        stage = "FG"
        if(object.STAGENAME != stage)
            # Return with error
            print function + object.name + " is not a valid parameter for the " + stage + "method because it is of stage " + object.stage + "\n"
        else:
            # Check for one of two things
            #   Has a new method been found previously
            #   is this a new method
            # If either of them is true then we have to run the method
            # Otherwise we continue
            if(self.new_method || !self.check_method(object.generate_id)):
                # Object should do work here
                self.train_x, self.train_y, self.test_x = object.run(self.train_x, self.train_y, self.test_x)
                if(self.submit):
                    self.log_event(object)
            else:
                self.load_interm_data(self.name + "_" + self.version + "_" + object.name)
                # It should do the equivalent
                # In this case load the latest data
                # which should have the name based on
                # pipeline + verion + method
    # Returns train_x, train_y, test_x to self
    def FMmethod(self, object):
        stage = "FM"
        if(object.STAGENAME != stage)
            # Return with error
            print function + object.name + " is not a valid parameter for the " + stage + "method because it is of stage " + object.stage + "\n"
        else:
            # Check for one of two things
            #   Has a new method been found previously
            #   is this a new method
            # If either of them is true then we have to run the method
            # Otherwise we continue
            if(self.new_method || !self.check_method(object.generate_id)):
                # The function wants to know
                self.train_x, self.train_y, self.test_x = object.run(self.train_x, self.train_y, self.test_x)
                if(self.submit):
                    self.log_event(object)
            else:
                self.load_interm_data(self.name + "_" + self.version + "_" + object.name)
    # Returns a parameter by name to the object
    def PFmethod(self, object):
        stage = "PF"
        if(object.STAGENAME != stage)
            # Return with error
            print function + object.name + " is not a valid parameter for the " + stage + "method because it is of stage " + object.stage + "\n"
        else:
                    # Check for one of two things
            #   Has a new method been found previously
            #   is this a new method
            # If either of them is true then we have to run the method
            # Otherwise we continue
            if(self.new_method || !self.check_method(object.generate_id)):
                # Param nows what to do.
                object.run(self.train_x, self.train_y, self.test_x)
                if(self.submit):
                    self.log_event(object)
            else:
                # These parameters exist in the xml file, find them
                self.load_interm_data(self.name + "_" + self.version + "_" + object.name)
    # Returns test_y to self
    def PAmethod(self, object_1, object_2):
        stage = "PA"
        if(object.STAGENAME != stage)
            # Return with error
            print function + object.name + " is not a valid parameter for the " + stage + "method because it is of stage " + object.stage + "\n"
        else:
                        # Check for one of two things
            #   Has a new method been found previously
            #   is this a new method
            # If either of them is true then we have to run the method
            # Otherwise we continue
            if(self.new_method || !self.check_method(object.generate_id)):
                self.train_y = object.work(self.train_x, self.train_y, self.test_x)
                if(self.submit):
                    self.log_event(object)
            else:
                # submission should exist in intermediary file if it was not the last submission
                self.load_interm_data(self.name + "_" + self.version + "_" + object.name)
                #pipeline + version + method_name
    # Can be done later
    def Emethod(self, object):
        stage = "E"
        if(object.STAGENAME != stage)
            # Return with error
            print function + object.name + " is not a valid parameter for the " + stage + "method because it is of stage " + object.stage + "\n"
            # Check for one of two things
            #   Has a new method been found previously
            #   is this a new method
            # If either of them is true then we have to run the method
            # Otherwise we continue
            if(self.new_method || !self.check_method(object.generate_id)):
                object.work(self)
                if(self.submit):
                    self.log_event(object)
            else:
                # submission should exist in intermediary file if it was not the last submission
                self.load_interm_data(self.name + "_" + self.version + "_" + object.name)
                #pipeline + version + method_name
    def create_report(self):
        # Need to add the name to the beginning of a number of entries in self.stage array.
        # Iterate over dictionary of stages that has arrays of entries
        report = open(self.name + ".xml", "w")
        report.write("%s\n" %xmlOpenTag(self.name))
        for stage in stages:
            report.write("\t%s\n" %xmlOpenTag(stage))
            for entry in stage
                report.write("\t")
                report.write("\t%s\n" %entry)
            report.write("\t%s\n"%xmlCloseTag(stage))
        report.write("%s\n",%xmlCloseTag(self.name))
        title = ID + ": " + Name
        # Loop through parameter list
        note = message

# These should be wrappers for the sci-kit functions
# They should have a dictionary of parameters, set to the initial default parameters but changed if we change them.
class FeatureGenerator( Event):
    'Takes Raw Data and Produces Features' # ClassName._doc_
    STAGENAME = "FG"
    def _init_(self,user_id,name = "", method_notes = None,params = None, parameter_notes = None,  ):
        self.user_id = user_id
        self.name = name
        if not method_notes:
            self.method_notes = []
        if not params:
            self.params = {}
        if not parameter_notes:
            self.parameter_notes = []
        self.date = date.today
        
        self.stage = ID

        self.method_id = ""
    def run():
class PCAwrapper(FeatureGenerator):
    'Wrapper for scikit-learn pca function'
    FUNCTIONNAME = "scikit-PCA"
    DEFAULTPARAMS = {"n_components": .8, "copy": False, "whiten":False}
    def _init_(self,user_id, method_notes = None,params = None, parameter_notes = None,  ):
        self.user_id = user_id
        self.name = FUNCTIONNAME
        if not method_notes:
            self.method_notes = []
        if not params:
            self.params = {}
        if not parameter_notes:
            self.parameter_notes = []
        # Generated by class or functions
        self.date = date.today
        self.stage = STAGENAME
        self.method_id = ""
    def run(self,po):
        pca = PCA(n_components = self.params["n_components"],copy = self.params["copy"], whiten = self.params["whiten"])
        po.train_x = pca.fit_transform(po.train_x)
        po.test_x = pca.transform(po.test_x)
    def addDefaults(self,params):
        for key in PCAwrapper.DEFAULTPARAMS:
            if key not in params:
                parmams[key] = PCAwrapper.DEFAULTPARAMS[key]
class FeatureSelector( Event):
    'Subsets Feature Data' # ClassName._doc_
    STAGENAME = "FS"
    def _init_(self):
    def run():
class ParameterFinder(Event):
    'Finds features for a given event'
    STAGENAME = "PF"
    def _init_(self):
class PredictionAlgorithm( Event):
    'Takes Feature Data and Produces a Prediction' # ClassName._doc_
    STAGENAME = "PA"
    def _init_(self):

    def run():
#Documentation can be found here.
#http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier
class KNNwrapper(PredictionAlgorithm):
    'Wrapper for scikit-learn pca function'
    FUNCTIONNAME = "scikit-KNearest Neighbors"
    DEFAULTPARAMS = {"n_neighbors": 5, "weights": "uniform", "algorithm":"auto", "leaf_size": 30, "metric": "minkowski", "p": 2, "metric_params":None}
    def _init_(self,user_id, method_notes = None,params = None, parameter_notes = None,  ):
        self.user_id = user_id
        self.name = FUNCTIONNAME
        if not method_notes:
            self.method_notes = []
        if not params:
            self.params = {}
        if not parameter_notes:
            self.parameter_notes = []
        # Generated by class or functions
        self.date = date.today
        self.stage = STAGENAME
        self.method_id = ""
        self.addDefaults(self.params)

    def run(self,po):
        # Makes the object with the parameters
        neigh = KNeighborsClassifier(n_neighbors = self.params[n_neighbors], weights = self.params["weights"], algorithm = self.params["auto"], leaf_size = self.params["leaf_size"], metric = self.params["metric"], metric_params = self.params["metric_params"])
        neigh.fit(po.train_x,po.train_y)
        po.test_y = neigh.predict(po.test_x)
    def addDefaults(self,params):
    for key in KNNwrapper.DEFAULTPARAMS:
        if key not in params:
            parmams[key] = PCAwrapper.DEFAULTPARAMS[key]
class Ensemble( Event):
    'Takes Feature Data and Produces a Prediction from many Prediction Models' # ClassName._doc_
    STAGENAME = "E "
    def _init_(self):    
    def run(self, po):

