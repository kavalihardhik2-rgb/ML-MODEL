# ML-MODEL

A beginner-friendly Machine Learning project created while learning how Machine Learning models work using Python and Scikit-learn.

## About the Project

This repository contains my practice and implementation of **Linear Regression**.

The project includes:

* A simple Linear Regression example using years of experience and salary.
* A House Price Prediction model using the California Housing dataset.
* Model training and prediction using Scikit-learn.
* Basic model evaluation using MSE and R² Score.
* Data visualization using Matplotlib.

The main purpose of this project is to understand the basic workflow of a Machine Learning model, from loading data to training, prediction, evaluation, and visualization.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## Project Files

```text
ML-MODEL/
│
├── LinearRegression.py
├── prediction.py
└── README.md
```

## 1. Simple Linear Regression

`LinearRegression.py` contains a basic example of Linear Regression.

The model uses:

* Years of experience as the input
* Salary as the output

Example dataset:

| Years of Experience | Salary |
| ------------------: | -----: |
|                   1 |   3000 |
|                   2 |   4000 |
|                   3 |   5000 |
|                   4 |   6000 |
|                   5 |   7000 |

The model is trained using Scikit-learn's `LinearRegression` class. It then predicts the salary for a new value of 6 years of experience.
The program also displays:

* Slope / coefficient
* Intercept
* Actual data points
* Predicted regression line

## 2. House Price Prediction

`prediction.py` uses the **California Housing dataset** available through Scikit-learn.

The dataset is converted into a Pandas DataFrame, with the target value stored as `Price`.

The data is divided into:

* Training data — 80%
* Testing data — 20%

using `train_test_split`.

A Linear Regression model is then trained on the training data and used to predict prices for the test data.

### Model Evaluation

The model is evaluated using:

* **Mean Squared Error (MSE)**
* **R² Score**

Both values are printed after making predictions.

The project also creates a graph comparing actual prices with predicted prices.

## How Linear Regression Works

Linear Regression tries to find a relationship between input variables and an output variable.

The basic equation is:

```text
y = mx + c
```

Where:

* `y` = predicted output
* `x` = input
* `m` = coefficient / slope
* `c` = intercept

In this project, the model learns these values from the given data and uses them to make predictions.

## Installation

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## How to Run

Run the simple Linear Regression example:

```bash
python LinearRegression.py
```

Run the House Price Prediction model:

```bash
python prediction.py
```

## Learning Outcomes

Through this project, I am learning:

* Basics of Machine Learning
* Linear Regression
* Loading datasets
* Preparing data using Pandas
* Splitting data into training and testing sets
* Training ML models
* Making predictions
* Evaluating ML models
* Visualizing predictions using Matplotlib

## Future Improvements

I plan to continue improving this repository by experimenting with:

* More Machine Learning algorithms
* Different datasets
* Better data preprocessing
* More model evaluation techniques
* Additional prediction projects

## Author

**Hardhik Kavali**

AI & ML Engineering Student

GitHub: [kavalihardhik2-rgb](https://github.com/kavalihardhik2-rgb)
