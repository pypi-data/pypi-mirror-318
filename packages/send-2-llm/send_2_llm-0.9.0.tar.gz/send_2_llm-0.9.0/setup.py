from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="send_2_llm",
    version="0.9.0",
    author="AI Tools Team",
    author_email="ai.tools.team@example.com",
    description="A flexible LLM provider switching library with multiple strategies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ai-tools-team/send_2_llm",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "aiohttp>=3.9.0",
        "python-dotenv>=1.0.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "tenacity>=8.2.0",
    ],
    extras_require={
        "together": ["together>=0.2.0"],
        "openai": ["openai>=1.12.0"],
        "anthropic": ["anthropic>=0.9.0"],
        "perplexity": ["perplexity-ai>=0.3.0"],
        "deepseek": ["deepseek>=0.1.0"],
        "gemini": ["google-generativeai>=0.3.0"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.23.0",
            "pytest-cov>=4.1.0",
            "black>=24.0.0",
            "isort>=5.13.0",
            "mypy>=1.8.0",
            "pylint>=3.0.0",
            "pre-commit>=3.6.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.5.0",
            "mkdocstrings>=0.24.0",
        ],
        "all": [
            "together>=0.2.0",
            "openai>=1.12.0",
            "anthropic>=0.9.0",
            "perplexity-ai>=0.3.0",
            "deepseek>=0.1.0",
            "google-generativeai>=0.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "send2llm=send_2_llm.cli:main",
            "send_2_llm=send_2_llm.cli:main",
        ],
    },
) 