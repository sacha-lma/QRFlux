from __future__ import annotations


def TextToOctets(Text: str) -> list[int]:
    return [ord(Char) for Char in Text]
