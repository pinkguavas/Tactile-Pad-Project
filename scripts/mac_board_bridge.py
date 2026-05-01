"""HTTP bridge for board I/O when Pico is attached to this machine.

Run on the Mac that has the Pico USB connection:
    python scripts/mac_board_bridge.py
"""

from __future__ import annotations

import base64
import os
import sys
from pathlib import Path

from flask import Flask, jsonify, request

_SRC_ROOT = Path(__file__).resolve().parent.parent / "src"
if str(_SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(_SRC_ROOT))

from tactile.serial_board import clear_board, reset_board, send_to_board  # noqa: E402
from tactile.ws2812_serial_board import (  # noqa: E402
    clear_ws2812_panel,
    send_ws2812_frame,
)

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/api/send_patterns")
def api_send_patterns():
    data = request.get_json() or {}
    send_to_board(data.get("patterns", []))
    return jsonify({"status": "ok"})


@app.post("/api/reset_board")
def api_reset_board():
    reset_board()
    return jsonify({"status": "ok"})


@app.post("/api/clear_board")
def api_clear_board():
    clear_board()
    return jsonify({"status": "ok"})


@app.post("/api/send_ws2812")
def api_send_ws2812():
    data = request.get_json() or {}
    b64 = data.get("rgb_base64", "")
    rgb = base64.b64decode(b64.encode("ascii")) if b64 else b""
    send_ws2812_frame(rgb)
    return jsonify({"status": "ok"})


@app.post("/api/clear_ws2812")
def api_clear_ws2812():
    data = request.get_json() or {}
    num_leds = int(data.get("num_leds", 256))
    clear_ws2812_panel(num_leds=num_leds)
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    host = os.environ.get("BOARD_BRIDGE_HOST", "0.0.0.0")
    port = int(os.environ.get("BOARD_BRIDGE_PORT", "5050"))
    debug = os.environ.get("BOARD_BRIDGE_DEBUG", "0").lower() in ("1", "true", "yes")
    app.run(host=host, port=port, debug=debug, use_reloader=False)
