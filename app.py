import streamlit as st
import pandas as pd
from linux_agent import run_linux_assistant
from report_generator import generate_pdf_report
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Linux Security Assistant", page_icon="🛡️", layout="wide")

st.sidebar.title("🛡️ Linux Security Assistant")
st.sidebar.markdown("Help students learn Linux Security through AI.")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Main Input Section
st.title("AI-Powered Linux Security Assistant")

tab1, tab2, tab3 = st.tabs(["Command Analysis", "Permission Checker", "System Hardening"])

with tab1:
    st.header("Linux Command Analysis")
    user_command = st.text_input("Enter a Linux command (e.g., chmod 777 file.txt):")
    if st.button("Analyze Command"):
        if user_command:
            with st.spinner("Analyzing..."):
                response = run_linux_assistant(f"Analyze this command: {user_command}")
                st.markdown(response)
                st.session_state['history'].append({"type": "Command", "input": user_command, "output": response})
        else:
            st.warning("Please enter a command.")

with tab2:
    st.header("Permission Analyzer")
    perm_string = st.text_input("Enter permissions (e.g., 755 or -rwxrwxrwx):")
    if st.button("Check Permissions"):
        if perm_string:
            with st.spinner("Analyzing..."):
                response = run_linux_assistant(f"Analyze these permissions: {perm_string}")
                st.markdown(response)
                st.session_state['history'].append({"type": "Permission", "input": perm_string, "output": response})
        else:
            st.warning("Please enter a permission string.")

with tab3:
    st.header("System Hardening")
    if st.button("Generate Hardening Steps"):
        with st.spinner("Generating..."):
            response = run_linux_assistant("Give me system hardening recommendations.")
            st.markdown(response)
            st.session_state['history'].append({"type": "Hardening", "input": "Hardening Steps", "output": response})

# Report Generation
st.divider()
st.header("Generate Security Report")
if st.button("Download PDF Report"):
    if st.session_state['history']:
        report_content = "Linux Security Assistant Analysis History\n\n"
        for item in st.session_state['history']:
            report_content += f"--- {item['type']} ---\nInput: {item['input']}\nOutput: {item['output']}\n\n"
        
        pdf_path = generate_pdf_report(report_content)
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", f, file_name="linux_security_report.pdf")
    else:
        st.info("No history available to generate a report. Perform some analyses first.")

# Display History in sidebar
if st.session_state['history']:
    st.sidebar.divider()
    st.sidebar.subheader("Recent Activity")
    for item in st.session_state['history'][-5:]:
        st.sidebar.text(f"{item['type']}: {item['input'][:20]}...")
