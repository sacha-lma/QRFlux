import QRFlux.App as App
from QRFlux.Config import QRConfig
from QRFlux.Encoding import Encrypt, TextToBytes
from QRFlux.Matrix import BuildMatrix, EmptyMatrix


def TestTextToBytesEncodesEachCharacter():
    assert TextToBytes("QR") == [81, 82]


def TestEncryptIsCurrentlyAPassthroughCopy():
    Data = [1, 2, 3]
    assert Encrypt(Data) == Data
    assert Encrypt(Data) is not Data


def TestEmptyMatrixIsSquareAndZeroed():
    Grid = EmptyMatrix(27)
    assert len(Grid) == 27
    assert all(len(Row) == 27 and set(Row) == {0} for Row in Grid)


def TestBuildMatrixPlacesTheFixedPatterns():
    Grid = BuildMatrix(TextToBytes("hello"), 41)
    assert Grid[3][3] == 1
    assert Grid[5][3] == 1
    assert Grid[41 - 4][41 - 4] == 1
    assert Grid[41 - 8][41 - 7] == 1


def TestRunOrchestratesWithoutOpeningAWindow(monkeypatch, capsys):
    monkeypatch.setattr(
        App, "PromptConfig", lambda: QRConfig(ModuleSize=10, SlotCount=41, Sentence="hi")
    )

    class FakeWindow:
        def mainloop(self):
            self.Looped = True

    FakeWin = FakeWindow()
    monkeypatch.setattr(App, "CreateWindow", lambda Config: (FakeWin, object()))
    monkeypatch.setattr(App, "RenderMatrix", lambda Matrix, Canvas, Config: None)

    App.Run()

    assert FakeWin.Looped is True
    assert "QRFlux requested" in capsys.readouterr().out
