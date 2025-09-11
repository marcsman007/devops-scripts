#!/usr/bin/env python3
import os
import subprocess
import time

SERVICE = "nginx"

def is_running(service):
    result = subprocess.run(['systemctl', 'is-active', service],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return result.stdout.decode().strip() == 'active'

def restart_service(service):
    print(f"Restarting {service}...")
    os.system(f"sudo systemctl restart {service}")

if __name__ == "__main__":
    while True:
        if not is_running(SERVICE):
            print(f"{SERVICE} is down! Restarting...")
            restart_service(SERVICE)
        else:
            print(f"{SERVICE} is running fine.")
        time.sleep(10)
