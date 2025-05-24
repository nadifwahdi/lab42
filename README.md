# LAB42 – Nadif's Personal Laboratory

**Welcome to LAB42 – my personal R\&D space. Why 42? Because it's the answer to life, the universe, and everything.**

This repository serves as a centralized hub for my personal projects, prototypes, and utilities. Over time, I've found myself losing track of past work—like that handy module for calling the OpenAI API and calculating usage costs. A useful tool... that I accidentally deleted because I couldn’t remember where I put it.

To prevent that from happening again and to keep my future self (and maybe you) sane, I created this repo for better organization and documentation.

Feel free to explore!

---

## 1. Repository Structure

```
lab42/                      # Root directory
├── lab42/                  # Main package directory containing all modules and work
│   └── __init__.py         # Package initializer
├── tests/                  # Unit tests for the modules inside lab42/
├── env310/                 # Local environment directory (created after setup)
├── pyproject.toml          # Project configuration and build metadata
├── requirements.txt        # Required dependencies to run the code
└── requirements_dev.txt    # Additional tools and packages for development
```

---

## 2. Getting Started

### 2.1 Clone the repository

```bash
git clone https://github.com/your-username/lab42.git
cd lab42
```

### 2.2 Install dependencies

Before installing dependencies, make sure that the virtual environment already activated:

```bash
python3.10 -m venv env310
source env310/bin/activate
```

Then, install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

For development:

```bash
pip install -r requirements_dev.txt
```

### 2.3 Install and Set Up Pre-commit

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

---

More modules and documentation will be added over time. Stay tuned!
