# HTB Starting Point

> A curated collection of writeups and evidence for Hack The Box **Starting Point** challenges — from Tier 0 fundamentals through Tier 2 exploitation.

All challenges were worked through step-by-step. Each folder contains `notes/writeup.md` with a full walkthrough and `evidence/` with raw artifacts (flags, scans, credentials, scripts, etc.).

---

## Repository Structure

```
.
├── tier0/              # Tier 0 — Fundamentals
│   ├── meow/           # Telnet, default credentials
│   ├── fawn/           # Anonymous FTP access
│   ├── dancing/        # SMB anonymous share
│   ├── redeemer/       # Unauthenticated Redis
│   ├── responder/      # LLMNR/NBT-NS poisoning
│   └── three/          # AWS S3 bucket enumeration
├── tier1/              # Tier 1 — Basic Web & Services
│   ├── appointment/    # SQL injection login bypass
│   ├── sequel/         # MySQL default credentials
│   └── crocodile/      # FTP → Web credential reuse
└── tier2/              # Tier 2 — Multi-step Exploitation
    ├── archetype/      # SMB/MSSQL → WinRM (Windows)
    ├── oopsie/         # IDOR + file upload → RCE
    ├── unified/        # UniFi controller → MongoDB RCE
    └── vaccine/        # FTP → SQL injection → sudo
```

---

## Challenge Overview

### Tier 0 — Fundamentals

| Challenge | Concept | Ports | Technique |
|-----------|---------|-------|-----------|
| **Meow** | Telnet misconfiguration | 23/tcp | Login with `root:root` default credentials |
| **Fawn** | Anonymous FTP | 21/tcp | Download flag without authentication |
| **Dancing** | SMB null session | 445/tcp | Enumerate and access anonymous shares |
| **Redeemer** | Redis no-auth | 6379/tcp | List keys and retrieve flag from Redis |
| **Responder** | LLMNR poisoning | — | Capture NetNTLMv2 hash, crack with hashcat |
| **Three** | S3 misconfiguration | 80/tcp (web) | VHost discovery → upload webshell to S3 bucket |

### Tier 1 — Basic Web & Services

| Challenge | Concept | Ports | Technique |
|-----------|---------|-------|-----------|
| **Appointment** | SQL injection | 80/tcp | Bypass login with `admin'-- -` |
| **Sequel** | MySQL weak auth | 3306/tcp | Connect as `root` with no password |
| **Crocodile** | FTP credential leak | 21/tcp, 80/tcp | Anonymous FTP → found creds → web login |

### Tier 2 — Multi-step Exploitation

| Challenge | Concept | Target | Attack Path |
|-----------|---------|--------|-------------|
| **Archetype** | Windows AD lateral movement | Win Server 2019 | SMB null session → MSSQL creds → `xp_cmdshell` → PowerShell history → admin WinRM |
| **Oopsie** | IDOR + file upload | Linux web app | IDOR to admin panel → upload webshell → DB cred discovery → privilege escalation |
| **Unified** | Log4Shell + MongoDB | Ubuntu Linux | Log4Shell RCE on UniFi controller → connect to MongoDB from target → read root flag |
| **Vaccine** | FTP + SQLi + sudo | Ubuntu Linux | Anonymous FTP → SQL injection → hash cracking → `pgpass` → sudo `vi` |

---

## Flags

| Challenge | Flag |
|-----------|------|
| Meow | _(retrieve via Telnet)_ |
| Fawn | `035db21c881520061c53e0536e44f815` |
| Dancing | `5f61c10dffbc77a704d76016a22f1664` |
| Redeemer | `03e1d2b376c37ab3f5319922053953eb` |
| Responder | Cracked `Administrator` password: `badminton` |
| Three | _(retrieve via webshell)_ |
| Appointment | `e3d0796d002a446c0e622226f42e9672` |
| Sequel | `7b4bec00d1a39e3dd4e021ec3d915da8` |
| Crocodile | _(retrieve via web login)_ |
| Archetype (user) | `3e7b102e78218e935bf3f4951fec21a3` |
| Archetype (root) | `b91ccec3305e98240082d4474b848528` |
| Oopsie | _(retrieve on target)_ |
| Unified (user) | _(in evidence/user.txt)_ |
| Unified (root) | _(in evidence/root-password.txt)_ |
| Vaccine | _(in evidence/hash.txt, cracked)_ |

---

## Tools Used

| Category | Tools |
|----------|-------|
| Scanning | `nmap`, `gobuster` |
| SMB | `smbclient`, `impacket-smbclient`, `impacket-mssqlclient` |
| Web | `curl`, `burpsuite`, browser dev tools |
| Database | `mysql`, `redis-cli`, `mongo`, `sqlmap` |
| Exploitation | `responder`, `hashcat`, `evil-winrm`, python reverse shells |
| Cloud | `aws-cli` (S3 endpoint) |
| File Transfer | `ftp`, `python3 -m http.server`, `certutil` |

---

## Organization

Each challenge follows this layout:

```
challenge/
├── evidence/           # Raw files from the target
│   ├── flag.txt        # Captured flag(s)
│   ├── host            # Target IP
│   ├── nmap-results.txt
│   └── ...             # Other artifacts
└── notes/
    └── writeup.md      # Full step-by-step walkthrough
```

---

*Created by Mario Galus — walkthroughs and evidence collected during HTB Starting Point practice.*
