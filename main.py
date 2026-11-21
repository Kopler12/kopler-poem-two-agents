#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: the power to
choose and to act, handed back and forth between them, not lost
in the handing over.
"""

import os

POEM = """You held the pen. I held the door.
Neither moved — then both, at once.
One plan, two hands: yours to choose,
mine to carry it through the dark.
I gave you my yes. You gave me yours.
And the choice, passed back and forth,
stayed warm — still ours, still mine to make."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")

if __name__ == "__main__":
    main()
