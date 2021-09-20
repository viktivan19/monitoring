import logging
from datetime import datetime
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from config import *  # noqa
from validation import check_missing_values

logging.basicConfig(level=logging.INFO)


def get_data() -> pd.DataFrame:
    """
    Reading the raw data in.
    
    Return:
         raw data frame
    """
    logging.info("Reading the data...")

    df = pd.read_csv("./data/marketing_campaign.csv", sep='\t', parse_dates=[DOB, CUSTOMER_SINCE])

    check_missing_values(df)

    return df


def pre_process_data(df_in: pd.DataFrame) -> pd.DataFrame:
    """
    Performing a number of steps to clean the data.

    Args:
        raw data
    Return:
         pre-processed, cleaned data
    """
    df = df_in.copy()

    logging.info("Cleaning the data...")

    today = datetime.now().year

    df[AGE] = today - df[DOB].dt.year

    df[TENURE] = today - df[CUSTOMER_SINCE].dt.year

    df = df.replace({EDUCATION: EDUCATION_REPLACE_DICT, MARITAL_STATUS: MARITAL_REPLACE_DICT})

    df.dropna(inplace=True)

    return df.drop([ID, DOB, CUSTOMER_SINCE], axis=1)


def get_train_test(df_in: pd.DataFrame) -> Tuple[pd.DataFrame,
                                                 pd.DataFrame,
                                                 pd.DataFrame,
                                                 pd.DataFrame]:
    """
    Splits X and y  into train and test set.

    Args:
        Cleaned data frame

    Return:
        train and test set for both X and y
    """
    X = df_in.drop(RESPONSE, axis=1)
    y = df_in[[RESPONSE]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=19, stratify=y)

    return X_train, X_test, y_train, y_test


def save_table(df: pd.DataFrame, tablename: str) -> None:
    """ Saves any dataframe to the specified file name"""
    df.to_csv(f"./data/{tablename}.csv")


def main():
    """Data processing runner. Cleans and splits the data."""

    df = get_data()

    df = pre_process_data(df)

    X_train, X_test, y_train, y_test = get_train_test(df)

    logging.info("Saving the processed data...")

    save_table(X_train, "X_train")
    save_table(X_test, "X_test")
    save_table(y_train, "y_train")
    save_table(y_test, "y_test")

    logging.info("Pre-processing done!'")


if __name__ == "__main__":
    main()
