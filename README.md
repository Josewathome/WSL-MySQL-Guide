

---

## Connecting WSL to Windows MySQL Server

This workflow assumes you are managing Windows MySQL instances from WSL or local tools. Focus is on **operational reliability, repeatable scripts, and maintainable privileges**—not basic command syntax.

### MySQL Operational Context

* Local MySQL in Windows often requires cross-context handling (WSL vs native tools).
* Scripts and automation should target **idempotent privilege management, automated backups, and operational monitoring**.
* Integrate with CI/CD or provisioning scripts where possible.

### Navigating MySQL

**Core queries for context, audit, and control**

```sql
-- List databases
SHOW DATABASES;

-- Switch working context
USE your_database;

-- Inspect schema
SHOW TABLES;
DESCRIBE table_name;

-- Users and privileges
SELECT user, host FROM mysql.user;
SHOW GRANTS FOR 'username'@'host';
```

### Typical Database Lifecycle Operations

* Emphasize scripts over manual entry

```sql
-- Table creation
CREATE TABLE example_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CRUD patterns
INSERT INTO example_table (name) VALUES ('example');
SELECT * FROM example_table;
UPDATE example_table SET name='new_name' WHERE id=1;
DELETE FROM example_table WHERE id=1;
```

### Server Inspection & Monitoring

* Scripts should check **version, user context, performance metrics** regularly

```sql
SELECT VERSION(), USER();
SHOW STATUS;
SHOW VARIABLES;
SHOW PROCESSLIST;
```

### Backups and Restore (Operational Perspective)

* Automate via scripts; include timestamped backups; integrate with monitoring

```bash
# Backup database (append date in production scripts)
mysqldump -u root -p your_database > backup_$(date +%F).sql

# Restore database
mysql -u root -p your_database < backup.sql
```

### MySQL Workbench Integration

* Useful for **visual schema management and performance monitoring**
* Recommended: script repetitive tasks; use Workbench for exception handling

  * SCHEMAS → view & modify databases
  * ADMINISTRATION → user, replication, server logs
  * PERFORMANCE → monitor slow queries, connections

### Best Practices (Senior-Level Focus)

1. **Naming & Consistency**

```sql
CREATE DATABASE my_app_db;
CREATE TABLE user_profiles;
```

2. **Automated Maintenance**

```sql
ANALYZE TABLE table_name;
OPTIMIZE TABLE table_name;
CHECK TABLE table_name;
```

3. **Privileges & Security**

* Always script privilege changes; avoid ad-hoc root usage

```sql
ALTER USER 'username'@'host' IDENTIFIED BY 'strong_password';
GRANT SELECT, INSERT ON my_app_db.* TO 'username'@'host';
REVOKE ALL PRIVILEGES ON my_app_db.* FROM 'username'@'host';
FLUSH PRIVILEGES;
```

4. **Performance Monitoring**

* Capture and alert on anomalies

```sql
SHOW VARIABLES LIKE '%slow_query%';
SHOW VARIABLES LIKE 'max_connections';
```

### Common Operational Issues

**Connectivity & visibility issues**

```sql
-- MySQL not reachable
SHOW STATUS;

-- Permissions issues
SHOW GRANTS;

-- Database not visible
FLUSH PRIVILEGES;
SHOW DATABASES LIKE 'target_db';
```

**Root password resets or user fixes**: script with proper auditing; avoid interactive ad-hoc resets in production.

---

