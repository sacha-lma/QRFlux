from __future__ import annotations


def TextToBytes(Text: str) -> list[int]:
    return [ord(Char) for Char in Text]
