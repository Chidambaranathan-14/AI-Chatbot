<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/d9ebd1ad-95d8-4c5c-a31f-fe93cb5e2a51" />﻿# AI-Chatbot
 
Markdown

# Custom LLM Console Chatbot

A lightweight, persistent-memory Python terminal chatbot utilizing the **OpenAI SDK** to stream conversations through the **OpenRouter API** using open-source models like `Llama 3.3 70B`. 

This project incorporates dynamic environment variable loading (`.env`) to ensure API credentials remain completely secure and decoupled from the codebase.

## 🚀 Features
* **Persistent Chat Memory:** Tracks full conversation history across loops, allowing the LLM to retain contextual memory of prior interactions.
* **Environment Configuration:** Keeps private keys and API endpoints safe by loading them dynamically via `python-dotenv`.
* **Robust Error Handling:** Protects against network drops or API configuration issues without crashing the terminal app.

---

## 🛠️ Installation & Setup

1. Clone the Repository
```bash:
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME

2. Set Up a Virtual Environment (Optional but Recommended)
Bash:
# Create a virtual environment
python -m venv .myvenv

# Activate it (Windows PowerShell)
.myvenv\Scripts\Activate.ps1

# Activate it (Mac/Linux)
source .myvenv/bin/activate

3. Install Dependencies
Install the official OpenAI client interface and the environment variable helper file:
Bash:
pip install openai python-dotenv
🔑 Environment Configuration
Create a file named .env in the root folder of your project (where chatbot_1.py lives) and input your credentials precisely as shown below:

Ini, TOML
OPENROUTER_API_KEY=sk-or-v1-your-actual-openrouter-key-here
base_url=[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)
⚠️ Important: Do not wrap your keys in quotation marks inside the .env file. The keys are automatically evaluated as literal strings.

🎮 How to Run
Execute the main Python script from your terminal:

Bash:
python chatbot_1.py
Type your queries naturally.


<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/f0e8a1fb-9026-478d-abcf-efb098015ce7" />



Type exit at any point to close down the chat application safely.

📂 File Architecture
Plaintext
├── .myvenv/               # Isolated python dependency folder
├── .env                   # Local configuration file (SECRET / Git ignored)
├── .gitignore             # Instructs git to avoid uploading credentials
├── chatbot_1.py           # Core conversational chatbot engine
└── README.md              # Project documentation
🔒 Security Note
This project utilizes a .gitignore profile to ensure .env and .myvenv/ folders are never committed to open-source records. Always keep your OpenRouter API keys completely confidential.


---

### 💡 Quick Tip Before Pushing to GitHub:
Make sure you create a file named `.gitignore` in your folder and put these two lines inside it so your secret keys don't accidentally leak online:
```text
.env
.myvenv/
__pycache__/
