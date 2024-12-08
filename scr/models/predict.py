from typing import Tuple
import numpy as np
from pandas import DataFrame
from sklearn.pipeline import Pipeline

def classify_sentiments(scores: np.ndarray) -> np.ndarray:
    """
    Classify scores into 'negative', 'neutral', or 'positive' categories.

    Args:
        scores (np.ndarray): Array of scores in the range [0, 1].

    Returns:
        np.ndarray: Array of sentiment classifications ('negative', 'neutral', 'positive').
    """
    
    sentiments = np.where(scores < 1/3, 'negative',
                 np.where(scores <= 2/3, 'neutral', 'positive'))
    return sentiments

def predict_sentiment(X: DataFrame, pipeline: Pipeline) -> Tuple[np.ndarray, np.ndarray]:
    """
    Predict continuous scores and classify sentiments for the given input data.

    Args:
        X (DataFrame): Input data containing text features for prediction.
        pipeline (Pipeline): A trained scikit-learn pipeline that includes 
                             preprocessing and a regression model.

    Returns:
        Tuple[np.ndarray, np.ndarray]:
            - np.ndarray: Predicted scores for each input sample (ranging from 0 to 1).
            - np.ndarray: Sentiment classifications based on the predicted scores 
                         (e.g., "negative", "neutral", "positive").
    """

    # Predict the score
    scores = pipeline.predict(X)
    sentiments = classify_sentiments(scores)

    return scores, sentiments