import pandas as pd
from typing import Optional
from warnings import warn


class DatetimeHandler:

    def __init__(
            self,
            df: pd.DataFrame,
            timestamp_col: Optional[str] = "timestamp",
            timezone_in: Optional[str] = "local",
            timezone_out: Optional[str] = "utc"
    ):
        self.df = df
        self._time_column = timestamp_col
        self._timezone_in = timezone_in
        self._timezone_out = timezone_out

    def convert_timestamp_column_to_datetimeindex(self) -> pd.DataFrame:

        # 1. convert timestamp column to datetime
        timeseries = pd.to_datetime(self.df[self._time_column])

        # 2. sort timestamp column
        self._sort_timestamp_column(timeseries)

        # 3. if local timezone: check whether daylight savings are applied
        # correctly. If not: remove extra hour in March and extrapolate hour in
        # October.
        if self._timezone_in != "utc":
            self._check_daylight_savings_local_timezone(timeseries)

        # 4. check on completeness
        self._check_timeseries_completeness(timeseries)

        # 5. convert timezones if needed. Default timezone for csv is set to local,
        # for output df it is utc. User is able to change this.
        # - If in and out are equal we set the timezone to the datetimeindex
        # - If in ad and out are differente we convert the datetimeindex and set tz
        if self._timezone_in == self._timezone_out:
            self._set_timezone(timeseries, self._timezone_out)
        else:
            self._convert_timezone(timeseries, self._timezone_in, self._timezone_out)

        # 6. set as index
        self.df.index = pd.DatetimeIndex(timeseries)
        return self.df

    def _sort_timestamp_column(self, timeseries):
        pass

    def _check_daylight_savings_local_timezone(self, timeseries):
        """
        Checks whether daylight savings is applied correctly.
        - daylight savings applied on correct hour. Sometimes this is done the next
        day...
        - If not applied correctly, adjust the timeseries
            - Add/remove daylight savings hour
            - If applied on wrong time: re-allocate correct timestamps
        """
        pass

    def _check_timeseries_completeness(self, timeseries):
        """
        Checks if there are missing hours and returns percentage of missing hours
        """
        missing_hours = 2
        if missing_hours:
            percentage_missing = (missing_hours / len(timeseries)) * 100
            warn(
                f"Caution! Timeseries is not complete, {percentage_missing}% is missing.")
        pass

    def _set_timezone(self, timeseries, timezone):
        pass

    def _convert_timezone(self, timeseries, timezone_in, timezone_out):
        pass


