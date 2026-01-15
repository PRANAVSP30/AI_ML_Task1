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