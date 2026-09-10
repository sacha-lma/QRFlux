"""Build the full QR matrix from an empty grid plus the fixed patterns."""

from __future__ import annotations

from .Patterns import QRMatrix, PlaceFinderPattern, PlaceTimingPattern


def EmptyMatrix(SlotCount: int) -> QRMatrix:
    """Return a ``SlotCount`` x ``SlotCount`` grid filled with zeros."""
    return [[0] * SlotCount for _ in range(SlotCount)]


def BuildMatrix(Data: list[int], SlotCount: int) -> QRMatrix:
    """Build the QR matrix for ``Data``.

    Only the fixed patterns are placed for now; the payload bytes are not
    laid into the data region yet.
    """
    Matrix = EmptyMatrix(SlotCount)
    Matrix = PlaceFinderPattern(Matrix, SlotCount)
    Matrix = PlaceTimingPattern(Matrix, SlotCount)
    return Matrix
