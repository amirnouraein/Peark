#!/usr/bin/env python3
"""Pinned rows sleep like other tabs; pinned squares stay awake (Peark).

Build first (./build.sh), then python3 Tests/pin_rows_sleep.py.
"""
import sys

import split_view as sv

sv.use("pin-rows-sleep")


def main():
    t = sv.T()
    try:
        sv.setup(sidebar=True, **{"pins.list": True})
        sv.launch()
        square, row = sv.page("square"), sv.page("row")
        sv.cmd({"do": "pin", "id": square})
        sv.cmd({"do": "pin", "id": row, "listed": True})
        sv.page("front")  # neither pin on screen
        said = sv.sp("sleep", id=square).get("sleepResult")
        t.ok("a pinned square stays awake", said == "pinned", said)
        said = sv.sp("sleep", id=row).get("sleepResult")
        t.ok("a pinned row sleeps", said == "asleep", said)
    finally:
        sv.finish()
        t.done()
    return int(t.failed > 0)


if __name__ == "__main__":
    sys.exit(main())
