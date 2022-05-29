# -*- coding: utf-8 -*-
"""Project : House Price Prediction using Machine Learning with Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MiOg14ah-fTUSCgMMNGBl73u5pBl43A5

# IMPORTING DEPENDENCIES
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRFRegressor
from sklearn import metrics

"""#IMPORTING THE BOSTON HOUSE PRICE DATASET"""

house_price_dataset = sklearn.datasets.load_boston()

house_price_dataset

"""# LOADING THE DATASET WITH PANDAS DATAFRAME"""

house_price_df = pd.DataFrame(data = house_price_dataset.data, 
                              columns=house_price_dataset.feature_names)

house_price_df.head()

"""#ADD THE TARGET COLOUMN TO THE DATASET"""

house_price_df['Price'] = house_price_dataset.target

house_price_df.head()

"""#CHECKING THE NUMBER OF ROWS & COLUMNS """

house_price_df.shape

"""#CHECKING FOR NULL VALUES IN THE DATA"""

house_price_df.isnull()

house_price_df.isna().sum()

"""#STATISTICAL MEASURES OF THE DATASET"""

house_price_df.describe()

"""#UNDERSTANDING THE CORRELATION BETWEEN VARIOUS FEATURES IN THE DATASET



1.   POSITIVE CORELATION 
2.   NEGATIVE CORELATION


"""

correlation = house_price_df.corr()

"""#CONSTRUCTING A HEATMAP TO UNDERSTAND CORRELATION BETWEEN VARIOUS FEATURES IN THE DATASET"""

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt=".1f", annot=True, annot_kws={"size":8}, cmap="Blues")

"""#SPLITTING THE DATA AND TARGET"""

X = house_price_df.drop(columns="Price", axis=1)
Y = house_price_df["Price"]

print(X)

print(Y)

"""#SPLITTING THE DATA INTO TRAINING AND TEST DATA

> Indented block


"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""#MODEL TRAINING



1.   XGBoost Regressor


"""

# Loading the model
model = XGBRFRegressor()

# Training the model with X_train
model.fit(X_train, Y_train)

"""#MODEL EVALUATION 



1.   PREDICTION ON TRAINING DATA


"""

# Accuracy for prediction on training data
training_data_prediction = model.predict(X_train)

training_data_prediction.shape

print(training_data_prediction)

# R SQUARED ERROR 
score_1 = metrics.r2_score(Y_train, training_data_prediction)


# MEAN ABSOLUTE ERROR
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print("R SQUARED ERROR:", score_1)
print("MEAN ABSOLUTE ERROR:", score_2)

"""# PREDICTION ON TEST DATA"""

# Accuracy for prediction on test data
test_data_prediction = model.predict(X_test)

print(test_data_prediction)

# R SQUARED ERROR 
score_1 = metrics.r2_score(Y_test, test_data_prediction)


# MEAN ABSOLUTE ERROR
score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("R SQUARED ERROR:", score_1)
print("MEAN ABSOLUTE ERROR:", score_2)

"""# VISUALIZE THE ACTUAL PRICES AND PREDICTED PRICES"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("ACTUAL PRICES")
plt.ylabel("PREDICTED PRICES")
plt.title("ACTUAL PRICE VS PREDICTED PRICE")
plt.figure(figsize=(10,10))
plt.show()

