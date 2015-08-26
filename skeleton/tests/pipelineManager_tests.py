# For naming conventions see the following article:
# http://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html
# For more information on nose testing, seek the following article:
# http://pythontesting.net/framework/nose/nose-fixture-reference/
from nose.tools import *
import os
from nose import with_setup
# This has to be the name of the folder for the class
from predictionGuide import pipelineManager

class TestPipelineManager: 

	def setup(self):
		print("TestPipelineManger:setup() before each test method")
		self.classPMInstance =  pipelineManager.PipelineManager('PipelineManager')

	def teardown(self):
		print("TestPipelineManger:teardown() after each test method")

	@classmethod
	def setup_class(cls):
		print os.getcwd()
		os.chdir("./../pipeline_manager_template/pipelines/")
		print("setup_class() before any methods in the class")

	@classmethod
	def teardown_class(cls):
		print("teardown_class() before andy methods in the class")

	def test_Constructor_ConstructsObjectWithName_ObjectReturned(self):
		pmInstance = pipelineManager.PipelineManager('Test PipelineManager Instance')
		assert pmInstance.name == 'Test PipelineManager Instance'
	# Our base method assumes 
		# headers in both test and train files
		# first column of train should be the prediction label
	def test_LoadFeaturedData_ReadDataFromCSVFile_DataLoaded(self):
		self.classPMInstance.load_featured_data()
		assert self.classPMInstance.num_features == 5
		assert self.classPMInstance.num_examples == 2


		
