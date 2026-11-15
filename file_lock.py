import os
import time

LOCK_FILE = "praca.csv.lock"


def acquire_lock():
    # os.O_EXCL makes creating the file fail if it already exists,
    # so only one process at a time can hold the lock
    while True:
        try:
            fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            return
        except FileExistsError:
            time.sleep(0.1)


def release_lock():
    os.remove(LOCK_FILE)
