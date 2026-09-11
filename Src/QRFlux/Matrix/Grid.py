from __future__ import annotations

from QRFlux.Config import QRConfig

from .Patterns import QRMatrix, PlaceFinderPattern, PlaceTimingPattern


def EmptyMatrix(SlotCount: int) -> QRMatrix:
    return [[0] * SlotCount for _ in range(SlotCount)]



def BuildMatrix(Data: list[int], config: QRConfig) -> QRMatrix:
    Matrix = EmptyMatrix(config.SlotCount)
    Matrix = PlaceFinderPattern(Matrix, config.SlotCount)
    Matrix = PlaceTimingPattern(Matrix, config.SlotCount)
    return Matrix