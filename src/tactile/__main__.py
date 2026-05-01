"""Run the Flask dev server: ``python -m tactile`` (add ``src`` to path if needed)."""

import sys
from pathlib import Path

_SRC_ROOT = Path(__file__).resolve().parent.parent
if str(_SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(_SRC_ROOT))

from tactile.app import run_server  # noqa: E402

if __name__ == "__main__":
    run_server()
