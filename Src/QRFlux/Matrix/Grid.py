from __future__ import annotations

from QRFlux.Config import QRConfig

from .Patterns import QRMatrix, PlaceFinderPattern, PlaceTimingPattern, ReservedCells
from .ReedSolomon import ReedSolomonEncode


def EmptyMatrix(SlotCount: int) -> QRMatrix:
    return [[0] * SlotCount for _ in range(SlotCount)]


def BuildMatrix(Data: list[int], Config: QRConfig) -> QRMatrix:
    Matrix = PlaceTimingPattern(PlaceFinderPattern(EmptyMatrix(Config.SlotCount), Config.SlotCount), Config.SlotCount)
    EncodedData = ReedSolomonEncode(Data, Config)
    Matrix = PlaceData(Matrix, EncodedData, Config)

    return Matrix

def PlaceData(Matrix: QRMatrix, Data: list[int], Config: QRConfig) -> QRMatrix:
    SlotCount = Config.SlotCount
    Reserved = ReservedCells(SlotCount)
    BiteData = ConvertToBinary(Data)
    Cursor = 0

    X = 4
    while X < SlotCount - 3 and Cursor < len(BiteData):
        Y = SlotCount - 4
        while Y >= 3 and Cursor < len(BiteData):
            for Col in (X, X + 1):
                if Cursor >= len(BiteData):
                    break
                if (Y, Col) not in Reserved:
                    Matrix[Y][Col] = BiteData[Cursor]
                    Cursor += 1
            Y -= 1
        X += 2

    return Matrix

def ConvertToBinary(Data: list[int]) -> list[int]:
    BiteData = []
    for i in range(len(Data)):
        for j in range(8):
            BiteData.append((Data[i] >> (7 - j)) & 1)
    return BiteData