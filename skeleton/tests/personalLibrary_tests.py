# For naming conventions see the following article:
# http://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html
# For more information on nose testing, seek the following article:
# http://pythontesting.net/framework/nose/nose-fixture-reference/
from nose.tools import *
import os
from nose import with_setup
# This has to be the name of the folder for the class
from predictionGuide import personalLibrary

class TestPersonalLibrary: 

	def setup(self):
		print("TestPipelineManger:setup() before each test method")

	def teardown(self):
		print("TestPipelineManger:teardown() after each test method")

	@classmethod
	def setup_class(cls):
		os.chdir("tests/personalLibraryTestDir/")
		print("setup_class() before any methods in the class")

	@classmethod
	def teardown_class(cls):
                os.chdir("../..")
		print("teardown_class() before andy methods in the class")
		
	def test_FindDataFilename_ReadAllFiles_Data(cls):
		assert personalLibrary.find_data_filename("testcsv.csv") == "testcsv.csv"
		assert personalLibrary.find_data_filename("compressedtestcsv.csv") == "compressedtestcsv.csv.gz"
