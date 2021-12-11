import sys
import traceback
from datetime import datetime
from importlib import import_module


def run(func, filename="filename"):
    try:
        with open(filename) as f:
            try:
                print(func(f))
            except:
                traceback.print_exc()
    except FileNotFoundError:
        print()


def run_day(day, extra=None):
    module = import_module(f"py.day{day:02}_{extra}" if extra else f"py.day{day:02}")

    print(f"DAY {day}")

    for i in ("p1", "p2"):
        if not hasattr(module, i):
            continue

        print(f"--- {i} ---")
        print("sample: ", end="")
        run(getattr(module, i), f"input/day{day:02}_sample.txt")
        print("input:  ", end="")
        run(getattr(module, i), f"input/day{day:02}.txt")


if __name__ == "__main__":
    day = sys.argv[1:]
    extra = sys.argv[2] if len(sys.argv) >= 3 else None
    day = int(sys.argv[1]) if len(sys.argv) >= 2 else datetime.now().day + 1
    run_day(day, extra)
