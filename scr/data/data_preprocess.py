import pandas as pd
from pandas import DataFrame
import re
import string

def clean_text(text: str) -> str:
    """
    Basic text cleaning: remove special characters, convert to lowercase.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text.
    """
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(f"[{string.punctuation}]", "", text)

    return text

def preprocess_data(df: DataFrame) -> DataFrame:
    """
    Preprocess the 'text_aug' column of the input DataFrame.

    Args:
        df (DataFrame): Input DataFrame.

    Returns:
        df (DataFrame): DataFrame with cleaned 'text_aug' column.
    """
    df['text_aug'] = df['text_aug'].apply(clean_text)
    return df
