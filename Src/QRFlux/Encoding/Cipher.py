"""End-to-end encryption of the payload bytes."""

from __future__ import annotations


def Encrypt(Data: list[int]) -> list[int]:
    """Return the encrypted payload.

    Encryption is not implemented yet, so the payload is copied through
    unchanged. Kept as a seam so the real cipher can drop in later.
    """
    return list(Data)
