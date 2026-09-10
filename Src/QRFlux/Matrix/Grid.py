from __future__ import annotations

from .Patterns import QRMatrix, PlaceFinderPattern, PlaceTimingPattern


def EmptyMatrix(SlotCount: int) -> QRMatrix:
    return [[0] * SlotCount for _ in range(SlotCount)]


def BuildMatrix(Data: list[int], SlotCount: int) -> QRMatrix:
    Matrix = EmptyMatrix(SlotCount)
    Matrix = PlaceFinderPattern(Matrix, SlotCount)
    Matrix = PlaceTimingPattern(Matrix, SlotCount)
    return Matrix
