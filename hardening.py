def get_hardening_recommendations():
    return [
        {
            "category": "SSH",
            "current": "PermitRootLogin yes",
            "recommendation": "PermitRootLogin no",
            "reason": "Prevents direct root access via SSH, forcing attackers to guess a user account first."
        },
        {
            "category": "SSH",
            "current": "PasswordAuthentication yes",
            "recommendation": "PasswordAuthentication no",
            "reason": "Enforces SSH key-based authentication, which is significantly more secure than passwords."
        },
        {
            "category": "Firewall",
            "current": "Firewall disabled",
            "recommendation": "sudo ufw enable",
            "reason": "Blocks unsolicited incoming connections and minimizes the attack surface."
        },
        {
            "category": "Updates",
            "current": "Manual updates",
            "recommendation": "Install unattended-upgrades",
            "reason": "Ensures security patches are applied automatically and promptly."
        },
        {
            "category": "Users",
            "current": "No MFA",
            "recommendation": "Configure libpam-google-authenticator",
            "reason": "Adds an extra layer of security beyond just a password."
        }
    ]
