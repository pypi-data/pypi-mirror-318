from pathlib import Path
from typing import Tuple

import attr


@attr.define
class DetectionLocation:
    file: Path = attr.field()
    frame: int = attr.field()
    box: Tuple[float, float, float, float]


@attr.define
class DetectionEvent:
    """
    Manage data about a single detection event. Where it happened, and how it was classified.
    """

    label: str
    confidence: float
    location: DetectionLocation

    @property
    def caption(self):
        return f"{self.label} {int(self.confidence * 100)}%, {self.location.box}"

    def __str__(self):
        return self.caption
