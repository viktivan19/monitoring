import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from unittest.mock import MagicMock
from config import *  # noqa

from data_processing import pre_process_data, main


@pytest.mark.parametrize(
    "input_df, expected_df",
    [
        (
            pd.DataFrame(
                data={
                    ID: [1, 2, 3, 4, 5, 6, 7],
                    DOB: pd.to_datetime(["1990-01-01"] * 5 + ["1925-01-01"] * 2),
                    EDUCATION: ["Graduation", "PhD", "Master"] * 2 + ["2n Cycle"],
                    CUSTOMER_SINCE: pd.to_datetime(["2012-01-01"] * 5 + ["2020-01-01"] * 2),

                }
            ),

            pd.DataFrame(
                data={
                    EDUCATION: [2, 4, 3] * 2 + [1],
                    AGE: [31] * 5 + [96] * 2,
                    TENURE: [9] * 5 + [1] * 2,

                }
            )
        ),
        (
            pd.DataFrame(
                data={
                    ID: [1, 2, 3, 4, 5, 6, 7],
                    DOB: pd.to_datetime(["1990-01-01"] * 5 + ["1925-01-01"] * 2),
                    EDUCATION: ["o","o", "p", "s", "i", "e"] + ["Other"],
                    CUSTOMER_SINCE: pd.to_datetime(["2012-01-01"] * 5 + ["2020-01-01"] * 2),

                }
            ),

            pd.DataFrame(
                data={
                    EDUCATION: ["o", "o", "p", "s", "i", "e", "Other"],
                    AGE: [31] * 5 + [96] * 2,
                    TENURE: [9] * 5 + [1] * 2,

                }
            )
        ),
    ], ids=["edgecase1", "edgecase1"]
)
def test_pre_process_data(input_df, expected_df):
    actual_df = pre_process_data(input_df)
    assert_frame_equal(actual_df, expected_df)


@pytest.mark.skip
def test_data_processing_main(mocker):
    mock_raw_df = pd.DataFrame(data={"col1": [1, 2, 3]})
    mocker.patch("data_processing.get_data", return_value=mock_raw_df)
    preprocessed_df = mocker.patch("data_processing.pre_process_data")
    mocker.patch("data_processing.get_train_test")
    mocker.patch("data_processing.save_table")

    main()

    preprocessed_df.assert_called()




