from typing import Dict
from pandas import DataFrame, Series
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error
from predict import predict_sentiment

def evaluate_model(X: DataFrame, y: Series, model_pipeline: Pipeline) -> Dict[str, float]:
    """
    Evaluate the saved regression pipeline on test data.

    This function computes evaluation metrics for a given model pipeline using
    test data. It returns the Mean Squared Error (MSE) and Mean Absolute Error (MAE)
    as a dictionary.

    Args:
        X (DataFrame): The input test features (e.g., preprocessed review text).
        y (Series): The ground truth target values (scaled ratings between 0 and 1).
        model_pipeline (Pipeline): The trained scikit-learn pipeline for prediction.

    Returns:
        Dict[str, Any]: A dictionary containing evaluation metrics:
            - 'mse': Mean Squared Error as a float.
            - 'mae': Mean Absolute Error as a float.
    """

    # Predict sentiment scores using the model pipeline
    # predict_sentiment function is expected to return both scores and sentiments
    y_pred, _ = predict_sentiment(X, model_pipeline)

    # Compute evaluation metrics
    metrics_dict = {
        'mse': float(mean_squared_error(y, y_pred)),  # Ensure the output is a plain float
        'mae': float(mean_absolute_error(y, y_pred)) # Ensure the output is a plain float
    }

    # Return the metrics as a dictionary
    return metrics_dict