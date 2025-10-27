# Reflection

**1. Which issues were easiest and hardest to fix?**  
- Easiest: Style and docstring issues flagged by Flake8.  
- Hardest: Removing eval() and refactoring exception handling for safety.

**2. Any false positives from the tools?**  
- Pylint warned about too few public methods — acceptable for small scripts.

**3. How could these tools be integrated into CI/CD?**  
- Add GitHub Actions workflow to run Pylint, Bandit, and Flake8 automatically.

**4. Improvements observed:**  
- Cleaner, more secure, and readable code.  
- Proper logging and validation prevent future bugs.
