from typing import Tuple, Dict
from pandas import DataFrame, Series
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPRegressor
from evaluate import evaluate_model

def train_model(X_train: DataFrame, y_train: Series) -> Tuple[Pipeline, Dict[str, float]]:
    """
    Train a machine learning pipeline model using a neural network regressor for review scoring.

    This function creates a pipeline that includes:
    - `TfidfVectorizer`: Converts text data into a TF-IDF feature matrix.
    - `MLPRegressor`: A neural network model with a sigmoid activation function for regression.

    Args:
        X_train (DataFrame): The training input data, expected to contain text reviews in one column.
        y_train (Series): The training target data, scores between 0 and 1.

    Returns:
        Tuple[Pipeline, Dict[str, float]]: A tuple containing:
            - The trained scikit-learn pipeline.
            - A dictionary with metrics for evaluating the model on the training data.
    """

    # Create a pipeline with TfidfVectorizer and MLPRegressor
    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer()),  # Converts text reviews into TF-IDF features
        ('regressor', MLPRegressor(
            hidden_layer_sizes=(16, 8),  # Two layers: first with 32 nodes, second with 8
            activation='logistic',  # Sigmoid activation function
            solver='adam',  # Adam optimizer for efficient training
            max_iter=100,  # Maximum iterations to converge
            random_state=42  # Reproducibility
        ))
    ])

    # Train the pipeline
    pipeline.fit(X_train, y_train)

    # Evaluate model performance on training data
    # `evaluate_model` function should return a dictionary with metrics such as MSE and MAE
    metrics_dict = evaluate_model(X_train, y_train, pipeline)

    # Return the trained pipeline and the training metrics
    return pipeline, metrics_dict
