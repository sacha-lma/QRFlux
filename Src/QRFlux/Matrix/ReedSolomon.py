from __future__ import annotations

from QRFlux.Config import QRConfig

from .GF256 import GF256


def ReedSolomonEncode(Data: list[int], Config: QRConfig) -> list[int]:
    ToComplete = (Config.UsableSlots // 8) - len(Data)
    CompletedData = FillEmptySlots(Data.copy(), ToComplete)
    Generator = CreatePolynomialGenerator(ToComplete)

    for i in range(len(Data)):
        Lead = CompletedData[i]
        if Lead != 0:
            for j in range(len(Generator)):
                CompletedData[i + j] ^= GF256(Generator[j], Lead)

    return CompletedData[len(Data):]

def FillEmptySlots(CompletedData: list[int], ToComplete: int) -> list[int]:
    for _ in range(ToComplete):
        CompletedData.append(0)
    return CompletedData

def CreatePolynomialList(ToComplete: int) -> list[int]:
    PolynomialList = [1]

    for _ in range(ToComplete + 2):
        PolynomialList.append(GF256(PolynomialList[-1], 2))
    return PolynomialList

def CreatePolynomialGenerator(ToComplete: int) -> list[int]:
    PolynomialList = CreatePolynomialList(ToComplete)
    Generator = [1]

    for i in range(ToComplete):
        Racine = PolynomialList[i]
        NouveauGenerator = [0] * (len(Generator) + 1)
        for j in range(len(Generator)):
            NouveauGenerator[j] ^= Generator[j]
            NouveauGenerator[j + 1] ^= GF256(Generator[j], Racine)
        Generator = NouveauGenerator

    return Generator
