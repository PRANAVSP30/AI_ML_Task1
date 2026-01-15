Task 1 — Understanding Dataset & Data Types

AI & ML Internship 
Report by: Pranav S P

1. Overview

The objective of this task is to deeply understand the structure, quality, and readiness of a dataset for machine learning.
I analyzed the Titanic dataset, which contains passenger details such as age, gender, ticket class, fare, and survival status.


2. Dataset Snapshot

Rows: 891
Columns: 12
Target Variable: Survived
Prediction Goal: Classify whether a passenger survived (1) or not (0)


3. Data Type Classification

Numerical Features

Age
Fare
SibSp
Parch

Categorical Features

Sex
Embarked
Cabin
Ticket
Name

Binary Features

Survived
Ordinal Features
Pclass (1 < 2 < 3)


4. Missing Values & Data Quality

Age has missing values → requires median imputation
Cabin has ~75% missing → drop or extract deck letter
Embarked has few missing values → fill with mode
Some features (Ticket, Name) require preprocessing before ML


5. Unique Value Observations

“Sex”      has 2 categories: male/female
“Embarked” has 3 categories
“Cabin”    has many unique values → high-cardinality
“Pclass”   has 3 ordered categories


6. ML Readiness Conclusion

The dataset is suitable for machine learning, but requires preprocessing:
Missing value imputation
Feature engineering
Encoding categorical values
Handling class imbalance
Removing irrelevant or noisy columns


7. Final Summary

This analysis gave a clear understanding of data structure, types, distributions, and challenges.
With proper cleaning and feature engineering, the Titanic dataset is ready for building ML models such as logistic regression or decision trees.