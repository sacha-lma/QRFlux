from QRFlux.Config import QRConfig

from .GF256 import GF256


def ReedSolomonEncode(data: list[int], config : QRConfig) -> list[int]:
    CompletedData = data.copy()
    DataGenerator = CreatePolynomialGenerator((config.UsableSlots // 8) - len(data))
    return CompletedData

def CreatePolynomialList(ToComplete: int) -> list[int]:
    PolynomialList = [1]

    for i in range(ToComplete + 2):
        PolynomialList.append(GF256(PolynomialList[-1], 2))
    return PolynomialList

def CreatePolynomialGenerator(ToComplete: int) -> list[int]:
    Generator = [1]
    PolynomialList = CreatePolynomialList(ToComplete)

    for i in range(ToComplete + 1):
        Generator.append(GF256(Generator[i], PolynomialList[i + 1]))
    return Generator
