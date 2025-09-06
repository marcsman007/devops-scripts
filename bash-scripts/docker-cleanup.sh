#!/bin/bash
# Docker Cleanup Script
# Usage: ./docker-cleanup.sh

echo "Cleaning up Docker..."

docker system prune -af
docker volume prune -f

echo "Docker cleanup complete!"
