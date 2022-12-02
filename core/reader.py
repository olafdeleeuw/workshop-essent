import pandas as pd
from typing import Optional

from core.datetime_handler import DatetimeHandler


def read_timeseries_data_from_csv(
        filepath: str,
        time_column: str = "timestamp",
        timezone_in: Optional[str] = "local",
        timezone_out: Optional[str] = "utc"
) -> pd.DataFrame:

    # 1. import csv
    df = pd.read_csv(filepath)

    datetime_handler = DatetimeHandler(df, time_column, timezone_in, timezone_out)
    datetime_handler.convert_timestamp_column_to_datetimeindex()
    return datetime_handler.df


if __name__ == "__main__":
    path_to_csv = "../data/time_format3.csv"
    df_formatted = read_timeseries_data_from_csv(path_to_csv, "timestamp")
    print(df_formatted)
