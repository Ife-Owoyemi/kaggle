import platform
if(platform.system() == "Windows"):
    slash = "\\"
else:
    slash = "/"

import sys
sys.path.insert(0,"../../../pythonModules")

import pm

###########################
# This is how you name a project then just load the data!
project = MLPipelineManager("Kaggle Submission 1")
# default: project.submit = false
# Save the output format for creating submissions from predictions
# A sample submission should be present in the file for this to work
project.get_submission_format()
# Loading all the input data- In this case it is featured and can be split into train and cross validation set
project.load_raw_as_featured()
###########################
# Here we do some feature modification
# We set the parameters, though we dont have to set all of them because the defaults are registered.
# We do have to set the non default ones.
pca_features = {"n_components": .8, "copy": False, "whiten":False}
fmas = PCAwrapper("FR",pca_features)
project.FMmethod(fmas)

'''
This is a multi line comment

'''
###########################
# Now we try a prediction model

paw = PredictionAlgorithmWrapper(param_names, param_values)
project.PAmethod(paw)

project.write_compressed_submission()

