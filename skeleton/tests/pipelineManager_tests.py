# For naming conventions see the following article:
# http://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html
# For more information on nose testing, seek the following article:
# http://pythontesting.net/framework/nose/nose-fixture-reference/
from nose.tools import *
import os
import pandas as pd
from pandas import *
import numpy as np
from datetime import date
from nose import with_setup
# This has to be the name of the folder for the class
from predictionGuide import pipelineManager
# Need to add a module setup method
def setup_module(module):
    print os.getcwd()
    os.chdir("./../pipeline_manager_template/pipelines/")                
def teardown_module(module):
    print ("teardown_module after everything in this file")

class TestPipelineManager:         

    def setup(self):
        self.classPMInstance = pipelineManager.PipelineManager('PipelineManager')
        self.classPCAWrapper = pipelineManager.PCAWrapper("FR")
        self.classPMInstance.load_featured_data()
        self.classKNNWrapper = pipelineManager.KNNWrapper("FR")

    def test_Constructor_ConstructsObjectWithName_ObjectReturned(self):
        pmInstance = pipelineManager.PipelineManager('Test PipelineManager Instance')
        assert pmInstance.name == 'Test_PipelineManager_Instance'
        assert pmInstance.submit == False
        assert pmInstance.cross_percentage == .3

    def test_SplitTrainCsv_PartitionData_SplitData(self):
        self.classPMInstance.load_featured_data()
        assert self.classPMInstance.x_train[0][0] == 1
        assert self.classPMInstance.y_train[0] == 1
    def test_LoadFeaturedData_ReadDataFromCSVFile_DataLoaded(self):
    	self.classPMInstance.load_featured_data()
    	assert self.classPMInstance.num_features == 5
    	assert self.classPMInstance.num_examples == 2
        
    def test_LoadConfigFile_WithHeaderOneColumnConfig_DataLoaded(self):
	# Override Config File For Testing
	self.classPMInstance.CONFIG_FILE = "withHeaderOneColumn" + self.classPMInstance.CONFIG_FILE
        self.classPMInstance.FULL_CONFIG_FILE_PATH = os.path.join(self.classPMInstance.PROJECT_ROOT_DIR, self.classPMInstance.CONFIG_FILE)
        self.classPMInstance.load_config_file()
	# Should be header
        assert self.classPMInstance.header
	# Should be 0
        assert self.classPMInstance.pred_index == 0
    def test_LoadConfigFile_WithoutHeaderMultiColumnConfig_DataLoaded(self):
	# Override Config File For Testing
	self.classPMInstance.CONFIG_FILE = "withoutHeaderMultiColumn" + self.classPMInstance.CONFIG_FILE
        self.classPMInstance.FULL_CONFIG_FILE_PATH = os.path.join(self.classPMInstance.PROJECT_ROOT_DIR, self.classPMInstance.CONFIG_FILE)
        self.classPMInstance.load_config_file()
	# Should be header
        assert self.classPMInstance.header == False
	# Should be 0
        assert self.classPMInstance.pred_index == 1
    def test_WriteSubmissionOneColumnWithHeader_ProduceOutputFile_File(self):
        self.classPMInstance.y_test = range(1,10)
        # Make a data frame
	# Override what the config did for this test
        self.classPMInstance.header = True
        self.classPMInstance.pred_id = 1
        self.classPMInstance.SUBMISSION_FILE_SUFFIX = "_sample_submission_onecolumn_wheader"
	# Output the data frame into a file
        self.classPMInstance.write_submission();
	# Based on the template
	# Make Sure file existed
        submission = pd.read_csv(self.classPMInstance.get_submission_path())
        assert submission.shape[0] == 9
        assert submission.shape[1] == 1
    def test_WriteCompressedSubmissionOneColumnWithHeader_ProduceOutputFile_File(self):
        self.classPMInstance.y_test = range(1,10)
        # Make a data frame
        # Override what the config did for this test
        self.classPMInstance.header = True
        self.classPMInstance.pred_id = 1
        self.classPMInstance.SUBMISSION_FILE_SUFFIX = "_sample_submission_onecolumn_wheader"
        # Output the data frame into a file
        self.classPMInstance.write_compressed_submission();
        # Based on the template
        # Make Sure file existed
        submission = pd.read_csv(self.classPMInstance.FULL_SUBMISSION_PATH)
        assert submission.shape[0] == 9
        assert submission.shape[1] == 1
        # Not implemented
    def WriteSubmissionOneColumnWithoutHeader_ProduceOutputFile_File(self):
        self.classPMInstance.y_test = range(1,10)
        self.classPMInstance.SUBMISSION_FILE_SUFFIX = "_sample_submission_one_column_woheader"
        self.classPMInstance.write_compressed_submission();
        assert os.path.isfile(self.classPMInstance.OUTPUT_DIR + self.classPMInstance.name + self.classPMInstance.SUBMISSION_FILE_SUFFIX)
        submission = pd.read_csv(self.classPMInstance.OUTPUT_DIR + self.classPMInstance.name + self.classPMInstance.SUBMISSION_FILE_SUFFIX + ".gz")
        # Not implemented
    def WriteSubmissionMultipleColumnsWithHeader_ProduceOutputFile_File(self):
        self.classPMInstance.y_test = range(1,10)
        self.classPMInstance.header = True
        self.classPMInstance.SUBMISSION_FILE_SUFFIX = "_sample_submission_multicolumn_wheader"
        self.classPMInstance.write_compressed_submission();
        assert os.path.isfile(self.classPMInstance.OUTPUT_DIR + self.classPMInstance.name + self.classPMInstance.SUBMISSION_FILE_SUFFIX)
        submission = pd.read_csv(self.classPMInstance.OUTPUT_DIR + self.classPMInstance.name + self.classPMInstance.SUBMISSION_FILE_SUFFIX + ".gz")
        # Not implemented
    def WriteSubmissionMultipleColumnsWithoutHeader_ProduceOutputFile_File(self):
        self.classPMInstance.y_test = range(1,10)
        self.classPMInstance.SUBMISSION_FILE_SUFFIX = "_sample_submission_multicolumn_woheader"
        self.classPMInstance.write_compressed_submission();
        assert os.path.isfile(self.classPMInstance.OUTPUT_DIR + self.classPMInstance.name + self.classPMInstance.SUBMISSION_FILE_SUFFIX)
        submission = pd.read_csv(self.classPMInstance.OUTPUT_DIR + self.classPMInstance.name + self.classPMInstance.SUBMISSION_FILE_SUFFIX + ".gz")
    def test_FMMethod_RunStageCode_MethodReturn(self):
        self.classPCAWrapper.stage = "PF"
        assert_raises(TypeError, self.classPMInstance.FMMethod(self.classPCAWrapper))
        self.classPCAWrapper.stage = "FM"
        # The next method should not raise an exception
        self.classPMInstance.FMMethod(self.classPCAWrapper)
    def test_PAMethod_RunStageCode_MethodReturn(self):
        self.classKNNWrapper.stage = "PF"
        assert_raises(TypeError, self.classPMInstance.PAMethod(self.classKNNWrapper))
        self.classKNNWrapper.stage = "PA"
        # The next method should not raise an exception
        self.classPMInstance.PAMethod(self.classKNNWrapper)

