# Unified — Tier 2

**Target:** `10.129.188.120` — Ubuntu Linux (UniFi Network Controller)

## Recon

```
PORT     STATE  SERVICE         VERSION
22/tcp   open   ssh             OpenSSH 8.2p1 Ubuntu
6789/tcp open   ibm-db2-admin?
8080/tcp open   http            Apache Tomcat (redirects → 8443)
8443/tcp open   ssl/nagios-nsca UniFi Network (HTTPS)
```

## Exploitation

### Step 1 — Log4Shell (CVE-2021-44228)

The UniFi login page at `https://10.129.188.120:8443/manage` is vulnerable to Log4j RCE. Sent a crafted JNDI payload via the `remember` field in the login POST request to trigger Log4Shell, spawning a reverse shell as `unifi`.

### Step 2 — Local MongoDB (No Auth)

MongoDB was running locally on port **27117** with no authentication:

```
mongo --port 27117
show dbs
# ace, ace_stat, admin, config, local
```

In the `ace` database, the `admin` collection contained the admin user's `x_shadow` hash (SHA-512). Replaced it with a known hash:

```
mongo --port 27117 ace --eval 'db.admin.updateOne(
  {_id: ObjectId("61ce278f46e0fb0012d47ee4")},
  {$set: {x_shadow: "$6$QosJcQDSZQwoHd.g$AXcHRGK29OHdWbAZuOhOlaC.AsotIg9Mlae9bhjuxmKxu8hwxyExR4ITg3VJ60hrXlPuGvWcGAo4P6BbOHYn1/"}})'
```

This set the admin password to `12qwaszx!`.

### Step 3 — UniFi Admin Access

Logged into the UniFi dashboard as `admin` / `12qwaszx!`. Found the device SSH credentials in **Settings → System → Device Authentication**:

| User   | Password                    |
|--------|-----------------------------|
| `root` | `NotACrackablePassword4U2022` |

### Step 4 — SSH as Root

Used the credentials to SSH directly as root.

## Flags

| Flag | Value |
|------|-------|
| User | `6ced1a6a89e666c0620cdb10262ba127` |
| Root | `NotACrackablePassword4U2022` |
