import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

# The competition datafiles are in the directory ../input
# Read competition data files:
train = pd.read_csv("train.csv")
test  = pd.read_csv("test.csv")


train_x = train.values[:,1:]
train_y = train.ix[:,0]
test_x = test.values

pca = PCA(n_components=0.8)
train_x = pca.fit_transform(train_x)
test_x = pca.transform(test_x)


neigh = KNeighborsClassifier(n_neighbors=4)
neigh.fit(train_x, train_y)

test_y = neigh.predict(test_x)
pd.DataFrame({"ImageId": range(1,len(test_y)+1), "Label": test_y}).to_csv('out.csv', index=False, header=True)
        
