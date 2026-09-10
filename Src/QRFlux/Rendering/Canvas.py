"""Draw a QR matrix onto a Tk canvas, one square per set module."""

from __future__ import annotations

import tkinter as tk

from ..Config import QRConfig
from ..Matrix import QRMatrix


def RenderMatrix(Matrix: QRMatrix, Canvas: tk.Canvas, Config: QRConfig) -> None:
    """Clear ``Canvas`` and paint a black square for every ``1`` in ``Matrix``."""
    Canvas.delete("all")
    Size = Config.ModuleSize
    for Row in range(Config.SlotCount):
        for Col in range(Config.SlotCount):
            if Matrix[Row][Col] != 1:
                continue
            X0 = Col * Size
            Y0 = Row * Size
            Canvas.create_rectangle(
                X0, Y0, X0 + Size, Y0 + Size, fill="black", outline="black"
            )
