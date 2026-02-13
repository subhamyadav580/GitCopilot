# GitCopilot 🚀

GitCopilot is an AI-powered Git CLI tool that automates your daily Git workflow.

It helps you:

- Find Git repositories on your system
- Select a repository interactively
- Detect unstaged changes
- Generate meaningful commit messages using an LLM
- Commit and push changes safely

All with one command.

---

## ✨ Key Features

- Single command: `gitcopilot init`
- Interactive repository selection
- Automatic detection of unstaged files
- AI-generated commit messages
- Safe staging, commit, and push
- Works from any directory
- No config files required
- No secrets stored
- Automatically detects available LLM provider
- Supports multiple LLM providers via LiteLLM

---

## 🧠 LLM Support

GitCopilot automatically detects the first available API key in your environment.

Supported providers:

| Provider   | Environment Variable        | Default Mini Model |
|------------|----------------------------|--------------------|
| OpenAI     | `OPENAI_API_KEY`           | `gpt-4o-mini`      |
| Anthropic  | `ANTHROPIC_API_KEY`        | `claude-3-haiku`   |
| Groq       | `GROQ_API_KEY`             | `llama3-8b-8192`   |
| Gemini     | `GEMINI_API_KEY`           | `gemini-1.5-flash` |
| Mistral    | `MISTRAL_API_KEY`          | `mistral-small`    |

You only need to set **one** of them.

No additional configuration required.

---

## 📦 Installation

### Prerequisites

- Python 3.9+
- Git installed and configured
- At least one supported LLM API key

---

### Set Your API Key

Choose one provider and export its key.

#### OpenAI
```bash
export OPENAI_API_KEY=sk-xxxx
```

#### Anthropic
```bash
export ANTHROPIC_API_KEY=sk-ant-xxxx
```

#### Groq
```bash
export GROQ_API_KEY=gsk_xxxx
```

You can add this to your ```~/.zshrc``` or ```~/.bashrc``` to avoid setting it every time.



### Install GitCopilot
Install directly from GitHub:

```
pip install git+https://github.com/subhamyadav580/GitCopilot.git
```

Verify installation:

```
which gitcopilot
gitcopilot --help
```

## Usage

Run GitCopilot from any directory:

```
gitcopilot init
```