"""Parameters that describe a single QRFlux session."""

from __future__ import annotations

from dataclasses import dataclass

MIN_MODULE_SIZE = 5
MIN_SLOT_COUNT = 27

RECOMMENDED_MODULE_SIZE = 10
RECOMMENDED_SLOT_COUNT = 41


@dataclass(frozen=True)
class QRConfig:
    """How a QR matrix should be built and drawn."""

    ModuleSize: int
    SlotCount: int
    Sentence: str

    @property
    def CanvasPixels(self) -> int:
        """Side length, in pixels, of the square canvas."""
        return self.SlotCount * self.ModuleSize
