"""Why modern tools matter
You’ve learned pip and virtual environments - that’s great! But there’s a better way.
Enter uv: A modern Python package manager that’s:
10-100x faster than pip
Simpler to use
More reliable
All-in-one tool
​
The problem with pip
Traditional Python development has pain points:
Slow package installation
Confusing virtual environment commands
Different tools for different tasks
Easy to mess up your environment
​
What is uv?
uv is a single tool that replaces:
pip (package installer)
venv (virtual environments)
pip-tools (dependency management)
pyenv (Python version management)
Written in Rust, it’s blazingly fast and just works."""

"""pip install pandas
# ⏱️ Takes 15-30 seconds
# 
# 
# uv pip install pandas
# ⚡ Takes 1-2 seconds"""

"""Traditional way

# Create virtual environment
python -m venv .venv

# Activate it (different per OS!)
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate

# Install packages
pip install requests pandas numpy

# Save dependencies
pip freeze > requirements.txt"""


# Time: ~45 seconds Commands: 4+ (varies by OS)

"""# Everything in one command
uv init
uv add requests pandas numpy"""
