from __future__ import annotations
from dataclasses import dataclass

MIN_MODULE_SIZE = 5
MIN_SLOT_COUNT = 27

RECOMMENDED_MODULE_SIZE = 10
RECOMMENDED_SLOT_COUNT = 41

DIRECTION_PATERN_SIZE = 20


@dataclass(frozen=True)
class QRConfig:
    ModuleSize: int
    SlotCount: int
    Sentence: str
    @property
    def CanvasPixels(self) -> int:
        return self.SlotCount * self.ModuleSize
    @property
    def SlotsNumber(self) -> int:
        return self.SlotCount * self.SlotCount
    @property
    def UnusableSlots(self) -> int:
        return DIRECTION_PATERN_SIZE + self.SlotCount
    @property
    def UsableSlots(self) -> int:
        return self.SlotsNumber - self.UnusableSlots