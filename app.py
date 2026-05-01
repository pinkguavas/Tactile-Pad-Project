"""Backward-compatible entry point for the Flask app.

Prefer ``pip install -e .`` then ``flask --app tactile.app run`` or
``python -m tactile``.
"""

import sys
from pathlib import Path

_SRC_ROOT = Path(__file__).resolve().parent / "src"
if str(_SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(_SRC_ROOT))

from tactile.app import app, run_server  # noqa: E402

__all__ = ["app"]

if __name__ == "__main__":
    run_server()

