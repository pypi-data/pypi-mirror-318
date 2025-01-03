"""Tests for CLI interface."""

import pytest
from unittest.mock import patch
import os
from click.testing import CliRunner
from send_2_llm.cli import cli

@pytest.fixture
def cli_runner():
    """Fixture for CLI testing."""
    return CliRunner()

@pytest.fixture
def mock_env():
    """Fixture for environment variables."""
    test_env = {
        "STRATEGY": "single",
        "DEFAULT_PROVIDER": "openai",
        "OPENAI_API_KEY": "test-key",
        "OPENAI_MODEL": "gpt-4"
    }
    with patch.dict(os.environ, test_env, clear=True):
        yield test_env

def test_cli_basic(cli_runner, mock_env):
    """Test basic CLI functionality."""
    result = cli_runner.invoke(cli, ["Hello, world!"])
    assert result.exit_code == 0
    assert "Error" not in result.output

def test_cli_with_options(cli_runner, mock_env):
    """Test CLI with various options."""
    result = cli_runner.invoke(cli, [
        "Hello, world!",
        "--provider", "openai",
        "--model", "gpt-4",
        "--format", "markdown"
    ])
    assert result.exit_code == 0
    assert "Error" not in result.output

def test_cli_format_options(cli_runner, mock_env):
    """Test different format options."""
    formats = ["markdown", "telegram_markdown", "json", "text"]
    for fmt in formats:
        result = cli_runner.invoke(cli, ["Hello", "--format", fmt])
        assert result.exit_code == 0

def test_cli_help(cli_runner):
    """Test help output."""
    result = cli_runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Options:" in result.output
    assert "--format" in result.output
    assert "--provider" in result.output
    assert "--model" in result.output

def test_cli_error_handling(cli_runner):
    """Test CLI error handling."""
    with patch.dict(os.environ, {"STRATEGY": "invalid"}, clear=True):
        result = cli_runner.invoke(cli, ["Hello, world!"])
        assert result.exit_code != 0
        assert "Error" in result.output 