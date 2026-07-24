# AI Linux Security Assistant 🛡️

An AI-powered assistant designed to help students and beginners learn Linux Security.

## Features
- **Linux Command Explanation:** Understand the purpose and security risks of commands.
- **Permission Analyzer:** Interpret symbolic and octal permissions and identify vulnerabilities.
- **System Hardening:** Get actionable recommendations for securing Linux servers.
- **Security Reports:** Generate downloadable PDF reports of your analysis history.

## Technology Stack
- **AI Framework:** LangChain & LangGraph
- **LLM:** Google Gemini (via `gemini-1.5-flash`)
- **Frontend:** Streamlit
- **PDF Generation:** ReportLab

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd AI_Linux_Security_Assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Google API Key:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `app.py`: Main Streamlit interface.
- `linux_agent.py`: LangGraph agent definition and logic.
- `tools.py`: Custom AI tools for command parsing and permission checking.
- `command_parser.py`: Logic for explaining Linux commands.
- `permission_checker.py`: Logic for analyzing file permissions.
- `hardening.py`: System hardening recommendations.
- `report_generator.py`: PDF report generation utility.
- `prompts.py`: System prompts for the AI.
