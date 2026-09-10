"""Create the Tk window and blank canvas that host the QR code."""

from __future__ import annotations

import tkinter as tk

from ..Config import QRConfig


def CreateWindow(Config: QRConfig) -> tuple[tk.Tk, tk.Canvas]:
    """Return a titled window and the blank canvas packed inside it."""
    Window = tk.Tk()
    Window.title("QRFlux")
    Window.geometry(f"{Config.CanvasPixels}x{Config.CanvasPixels}")

    Canvas = tk.Canvas(
        Window,
        width=Config.CanvasPixels,
        height=Config.CanvasPixels,
        bg="white",
    )
    Canvas.pack()

    return Window, Canvas
