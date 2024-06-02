# Industrial Copper Modeling

Industrial Copper Modeling project aims to deals with dataset which is less complex data related to sales and pricing.

## Introduction
The Industrial Copper Modeling project focuses on predicting the selling price and status (won or lost) in the industrial copper market using machine learning regression and classification algorithms. By exploring the dataset, performing data cleaning and preprocessing, and applying various machine learning techniques, we aim to develop models that can accurately predict the selling price and status in the copper market.

## Technologies Used
#### Numpy
#### Pandas
#### Scikit-Learn
#### Seaborn
#### Matplotlib
#### Pickle

## Skills Takeaway
- Python scripting
- Data Preprocessing
- EDA
- Streamlit

## Domain
- Manufacturing

## Problem Statement
The copper industry faces challenges with skewed and noisy sales and pricing data, affecting manual predictions. This project aims to build machine learning models to predict `Selling_Price` and lead `Status` (WON/LOST) to improve decision-making.

## Solution Steps
- **Explore skewness and outliers.**
- **Clean and preprocess data.**
- **Build a regression model for `Selling_Price`.**
- **Build a classification model for `Status`.**
- **Create a Streamlit page for predictions.**

## Approach
- **Data Understanding**: Identify variable types and distributions. Convert invalid `Material_Reference` values to null and treat reference columns as categorical.
- **Data Preprocessing**: Handle missing values, treat outliers with IQR or Isolation Forest, address skewness with data transformations, and encode categorical variables appropriately.
- **EDA**: Visualize outliers and skewness using Seaborn.
- **Feature Engineering**: Engineer new features and drop highly correlated ones.
- **Model Building**: Train and evaluate classification models (e.g., ExtraTreesClassifier, XGBClassifier). Optimize hyperparameters with cross-validation. Follow similar steps for regression models, focusing on tree-based models.
- **Model GUI**: Create a Streamlit page for task input (Regression or Classification) and column value inputs. Apply preprocessing and feature engineering steps to new data and display predictions.
- **Tips**: Use `pickle` to save and load models.

## Learning Outcomes
- Proficiency in Python and data analysis libraries.
- Experience in data preprocessing and EDA.
- Application of regression and classification techniques.
- Building and optimizing ML models.
- Feature engineering.
- Developing a Streamlit web application.
- Understanding manufacturing domain challenges and ML solutions.

