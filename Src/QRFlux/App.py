from __future__ import annotations

from .Cli import PromptConfig
from .Encoding import Encrypt, TextToOctets
from .Matrix import BuildMatrix
from .Rendering import CreateWindow, RenderMatrix


def Run() -> None:
    Config = PromptConfig()

    Payload = Encrypt(TextToOctets(Config.Sentence))
    Matrix = BuildMatrix(Payload, Config)

    Window, Canvas = CreateWindow(Config)
    RenderMatrix(Matrix, Canvas, Config)
    Window.mainloop()

    print("QRFlux requested : ", Config.Sentence)
