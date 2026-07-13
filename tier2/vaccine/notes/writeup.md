# Vaccine — Tier 2

**Target:** `10.129.187.230` — Ubuntu Linux (FTP + HTTP + SSH)

## Recon

```
PORT   STATE  SERVICE    VERSION
21/tcp open   ftp        vsftpd 3.0.3 (Anonymous login allowed)
22/tcp open   ssh        OpenSSH 8.0p1 Ubuntu
80/tcp open   http       Apache httpd 2.4.41 (Ubuntu) — MegaCorp Login
```

Anonymous FTP contained `backup.zip` (password-protected).

## Exploitation

### Step 1 — Crack the ZIP

Extracted the PKZIP hash from `backup.zip` using `zip2john` and cracked it with John/Hashcat.

### Step 2 — Source Code Review

Extracted `index.php` from the ZIP. The login page checks:
```php
if($_POST['username'] === 'admin' && md5($_POST['password']) === "2cb42f8734ea607eefed3b70af13bbd3")
```

MD5 hash: `2cb42f8734ea607eefed3b70af13bbd3` — cracked to reveal the password.

### Step 3 — SQL Injection in Dashboard

Logged in and found a `dashboard.php` page vulnerable to SQL injection. Used it to extract PostgreSQL credentials:

| Field | Value |
|-------|-------|
| Host | localhost |
| Port | 5432 |
| Database | carsdb |
| User | postgres |
| Password | `P@s5w0rd!` |

### Step 4 — PostgreSQL RCE

Connected to PostgreSQL and used `COPY ... FROM PROGRAM` to execute system commands, gaining a reverse shell.

## Credentials Summary

| Source | User | Password |
|--------|------|----------|
| Login page | `admin` | (cracked MD5: `2cb42f8734ea607eefed3b70af13bbd3`) |
| PostgreSQL | `postgres` | `P@s5w0rd!` |
