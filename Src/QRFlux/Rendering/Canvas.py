from __future__ import annotations

import tkinter as tk

from ..Config import QRConfig
from ..Matrix import QRMatrix


def RenderMatrix(Matrix: QRMatrix, Canvas: tk.Canvas, Config: QRConfig) -> None:
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
