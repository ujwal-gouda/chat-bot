# ChatBot v1.0.0 – Windows Executable

A desktop AI chatbot application built using **CustomTkinter** for the interface and **Google Gemini API** for generating intelligent responses. The chatbot features a modern dark-themed GUI and real-time AI conversation.

---

## Features

- Dark-themed GUI with rounded chat bubbles.
- AI-powered responses using Google Gemini (`gemini-1.5-flash` model).
- Scrollable chat window for conversation history.
- Input box and send button for quick interaction.
- Supports dark/light mode via `CustomTkinter`.

---

## Installation
1 **Clone this repository**:

```bash
git clone https://github.com/ujwal-gouda/chat-bot.git
cd chat-bot
```
2 **Install Dependencies:**
```bash

pip install customtkinter python-dotenv google-generativeai

```
3 **Add your Google API key in a .env file:**
```bash
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```
4 **Run the App**
```bash
python index.py
```

## Usage
- Type a message in the input box.
- Press Enter or click Send.
- Chat with the AI in the scrollable window.

## Project Structure
```bash
|
├─ index.py
├─ .env
├─ .gitignore
└─ README.md
```

## Contributing
- Fork the repo.
- Create a branch: git checkout -b feature/YourFeature.
- Make changes and commit: git commit -m "Add some feature".
- Push branch: git push origin feature/YourFeature.
- Open a Pull Request.
