import os

configs = [
    {"users": 1, "rate": 1, "time": "1m"},
    {"users": 5, "rate": 2, "time": "1m"},
    {"users": 10, "rate": 2, "time": "3m"},
    {"users": 25, "rate": 4, "time": "5m"},
]

for cfg in configs:
    filename = f"results/results_{cfg['users']}u_{cfg['rate']}r"
    command = (
        f"locust -f locustfile.py --headless -u {cfg['users']} "
        f"-r {cfg['rate']} --run-time {cfg['time']} "
        f"--host https://sarvam.ai --csv={filename} --only-summary"
    )
    print(f"Running test: {command}")
    os.system(command)
