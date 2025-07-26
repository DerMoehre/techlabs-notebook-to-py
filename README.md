# Data Analysis Workflow Example: Pima Indians Diabetes Dataset

This repository contains a practical example demonstrating a typical data analysis workflow, from data loading and cleaning to feature engineering and visualization. A key purpose of this example is to illustrate **how to convert an interactive Jupyter Notebook (`.ipynb`) into a runnable Python script (`.py`)**, allowing for easier automation, integration into larger projects, and sharing.

## Project Goal

The primary goals of this example project are to:
* Showcase fundamental steps in Exploratory Data Analysis (EDA).
* Demonstrate common data cleaning and feature engineering techniques.
* Provide clear examples of data visualization using Matplotlib and Seaborn.

## Dataset

This project utilizes the **Pima Indians Diabetes Database** from Kaggle.

* **Source:** [https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database?resource=download](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database?resource=download)
* **Description:** This dataset comprises diagnostic measurements aiming to predict whether a patient has diabetes based on several medical predictor variables. It's a classic binary classification dataset, ideal for demonstrating initial data exploration.

## Features & Analysis Demonstrated

The `diabetes_eda_analysis.ipynb` notebook (and its converted `.py` script) walks through the following steps:

1.  **Data Loading and Initial Inspection:**
    * Loading the `diabetes.csv` file into a Pandas DataFrame.
    * Displaying the first few rows, checking data types (`.info()`), and generating descriptive statistics (`.describe()`).
2.  **Data Cleaning:**
    * Identifying and handling problematic '0' values in medical columns (e.g., Glucose, BloodPressure) by replacing them with `NaN`.
    * Applying a simple imputation strategy (e.g., median imputation) to fill missing values.
3.  **Feature Engineering:**
    * Creating a new categorical feature (`BMI_Category`) from the continuous 'BMI' column using a custom Python function.
4.  **Exploratory Data Visualization:**
    * Defining and using a function to plot numerical feature distributions (histograms with KDE) separated by the 'Outcome' (diabetes status).
    * Defining and using a function to visualize the distribution of a newly created categorical feature (`BMI_Category`) across different 'Outcome' classes using count plots.
5.  **Demonstrating Jupyter to Python Conversion:**
    * This `README` itself serves as an instruction manual for taking the `.ipynb` and making it a runnable `.py` file.

## Technologies Used

* Python 3.x
* `pandas` (for data manipulation and analysis)
* `numpy` (for numerical operations, especially NaN handling)
* `matplotlib` (for creating static, interactive, and animated visualizations)
* `seaborn` (for making statistical graphics more attractive and informative)

## Setup and Installation

To get this project up and running locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/DerMoehre/techlabs-classification.git](https://github.com/DerMoehre/techlabs-classification.git)
    cd techlabs-classification
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```
3.  **Install the required packages:**
    Since this project uses `pyproject.toml` for dependency management, you can install all dependencies and the project itself in editable mode:
    ```bash
    pip install -e .
    ```

## Usage

You can run this analysis either directly within Jupyter Notebook or by executing the provided standalone Python script.

### Option 1: Running in Jupyter Notebook

1.  Start a Jupyter Notebook server from your project's root directory:
    ```bash
    jupyter notebook
    ```
2.  Open the `diabetes_eda_analysis.ipynb` file in your browser.
3.  Execute the cells sequentially to see the data loading, cleaning, feature engineering, and plots generated.

### Option 2: Running the Python Script

The `diabetes_eda_analysis.py` file has been meticulously prepared to run the entire analysis workflow directly.

1.  **Execute the Python Script:**
    From your terminal in the project's root directory, run:
    ```bash
    python diabetes_eda_analysis.py
    ```
    The script will print outputs to your console and display the generated plots (each plot will appear in a separate window and require closing to proceed to the next, unless `plt.savefig()` is used instead of `plt.show()`).to the code).

## Important Considerations for Manual Notebook-to-Script Conversion

When manually converting code from a Jupyter Notebook (`.ipynb`) to a Python script (`.py`), keep the following best practices and common pitfalls in mind:

* **Maintain Execution Order:** Ensure the code in your `.py` file flows logically, just as it would if you were running the notebook cells from top to bottom. Dependencies between cells must be preserved.
* **Handle Markdown/Text Cells:** Jupyter Notebooks allow for rich text and explanations in Markdown cells. These are *not* automatically transferred to `.py` files. You should manually convert any crucial explanations or section headers into Python comments (`#`) in your script.
* **`print()` Statements are Your Friends:** In a Jupyter Notebook, simply typing a variable name on the last line of a cell will display its value. In a Python script, you *must* explicitly use `print()` to see any output in the console.
* **Plot Display (`plt.show()`):** Plots in Jupyter Notebooks render inline automatically. In a `.py` script, you need to call `plt.show()` after creating a plot to display it. If you create multiple plots, `plt.show()` will display them. For long-running scripts where you don't want plots to interrupt execution, consider using `plt.savefig()` to save them to files instead of `plt.show()`, and then `plt.close()` to free up memory.
* **Interactive Elements:** Features like interactive widgets or specific display functions (e.g., `display()`) are Jupyter-specific and will not work in a plain Python script.
* **Imports:** Gather all necessary `import` statements at the very beginning of your `.py` script for clarity and best practice.
* **Testing:** After manual conversion, always run the `.py` script completely to ensure it executes without errors and produces the expected outputs and plots.

By being mindful of these points, you can effectively translate your interactive data analysis work into robust and reusable Python scripts.