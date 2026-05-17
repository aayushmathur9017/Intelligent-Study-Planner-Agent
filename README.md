# Intelligent Study Planner Agent

A simple Python agent that uses LangChain with Ollama to create a personalized intelligent study planner.

## Prerequisites

- Python 3.10+ installed
- [Ollama](https://ollama.ai) installed and running locally
- A model available in Ollama, for example `llama3.2:latest` or `llama3:latest`

## Setup

1. Open a terminal in this project folder.
2. Create a virtual environment and activate it:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Start Ollama if it is not already running.

## Run the agent

```powershell
python intelligent_study_planner.py
```

Then type a study planning request, for example:

> I need a 2-week study plan for biology and math with 3 hours per day and an exam on June 1.

## Run the web interface

Install dependencies if you have not already:

```powershell
python -m pip install -r requirements.txt
```

Start the local website:

```powershell
python app.py
```

Open your browser to:

```text
http://127.0.0.1:5000
```

The web UI now accepts:
- a study request
- syllabus or topic list
- weak areas to adjust the plan

## Customization

- Change the Ollama model in `app.py` if you want to use a different local model.
- Extend the planning tool with additional constraints like learning style, topic difficulty, or review sessions.
