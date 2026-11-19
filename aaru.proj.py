
# ==========================================================
# DATA SCIENCE FUNDAMENTALS ASSESSMENT
# Internship Project
# ==========================================================

# 1. Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("DATA SCIENCE FUNDAMENTALS ASSESSMENT")
print("=" * 60)


# ==========================================================
# 2. PYTHON FUNDAMENTALS
# ==========================================================

print("\n1. PYTHON FUNDAMENTALS")

name = "Data Science Student"
age = 21
percentage = 85.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)
print("Student:", is_student)

# Conditional statements

if percentage >= 80:
    print("Performance: Excellent")
elif percentage >= 60:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")

# Loops

print("\nNumbers from 1 to 5:")

for i in range(1, 6):
    print(i)

# Functions

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

marks = [85, 90, 78, 92, 88]

print("Average Marks:", calculate_average(marks))


# ==========================================================
# 3. PYTHON DATA TYPES AND STRUCTURES
# ==========================================================

print("\n2. DATA TYPES AND STRUCTURES")

# List
subjects = ["Python", "Statistics", "Machine Learning"]

# Tuple
coordinates = (10, 20)

# Dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Data Science"
}

# Set
unique_numbers = {10, 20, 30, 10}

print("List:", subjects)
print("Tuple:", coordinates)
print("Dictionary:", student)
print("Set:", unique_numbers)

# Data types

print("\nData Types:")

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))


# ==========================================================
# 4. NUMPY FUNDAMENTALS
# ==========================================================

print("\n3. NUMPY OPERATIONS")

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Sum:", np.sum(numbers))

# Matrix operations

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nMatrix:")
print(matrix)

print("Matrix Transpose:")
print(matrix.T)


# ==========================================================
# 5. CREATE A DATASET USING PANDAS
# ==========================================================

print("\n4. DATASET CREATION")

data = {
    "Student": [
        "Amit", "Priya", "Rahul", "Sneha",
        "Karan", "Neha", "Arjun", "Riya",
        "Vikas", "Anjali"
    ],

    "Age": [21, 22, 20, 23, 21, 22, 24, 20, 21, 23],

    "Study_Hours": [
        5, 7, 3, 8, 6, 7, 4, 9, 5, 8
    ],

    "Attendance": [
        85, 90, 65, 95, 80, 88, 70, 98, 82, 92
    ],

    "Marks": [
        75, 88, 55, 92, 70, 85, 60, 95, 72, 90
    ],

    "Department": [
        "IT", "CS", "IT", "CS", "IT",
        "CS", "IT", "CS", "IT", "CS"
    ]
}

df = pd.DataFrame(data)

print("\nComplete Dataset:")
print(df)


# ==========================================================
# 6. DATA EXPLORATION
# ==========================================================

print("\n5. DATA EXPLORATION")

print("\nFirst Five Rows:")
print(df.head())

print("\nLast Five Rows:")
print(df.tail())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================================
# 7. DATA CLEANING
# ==========================================================

print("\n6. DATA CLEANING")

# Check duplicate records

print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicates

df = df.drop_duplicates()

# Check missing values

print("Missing Values:")
print(df.isnull().sum())

# Convert data types if necessary

df["Age"] = df["Age"].astype(int)

print("\nCleaned Dataset:")
print(df)


# ==========================================================
# 8. STATISTICAL FOUNDATIONS
# ==========================================================

print("\n7. STATISTICAL ANALYSIS")

marks = df["Marks"]

# Measures of central tendency

print("Mean:", marks.mean())
print("Median:", marks.median())
print("Mode:", marks.mode().tolist())

# Measures of dispersion

print("Variance:", marks.var())
print("Standard Deviation:", marks.std())
print("Range:", marks.max() - marks.min())

# Quartiles

print("Q1:", marks.quantile(0.25))
print("Q2:", marks.quantile(0.50))
print("Q3:", marks.quantile(0.75))

# Correlation

print("\nCorrelation Matrix:")
print(
    df[["Study_Hours", "Attendance", "Marks"]]
    .corr()
)


# ==========================================================
# 9. DATA ANALYSIS
# ==========================================================

print("\n8. DATA ANALYSIS")

# Students scoring above 80

high_scorers = df[df["Marks"] > 80]

print("\nStudents scoring above 80:")
print(high_scorers)

# Average marks by department

department_analysis = df.groupby(
    "Department"
)["Marks"].mean()

print("\nAverage Marks by Department:")
print(department_analysis)

# Highest scoring student

top_student = df.loc[df["Marks"].idxmax()]

print("\nTop Performing Student:")
print(top_student)

# Average study hours

print(
    "\nAverage Study Hours:",
    df["Study_Hours"].mean()
)


# ==========================================================
# 10. DATA VISUALIZATION
# ==========================================================

print("\n9. DATA VISUALIZATION")

# Bar chart

plt.figure(figsize=(9, 5))

plt.bar(df["Student"], df["Marks"])

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Histogram

plt.figure(figsize=(8, 5))

plt.hist(df["Marks"], bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# Scatter plot

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours"],
    df["Marks"]
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()


# Correlation heatmap

plt.figure(figsize=(8, 5))

sns.heatmap(
    df[["Study_Hours", "Attendance", "Marks"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()


# ==========================================================
# 11. INDUSTRY BEST PRACTICES
# ==========================================================

print("\n10. INDUSTRY BEST PRACTICES")

# Use meaningful variable names
# Write reusable functions
# Handle missing values
# Remove duplicate records
# Validate data types
# Use comments and documentation
# Avoid unnecessary repetition
# Keep data organized

def validate_dataset(dataframe):

    required_columns = [
        "Student",
        "Age",
        "Study_Hours",
        "Attendance",
        "Marks"
    ]

    for column in required_columns:

        if column not in dataframe.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )

    if dataframe.empty:
        raise ValueError("Dataset is empty")

    if not dataframe["Marks"].between(0, 100).all():
        raise ValueError("Marks must be between 0 and 100")

    return True


print(
    "Dataset Validation:",
    validate_dataset(df)
)

# Export cleaned dataset

df.to_csv(
    "cleaned_student_dataset.csv",
    index=False
)

print("\nCleaned dataset exported successfully!")

print("\n" + "=" * 60)
print("ASSESSMENT COMPLETED SUCCESSFULLY")
print("=" * 60)
