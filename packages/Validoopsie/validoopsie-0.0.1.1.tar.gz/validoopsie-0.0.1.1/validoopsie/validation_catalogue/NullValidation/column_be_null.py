from __future__ import annotations

import narwhals as nw
from narwhals.typing import FrameT

from validoopsie.base import BaseValidationParameters, base_validation_wrapper


@base_validation_wrapper
class ColumnBeNull(BaseValidationParameters):
    """Check if the values in a column are null."""

    @property
    def fail_message(self) -> str:
        """Return the fail message, that will be used in the report."""
        return f"The column '{self.column}' doesn't have values that are null."

    def __call__(self, frame: FrameT) -> FrameT:
        """Check if the unique values are in the list.

        Return will be used in the `execute_check` method in `column_check`
        decorator.
        """
        return (
            frame.with_columns(
                nw.col(self.column).is_null().alias("null_values"),
            )
            .filter(
                nw.col("null_values") == False,
            )
            .select(
                nw.col(self.column),
            )
            .group_by(self.column)
            .agg(
                nw.col(self.column).count().alias(f"{self.column}-count"),
            )
        )
