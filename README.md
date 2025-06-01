Here's a complete `README.md` file for your **Language Translator Bot built with Chainlit and Gemini API**:

---

````markdown
# 🌐 Language Translator Bot

This is a **Language Translation Bot** built using [Chainlit](https://docs.chainlit.io/), the **Gemini 2.0 API**, and Python. The bot can detect the input language, ask the user for a target language (if not specified), and translate the text accordingly.

---

## ✨ Features

- ✅ Detects input language automatically.
- 🌍 Supports translation between multiple languages:
  - English
  - Urdu
  - Arabic
  - French
  - Spanish
  - German
  - Hindi
  - Chinese
- 🤖 Powered by Gemini 2.0 Flash model.
- 🧠 Built using Chainlit for real-time chat interaction.
- 🛡️ Secure API key loading via `.env` and `python-dotenv`.

---

## 🚀 How It Works

1. User sends a message like:
   - `Translate "Hello" to Urdu`
   - `Bonjour`
2. The agent:
   - Detects the input language
   - Translates to the specified target language (or asks for one)
3. The response is sent back to the user in real-time.

---

## 🛠 Tech Stack

| Tool         | Purpose                          |
|--------------|----------------------------------|
| Chainlit     | Chat interface and session state |
| Gemini API   | LLM-based translation            |
| Python       | Core programming language        |
| dotenv       | Environment variable management  |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/translator-bot.git
   cd translator-bot
````

2. **Create a virtual environment (optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

---

## 🚦 Running the App

```bash
chainlit run app.py
```

> The bot will launch on `http://localhost:8000` (or as shown in the terminal)

---

## 📁 File Structure

```
.
├── app.py               # Main Chainlit app logic
├── agents/              # Agent, runner, and tool definitions
│   ├── agent.py
│   └── tool.py
├── .env                 # API key storage (not committed)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📌 Notes

* You can customize the default translation language, UI appearance, or add logging features.
* Add OAuth or JWT if deploying to a public environment.

---

## 👩‍💻 Author

**Muskan Fatima**
Frontend Developer & AI Explorer
[Portfolio Website](https://m-f-resume.vercel.app)

---



