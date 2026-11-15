import csv
import os
import time

from file_lock import acquire_lock, release_lock

FILE_NAME = "praca.csv"
WORK_TIME = 30
CHECK_INTERVAL = 5


def read_jobs():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, mode="r", newline='', encoding="utf-8") as file:
        return [row for row in csv.reader(file) if row]


def save_jobs(jobs):
    with open(FILE_NAME, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(jobs)


def take_job():
    # find the first pending job, mark it as in_progress and return its ID
    acquire_lock()
    try:
        jobs = read_jobs()
        for job in jobs:
            if job[1] == "pending":
                job[1] = "in_progress"
                save_jobs(jobs)
                return job[0]
        return None
    finally:
        release_lock()


def finish_job(job_id):
    acquire_lock()
    try:
        # read the file again - other consumers changed it in the meantime
        jobs = read_jobs()
        for job in jobs:
            if job[0] == job_id:
                job[1] = "done"
                break
        save_jobs(jobs)
    finally:
        release_lock()


def main():
    consumer_id = os.getpid()
    print(f"Consumer {consumer_id} started")
    while True:
        job_id = take_job()
        if job_id is None:
            time.sleep(CHECK_INTERVAL)
            continue
        print(f"Consumer {consumer_id}: {job_id} -> in_progress")
        time.sleep(WORK_TIME)
        finish_job(job_id)
        print(f"Consumer {consumer_id}: {job_id} -> done")


if __name__ == "__main__":
    main()
