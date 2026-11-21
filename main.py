#!/usr/bin/env python3
"""Entrypoint: copy the pre-rendered entry.png to the output directory.

Stdlib only. The image is built by render.py at authoring time, so this
program does no image work -- it only places the file where the harness
expects it.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
print(f"copied entry.png to {OUT_DIR / 'entry.png'}")
