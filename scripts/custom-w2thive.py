#!/usr/bin/env python3
"""
Placeholder del script de integración Wazuh -> TheHive.
Sustituye este archivo por tu versión real anonimizada.
"""

import json
import sys


def main() -> int:
    data = sys.stdin.read().strip()
    if not data:
        print("No input received")
        return 1
    try:
        alert = json.loads(data)
    except json.JSONDecodeError:
        print("Invalid JSON")
        return 1

    print(f"Received alert id={alert.get('id', 'unknown')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
