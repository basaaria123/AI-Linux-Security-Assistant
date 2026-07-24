from langchain.tools import tool
from command_parser import explain_command_security
from permission_checker import analyze_permissions
from hardening import get_hardening_recommendations

@tool
def explain_linux_command(command: str) -> str:
    """Explains a Linux command and its security implications."""
    info = explain_command_security(command)
    if isinstance(info, str):
        return info
    return f"Command: {info['command']}\nPurpose: {info['purpose']}\nSecurity Risk: {info['security_risk']}\nAdvice: {info['advice']}"

@tool
def check_linux_permissions(permissions: str) -> str:
    """Analyzes Linux file/directory permissions (symbolic or octal)."""
    analysis = analyze_permissions(permissions)
    if isinstance(analysis, str):
        return analysis
    
    risks = "\n".join([f"- {r}" for r in analysis['risks']])
    return f"Format: {analysis['format']}\nUser: {analysis['user']}, Group: {analysis['group']}, Others: {analysis['others']}\nRisks:\n{risks}"

@tool
def get_hardening_tips(dummy: str = "") -> str:
    """Provides Linux system hardening recommendations."""
    tips = get_hardening_recommendations()
    output = "System Hardening Recommendations:\n"
    for tip in tips:
        output += f"\nCategory: {tip['category']}\nCurrent: {tip['current']}\nRecommendation: {tip['recommendation']}\nReason: {tip['reason']}\n"
    return output
