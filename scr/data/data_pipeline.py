from typing import Tuple
import pandas as pd
from pandas import DataFrame
from pandas import Series
from sklearn.model_selection import train_test_split

def clean_data(filepath: str) -> DataFrame:
    """
    Cleans and preprocesses raw review data from a `.jsonl` file for model training.

    This function performs the following steps:
    1. Loads a `.jsonl` file into a pandas DataFrame.
    2. Removes unnecessary columns, keeping only those relevant for prediction (`rating`, `title`, and `text`).
    3. Concatenates the `title` and `text` columns into a single `text_aug` column for feature representation.
    4. Scales the `rating` column to a range between 0 and 1, creating a `scaled_rating` column.

    Args:
        filepath (str): Path to the `.jsonl` file containing raw data.

    Returns:
        DataFrame: A cleaned DataFrame with two columns:
            - `text_aug` (str): Combined text of the review title and body.
            - `scaled_rating` (float): Scaled rating between 0 (lowest) and 1 (highest).
    """
    
    # 1 - Read raw .jsonl
    df = pd.read_json(filepath, lines=True)

    # 2 - Keep columns for prediction
    df = df[['rating','title','text']]

    # 3 - Condense text columns
    df['text_aug'] = df['title'] + " " + df['text']

    # 4 - Scale rating
    df['scaled_rating'] = (df['rating'] - 1) / 4

    return df[['text_aug', 'scaled_rating']]

def split_data(df: DataFrame, test_size: float = 0.3) -> Tuple[DataFrame, DataFrame, Series, Series]:
    """
    Splits the data into training and test sets.
    
    Args:
        df (DataFrame): The input DataFrame to split.
        test_size (float): Proportion of the data to use as the test set.
        
    Returns:
        tuple: Splits the data into features (X_train, X_test) and target (y_train, y_test).
    """

    X = df['text_aug']  # Input text (book review)
    y = df['scaled_rating']  # Target label (rating between 0 and 1)
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    return X_train, X_test, y_train, y_test
