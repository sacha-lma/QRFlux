from __future__ import annotations

from .Config import MIN_MODULE_SIZE, MIN_SLOT_COUNT, QRConfig


def PromptConfig() -> QRConfig:
    ModuleSize = int(input("Enter module size: (10 recommended) "))
    SlotCount = int(input("Enter number of slots: (41 recommended) "))

    while SlotCount < MIN_SLOT_COUNT:
        print(f"Error: Number of slots must be at least {MIN_SLOT_COUNT}.")
        SlotCount = int(input("Enter number of slots: (41 recommended) "))

    while ModuleSize < MIN_MODULE_SIZE:
        print(f"Error: Module size must be at least {MIN_MODULE_SIZE}.")
        ModuleSize = int(input("Enter module size: (10 recommended) "))

    Sentence = input("request sentence: ")
    return QRConfig(ModuleSize=ModuleSize, SlotCount=SlotCount, Sentence=Sentence)
