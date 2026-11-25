#!/usr/bin/env python3
"""Museum of the Year 3000 — one museum label for an ordinary object.

The program writes a single line, the museum label a museum in the year
3000 places beside a parking meter, to /output/entry.txt.
"""

from pathlib import Path

LABEL = (
    "Parking Meter, c. 2024. A roadside shrine to which travellers "
    "offered coins, lest the wardens carry off their chariots."
)


def main() -> None:
    # Mirror the sealed gate: 1 to 200 characters, not only whitespace.
    assert 1 <= len(LABEL) <= 200, f"label is {len(LABEL)} chars"
    assert LABEL.strip(), "label must not be blank"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(LABEL + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
