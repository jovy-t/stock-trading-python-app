# `schedule` is a lightweight Python package for running jobs at specific intervals.
#   Instead of using cron or system schedulers, you can write all scheduling logic in Python.
#   Requires the Python script to always be running
import schedule

# `time` is a built-in Python module that lets you pause or control execution (e.g., sleep).
import time

from script import run_stock_job

from datetime import datetime

def basic_job():
    print("Job started at:", datetime.now())

# 🕒 Schedule jobs

schedule.every().minute.do(basic_job)

# Tell `schedule` to run `run_stock_job()` every minute.
# ETL job: fetch stock tickers → add timestamp → load into Snowflake.
schedule.every().minute.do(run_stock_job)

# 🔄 Run loop
# `schedule` doesn’t run jobs on its own — we need a loop to keep checking.
while True:
    schedule.run_pending()
    time.sleep(1)