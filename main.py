import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from typing import List

# gloabl settings
warnings.filterwarnings("ignore")
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

def plot_distribution_by_outcome(data, feature: str, bins=30):
    """
    Plots the distribution of a numerical feature, separated by the 'Outcome' (diabetes).
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(data=data, x=feature, hue='Outcome', kde=True, bins=bins, palette='viridis')
    plt.title(f'Distribution of {feature} by Diabetes Outcome')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.legend(title='Outcome', labels=['No Diabetes', 'Diabetes'])
    #plt.savefig(f'distribution_{feature}.png')
    plt.show()

def plot_categorical_distribution_by_outcome(data, feature):
    """
    Plots the distribution of a categorical feature, separated by the 'Outcome' (diabetes).
    Shows counts for each category and outcome.
    """
    plt.figure(figsize=(10, 7))
    sns.countplot(data=data, x=feature, hue='Outcome', palette='magma', order=data[feature].value_counts().index)
    plt.title(f'Diabetes Outcome by {feature} Category')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right') # Rotate labels if they overlap
    plt.legend(title='Outcome', labels=['No Diabetes', 'Diabetes'])
    plt.tight_layout() # Adjust layout to prevent labels from being cut off
    #plt.savefig(f'categorical_distribution_{feature}.png')
    plt.show()

def get_bmi_category(bmi: float) -> str:
    """Categorizes BMI values into standard groups."""
    if pd.isna(bmi):
        return 'Unknown'
    elif bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal Weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

def replace_zeros_with_nan(df, cols: List[str]) -> None:
    for col in cols:
        df[col] = df[col].replace(0, np.nan)

        if df[col].isnull().any():
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)

def main():

    # Load the dataset
    df = pd.read_csv('diabetes.csv')

    cols_to_replace_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    replace_zeros_with_nan(df, cols_to_replace_zero)

    df['BMI_Category'] = df['BMI'].apply(get_bmi_category)

    plot_distribution_by_outcome(df, 'Glucose')
    plot_distribution_by_outcome(df, 'BloodPressure')

    plot_categorical_distribution_by_outcome(df, 'BMI_Category')


if __name__ == "__main__":

    main()