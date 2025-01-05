from setuptools import setup, find_packages
import os
from typing import Dict, List

def read_requirements(filename: str) -> List[str]:
    """Read requirements from file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def read_provider_requirements() -> Dict[str, List[str]]:
    """Read all provider requirements."""
    providers_dir = os.path.join('requirements', 'providers')
    provider_reqs = {}
    
    if os.path.exists(providers_dir):
        for filename in os.listdir(providers_dir):
            if filename.endswith('.txt'):
                provider_name = filename[:-4]  # Remove .txt
                provider_reqs[provider_name] = read_requirements(os.path.join(providers_dir, filename))
    
    return provider_reqs

# Read requirements
base_reqs = read_requirements('requirements/base.txt')
dev_reqs = read_requirements('requirements/dev.txt')
provider_reqs = read_provider_requirements()

# Read README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Prepare extras_require
extras_require = {
    'dev': [
        'pytest>=7.0.0',
        'pytest-asyncio>=0.20.0',
        'pytest-cov>=4.0.0',
        'black>=22.0.0',
        'isort>=5.0.0',
        'mypy>=1.0.0',
        'pylint>=2.0.0',
        'pre-commit>=3.0.0',
    ],
    'docs': [
        'mkdocs>=1.4.0',
        'mkdocs-material>=9.0.0',
        'mkdocstrings>=0.20.0',
    ],
    'openai': ['openai>=1.58.1'],
    'anthropic': ['anthropic>=0.3.0'],
    'together': ['together>=0.2.11'],
    'deepseek': ['openai>=1.58.1'],
    'perplexity': [
        'requests>=2.31.0',
        'aiohttp>=3.9.0'
    ],
}

# Add all providers
extras_require['all'] = [
    req for provider_reqs in extras_require.values() 
    for req in (provider_reqs if isinstance(provider_reqs, list) else [provider_reqs])
]

setup(
    name="send_2_llm",
    version="0.9.2",
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
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.11",
    install_requires=base_reqs,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "send2llm=send_2_llm.cli:main",
            "send_2_llm=send_2_llm.cli:main",
        ],
    },
) 