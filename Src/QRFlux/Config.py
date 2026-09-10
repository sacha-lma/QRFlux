from __future__ import annotations
from dataclasses import dataclass

MIN_MODULE_SIZE = 5
MIN_SLOT_COUNT = 27

RECOMMENDED_MODULE_SIZE = 10
RECOMMENDED_SLOT_COUNT = 41


@dataclass(frozen=True)
class QRConfig:
    ModuleSize: int
    SlotCount: int
    Sentence: str
    @property
    def CanvasPixels(self) -> int:
        return self.SlotCount * self.ModuleSize
