"""Interactive prompts that collect a :class:`QRConfig` from the user."""

from __future__ import annotations

from .Config import (
    MIN_MODULE_SIZE,
    MIN_SLOT_COUNT,
    RECOMMENDED_MODULE_SIZE,
    RECOMMENDED_SLOT_COUNT,
    QRConfig,
)


def _PromptInt(Prompt: str, *, Minimum: int, Noun: str) -> int:
    """Read an int from stdin, re-asking until it reaches ``Minimum``."""
    Value = int(input(Prompt))
    while Value < Minimum:
        print(f"Error: {Noun} must be at least {Minimum}.")
        Value = int(input(Prompt))
    return Value


def PromptConfig() -> QRConfig:
    """Ask for a module size, a slot count and a sentence to encode."""
    ModuleSize = _PromptInt(
        f"Enter module size: ({RECOMMENDED_MODULE_SIZE} recommended) ",
        Minimum=MIN_MODULE_SIZE,
        Noun="Module size",
    )
    SlotCount = _PromptInt(
        f"Enter number of slots: ({RECOMMENDED_SLOT_COUNT} recommended) ",
        Minimum=MIN_SLOT_COUNT,
        Noun="Number of slots",
    )
    Sentence = input("request sentence: ")
    return QRConfig(ModuleSize=ModuleSize, SlotCount=SlotCount, Sentence=Sentence)
