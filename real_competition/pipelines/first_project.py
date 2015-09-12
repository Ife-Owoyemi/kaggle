import pipelineManager as pm

###########################
# This is how you name a project then just load the data!
project = pm.PipelineManager("Kaggle Submission 1")
# default: project.submit = false
# Save the output format for creating submissions from predictions
# A sample submission should be present in the file for this to work

# Loading all the input data- In this case it is featured and can be split into train and cross validation set
project.load_featured_data()
print "Loaded data"
###########################
# Here we do some feature modification
# We set the parameters, though we dont have to set all of them because the defaults are registered.
# We do have to set the non default ones.

fmas = pm.PCAWrapper("FR")
print "Made Wrapper"
project.FMMethod(fmas)
print "Called PCA"
###########################
# Now we try a prediction model
paw = pm.KNNWrapper("FR")
print "Made Wrapper"
project.PAMethod(paw)
print "Called KNN"
project.write_compressed_submission()
print "Write submission"

