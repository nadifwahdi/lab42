# LAB42 – Nadif's Personal Laboratory

**Welcome to LAB42 – my personal R\&D space. Why 42? Because it's the answer to life, the universe, and everything.**

This repository serves as a centralized hub for my personal projects, prototypes, and utilities. Over time, I've found myself losing track of past work—like that handy module for calling the OpenAI API and calculating usage costs. A useful tool... that I accidentally deleted because I couldn’t remember where I put it.

To prevent that from happening again and to keep my future self (and maybe you) sane, I created this repo for better organization and documentation.

Feel free to explore!

---

## 📦 Structure

```
lab42/
├── apps/                   # Individual applications
│   ├── ielts_tutor/        # GPT-powered IELTS writing tutor app (on progress...)
│
├── packages/               # Shared Python packages
│   ├── llm/                # LLM clients, prompt handling, providers
│   ├── core/               # Types, constants, error handling
│   ├── utils/              # General-purpose utilities
│   └── data/               # Data loading, preprocessing helpers
│
├── docker/                 # Docker-related files
├── Makefile                # Useful commands
├── setup.py                # Editable pip install of packages/
└── README.md
```

---

## 🚀 Projects

### 🧠 TOEFL Tutor (Coming soon)

* Web-based interface for writing task evaluation
* Uses GPT (or fallback LLMs) to provide structured feedback
* Built with FastAPI and Streamlit

## 🔁 Shared Packages

### `llm/`

* LLM base clients, OpenAI integration, prompt builders, fallbacks

### `core/`

* App-wide constants, errors, and shared types

### `utils/`

* Generic helpers like safe string casting, env loaders, logging

## 🐳 Docker (Coming soon)

Each app includes its own Dockerfile and can be run independently. See `/docker/` folder for templates and examples.

## ⚙️ Setup

```bash
# Clone the repo
$ git clone https://github.com/nadiffw/lab42.git
$ cd lab42

# Create and activate virtual environment
$ python3.10 -m venv env310
$ source env310/bin/activate  # On Windows use `env310\Scripts\activate`

# Install editable packages
$ pip install -e .
```

For development:

```bash
pip install -r requirements_dev.txt
```

To ensure code quality and consistency, this project uses `pre-commit` hooks. You can install and activate them with the following commands:

```bash
pip install pre-commit
pre-commit install
```

This will automatically run checks like formatting and linting before you make any commits.

Then apply `pre-commit` to all files

```bash
pre-commit run --all-files
```

## 🛠️ Make Commands

```bash
make install        # Install dependencies
make lint           # Run linters
make run-app        # Run a selected app (set default in Makefile)
```

## ✅ Status

* [x] Monorepo structure
* [x] Shared packages
* [ ] Docker support
* [ ] MLflow tracking
* [ ] LLM fallback logic


---

Built for learning, showcasing, and scaling up experiments 💡
