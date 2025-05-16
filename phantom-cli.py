#!/usr/bin/env python3
import sys

def banner():
    print("Phantom CLI v0.0.1 - APT0x33 Internal Toolkit")

def help():
    print("Usage: phantom-cli <route>")
    print("Example: phantom-cli mystify_user_route_2024")

def main():
    banner()
    if len(sys.argv) < 2:
        help()
        return
    route = sys.argv[1]
    if route == "mystify_user_route_2024":
        print("Accessing vault... 🔓")
        # flag{cl1_4cc355_r0ut3_v4l1d4t3d}
    else:
        print("Error: Invalid route")

if __name__ == "__main__":
    main()
