"""Write one short, steadying text to /output/entry.txt.

The text is a single quiet scene — a kettle off the boil, rain finished,
a dog asleep — meant to leave the reader a little braver than before.
"""

import os

TEXT = "Somewhere a kettle is coming off the boil, and nobody is in a hurry. The rain has finished with the roof. A dog sleeps under the table, dreaming of fields. Nothing is asked of you here. The next page can wait — the light will still be on when you turn to it."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
