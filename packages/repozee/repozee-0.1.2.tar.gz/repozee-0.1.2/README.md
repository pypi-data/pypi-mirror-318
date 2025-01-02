# RepoZee

Explore the contents of a Git repository in a local filesystem with AI

(README by RepoZee)

RepoZee is an intelligent agent designed to help developers explore, understand, and contribute to Git repositories through natural language interaction, providing insights into:
- Project organization and structure
- Coding practices analysis
- Architecture and design patterns
- Development contribution opportunities

## Features

- **Repository Navigation**: Explore directory structures and file contents through natural language queries
- **Context-Aware Analysis**: Maintains understanding of the current repository state
- **File Content Examination**: Read and analyze specific files on request
- **Safe Operations**: Limited to read-only operations on the currently checked out commit

## Tools

Repozee provides the following core capabilities:
- `list`: Display the full directory tree of the repository
- `read_file`: Examine the contents of specific files
- `quit`: End the exploration session

## Usage

Interact with Repozee using natural language queries. Examples:
- "Show me the project structure"
- "What's in the src directory?"
- "Can you read the configuration file?"
- "Help me understand the project architecture"

## Technical Details

- Operates on local filesystem
- Works with the currently checked out Git commit
- Read-only operations for safety
- Context-aware responses based on repository state

## Purpose

Repozee aims to make repository exploration more intuitive and efficient by:
- Reducing the learning curve for new contributors
- Providing quick insights into project structure
- Facilitating better understanding of codebases
- Supporting development decisions with contextual analysis

## Limitations

- Limited to read-only operations
- Works only with currently checked out commit
- Requires local filesystem access

## Installation (MacOS)

Assumes Python 3.11.

```bash
brew install python3.11
python3.11 -m pip install pipx
pipx install repozee
```

## Usage

```bash
ANTHROPIC_API_KEY=__your_key_here___ repozee chat __your/directory/here__
```

---

<a href="https://www.flaticon.com/free-icons/rabbit">Icon by Flaticon</a>


