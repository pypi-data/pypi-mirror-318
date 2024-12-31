"""
Copyright (c) 2024 l.feng. All rights reserved.

pybit7z: A wrapper based on bit7z.
"""

from __future__ import annotations

from pathlib import Path

from importlib_metadata import distribution

from pybit7z import _core as core

from ._version import version as __version__

__all__ = ["__version__", "core"]

if not Path(core.set_lib7zip_path()).exists():
    lib7zip_path = (
        distribution(__package__).locate_file(__package__) / core.set_lib7zip_path()
    )
    if lib7zip_path.exists():
        core.set_lib7zip_path(str(lib7zip_path))
        core.set_large_page_mode()
