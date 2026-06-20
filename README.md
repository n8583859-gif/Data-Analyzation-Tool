# Dataset Analyzer Tool

A menu-driven Python project for loading, exploring, and cleaning CSV datasets.

This project was built as part of my Python and Data Analysis learning journey. The goal was not only to create a working tool but also to understand how real-world software is designed, organized, and improved step by step.

While building this project, I practiced Python programming, Object-Oriented Programming (OOP), file handling, Pandas, NumPy, error handling, Git, GitHub workflow, and project structuring.

---

## Project Overview

Working with datasets often involves repetitive tasks such as checking missing values, inspecting columns, removing duplicates, and cleaning data before analysis.

This tool provides a simple menu-driven interface that helps perform these tasks directly from the terminal.

The project focuses on creating a structured workflow that allows a user to:

1. Load a dataset
2. Explore the dataset
3. Analyze data quality
4. Clean the dataset
5. Save the cleaned dataset

---

## Features

### Dataset Loading

* Load CSV files from the local system
* Handle invalid file paths safely
* Validate file extensions before loading
* Display dataset dimensions after successful loading

### Data Exploration

The exploration module allows users to quickly inspect the dataset.

Available options:

* Dataset Shape
* Column Names
* Data Types
* Dataset Information
* First 5 Rows
* Last 5 Rows
* Statistical Summary
* Missing Value Report
* Unique Values in a Selected Column

### Data Cleaning

The cleaning module provides multiple options for handling common data quality issues.

#### Missing Value Report

* View total missing values for each column
* View percentage of missing values

#### Fill Missing Values

Before filling values, the tool performs a quick analysis of the selected column:

* Data Type
* Missing Value Count
* Missing Value Percentage
* First 5 Rows
* Last 5 Rows

Supported filling methods:

* Mean
* Median
* Mode
* Custom Value
* Forward Fill
* Backward Fill
* Linear Interpolation

#### Drop Missing Rows

* Preview rows that will be removed
* Show removal statistics
* Ask for confirmation before execution

#### Drop Missing Columns

* Display missing value report
* Remove a specific column
* Remove all columns containing missing values
* Warn users before removing columns that contain no missing values

#### Remove Duplicate Rows

* Detect duplicate rows
* Display duplicate count
* Remove duplicates after confirmation

#### Save Cleaned Dataset

* Save the cleaned dataset as a new CSV file
* Preserve the original dataset

---

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Pandas
* NumPy
* OS Module

---

## Object-Oriented Design

The project follows an Object-Oriented Programming approach.

### DatasetManager

Responsible for:

* Loading datasets
* Managing dataset state
* Validating dataset availability

### DataCleaner

Responsible for:

* Missing value analysis
* Missing value handling
* Removing missing rows
* Removing missing columns
* Removing duplicate rows
* Saving cleaned datasets

### DatasetAnalyzerApp

Responsible for:

* Main menu navigation
* Data exploration menu
* Data cleaning menu
* Application flow control

---

## Skills Demonstrated

This project demonstrates practical knowledge of:

### Python

* Classes and Objects
* Functions and Methods
* Loops
* Conditional Statements
* Exception Handling
* File Operations

### Pandas

* DataFrame Operations
* Missing Value Analysis
* Data Cleaning
* Data Exploration
* Duplicate Detection
* CSV Handling

### Software Development

* Object-Oriented Design
* Modular Programming
* Problem Solving
* User Input Validation
* Menu-Driven Applications
* Code Organization

### Git & GitHub

* Feature Branch Workflow
* Incremental Development
* Commit Management
* Version Control

---

## Example Workflow

A typical workflow looks like this:

1. Load a dataset
2. Inspect dataset structure
3. Check missing values
4. Analyze specific columns
5. Apply appropriate cleaning methods
6. Remove duplicate records
7. Save the cleaned dataset

---

## Project Structure

```text
DatasetAnalyzerTool/
│
├── main.py
├── README.md
├── data/
│   └── dataset.csv
│
└── output/
    └── cleaned_dataset.csv
```

---

## Future Improvements

Potential future enhancements include:

* Data Visualization Module
* Column Renaming
* Data Type Conversion
* Dataset Reset Option
* Export Reports
* GUI Version using Tkinter
* Dashboard-Based Interface

---

## What I Learned

Building this project helped me understand:

* How to design software using classes
* How to separate responsibilities between modules
* How data cleaning workflows are structured
* How to work with real datasets using Pandas
* How to build interactive terminal applications
* How to manage project development using Git and GitHub

More importantly, this project taught me how to think about software architecture, user experience, and problem solving instead of only writing code.

---

## Author:-

### ***Jitendra Kumawat***

```bash
Aspiring AI/ML Engineer focused on building strong foundations in Python, Data Analysis, Machine Learning, and real-world software development through hands-on projects.
```
