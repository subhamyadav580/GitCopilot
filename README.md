# PersonalGitCopilot

GitCopilot is an AI-powered Git CLI tool that automates your daily Git workflow:

* Finds Git repositories on your system
* Lets you select a repository interactively
* Detects unstaged changes
* Generates meaningful commit messages using an LLM
* Commits and pushes changes safely

All with one command.

## Key Features

* Single command: ```gitcopilot init```
* Interactive repository selection
* Automatic detection of unstaged files
* AI-generated commit messages
* Safe staging, commit, and push
* Works from any directory
* No config files or secrets stored
* Uses existing Git & environment setu

## Installation

### Prerequisites

* Python 3.9+
* Git installed and configured
* OpenAI API key

Set the API key in your environment (PersonalGitCopilot reads it automatically):
```
export OPENAI_API_KEY=sk-xxxx
```
You can add this to your ```~/.zshrc``` or ```~/.bashrc``` to avoid setting it every time.



### Install GitCopilot
Install directly from GitHub:

```
pip install git+https://github.com/subhamyadav580/PersonalGitCopilot.git
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