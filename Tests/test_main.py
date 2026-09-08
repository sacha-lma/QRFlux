from main import main


def test_main_runs(capsys):
    main()
    assert "QRFlux" in capsys.readouterr().out
