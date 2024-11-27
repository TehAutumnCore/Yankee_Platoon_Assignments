# Curriculum
- https://github.com/Code-Platoon-Curriculum/curriculum/blob/main/06-AI-LLMs/3-working-with-data/1-working-with-data.md

# Pandas
- pip install pandas
- import pandas as pd

## Reading a CSV 
Load the dataset
- data = pd.read_csv('./water_potability.csv')
- print(data) 

## Using methods to view and manipulate data
#### grabs the column of ph
- data['ph']
#### grabs the column of Hardness
- data['Hardness']
#### grabs row 35
- data.iloc[35] 
#### grabs rows 1-25 (slice)
- data.iloc[1:25] 
#### check for missing values
- data.isnull().sum() 
#### input missing values with the mean of each column(Imputation)
- data.fillna(data.mean(), inplace=True) 

## Features and Labels
#### (input to model)Features: Helps predict i.e. the puzzle pieces used to create that picture
#### (Output to model)Labels: What you're trying to predict. i.e. the finished picture of the puzzle on the box
Selects "features" and "target"
- features = data.drop('Potability', axis=1) Selects features and "target"
- labels = data['Potability']

## Standardizing and Scaling Data
#### Standardizing Data: Makes sure data is at the same starting point. (the mean/average)
#### Scaling Data: to "squish" the data, so its easier to work with. i.e. a Small photo is enlarged to fit the frame, a large photo is shrunk to fit the frame
#### Spread aka Standard Deviation: how far the values in data are from least to most
- https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.StandardScaler.html 
- pip install -U scikit-learn
#### grabbing to show its current form
- features[1:5] 
#### Standardize the features
- scaler = StandardScaler()
- standardized_features = scaler.fit_transform(features)

## Creating Training and Evaluation Data
- from sklearn.model_selection import train_test_split
#### Returns a tuple(training_features, testing_features, training_labels, testing_labels)
- train_test_split(standardized_features, labels, test_size=0.2, random_state=42)
#### Assigning/ Splitting the dataset into training and testing sets using the training features,testing features, training labels, and testing labels.
- training_features, testing_features, training_labels, testing_labels = train_test_split(standardized_features, labels, test_size=0.2, random_state=42)
#### converting to pytorch tensors:
-training_features = torch.tensor(training_features,dtype=torch.float32)
-training_labels = torch.tensor(training_labels.values,dtype=torch.float32).view(-1,1)
-testing_features =torch.tensor(testing_features,dtype=torch.float32)
-testing_labels = torch.tensor(testing_labels.values,dtype=torch.float32).view(-1,1)