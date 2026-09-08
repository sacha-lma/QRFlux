# QRFlux
File transfer between two devices via a QR code stream on screen read by camera, works for entire files, no network, logs, or trace. Built from scratch in Python: custom QR generator (Reed-Solomon, masking), Luby Transform fountain coding, peeling decoder, end-to-end encryption so watching both screens reveals nothing.

## Development

The project uses [uv](https://docs.astral.sh/uv/) with [poethepoet](https://poethepoet.natn.io/) as a cross-platform task runner:

```sh
uv sync                 # set up the environment (dependencies + dev tools)
uv run poe run          # run the application (Src/main.py)
uv run poe test-run     # run the tests
uv run poe clean        # remove Python caches and build artifacts
```
