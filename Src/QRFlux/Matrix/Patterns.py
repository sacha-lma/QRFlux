from __future__ import annotations

QRMatrix = list[list[int]]


def PlaceTimingPattern(Matrix: QRMatrix, SlotCount: int) -> QRMatrix:
    for Row in range(3, SlotCount - 3, 2):
        Matrix[Row][3] = 1
    return Matrix


def PlaceFinderPattern(Matrix: QRMatrix, SlotCount: int) -> QRMatrix:
    Matrix[SlotCount - 4][SlotCount - 4] = 1
    Matrix[SlotCount - 5][SlotCount - 4] = 1
    Matrix[SlotCount - 5][SlotCount - 5] = 1
    Matrix[SlotCount - 6][SlotCount - 4] = 1
    Matrix[SlotCount - 8][SlotCount - 4] = 1
    Matrix[SlotCount - 8][SlotCount - 5] = 1
    Matrix[SlotCount - 8][SlotCount - 6] = 1
    Matrix[SlotCount - 8][SlotCount - 7] = 1
    Matrix[SlotCount - 7][SlotCount - 7] = 1
    Matrix[SlotCount - 6][SlotCount - 7] = 1
    Matrix[SlotCount - 5][SlotCount - 7] = 1
    Matrix[SlotCount - 4][SlotCount - 7] = 1
    return Matrix
