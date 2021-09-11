import logging

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from config import *  # noqa

logging.basicConfig(level=logging.INFO)


def train_model(X: pd.DataFrame, y: pd.DataFrame) -> RandomForestClassifier:
    """
    Initialises and fits a Random Forest model.

    Args:
        X: features to train on
        y: target
    Return:
        fitted model
    """

    logging.info("Training the model...")

    model = RandomForestClassifier()

    model.fit(X, y)

    return model


def get_predictions(model: RandomForestClassifier, X_test: pd.DataFrame) -> np.ndarray:
    """
    Scoring the test set with the fitted model.

    Args:
        model: fitted model
        X_test: features for the test set
    Return:
        prediction for the test set indices
    """

    logging.info("Getting the predictions...")

    preds = model.predict(X_test)

    return preds


def calculate_metrics(preds: np.ndarray, actuals: pd.DataFrame) -> None:
    """
    Compares the predictions with actuals and logs the accuracy metrics.

    Args:
        preds: predictions for the test set (yhat)
        actuals: actual values for the target (y)
    """

    actuals.rename({RESPONSE: Y}, axis=1, inplace=True)
    actuals.set_index("Unnamed: 0", inplace=True)

    preds = pd.DataFrame(preds).rename({1: YHAT}, axis=1)
    preds.set_index(0, inplace=True)

    logging.info("The accuracy score is {}".format(accuracy_score(actuals, preds)))


def main():
    """Main runner. Fits and scores the model."""

    X_train = pd.read_csv("./data/X_train.csv")
    y_train = pd.read_csv("./data/y_train.csv")
    X_test = pd.read_csv("./data/X_test.csv")
    y_test = pd.read_csv("./data/y_test.csv")

    model = train_model(X_train, y_train)

    preds = get_predictions(model, X_test)

    calculate_metrics(preds, y_test)


if __name__ == "__main__":
    main()
