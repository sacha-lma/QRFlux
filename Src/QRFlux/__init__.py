"""QRFlux: build and display a QR matrix generated from a sentence.

The package is split by concern:

* :mod:`QRFlux.Config`    - session parameters (:class:`~QRFlux.Config.QRConfig`)
* :mod:`QRFlux.Cli`       - interactive prompts
* :mod:`QRFlux.Encoding`  - text -> bytes -> encrypted payload
* :mod:`QRFlux.Matrix`    - QR grid assembly and fixed patterns
* :mod:`QRFlux.Rendering` - Tk window and canvas drawing
* :mod:`QRFlux.App`       - orchestration (:func:`~QRFlux.App.Run`)
"""
