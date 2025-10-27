# 📘 Lab 5: Static Code Analysis

**Name:** Nandani Sonale  
**SRN:** PES2UG23CS364  
**Section:** F  
**Course:** Software Engineering Lab  
**University:** PES University, Electronic City Campus  

---

## 🧩 Objective
To enhance Python code quality, security, and style by using **static code analysis** tools — **Pylint**, **Flake8**, and **Bandit** — to detect and correct common programming issues in the given `inventory_system.py` file.

---

## 🧰 Tools Used
| Tool | Purpose | Description |
|------|----------|--------------|
| **Pylint** | Code Quality | Detects logical errors, unused variables, poor naming conventions, and design flaws. |
| **Flake8** | Code Style Checker | Ensures adherence to **PEP 8** standards such as indentation, whitespace, and line length. |
| **Bandit** | Security Analysis | Identifies vulnerabilities like unsafe functions (`eval`, `pickle`, `shell=True`), insecure file handling, etc. |
| **GitHub Codespaces** | Development Environment | Provides an online IDE to write, test, and analyze Python code without local setup. |
| **Python 3.12** | Programming Language | Used to execute and test the refactored `inventory_system.py` program. |
| **Git & GitHub** | Version Control | Used for tracking changes, committing code, and hosting the final lab submission repository. |

---

## 🔍 Introduction
**Static Code Analysis** is a crucial technique that examines source code **without executing it**, to identify potential bugs, vulnerabilities, and style violations before runtime.

This lab guided me through using three industry-standard Python tools:

- **Pylint:** Acts as a strict *code reviewer*, checking code quality, naming conventions, and potential logic errors.  
- **Flake8:** Works as a *grammar checker*, ensuring compliance with **PEP 8** style and formatting rules.  
- **Bandit:** Functions as a *security guard*, scanning for risky coding patterns and vulnerabilities.

Together, these tools help developers write code that is **secure, clean, and maintainable**.

---

## ⚙️ Procedure Summary
1. Opened the Codespaces environment and created a virtual environment (`.venv`).  
2. Installed the tools:
   ```bash
   pip install pylint flake8 bandit
