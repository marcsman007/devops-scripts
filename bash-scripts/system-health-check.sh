#!/bin/bash
# System Health Check Script
# Usage: ./system-health-check.sh

echo "===== System Health Check ====="
echo "Hostname: $(hostname)"
echo "Date: $(date)"
echo "--------------------------------"

# CPU
echo "CPU Load:"
uptime

# Memory
echo "--------------------------------"
echo "Memory Usage:"
free -h

# Disk
echo "--------------------------------"
echo "Disk Usage:"
df -h --total | grep total

# Top 5 processes by memory
echo "--------------------------------"
echo "Top 5 Memory-Consuming Processes:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6

echo "--------------------------------"
echo "Done!"
