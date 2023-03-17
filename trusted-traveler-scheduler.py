#!/usr/bin/env python3
"""Entrypoint into the script where the arguments are passed to src.main"""

import sys

from src.main import main

if __name__ == "__main__":
    arguments = sys.argv[1:]

    try:
        main(arguments)
    except KeyboardInterrupt:
        print("\nCtrl+C pressed. Stopping all checkins")
        sys.exit()