<p align="center">
    <img src="https://img.freepik.com/free-vector/chatbot-chat-message-vectorart_78370-4104.jpg?semt=ais_hybrid&w=740" align="center" width="30%">
</p>
<p align="center"><h1 align="center">INTERVIEWBOT</h1></p>
<p align="center">
	<img src="https://img.shields.io/github/license/Arush04/InterviewBot?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Arush04/InterviewBot?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Arush04/InterviewBot?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Arush04/InterviewBot?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

##  Overview

<p>❯ Interview Bot is an AI-powered virtual interviewer designed to simulate real-world interview experiences. Built using the OpenAI API for natural language understanding and the Whisper model for speech-to-text transcription, the bot can conduct voice-based interviews, interpret responses, and provide dynamic follow-up questions — much like a human interviewer would.
</p>
<p>
❯ This project aims to assist job seekers in preparing for interviews by offering realistic, interactive mock sessions. Whether you're practicing for technical, behavioral, or situational questions, Interview Bot adapts in real time to simulate a wide range of interview styles and question flows.
</p>

##  Features

<ul>
  <li>
    🎤 <strong>Audio Input Support</strong>
    <ul>
      <li>Accepts spoken responses via audio file uploads at the <code>/talk</code> endpoint.</li>
      <li>Uses OpenAI’s <strong>Whisper</strong> model to transcribe audio into text.</li>
    </ul>
  </li>

  <li>
    🧠 <strong>AI-Powered Interviewer</strong>
    <ul>
      <li>Simulates an AI interviewer using <strong>GPT-3.5 Turbo</strong>.</li>
      <li>Asks contextually relevant questions based on user responses.</li>
      <li>Maintains a consistent persona: <code>Jarvis</code>, interviewing the user <code>Arush</code>.</li>
    </ul>
  </li>

  <li>
    📂 <strong>Session Memory</strong>
    <ul>
      <li>Stores full conversation history in <code>database.json</code>.</li>
      <li>Uses stored messages to keep the conversation contextual and coherent.</li>
    </ul>
  </li>

  <li>
    📄 <strong>Customizable Interview Prompts</strong>
    <ul>
      <li>Starts with a system prompt tailored for Machine Learning Engineer interviews.</li>
      <li>Can be easily adapted for other roles by modifying the system prompt.</li>
    </ul>
  </li>

  <li>
    ⚡ <strong>Lightweight & Fast API</strong>
    <ul>
      <li>Built using <strong>FastAPI</strong> for quick performance and easy integration.</li>
    </ul>
  </li>

  <li>
    🔒 <strong>Environment Variable Configuration</strong>
    <ul>
      <li>Securely manages API keys and organization ID using <code>.env</code> and <code>python-dotenv</code>.</li>
    </ul>
  </li>

  <li>
    📊 <strong>Minimal Dependencies</strong>
    <ul>
      <li>Uses only essential libraries: <code>openai</code>, <code>torch</code>, <code>fastapi</code>, <code>requests</code>, and <code>dotenv</code>.</li>
    </ul>
  </li>
</ul>


##  Project Structure

```sh
└── InterviewBot/
    ├── LICENSE
    ├── README.md
    ├── main.py
    └── requirements.txt
```


##  Getting Started

###  Installation

Install InterviewBot using one of the following methods:

## 🚀 Build from Source

Follow these steps to set up the development environment locally:

<ul>
  <li><strong>Clone the InterviewBot repository:</strong>
    <pre><code>git clone https://github.com/Arush04/InterviewBot.git</code></pre>
  </li>

  <li><strong>Navigate to the project directory:</strong>
    <pre><code>cd InterviewBot</code></pre>
  </li>

  <li><strong>Install the project dependencies:</strong><br>
    Using <code>pip</code> &nbsp;
    <a href="https://pypi.org/project/pip/">
      <img src="https://img.shields.io/badge/Pip-3776AB.svg?style=flat&logo=pypi&logoColor=white" alt="pip badge" />
    </a>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Configure your OpenAI credentials:</strong><br>
    Open the <code>main.py</code> file and replace the following with your own keys:
    <ul>
      <li><code>openai.api_key</code> &rarr; Your OpenAI API Key</li>
      <li><code>openai.organization</code> &rarr; Your OpenAI Organization ID</li>
    </ul>
  </li>

  <li><strong>Create an empty database file:</strong><br>
    In the project root directory, run:
    <pre><code>touch database.json</code></pre>
  </li>

  <li><strong>Start the FastAPI server with Uvicorn:</strong>
    <pre><code>uvicorn main:app --reload</code></pre>
  </li>

  <li><strong>Access the application:</strong><br>
    Visit <code>http://localhost:8000</code> in your browser.
  </li>

  <li><strong>Talk to the bot:</strong><br>
    Send audio files to <code>http://localhost:8000/talk</code> via a client like Postman or Curl.
  </li>
</ul>



##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement basic features (TTS using whisper, saving conversations in db).</strike>
- [ ] **`Task 2`**: Use open source models for TTS and also understand context from user's experience/resume (RAG).
- [ ] **`Task 3`**: Implement Frontend.



##  Contributing

- **🐛 [Report Issues](https://github.com/Arush04/InterviewBot/issues)**: Submit bugs found or log feature requests for the `InterviewBot` project.
- **💡 [Submit Pull Requests](https://github.com/Arush04/InterviewBot/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
