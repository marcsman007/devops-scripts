# DevOps Scripts Collection

A collection of **Bash** and **Python** scripts for **system automation, monitoring, and cloud management**.  
These scripts showcase my skills in **DevOps**, **cloud infrastructure**, and **automation** by solving real-world problems like backups, service management, AWS operations, and log analysis.

---

## 📂 Project Structure

```
devops-scripts/
│
├── README.md
│
├── bash-scripts/
│ ├── system-health-check.sh       # System performance report
│ ├── backup-to-s3.sh              # Backup files to AWS S3
│ ├── restart-service.sh           # Restart a Linux service
│ └── docker-cleanup.sh            # Clean up Docker resources
│
└── python-scripts/
    ├── aws/                       # AWS / Cloud automation scripts
    │   ├── ec2_health_check.py    # Check EC2 instance health
    │   ├── s3_backup.py           # Backup local folder to S3
    │   └── aws-ec2-manager.py     # List EC2 instances
    │
    └── system/                    # Local system automation scripts
        ├── monitor-cpu-memory.py  # Monitor CPU & memory, send alerts
        ├── log-parser.py          # Search logs for keywords
        └── auto-restart-service.py # Restart a service if it goes down

```

---

## 🚀 Getting Started

### **1. Clone the Repository**
```bash
git clone https://github.com/marcsman007/devops-scripts.git
cd devops-scripts

```

### **2. Requirements**
Bash Scripts

Linux or MacOS terminal

awscli installed for S3 backup script

```bash
sudo apt-get install awscli
aws configure

```

Python Scripts

Python 3.8+

Install dependencies

```bash
pip install -r requirements.txt

```

Sample requirements.txt
```nginx
boto3
psutil

```

🐚 Bash Scripts
1. System Health Check

Checks CPU, memory, disk usage, and top processes.

```bash
bash bash-scripts/system-health-check.sh

```

```yaml
===== System Health Check =====
Hostname: dev-server
Date: Sat Sep 6 10:00:00 UTC 2025
--------------------------------
CPU Load:
10:00:00 up 5 min, 2 users, load average: 0.12, 0.10, 0.05
--------------------------------
Memory Usage:
              total        used        free
Mem:           7.8G        3.2G        4.6G
--------------------------------
Disk Usage:
total        50G   30G   20G  60%
--------------------------------
Top 5 Memory-Consuming Processes:
PID   PPID  CMD             %MEM %CPU
2345  1     python3 app.py  12.3 8.5

```

2. Backup to S3

Uploads a folder to an S3 bucket with timestamp.

```bash
bash bash-scripts/backup-to-s3.sh /path/to/folder my-backup-bucket

```

Example:
```swift
Backing up /home/user/projects to s3://my-backup-bucket/backup_20250906_100000 ...
Backup completed successfully!

```

3. Restart a Service

Restarts a Linux service and logs the action.

```bash
bash bash-scripts/restart-service.sh nginx

```
Log file location: /var/log/service-restart.log

4. Docker Cleanup

Removes unused containers, images, and volumes.

```bash
bash bash-scripts/docker-cleanup.sh

```

🐍 Python Scripts
AWS / Cloud Automation
1. EC2 Health Check
Checks the health/status of all EC2 instances in a region.
```bash
python3 python-scripts/aws/ec2_health_check.py --region ap-southeast-1
```
Sample Output:
```yaml
INFO:__main__:Instance ID: i-05f2ce0b34ca10b09, State: running
INFO:__main__:Instance ID: i-0abcd1234efgh5678, State: stopped
WARNING:__main__:Instance i-0abcd1234efgh5678 is not running!
```

2. S3 Backup
Backs up a local folder to an S3 bucket under a timestamped folder.
```bash
python3 python-scripts/aws/s3_backup.py --local ~/test_backup --bucket my-bucket-name
```
Sample Output:
```yaml
INFO:__main__:Uploaded /home/ubuntu/test_backup/file1.txt to s3://my-bucket-name/backup/20250911_041000/file1.txt
```
3. AWS EC2 Manager

Lists all EC2 instances in your AWS account.
```bash
python3 python-scripts/aws-ec2-manager.py

```

Sample Output:
```yaml
EC2 Instances:
ID: i-0abcd1234efgh5678 | State: running
ID: i-0abcd1234efgh5679 | State: stopped

```
💡 Make sure AWS CLI is configured:
```bash
aws configure
```

System Automation
1. Monitor CPU & Memory

Alerts if CPU or memory usage exceeds 80%.

```bash
python3 python-scripts/monitor-cpu-memory.py

```

Sample Output:
```yaml
CPU Usage: 75% | Memory Usage: 62%
CPU Usage: 85% | Memory Usage: 90%
Alert! CPU: 85% | Memory: 90%
Alert email sent!

```

2. Log Parser

Searches for a specific keyword in a log file.

```bash
python3 python-scripts/log-parser.py /var/log/syslog error

```

Sample Output:
```nginx
Sep 06 10:00:00 server1 kernel: error: disk failure detected
Sep 06 10:05:00 server1 app: error: service crashed
```

3. Auto-Restart Service

Monitors a service and restarts it automatically if down.

```bash
python3 python-scripts/auto-restart-service.py
```
Sample Output:
```csharp
nginx is running fine.
nginx is down! Restarting...
Restarting nginx...
```

🧑‍💻 About Me

Hi, I'm Marc Jayson Macaburas, a Technical Support Specialist transitioning into DevOps.
I built this repository to showcase practical automation and infrastructure scripts.

🌍 Location: Philippines

💼 LinkedIn: www.linkedin.com/in/marc-jayson-macaburas

🐙 GitHub: https://github.com/marcsman007

