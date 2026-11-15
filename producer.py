import csv
import os

from file_lock import acquire_lock, release_lock

FILE_NAME = "praca.csv"

acquire_lock()
try:
    # count existing calls to get a new call ID
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r", newline='', encoding="utf-8") as file:
            lines = file.readlines()
        lines_count = len(lines)
    else:
        lines_count = 0

    new_id = lines_count + 1

    with open(FILE_NAME, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([f"rozmowa {new_id}", "pending"])
finally:
    release_lock()
