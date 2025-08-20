import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataframe = pd.read_csv('zomato-data.csv')
print(dataframe.head())

# Data Cleaning and Preparation
def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

#Information about the DataFrame
print("Information of the DataFrame:")
print(dataframe.info())

# Check for missing values
print("Missing values in each column:")
print(dataframe.isnull().sum())


# Fill missing values in 'rate' with the mean
dataframe['rate'].fillna(dataframe['rate'].mean(), inplace=True)