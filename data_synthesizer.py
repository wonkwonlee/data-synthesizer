# Import required libraries
import pandas as pd
import numpy as np
from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.lib.utils import read_json_file
from scipy.stats import ks_2samp, entropy
import seaborn as sns
import matplotlib.pyplot as plt

# Helper functions for data analysis
def describe_dataset(data, attributes):
    """
    Calculate statistical metrics for a dataset.
    """
    for attr in attributes:
        print(f"\n{attr} statistics:")
        print(f"Median: {data[attr].median()}")
        print(f"Mean: {data[attr].mean()}")
        print(f"Min: {data[attr].min()}")
        print(f"Max: {data[attr].max()}")

def plot_distribution(data_real, data_synthetic, attribute, title):
    """
    Plot histogram comparisons for a specific attribute.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(data_real[attribute], kde=True, label="Real Data", color="blue", stat="density")
    sns.histplot(data_synthetic[attribute], kde=True, label="Synthetic Data", color="orange", stat="density")
    plt.title(title)
    plt.legend()
    plt.show()

# Load real dataset (COMPAS)
real_data_path = "path_to_real_data.csv"
df_real = pd.read_csv(real_data_path)
attributes = ["age", "score"]

# Describe real dataset
print("Original Dataset Statistics")
describe_dataset(df_real, attributes)

# Generate synthetic datasets using DataSynthesizer
def generate_synthetic_data(df, mode, epsilon=None, degree=None):
    """
    Generate synthetic data using DataSynthesizer in different modes.
    """
    describer = DataDescriber()
    describer.describe_dataset_in_random_mode(df, epsilon=epsilon)
    synthetic_data_path = "synthetic_data.csv"
    data_generator = DataGenerator()
    data_generator.generate_dataset_in_random_mode(synthetic_data_path)
    return pd.read_csv(synthetic_data_path)

synthetic_modes = {
    "Random": {"mode": "random"},
    "Independent": {"mode": "independent", "epsilon": 0.1},
    "Correlated (k=1)": {"mode": "correlated", "epsilon": 0.1, "degree": 1},
    "Correlated (k=2)": {"mode": "correlated", "epsilon": 0.1, "degree": 2},
}

# Generate datasets and analyze
synthetic_datasets = {}
for mode, config in synthetic_modes.items():
    synthetic_datasets[mode] = generate_synthetic_data(df_real, **config)

# Compare distributions
for mode, data in synthetic_datasets.items():
    plot_distribution(df_real, data, "age", f"Age Distribution - {mode}")

# Mutual information analysis
def mutual_info_heatmap(df, title):
    """
    Generate a mutual information heatmap for the dataset.
    """
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title(title)
    plt.show()

mutual_info_heatmap(df_real, "Real Data Mutual Information")
for mode, data in synthetic_datasets.items():
    mutual_info_heatmap(data, f"{mode} Synthetic Data Mutual Information")