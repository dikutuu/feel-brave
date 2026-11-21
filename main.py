"""Write one short, steadying text to /output/entry.txt.

The text is a single quiet scene — a kettle off the boil, rain finished,
a dog asleep — meant to leave the reader a little braver than before.

The entry gate accepts between 1 and 280 characters, so the piece is
kept short on purpose: at 258 characters it sits comfortably inside
the limit while still leaving the scene room to breathe.
"""

import os

TEXT = "Somewhere a kettle is coming off the boil, and nobody is in a hurry. The rain has finished with the roof. A dog sleeps under the table, dreaming of fields. Nothing is asked of you here. The next page can wait — the light will still be on when you turn to it."

OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def write_entry(text, out_dir):
    """Write ``text`` to ``entry.txt`` inside ``out_dir``, creating it if needed."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(TEXT, OUTPUT_DIR)


if __name__ == "__main__":
    main()
