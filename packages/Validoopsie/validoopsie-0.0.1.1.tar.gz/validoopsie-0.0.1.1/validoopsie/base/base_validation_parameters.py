from typing import Optional


class BaseValidationParameters:
    """Base class for validation parameters."""

    def __init__(
        self,
        column: str,
        impact: Optional[str] = "low",
        threshold: Optional[float] = 0.00,
        **kwargs: object,
    ) -> None:
        self.column = column
        self.impact = impact.lower() if impact else impact
        self.threshold = threshold
        self.__dict__.update(kwargs)
