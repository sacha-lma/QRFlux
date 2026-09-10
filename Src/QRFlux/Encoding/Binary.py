"""Convert human-readable text into the byte values fed to the encoder."""

from __future__ import annotations


def TextToBytes(Text: str) -> list[int]:
    """Return the code point of each character in ``Text`` (one byte per char)."""
    return [ord(Char) for Char in Text]
