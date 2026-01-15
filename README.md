AI & ML Internship — Task 1
Understanding Dataset & Data Types
Submitted by: Pranav S P


**Project Overview**

This project focuses on understanding data structure, data types, and ML readiness using the Titanic Dataset.
It includes a modular Python codebase, a clean notebook, and a professional analysis report.

The goal was not to build a model, but to:

Explore the dataset
Identify feature types
Check data quality
Understand missing values
Evaluate dataset suitability for ML


**Project Structure**

AI_ML_Task1/
│
├── data/                 # Dataset (titanic.csv)
│
├── src/                  # Custom Python modules 
│   ├── loader.py         # Handles dataset loading
│   ├── analyzer.py       # Generates dataset summary + feature classification
│   └── utils.py          # Helper functions for clean output
│
├── notebooks/
│   └── analysis.ipynb    # Main analysis notebook
│
├── reports/
│   └── task1_report.md   # 1-page dataset analysis report
│
├── outputs/
│   └── screenshots/      # Notebook screenshots (optional)
│
└── README.md             # Project documentation


**Tech Stack**

Python
Pandas
NumPy
VS Code
Jupyter Notebook (via VS Code)


**Dataset Used**

Titanic Dataset
Contains passenger details such as age, sex, class, fare, and survival status.

Target variable → Survived


**How to Run the Project**

Install dependencies:
*pip install pandas numpy ipykernel*

Open : notebooks/analysis.ipynb
Select Python Kernel, then run all cells.


**What I Learned from this Task**

How to structure a data project
How to build reusable python modules
How to examine data quality
How to identify feature types
How to evaluate dataset readiness for ML
How to document work professionally  

---

## 📚 Interview Questions & Answers (Based on Task-1)
Here i am answering based om what i understand from the above task


### 1️. What is the difference between Numerical and Categorical data?

**Numerical Data**  
- Contains numbers  
- Used for mathematical operations  
- Examples: Age, Fare, SibSp, Parch  
- Used directly in ML after scaling  

**Categorical Data**  
- Contains labels/text  
- Cannot be used for math  
- Examples: Sex, Embarked, Cabin, Ticket  
- Must be encoded before ML  

**In my project:**  
I used my custom 'classify_features()' function to automatically identify them.



### 2️. What is a Target Variable?

The target variable is what the ML model predicts.

**In the Titanic dataset:**  
'Survived' is the target variable (0 = died, 1 = survived).

I identified it clearly in my analysis notebook.



### 3️. Why is Understanding the Dataset Important before Modeling?

Because it helps identify:  
- Missing values  
- Data types  
- Distribution  
- Imbalance  
- Preprocessing requirements  

**In my project:**  
'dataset_summary(df)' helped me understand shape, null values, unique values, and data types.



### 4️. What is Data Imbalance?

When one class has many more samples than another.

**Example:**  
In Titanic dataset:  
- More passengers died than survived  
- More males than females  

This can cause biased models.

I analyzed imbalance using 'value_counts()'.



### 5️. What does df.describe() show?

Statistical summary:  
- Mean  
- Std deviation  
- Min/max  
- Percentiles  

Helps detect:  
- Outliers  
- Distribution  
- Missing patterns  

**In my project:**  
I used it to analyze Fare and Age distributions.
