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


# First plot for restaurant types
plt.figure(figsize=(10, 6))
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.xticks(rotation=45)
plt.title("Distribution of Restaurant Types")
plt.tight_layout()
plt.show()

# Second plot for ratings
plt.figure(figsize=(10, 6))
sns.countplot(x=dataframe['rate'])
plt.xlabel("Restaurant Ratings")
plt.xticks(rotation=45)
plt.title("Distribution of Restaurant Ratings")
plt.tight_layout()
plt.show()

# Third plot for approximate cost
plt.figure(figsize=(10, 6))
sns.histplot(data=dataframe, x='approx_cost(for two people)', bins=30)
plt.xlabel("Approximate Cost for Two People")
plt.xticks(rotation=45)
plt.title("Distribution of Restaurant Costs")
plt.tight_layout()
plt.show()


# Fourth plot for restaurant types vs average ratings
plt.figure(figsize=(12, 8))
avg_ratings = dataframe.groupby('listed_in(type)')['rate'].mean().sort_values(ascending=True)
sns.barplot(x=avg_ratings.values, y=avg_ratings.index)
plt.xlabel("Average Rating")
plt.ylabel("Restaurant Type")
plt.title("Average Ratings by Restaurant Type")
plt.tight_layout()
plt.show()

# Fifth plot for online order distribution
plt.figure(figsize=(10, 6))
sns.countplot(x=dataframe['online_order'])
plt.xlabel("Online Order Available")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurants by Online Order Availability")
plt.tight_layout()
plt.show()

