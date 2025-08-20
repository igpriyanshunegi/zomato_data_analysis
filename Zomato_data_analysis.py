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


# Visualizing the distribution of restaurant ratings
plt.figure(figsize=(10, 6))  # Optional: Set figure size for better visibility
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.title("Distribution of Restaurant Types")
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()  # Add this line to display the plot