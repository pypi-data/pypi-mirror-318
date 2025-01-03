from __future__ import annotations

import logging
from typing import Callable, TypeVar

import narwhals as nw
import pendulum
from narwhals.typing import IntoFrame

T = TypeVar("T", bound=type)


def get_items(
    nw_frame: IntoFrame,
    column: str,
) -> list[str | int | float]:
    if isinstance(nw_frame, nw.LazyFrame):
        return (
            nw_frame.select(nw.col(column).unique())
            .collect()
            .get_column(column)
            .sort()
            .to_list()
        )
    if isinstance(nw_frame, nw.DataFrame):
        return nw_frame.get_column(column).sort().unique().to_list()
    msg = (
        f"The frame is not a valid type. {type(nw_frame)}, if "
        "you reached this point please open an issue."
    )
    raise TypeError(msg)


def get_length(nw_frame: IntoFrame) -> int:
    if isinstance(nw_frame, nw.LazyFrame):
        return nw_frame.select(nw.len()).collect().item()
    if isinstance(nw_frame, nw.DataFrame):
        return nw_frame.select(nw.len()).item()
    msg = (
        f"The frame is not a valid type. {type(nw_frame)}, if "
        "you reached this point please open an issue."
    )
    raise TypeError(msg)


def get_count(nw_input_frame: nw.DataFrame, column: str) -> int:
    return nw_input_frame.select(nw.col(f"{column}-count").sum()).item()


def log_exception_summary(cls, e) -> str:
    name = type(e).__name__
    error_str = str(e)
    fail_msg = (
        f"An error occurred while validating {cls.__name__}:\n{name} - {error_str!s}"
    )
    logging.error(fail_msg)
    return error_str


def base_validation_wrapper(
    cls: T,
) -> Callable[[IntoFrame], dict[str, str | list[object] | dict[str, str]]]:
    class Wrapper(cls):
        def __init__(
            self,
            *args: object,
            **kwargs: object,
        ) -> None:
            super().__init__(*args, **kwargs)
            self.column: str
            self.impact: str
            self.threshold: float
            self.__check__impact()
            self.__check__threshold()

        def __check__impact(self) -> None:
            fail_message: str = "Argument 'impact' is required."
            assert self.impact.lower() in ["low", "medium", "high"], fail_message

        def __check__threshold(self) -> None:
            fail_message: str = "Argument 'threshold' should be between 0 and 1."
            assert 0 <= self.threshold <= 1, fail_message

        def execute_check(
            self,
            frame: IntoFrame,
        ) -> dict[str, str | dict[str, str]]:
            try:
                validated_frame = self(frame)

                # LazyFrame is a bit complicating situation, the transformation done by
                # the validation function should reduce the collection size. This is
                # done because there is no other way (currently) to validate a query.
                if isinstance(validated_frame, nw.LazyFrame):
                    validated_frame: nw.DataFrame = validated_frame.collect()

            except Exception as e:
                error_str = log_exception_summary(cls, e)
                return {
                    "validation": str(cls.__name__),
                    "impact": self.impact,
                    "timestamp": pendulum.now().isoformat(),
                    "column": self.column,
                    "result": {
                        "status": "Fail",
                        "message": f"ERROR: {error_str!s}",
                    },
                }

            og_frame_rows_number: int = get_length(frame)
            vf_count_number: int = get_count(validated_frame, self.column)
            vf_row_number: int = get_length(validated_frame)
            failed_percentage: float = (
                vf_count_number / og_frame_rows_number if vf_count_number > 0 else 0.00
            )
            threshold_pass: bool = failed_percentage <= self.threshold

            if vf_row_number > 0:
                items: list[str | int | float] = get_items(validated_frame, self.column)
                if not threshold_pass:
                    result = {
                        "result": {
                            "status": "Fail",
                            "threshold pass": threshold_pass,
                            "message": self.fail_message,
                            "failing items": items,
                            "failed number": vf_count_number,
                            "frame row number": og_frame_rows_number,
                            "threshold": self.threshold,
                            "failed percentage": failed_percentage,
                        },
                    }
                elif threshold_pass:
                    result = {
                        "result": {
                            "status": "Success",
                            "threshold pass": threshold_pass,
                            "message": self.fail_message,
                            "failing items": items,
                            "failed number": vf_count_number,
                            "frame row number": og_frame_rows_number,
                            "threshold": self.threshold,
                            "failed percentage": failed_percentage,
                        },
                    }

            else:
                result = {
                    "result": {
                        "status": "Success",
                        "threshold pass": threshold_pass,
                        "message": "All items passed the validation.",
                        "frame row number": og_frame_rows_number,
                        "threshold": self.threshold,
                    },
                }

            return {
                "validation": str(cls.__name__),
                "impact": self.impact,
                "timestamp": pendulum.now().isoformat(),
                "column": self.column,
                **result,
            }

    Wrapper.__name__ = cls.__name__
    return Wrapper
