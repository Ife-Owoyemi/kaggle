Work flow
Each Project Managment(PM) object should be a unique attempt to create a prediction
The following are functions(maybe classes, but for now should I have them as functions) that have functions that take a PM object.
They take PM object because they manipulate the data or make prediction and need to write what they do to the log of the object, which in theory should help us generate a complete report of how the output  was developed from raw data to prediction.

If you give a PM to a feature generator(FG):
   It should put the feature at the end and give an explanation to the generation
If you give PM to a feature selector(FS):
   It creates a subset of the features to use in prediction
   It should store this as a set of indexes: The default should be all of the
   features
If you give PM to a prediction algorithm(PA):
   It should know run it on the set of features
If you give PM to the ensembles(E):
   It should know to run based on the features

Here are the basic function/Class contracts
PM class Responsibilities
	abstract away the input and output of the data to the correct folder
	Separate training data into train and cross validation set
	track data manipulation and print report
	       Different logs for different types of transformations 
	       described below that should just be compiled together
	visualize data(later feature) 	

Feature generator
	Reponsible for turning raw data into features
	

Feature Selector
	Responsible for selecting a number of features 
	dimensionality reduction falls into this

Prediction Algorithm
	Takes in feature data and returns a prediction

Ensemble
	Takes in data and a set of learning algorithms and returns a prediction.
#######
The following is the thought process that brought me to the above workflow.
Its mostly random stuff, but some of it is useful for understanding the general workflow
###### 
GENERIC WORK PIPELINE
RAW DATA - no features
    this data is not separated into features that are given to each example. 
    instead often this data is mixed behavior of many features

Featured data
	 Has the convention that it can be formatted into matrices
	 There should be a train and test data. and the column of the train 
	 data should be the label for the examples
	 This data is ready to be used in prediction.
	 But we can also do different things with this data.
	 Such as feature selection
	 Add new features based on the existing or from the raw data.

Precition Step
	  Select what features you want to use
	  intermediary file if necessary.
	  predict and track out come

Ensemble method should track what total input data it used
	 prediction score report
END PIPELINE
########
So I want to write a class for prediction
Why?
Well it would be useful in that if would import evertything we need for data mining.
For datat mining we often have raw data

We write to find predictions
first we find features
The we use an algorithm to predict
Now we do that with several algorithems == Ensembling

Wrapper Function for SciKit function calls
	These simply take parameters and gives a result.
	Thats all it does, take data, parameters
	The reason to wrap the function is so that we can log what was done to the data

!!!We need good portability for prediction methods

as a class, we can call
object that takes inputs as data, train, test
it should separate train, cv.
our class would know where to put the data and find the data

Project
constructors take string
read input data
separate into 
	 train
	 csv
hard coded
     input data folder path
     intermediary data folder path
     output data folder path

save data state output to .....


ideal situation
      open object
      	   load previous work for problem
	   want to then work

want to prevent
     repeating methods
     keep as little data as possible

Each repository should have a me.txt file to state who they are.

What to ask yourself
     is the data ready for prediction?

you can alter model or alter the data
model alteration
      the model still has the same type of output and input

The thing about data alterations
    is nothing I guess
    it should be equally as portable
    so what promise should methods that alter data make?
    Theses are those that create features


Now I am wondering how to manage portability

file structure should preview what type of data is available and give a brief on that data

if a new feature is created we should know how but also why

files should be queried to reduce work

but each submission should be its own script so that there is documentation to go along with it.

fine tuning???
     not sure how to save the fine tuning for a feature
     if null? test or provide? save in object, 

What should we do as a project evolves

the only thing that matters is when a submission is made

Every time a submission is made?
      how do we know if a submission is made?
      we ask... plan to submit? if so we write a report
      if not we dont

Should the program wait to accept double submissions?
Should ask?
maybe ask by name

This way we track the evolution of a file will need logging.
