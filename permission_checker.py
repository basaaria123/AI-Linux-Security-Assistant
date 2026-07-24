import stat
import os

def analyze_permissions(perm_string):
    """
    Analyzes a permission string like '-rwxrwxrwx' or '777'.
    """
    if len(perm_string) == 10: # Symbolic format: -rwxrwxrwx
        return analyze_symbolic(perm_string)
    elif len(perm_string) == 3 and perm_string.isdigit(): # Octal format: 777
        return analyze_octal(perm_string)
    else:
        return "Invalid permission format. Use symbolic (e.g., -rwxr-xr-x) or octal (e.g., 755)."

def analyze_symbolic(perm):
    file_type = perm[0]
    user = perm[1:4]
    group = perm[4:7]
    others = perm[7:10]
    
    risks = []
    if 'w' in others:
        risks.append("World-writable: Anyone can modify this file/directory.")
    if 'x' in others and file_type != 'd':
        risks.append("World-executable: Anyone can execute this file.")
    if user == 'rwx' and group == 'rwx' and others == 'rwx':
        risks.append("Critical: Full permissions granted to everyone (777).")

    return {
        "format": "Symbolic",
        "user": user,
        "group": group,
        "others": others,
        "risks": risks if risks else ["No obvious weak permissions detected for this string."]
    }

def analyze_octal(perm):
    mapping = {
        '7': 'rwx', '6': 'rw-', '5': 'r-x', '4': 'r--',
        '3': '-wx', '2': '-w-', '1': '--x', '0': '---'
    }
    user = mapping.get(perm[0], '???')
    group = mapping.get(perm[1], '???')
    others = mapping.get(perm[2], '???')
    
    return analyze_symbolic(f"-{user}{group}{others}")
