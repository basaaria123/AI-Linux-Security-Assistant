import re

def parse_command(command_str):
    """
    Parses a Linux command string to extract the base command and options.
    In a real scenario, this might use a more robust parser or an LLM.
    """
    parts = command_str.split()
    if not parts:
        return None
    
    base_command = parts[0]
    options = [p for p in parts[1:] if p.startswith('-')]
    arguments = [p for p in parts[1:] if not p.startswith('-')]
    
    return {
        "command": base_command,
        "options": options,
        "arguments": arguments
    }

def explain_command_security(command_str):
    """
    Provides a basic explanation and security context for common Linux commands.
    """
    parsed = parse_command(command_str)
    if not parsed:
        return "Invalid command."

    cmd = parsed['command']
    
    security_database = {
        "chmod": {
            "purpose": "Change file mode bits (permissions).",
            "security_risk": "High if used incorrectly (e.g., chmod 777).",
            "advice": "Always use the most restrictive permissions possible (e.g., 600 or 700)."
        },
        "chown": {
            "purpose": "Change file owner and group.",
            "security_risk": "Medium. Incorrect ownership can lead to unauthorized access or privilege escalation.",
            "advice": "Ensure files are owned by the appropriate service user, not root, if possible."
        },
        "sudo": {
            "purpose": "Execute a command as another user, usually the superuser.",
            "security_risk": "Critical. Grants full system access.",
            "advice": "Use sudo only for tasks that strictly require it. Audit sudoers file regularly."
        },
        "rm": {
            "purpose": "Remove files or directories.",
            "security_risk": "Low/Medium (Data loss). rm -rf / is catastrophic.",
            "advice": "Use with caution, especially with wildcards and recursive flags."
        },
        "ssh": {
            "purpose": "OpenSSH SSH client (remote login program).",
            "security_risk": "Medium/High. If misconfigured, allows remote access.",
            "advice": "Disable root login, use SSH keys instead of passwords, and change default port."
        },
        "ufw": {
            "purpose": "Uncomplicated Firewall - interface for managing a netfilter firewall.",
            "security_risk": "Low (Protective).",
            "advice": "Always enable a firewall and only allow necessary ports."
        }
    }

    info = security_database.get(cmd, {
        "purpose": "General Linux command.",
        "security_risk": "Varies by usage.",
        "advice": "Check the man pages (man " + cmd + ") for detailed security information."
    })
    
    return {
        "command": cmd,
        "purpose": info['purpose'],
        "security_risk": info['security_risk'],
        "advice": info['advice']
    }
