"""Route board I/O either locally (USB) or via a remote bridge service."""

from __future__ import annotations

import base64
import json
import os
from urllib import error, request

from tactile.serial_board import clear_board as _local_clear_board
from tactile.serial_board import reset_board as _local_reset_board
from tactile.serial_board import send_to_board as _local_send_to_board
from tactile.ws2812_serial_board import clear_ws2812_panel as _local_clear_ws2812_panel
from tactile.ws2812_serial_board import send_ws2812_frame as _local_send_ws2812_frame

_REMOTE_TIMEOUT = float(os.environ.get("BOARD_BRIDGE_TIMEOUT_SEC", "5.0"))


def _bridge_base_url() -> str:
    return os.environ.get("BOARD_BRIDGE_URL", "").rstrip("/")


def _using_remote_bridge() -> bool:
    return bool(_bridge_base_url())


def _post_json(path: str, payload: dict) -> dict:
    base = _bridge_base_url()
    if not base:
        raise RuntimeError("BOARD_BRIDGE_URL is not configured.")
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        f"{base}{path}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=_REMOTE_TIMEOUT) as resp:
            data = resp.read().decode("utf-8")
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Bridge HTTP {exc.code}: {details}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Bridge unreachable at {base}: {exc.reason}") from exc

    result = json.loads(data) if data else {}
    if result.get("status") == "error":
        raise RuntimeError(result.get("message", "Bridge request failed"))
    return result


def send_to_board(patterns):
    if _using_remote_bridge():
        _post_json("/api/send_patterns", {"patterns": patterns})
        return
    _local_send_to_board(patterns)


def reset_board():
    if _using_remote_bridge():
        _post_json("/api/reset_board", {})
        return
    _local_reset_board()


def clear_board():
    if _using_remote_bridge():
        _post_json("/api/clear_board", {})
        return
    _local_clear_board()


def send_ws2812_frame(rgb_bytes: bytes):
    if _using_remote_bridge():
        payload = {"rgb_base64": base64.b64encode(rgb_bytes).decode("ascii")}
        _post_json("/api/send_ws2812", payload)
        return
    _local_send_ws2812_frame(rgb_bytes)


def clear_ws2812_panel(num_leds: int = 256):
    if _using_remote_bridge():
        _post_json("/api/clear_ws2812", {"num_leds": num_leds})
        return
    _local_clear_ws2812_panel(num_leds=num_leds)
