#!/bin/bash
# Restart a service and log the event
# Usage: ./restart-service.sh service_name

SERVICE=$1
LOGFILE="/var/log/service-restart.log"

if [ -z "$SERVICE" ]; then
  echo "Usage: $0 service_name"
  exit 1
fi

echo "$(date): Restarting $SERVICE..." | tee -a $LOGFILE
sudo systemctl restart $SERVICE

if [ $? -eq 0 ]; then
  echo "$(date): $SERVICE restarted successfully!" | tee -a $LOGFILE
else
  echo "$(date): Failed to restart $SERVICE!" | tee -a $LOGFILE
fi
