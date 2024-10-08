import kaggle
import os

# Ensure kaggle.json is in place
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')

# Define the dataset name and destination path
dataset_name = 'shubhangihande14797/games-dataset'
destination_path = "C:/Users/shubhangi hande/my-data-project/dataset"

# Download the dataset
kaggle.api.dataset_download_files(dataset_name, path=destination_path, unzip=True)
