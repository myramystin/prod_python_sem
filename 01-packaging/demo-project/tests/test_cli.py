import subprocess
import sys


def test_module_cli_normalizes() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "text_tools", "  hello   world  "],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "hello world\n"


def test_module_cli_counts() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "text_tools", "hello world", "--count"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "2\n"


def test_module_cli_requires_text() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "text_tools"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert "usage:" in result.stderr
