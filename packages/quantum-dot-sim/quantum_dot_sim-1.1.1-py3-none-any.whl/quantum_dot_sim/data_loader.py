import numpy as np
import tensorflow as tf
import os
import logging
from sklearn.preprocessing import StandardScaler
from .custom_exceptions import DatasetNotFoundError, ModelNotFoundError, InvalidDatasetFormatError

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def normalize_data(X):
    """Normalize the features using StandardScaler."""
    logging.info("Normalizing the feature data.")
    scaler = StandardScaler()
    return scaler.fit_transform(X)

def load_dataset(dataset_path):
    """Load and preprocess the dataset."""
    if not os.path.exists(dataset_path):
        raise DatasetNotFoundError(
            dataset_path,
            message="Dataset file not found. Please check the path and ensure the file exists."
        )
    
    try:
        # Assuming the dataset is a .npy file; adjust logic if a different format is used
        data = np.load(dataset_path, allow_pickle=True)
        logging.info(f"Dataset successfully loaded from {dataset_path}.")
        
        # Assuming dataset contains two parts: features (X) and labels (Y)
        if len(data) == 2:
            X, Y = data
            logging.info("Dataset successfully unpacked into features and labels.")
            X = normalize_data(X)  # Normalize the feature data
            return X, Y
        else:
            raise InvalidDatasetFormatError(
                dataset_path,
                message="Dataset must contain exactly two parts: features (X) and labels (Y)."
            )
    except Exception as e:
        logging.error(f"Failed to load dataset: {e}")
        raise

def load_model(model_path):
    """Load the trained model."""
    if not os.path.exists(model_path):
        raise ModelNotFoundError(
            model_path,
            message="Model file not found. Please check the path and ensure the file exists."
        )
    
    try:
        model = tf.keras.models.load_model(model_path)
        logging.info(f"Model successfully loaded from {model_path}.")
        return model
    except Exception as e:
        logging.error(f"Failed to load model: {e}")
        raise
