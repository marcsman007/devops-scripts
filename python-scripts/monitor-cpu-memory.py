#!/usr/bin/env python3
import psutil
import smtplib

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")

    if cpu > CPU_THRESHOLD or memory > MEM_THRESHOLD:
        send_alert(cpu, memory)

def send_alert(cpu, memory):
    message = f"Alert! CPU: {cpu}% | Memory: {memory}%"
    print(message)

    # Example email notification
    sender = "your_email@example.com"
    recipient = "admin@example.com"
    subject = "System Alert"
    body = message
    email_message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP('localhost') as server:
            server.sendmail(sender, recipient, email_message)
        print("Alert email sent!")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    check_system()
