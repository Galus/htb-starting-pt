# Oopsie — Tier 2

**Target:** `10.129.x.x` — Web application with IDOR and file upload vulnerability leading to privilege escalation.

## Recon

```
PORT   STATE SERVICE
80/tcp open  http
```

## Exploitation

### Step 1 — Web Enumeration

Discovered the web application and identified an IDOR (Insecure Direct Object Reference) vulnerability in the URL parameters, allowing access to another user's session.

### Step 2 — IDOR to Access Admin Section

Modified the user ID parameter in the URL to access the admin panel, revealing an upload functionality.

### Step 3 — File Upload to Reverse Shell

Uploaded a PHP reverse shell to the server and triggered it to gain a foothold on the target.

### Step 4 — Database Credential Discovery

Found database credentials in the web application's configuration files:

```
mysql-creds.txt
```

### Step 5 — Privilege Escalation

Used discovered credentials to escalate privileges and read the root flag.

## Evidence

Key files collected during the challenge:

| File | Description |
|------|-------------|
| `cookie.txt` | Session cookies captured during exploitation |
| `dumped-login.php.txt` | PHP source code from the login page |
| `get-admin-user.py` / `get-admin-user2.py` | Scripts to extract admin user information |
| `main.py` | Python script used during exploitation |
| `mysql-creds.txt` | MySQL credentials discovered in config |
| `passwd-users.txt` | Password hash list |
| `passwdfile.txt` | Password file contents |
| `user-creds.txt` | User credentials |

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Service | HTTP (port 80) |
| Vulnerability | IDOR + File Upload |
| Attack Vector | IDOR to access admin panel -> upload webshell -> privilege escalation |
