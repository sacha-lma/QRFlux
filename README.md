# QRFlux
File transfer between two devices via a QR code stream on screen read by camera, works for entire files, no network, logs, or trace. Built from scratch in Python: custom QR generator (Reed-Solomon, masking), Luby Transform fountain coding, peeling decoder, end-to-end encryption so watching both screens reveals nothing.

## Development

The project uses [uv](https://docs.astral.sh/uv/) with [poethepoet](https://poethepoet.natn.io/) as a cross-platform task runner:

```sh
uv sync                 # set up the environment (dependencies + dev tools)
uv run poe run          # run the application (Src/Main.py)
uv run poe test-run     # run the tests
uv run poe clean        # remove Python caches and build artifacts
```

## Layout

`Src/Main.py` is a thin entry point; everything else lives in the `QRFlux`
package, split by concern:

```text
Src/QRFlux/
  Config.py      session parameters (QRConfig)
  Cli.py         interactive prompts
  App.py         orchestration (Run())
  Encoding/      text -> bytes -> encrypted payload
  Matrix/        QR grid assembly + fixed patterns (finder, timing)
  Rendering/     Tk window creation and canvas drawing
```

Names follow the project's UpperCamelCase convention for modules, functions
and variables (module-level constants stay `UPPER_SNAKE_CASE`).
