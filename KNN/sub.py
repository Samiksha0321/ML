import pandas as pd
import numpy as np
import sklearn
from sklearn.utils import shuffle
from sklearn import linear_model, preprocessing
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("car.data")
print(data.head())