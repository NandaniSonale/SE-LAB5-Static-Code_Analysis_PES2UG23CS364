# Issues Table

| Issue ID | Tool Used | Severity | Description | Fix Implemented | Status |
|-----------|------------|-----------|---------------|------------------|----------|
| I1 | Pylint | High | Mutable default argument (`logs=[]`) | Replaced with `logs=None` | Fixed |
| I2 | Bandit | High | Use of eval() (security risk) | Removed unsafe eval | Fixed |
| I3 | Bandit | Medium | Files opened without context manager | Replaced with with open() | Fixed |
| I4 | Pylint | Medium | Bare except: used | Changed to except Exception as e: | Fixed |
| I5 | Flake8 | Low | Missing docstrings | Added proper docstrings | Fixed |
| I6 | Pylint | Low | Missing type checks for inputs | Added validation using isinstance() | Fixed |

