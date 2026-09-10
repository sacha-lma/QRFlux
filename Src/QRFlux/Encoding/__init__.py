"""Turn a sentence into the (encrypted) payload bytes placed in the matrix."""

from __future__ import annotations

from .Binary import TextToBytes
from .Cipher import Encrypt

__all__ = ["TextToBytes", "Encrypt"]
