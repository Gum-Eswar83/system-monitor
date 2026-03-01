import psutil
import time
import os
from datetime import timedelta


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return str(timedelta(seconds=int(uptime_seconds)))


def get_top_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
    return processes[:5]


try:
    while True:
        clear_screen()

        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        uptime = get_uptime()
        top_processes = get_top_processes()

        print("=" * 50)
        print("         SYSTEM MONITOR DASHBOARD")
        print("=" * 50)
        print(f"CPU Usage       : {cpu}%")
        print(f"Memory Usage    : {memory}%")
        print(f"Disk Usage      : {disk}%")
        print(f"System Uptime   : {uptime}")

        print("\nTop 5 Processes:")
        for proc in top_processes:
            print(f"{proc['name']} (PID: {proc['pid']}) - CPU: {proc['cpu_percent']}%")

        if cpu > 80:
            print("\n⚠ ALERT: High CPU Usage!")
        if memory > 85:
            print("⚠ ALERT: High Memory Usage!")

        time.sleep(5)

except KeyboardInterrupt:
    print("\n\nMonitoring stopped safely ✅")