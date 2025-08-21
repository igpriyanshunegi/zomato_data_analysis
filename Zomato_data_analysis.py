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


# Create a figure with two subplots side by side
plt.figure(figsize=(15, 6))

# First subplot for restaurant types
plt.subplot(1, 2, 1)
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.xticks(rotation=45)
plt.title("Distribution of Restaurant Types")

# Second subplot for ratings
plt.subplot(1, 2, 2)
sns.countplot(x=dataframe['rate'])
plt.xlabel("Restaurant Ratings")
plt.xticks(rotation=45)
plt.title("Distribution of Restaurant Ratings")

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()