import typing_extensions
from narwhals.typing import IntoFrame

ResultReturnType: typing_extensions.TypeAlias = dict[
    str,
    str | dict[str, str | None | bool | list[str]],
]

class DataSet:
    frame: IntoFrame
    @property
    def results(self) -> ResultReturnType: ...
    def __init__(self, frame: IntoFrame) -> None: ...
    def validate(self) -> DataSet: ...

    class DateValidation:
        @staticmethod
        def column_match_date_format(
            column: str,
            date_format: str,
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the values in a column match the date format."""

    class EqualityValidation:
        @staticmethod
        def pair_column_equality(
            column: str,
            target_column: str,
            groupby_combined: bool = True,
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the pair of columns are equal."""

    class NullValidation:
        @staticmethod
        def column_be_null(
            column: str,
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the values in a column are null."""
        @staticmethod
        def column_not_be_null(
            column: str,
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the values in a column are not null."""

    class ValuesValidation:
        @staticmethod
        def column_unique_values_to_be_in_list(
            column: str,
            values: list[str | int | float],
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the unique values are in the list."""
        @staticmethod
        def column_values_to_be_between(
            column: str,
            min_value: int,
            max_value: int,
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the values in a column are between a range."""
        @staticmethod
        def columns_sum_to_be_equal_to(
            columns_list: list[str],
            sum_value: float,
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the sum of the columns is equal to `sum_value`."""
        @staticmethod
        def columns_sum_to_be_greater_equal_than(
            columns_list: list[str],
            max_sum: float,
            threshold: float = 0.00,
            impact: str = "low",
            **kwargs,
        ) -> DataSet: ...
        """Check if the sum of columns greater or equal than `max_sum`."""
