# Connecting WSL to Windows MySQL Server
[Previous sections remain the same until we add the new section after User and Privileges Setup]

## MySQL Windows Navigation Guide
### Accessing MySQL in Windows
1. **Using MySQL Command Line Client**
```bash
# Method 1: Using MySQL Command Line Client
# Open MySQL Command Line Client from Start Menu
# Enter root password when prompted

# Method 2: Using command prompt
mysql -u root -p
# Enter password when prompted
```

### Basic MySQL Navigation Commands
```sql
-- Show all databases
SHOW DATABASES;

-- Create a new database
CREATE DATABASE your_database_name;

-- Select a database to use
USE your_database_name;

-- Show all tables in current database
SHOW TABLES;

-- Show current database
SELECT DATABASE();

-- Show table structure
DESCRIBE table_name;
-- OR
SHOW COLUMNS FROM table_name;

-- Show users and their hosts
SELECT user, host FROM mysql.user;

-- Show user privileges
SHOW GRANTS FOR 'username'@'host';
```

### Common Database Operations
```sql
-- Create a new table
CREATE TABLE example_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO example_table (name) VALUES ('test_name');

-- Select data
SELECT * FROM example_table;

-- Update data
UPDATE example_table SET name = 'new_name' WHERE id = 1;

-- Delete data
DELETE FROM example_table WHERE id = 1;
```

### MySQL Status and Information
```sql
-- Show MySQL version
SELECT VERSION();

-- Show current user
SELECT USER();

-- Show server status
SHOW STATUS;

-- Show server variables
SHOW VARIABLES;

-- Show running processes
SHOW PROCESSLIST;
```

### Database Backup and Restore
```bash
# In Windows Command Prompt

# Backup database
mysqldump -u root -p your_database > backup.sql

# Restore database
mysql -u root -p your_database < backup.sql
```

### Using MySQL Workbench
1. **Open MySQL Workbench**
   - Launch MySQL Workbench from Start Menu
   - Connect to your local instance (usually localhost:3306)

2. **Navigator Panel Operations**
   - SCHEMAS: View and manage databases
   - ADMINISTRATION: Server management
   - PERFORMANCE: Monitor server performance

3. **Common Tasks in Workbench**
   ```
   - Create new schema: Right-click in SCHEMAS → Create Schema
   - Create new table: Right-click on Tables → Create Table
   - Execute queries: Click on 'Create a new SQL tab' button
   - Import/Export data: Server → Data Import/Export
   ```

### Best Practices for Database Management
1. **Naming Conventions**
   ```sql
   -- Use lowercase for database names
   CREATE DATABASE my_application_db;
   
   -- Use underscores for table names
   CREATE TABLE user_profiles;
   ```

2. **Regular Maintenance**
   ```sql
   -- Analyze tables
   ANALYZE TABLE table_name;
   
   -- Optimize tables
   OPTIMIZE TABLE table_name;
   
   -- Check table
   CHECK TABLE table_name;
   ```

3. **Security Best Practices**
   ```sql
   -- Change user password
   ALTER USER 'username'@'host' IDENTIFIED BY 'new_password';
   
   -- Revoke privileges if needed
   REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'host';
   
   -- Grant specific privileges
   GRANT SELECT, INSERT ON database_name.* TO 'username'@'host';
   ```

4. **Performance Monitoring**
   ```sql
   -- Check slow queries
   SHOW VARIABLES LIKE '%slow_query%';
   SHOW VARIABLES LIKE '%long_query_time%';
   
   -- Check max connections
   SHOW VARIABLES LIKE 'max_connections';
   ```

[Rest of the previous README.md content remains the same]

### Quick Reference for Common Issues
1. **Can't Connect to MySQL**
   ```sql
   -- Check if MySQL is running
   SHOW STATUS;
   
   -- Check user permissions
   SHOW GRANTS;
   ```

2. **Access Denied Errors**
   ```sql
   -- Verify user exists
   SELECT user, host FROM mysql.user WHERE user = 'your_username';
   
   -- Reset root password (if needed)
   -- Follow MySQL documentation for password reset procedure
   ```

3. **Database Not Visible**
   ```sql
   -- Refresh privileges
   FLUSH PRIVILEGES;
   
   -- Check database existence
   SHOW DATABASES LIKE 'database_name';
   ```



## By Joseph G. Wathome