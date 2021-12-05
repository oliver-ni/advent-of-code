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


def run_day(day):
    module = import_module(f"{day}.main")

    print(f"DAY {day}")

    for i in ("p1", "p2"):
        if not hasattr(module, i):
            continue

        print(f"--- {i} ---")
        print("sample: ", end="")
        run(getattr(module, i), f"{day}/sample")
        print("input:  ", end="")
        run(getattr(module, i), f"{day}/input")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
    except IndexError:
        day = datetime.now().day
    run_day(day)