class TestPCAWrapper: 
    def setup(self):
        self.classPMInstance = pipelineManager.PipelineManager('PipelineManager')
        self.classPCAWrapper = pipelineManager.PCAWrapper("FR")
        print("TestPipelineManger:setup() before each test method")

    def test_GenerateID_CreateString_EmptyString(self):
        string = "FMscikit-PCA"
        self.classPCAWrapper.generate_id()
        assert self.classPCAWrapper.method_id[0:len(string)] == string
        assert len(self.classPCAWrapper.method_id) > len(string)
    def test_ConstructorWithDefaultParams_CreateObject_DefaultParams(self):
        assert self.classPCAWrapper.user_id == "FR"
        assert self.classPCAWrapper.FUNCTIONNAME == "scikit-PCA"
        assert self.classPCAWrapper.method_notes == []
        assert self.classPCAWrapper.params["n_components"] == .8
        assert self.classPCAWrapper.params["copy"] == False
        assert self.classPCAWrapper.params["whiten"] == False
        assert self.classPCAWrapper.date == date.today()
        assert self.classPCAWrapper.stage == "FM"
    def test_Run_FeatureReduction_Arrays(self):
        d = {'A': [1, 2, 3],'B': [4, 5, 6]}
        temp_train = DataFrame(d)
        self.classPMInstance.x_train = temp_train.values[0:]
        self.classPMInstance.x_test = temp_train.values[0:]
        self.classPCAWrapper.run(self.classPMInstance)
        assert temp_train.values[0][0] != self.classPMInstance.x_train[0][0]
    def test_AddDefaults_FillInParameterHoles_CompleteMap(self):
        self.my_params = {'n_components': .8}
        self.classPCAWrapper = pipelineManager.PCAWrapper("FR", params = self.my_params)
        assert self.classPCAWrapper.params["whiten"] == False

class TestKNNWrapper: 
    def setup(self):
        self.classPMInstance = pipelineManager.PipelineManager('PipelineManager')
        self.classPMInstance.load_featured_data()
        self.classKNNWrapper = pipelineManager.KNNWrapper("FR")
        print("TestPipelineManger:setup() before each test method")

    def test_GenerateID_CreateString_EmptyString(self):
        string = "PAscikit-K Nearest Neighbors"
        self.classKNNWrapper.generate_id()
        assert self.classKNNWrapper.method_id[0:len(string)] == string
        assert len(self.classKNNWrapper.method_id) > len(string)
    def test_ConstructorWithDefaultParams_CreateObject_DefaultParams(self):
        assert self.classKNNWrapper.user_id == "FR"
        assert self.classKNNWrapper.FUNCTIONNAME == "scikit-K Nearest Neighbors"
        assert self.classKNNWrapper.method_notes == []
        assert self.classKNNWrapper.params["n_neighbors"] == 5
        assert self.classKNNWrapper.params["weights"] == "uniform"
        assert self.classKNNWrapper.params["algorithm"] == "auto"
        assert self.classKNNWrapper.params["leaf_size"] == 30
        assert self.classKNNWrapper.params["metric"] == "minkowski"
        assert self.classKNNWrapper.params["p"] == 2
        assert self.classKNNWrapper.params["metric_params"] == None
        assert self.classKNNWrapper.date == date.today()
        assert self.classKNNWrapper.stage == "PA"
    def test_Run_PredictionGeneration_Array(self):
        assert True
    def test_AddDefaults_FillInParameterHoles_CompleteMap(self):
        self.my_params = {'n_neighbors': 1}
        self.classKNNWrapper = pipelineManager.KNNWrapper("FR", params = self.my_params)
        assert self.classKNNWrapper.params["n_neighbors"] != 5
        assert self.classKNNWrapper.params["p"] == 2
