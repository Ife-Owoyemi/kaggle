import pandas as pd
import gzip
from sklearn.decomposition import PCA, KernelPCA
from sklearn import svm
# Run PCA Function####################
# Arguments for tuning variance explanation threshold
test_threshold = 0
default_threshold = .8
starting_threshold = .8
interval = .01
num_intervals = 15 # starting_threshold + interval* num_intervals <= 1
# Arguments for kernel
test_kernels = 0
default_kernel = 'rbf'
kernel_types = ["linear", "poly", "rbf", "sigmoid"]

if(starting_threshold + interval*num_intervals > 1):
    print "Your PCA threshold will exceed 100"
# The competition datafiles are in the directory ../input
train = pd.read_csv("../data/input/train.csv")
test  = pd.read_csv("../data/input/test.csv")

# Train Set
train_x = train.values[1:33600,1:]
train_y = train.values[1:33600,0]
# Cross Val Set
cval_x = train.values[33601:,1:]
cval_y = train.values[33601:,0]
# Test Set
test_x = test.values
most = 0;
# PCA Test function

# returns optimal parameter
# consider a wrapping function for the prediction algorithms.  In theory, they should be classes, that you set the parameters to as you find the optimal ones.ch
#def PCA(, [):

if(test_threshold):
    # Loop through a predetermed amount of ranges
    for i in range(0,num_intervals):
        print i;
        # Reducing Dim
        pca = PCA(n_components = starting_threshold + i*interval, whiten = True)
        train_x_i = pca.fit_transform(train_x)
        test_x_i = pca.transform(cval_x)
        # SVM
        svc = svm.SVC(kernel='rbf',C=10)
        # Training
        svc.fit(train_x_i, train_y)
        # Prediction
        test_y_i = svc.predict(test_x_i)
        # Calculating Accuracy
        correct = 0
        for j in range(0,8398):
            if(test_y_i[j] - cval_y[j]==0):
                correct += 1
                print correct
            if(correct > most):
                most = correct
                best_index = i
else:
    best_index = default_threshold
best_kernel = default_kernel
# Reducing Dim
pca = PCA(n_components = starting_threshold + best_index*interval, whiten = True)
train_x = pca.fit_transform(train_x)
test_x = pca.transform(test_x)
# SVM
svc = svm.SVC(kernel='rbf',C=10)
svc.fit(train_x, train_y)
test_y = svc.predict(test_x)
pd.DataFrame({"ImageId": range(1,len(test_y)+1), "Label": test_y}).to_csv('../data/output/out.csv', index=False, header=True)
f_in = open('../data/output/out.csv', 'rb')
f_out = gzip.open('../data/output/out.csv.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()
