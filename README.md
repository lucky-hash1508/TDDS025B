# Multi-Agent API

API Development with Python — a multi-agent orchestration system built with FastAPI (or similar) and the Groq API for LLM-powered agent responses.

## Project Structure

```
multi_agent_api/
├── agents/           # Individual agent definitions and AI client logic
├── models/           # Data models / schemas
├── orchestration/     # Logic for coordinating multiple agents
├── patterns/          # Reusable design patterns used across agents
├── routes/            # API route definitions
├── main.py            # Application entry point
├── requirements.txt   # Python dependencies
└── .env                # Environment variables (not committed)
```

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/lucky-hash1508/TDDS025B.git
   cd TDDS025B
   ```

2. Create a virtual environment and install dependencies
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Run the application
   ```bash
   python main.py
   ```

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key for accessing the Groq API |

## Notes

- Never commit your `.env` file — it's excluded via `.gitignore`.
- Rotate your API key immediately if it's ever exposed in code or version control.

## License

Add your license here.
