# Why Connect WSL to Windows MySQL?

## Resource Efficiency and Development Streamlining

### 1. Avoid Redundant Installations
- Eliminate the need to install and maintain MySQL on both Windows and WSL
- Save valuable disk space by using a single MySQL instance
- Reduce system resource usage by running only one database server

### 2. Simplified Database Management
- Maintain a single source of truth for your data
- Avoid data synchronization issues between multiple MySQL instances
- Use familiar Windows tools like MySQL Workbench for database administration

### 3. Development Workflow Benefits
- Work seamlessly with existing Windows-based MySQL databases in WSL projects
- Keep your production-like environment in WSL while leveraging existing Windows infrastructure
- Utilize Windows backup and maintenance tools you're already familiar with

### 4. System Performance
- Reduce memory usage by not running duplicate database services
- Minimize background processes and system load
- Better resource allocation for development tasks

### 5. Maintenance Advantages
- Single point for updates and security patches
- One configuration to manage and backup
- Consistent database version across your development environment

This setup, while requiring initial configuration effort, provides a more efficient and manageable development environment that bridges the best of both Windows and Linux worlds.


# Connecting WSL to Windows MySQL Server
A comprehensive guide for connecting to a MySQL server installed on Windows from WSL (Windows Subsystem for Linux) on the same machine.

## Prerequisites
- Windows 10/11 with WSL installed
- MySQL Server installed on Windows
- MySQL Workbench (recommended for management)
- WSL Ubuntu distribution
- Python/Django project in WSL (if using with Django)

## Table of Contents
1. [MySQL Windows Configuration](#1-mysql-windows-configuration)
2. [User and Privileges Setup](#2-user-and-privileges-setup)
3. [Windows Firewall Configuration](#3-windows-firewall-configuration)
4. [WSL Configuration](#4-wsl-configuration)
5. [Testing Connection](#5-testing-connection)
6. [Django Integration](#6-django-integration)
7. [Troubleshooting](#7-troubleshooting)

## 1. MySQL Windows Configuration
### Locate MySQL Configuration File
The default MySQL configuration file is typically located at:
```
C:\ProgramData\MySQL\MySQL Server 8.0\my.ini
```

### Modify MySQL Configuration
1. Open `my.ini` with administrator privileges
2. Locate or add the following configuration under the `[mysqld]` section:
```ini
bind-address = 0.0.0.0
port = 3306
```
3. Save the file and restart MySQL service:
```powershell
# In Windows PowerShell (Admin)
Restart-Service MySQL80
```

## 2. User and Privileges Setup
### Create User and Grant Privileges
1. Open MySQL Workbench or MySQL Command Line Client
2. Connect as root user
3. Execute the following commands:
```sql
-- Option 1: Create new user with privileges
CREATE USER 'your_username'@'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database.* TO 'your_username'@'%';

-- Option 2: Grant privileges to existing user
GRANT ALL PRIVILEGES ON your_database.* TO 'existing_user'@'%';

-- Apply privileges
FLUSH PRIVILEGES;
```
for more information check the readme.md file

## 3. Windows Firewall Configuration
### Create Inbound Rule
1. Open "Windows Defender Firewall with Advanced Security"
2. Navigate to Inbound Rules
3. Create New Rule:
   - Rule Type: Port
   - Protocol: TCP
   - Port: 3306
   - Action: Allow the connection
   - Profile: Domain, Private, Public (or as needed)
   - Name: "MySQL WSL Access"

### Verify Firewall Rule
```powershell
# In Windows PowerShell (Admin)
Get-NetFirewallRule | Where-Object { $_.DisplayName -like "*MySQL*" }
```

## 4. WSL Configuration
### Install Required Packages
```bash
# In WSL terminal
sudo apt update
sudo apt install mysql-client
```

### Find Windows Host IP
```bash
# Method 1: Check resolv.conf
cat /etc/resolv.conf
# Look for nameserver IP

# Method 2: Using hostname
hostname -I

# Method 3: Get default gateway
ip route | grep default | awk '{print $3}'
```

## 5. Testing Connection
### Test MySQL Connection from WSL
```bash
# Basic connection test
mysql -h <windows-ip> -u your_username -p

# Test with specific database
mysql -h <windows-ip> -u your_username -p your_database

# Connection test using telnet
telnet <windows-ip> 3306
```

## 6. Django Integration
### Install MySQL Connector
```bash
# In your Django project's virtual environment
pip install mysqlclient
```

### Configure Django Settings
intsall requirements first
```bash
    # Navigate to project folder where requirements are located
    cd <project>
    # Install requirements
    pip install -r requirements.txt
```
Create a .env file first and save your settings
```.env
	DB_PASSWORD=password
	DB_USERNAME=username
	DB_DATABASE_NAME=name-of-your-database
	WINDOWS_HOST_IP=0.0.0.0
	PORT=3306
```
Update `settings.py`:
```python
import os
from pathlib import Path
import environ

# Initialize environment variables
env = environ.Env()
# Set the base directory to two levels up, reaching the folder with .env
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load the .env file
env.read_env(env_file=BASE_DIR / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_DATABASE_NAME'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('WINDOWS_HOST_IP'),  # Replace with your Windows IP address
        'PORT': env('PORT'),
    }
}
```

### Test Django Database Connection
```bash
# Test migrations
python manage.py migrate --dry-run

# Apply migrations
python manage.py migrate
```

## 7. Troubleshooting
### Common Issues and Solutions

#### Connection Refused
```bash
# Check if MySQL is running on Windows
sc query MySQL80

# Verify IP accessibility
ping <windows-ip>

# Check port accessibility
telnet <windows-ip> 3306
```

#### Access Denied
```sql
-- Verify user privileges in MySQL
SELECT user, host FROM mysql.user WHERE user = 'your_username';
SHOW GRANTS FOR 'your_username'@'%';
```

#### WSL Network Issues
```bash
# Restart WSL
wsl --shutdown
wsl

# Update WSL
wsl --update
```

## Security Considerations
1. Use strong passwords for MySQL users
2. Consider using environment variables for sensitive credentials
3. Limit user privileges to only necessary operations
4. Use specific host patterns instead of '%' when possible
5. Regularly update MySQL and WSL
6. Monitor login attempts and database access

## Additional Resources
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Django Database Documentation](https://docs.djangoproject.com/en/stable/ref/databases/#mysql-notes)

## License
This guide is provided under the MIT License. Feel free to modify and distribute as needed.

## By Joseph G. Wathome