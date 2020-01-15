# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:25:52 2019

@author: IMRAN
"""
import pandas as pd
import numpy as np

df=pd.read_csv("melbourne_dataset.csv")
#print(df.shape)

#to print 5 rows
#print(df.head())
#to check dType index, size 
#print(df.info())
 #to check all null values
#print(df.isnull().sum()) 
#to check null values in columns
#print(df.isnull().any(axis=0))
#to check null values in rows
#print(df.isnull().any(axis=1))

#to check rows with all missing values
#print(df.isnull().all(axis=1).sum())
#summimg up the missing values

#print(round(100*(df.isnull().sum()/len(df.index)),2))
#dropping columns with more no. of missing values
df = df.drop('BuildingArea', axis=1)
df = df.drop('YearBuilt', axis=1)
df = df.drop('CouncilArea', axis=1)
# have a look at the rows having more than 5 missing values.
df[df.isnull().sum(axis=1) > 5]

#we can remove the rows with (say) more than 5 missing values.
#to find how many such rows are there
len(df[df.isnull().sum(axis=1) > 5].index)
# retaining the rows having <= 5 NaNs
df = df[df.isnull().sum(axis=1) <= 5]

# look at the summary again
print(round(100*(df.isnull().sum()/len(df.index)), 2))
# removing NaN Price rows
df = df[~np.isnan(df['Price'])]
# look at the summary again
print(round(100*(df.isnull().sum()/len(df.index)), 2))

print(df['Landsize'].describe())
# removing NaNs in Landsize
df = df[~np.isnan(df['Landsize'])]

# rows having Lattitude and Longitude missing
df[np.isnan(df['Lattitude'])]

df.loc[:, ['Lattitude', 'Longtitude']].describe()
# imputing Lattitude and Longitude by mean values
# the variation is less thus using mean
df.loc[np.isnan(df['Lattitude']), ['Lattitude']] = df['Lattitude'].mean()
df.loc[np.isnan(df['Longtitude']), ['Longtitude']] = df['Longtitude'].mean()

df.loc[:, ['Bathroom', 'Car']].describe()

# converting to type 'category'
df['Car'] = df['Car'].astype('category')

# displaying frequencies of each category
df['Car'].value_counts()

#The most common value of Car is 2 
#imputing nans with 2
df.loc[pd.isnull(df['Car']), ['Car']] = 2

# converting to type 'category'
df['Bathroom'] = df['Bathroom'].astype('category')

# displaying frequencies of each category
df['Bathroom'].value_counts()

# imputing NaNs by 1
df.loc[pd.isnull(df['Bathroom']), ['Bathroom']] = 1

# look at the summary again
print(round(100*(df.isnull().sum()/len(df.index)), 2))


print(df.shape)
 