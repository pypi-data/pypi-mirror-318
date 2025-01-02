import os
import tempfile
import subprocess
import random
from pathlib import Path

import pytest
from click.testing import CliRunner
from search_and_replace.diff_apply import (
    main,
    split_into_hunks,
    process_hunk,
    HUNK_HEADER_PATTERN,
)


def write_temp_file(content: str) -> str:
    """Write content to a temporary file and return its path."""
    fd, path = tempfile.mkstemp(text=True)
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)
    return path


def apply_with_git(diff_content: str, target_content: str, file_path: str) -> str:
    """Apply diff using git apply and return the result."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # Initialize git repo
        git_init = ["git", "init"]
        subprocess.run(git_init, cwd=tmp_path, capture_output=True, check=True)

        # Write target and diff files
        target_file = tmp_path / file_path
        target_file.write_text(target_content)

        diff_file = tmp_path / "changes.diff"
        diff_file.write_text(diff_content)

        # Add target file to git
        git_add = ["git", "add", file_path]
        subprocess.run(git_add, cwd=tmp_path, capture_output=True, check=True)

        git_commit = ["git", "commit", "-m", "initial"]
        subprocess.run(git_commit, cwd=tmp_path, capture_output=True, check=True)

        # Apply the diff with relaxed options
        git_apply = [
            "git",
            "apply",
            "--ignore-whitespace",
            "--unidiff-zero",
            "-C0",
            "--whitespace=nowarn",
            "changes.diff",
        ]
        result = subprocess.run(
            git_apply,
            cwd=tmp_path,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"git apply failed with return code {result.returncode}:\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )

        return target_file.read_text()


# Test files in different formats
PYTHON_CODE = '''"""Example Python module."""

import sys
from typing import List, Optional

def fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n."""
    result = [0, 1]
    while result[-1] <= n:
        result.append(result[-1] + result[-2])
    return result[:-1]

class Calculator:
    """Simple calculator class."""
    
    def __init__(self, initial: int = 0):
        self.value = initial
    
    def add(self, x: int) -> int:
        """Add x to current value."""
        self.value += x
        return self.value
    
    def multiply(self, x: int) -> int:
        """Multiply current value by x."""
        self.value *= x
        return self.value

def main() -> None:
    """Main function."""
    calc = Calculator(10)
    print(f"Initial value: {calc.value}")
    print(f"Add 5: {calc.add(5)}")
    print(f"Multiply by 2: {calc.multiply(2)}")
    print(f"Fibonacci up to 100: {fibonacci(100)}")

if __name__ == "__main__":
    main()
'''

CPP_CODE = """// Example C++ program
#include <iostream>
#include <vector>
#include <string>

class Shape {
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
private:
    double radius;

public:
    explicit Circle(double r) : radius(r) {}

    double area() const override {
        return 3.14159 * radius * radius;
    }
};

class Rectangle : public Shape {
private:
    double width;
    double height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}

    double area() const override {
        return width * height;
    }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5.0));
    shapes.push_back(std::make_unique<Rectangle>(4.0, 6.0));

    for (const auto& shape : shapes) {
        std::cout << "Area: " << shape->area() << std::endl;
    }

    return 0;
}
"""

MARKDOWN_DOC = """# Project Documentation

## Overview

This is a sample project documentation written in Markdown.

### Features

- Easy to read
- Simple syntax
- Supports code blocks
- Handles lists well

### Code Example

```python
def hello_world():
    print("Hello, World!")
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests:
   ```bash
   pytest tests/
   ```

## Configuration

The project can be configured using a YAML file:

```yaml
debug: true
port: 8080
database:
  host: localhost
  port: 5432
```

## License

This project is licensed under the MIT License.
"""

HTML_DOC = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        .header {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 5px;
        }
        .content {
            margin-top: 20px;
        }
        .footer {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Welcome to Our Website</h1>
            <p>This is a sample HTML page with some basic styling.</p>
        </div>
        <div class="content">
            <h2>Features</h2>
            <ul>
                <li>Responsive design</li>
                <li>Clean and simple layout</li>
                <li>Easy to customize</li>
            </ul>
            <h2>About Us</h2>
            <p>We are a team of developers passionate about creating great software.</p>
        </div>
        <div class="footer">
            <p>&copy; 2024 Our Company. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
"""

CONFIG_FILE = """# Server Configuration

# Network settings
port = 8080
host = "localhost"
max_connections = 1000
timeout = 30

# Database settings
[database]
host = "db.example.com"
port = 5432
name = "myapp"
user = "admin"
pool_size = 20
max_overflow = 10

# Cache settings
[cache]
backend = "redis"
url = "redis://localhost:6379/0"
ttl = 3600

# Logging configuration
[logging]
level = "INFO"
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
file = "/var/log/myapp.log"

# Feature flags
[features]
enable_auth = true
enable_cache = true
debug_mode = false

# API settings
[api]
version = "v1"
rate_limit = 100
timeout = 5
"""


@pytest.fixture
def test_files(tmp_path: Path) -> dict[str, Path]:
    """Create test files in different formats."""
    files = {
        "example.py": PYTHON_CODE,
        "shapes.cpp": CPP_CODE,
        "docs.md": MARKDOWN_DOC,
        "index.html": HTML_DOC,
        "config.toml": CONFIG_FILE,
    }

    result = {}
    for name, content in files.items():
        file_path = tmp_path / name
        file_path.write_text(content)
        result[name] = file_path

    return result


def make_random_changes(content: str) -> str:
    """Make random modifications to text content.

    Creates complex changes with multiple hunks by:
    - Modifying multiple lines in different ways
    - Adding and removing lines in different places
    - Ensuring changes are spread throughout the file
    """
    lines = content.splitlines(keepends=True)
    if not lines:
        return content

    # Choose 2-5 hunks
    num_hunks = random.randint(2, 5)

    # Divide the file into regions for each hunk
    file_length = len(lines)
    region_size = file_length // num_hunks

    # Make changes in each region to ensure spread
    for i in range(num_hunks):
        start = i * region_size
        end = (i + 1) * region_size if i < num_hunks - 1 else file_length

        # Make 1-3 changes in this region
        num_changes = random.randint(1, 3)
        for _ in range(num_changes):
            if end - start < 2:  # Skip if region too small
                continue

            change_type = random.choice(
                [
                    "modify",
                    "add",
                    "delete",
                    "swap",  # New: swap two lines
                    "duplicate",  # New: duplicate a line
                    "comment",  # New: comment out a line
                ]
            )

            if change_type == "modify":
                # Modify a random line
                if end <= len(lines):  # Check if indices are valid
                    idx = random.randrange(start, min(end, len(lines)))
                    line = lines[idx].rstrip()
                    if line:
                        # More varied modifications
                        action = random.choice(
                            [
                                "insert",
                                "modify",
                                "append",
                                "uppercase",  # New: convert to uppercase
                                "reverse",  # New: reverse the line
                            ]
                        )
                        if action == "insert":
                            pos = random.randrange(len(line) + 1)
                            line = line[:pos] + "NEW_" + line[pos:]
                        elif action == "modify":
                            pos = random.randrange(len(line))
                            line = line[:pos] + "MODIFIED" + line[pos + 8 :]
                        elif action == "uppercase":
                            line = line.upper()
                        elif action == "reverse":
                            line = line[::-1]
                        else:  # append
                            line = line + "_UPDATED"
                        lines[idx] = line + "\n"

            elif change_type == "add":
                # Add 1-3 new lines
                num_lines = random.randint(1, 3)
                idx = random.randrange(start, min(end + 1, len(lines) + 1))
                for j in range(num_lines):
                    prefix = random.choice(
                        [
                            "// New line",
                            "# Added line",
                            "/* Extra line */",
                            "<!-- HTML comment -->",
                        ]
                    )
                    new_line = f"{prefix} {j + 1} added here\n"
                    lines.insert(idx + j, new_line)
                end += num_lines  # Adjust region end

            elif change_type == "delete":
                # Delete 1-2 consecutive lines
                if end - start > 2 and start < len(lines):
                    num_lines = min(random.randint(1, 2), end - start - 1)
                    idx = random.randrange(start, min(end - num_lines + 1, len(lines)))
                    for _ in range(num_lines):
                        if idx < len(lines):  # Check if index is still valid
                            lines.pop(idx)
                            end -= 1  # Adjust region end

            elif change_type == "swap" and end - start > 2:
                # Swap two adjacent lines
                if end - 1 < len(lines):  # Check if indices are valid
                    idx = random.randrange(start, min(end - 1, len(lines) - 1))
                    if idx + 1 < len(lines):
                        lines[idx], lines[idx + 1] = lines[idx + 1], lines[idx]

            elif change_type == "duplicate":
                # Duplicate a line
                if end <= len(lines):  # Check if index is valid
                    idx = random.randrange(start, min(end, len(lines)))
                    if idx < len(lines):  # Double check index
                        lines.insert(idx, lines[idx])
                        end += 1  # Adjust region end

            else:  # comment
                # Comment out a line
                if end <= len(lines):  # Check if indices are valid
                    idx = random.randrange(start, min(end, len(lines)))
                    line = lines[idx].rstrip()
                    if line:
                        comment_style = random.choice(
                            [
                                ("// ", ""),  # C-style
                                ("# ", ""),  # Python-style
                                ("<!-- ", " -->"),  # HTML-style
                                ("/* ", " */"),  # C-block-style
                            ]
                        )
                        lines[idx] = f"{comment_style[0]}{line}{comment_style[1]}\n"

    result = "".join(lines)
    # Make sure we actually made changes
    if result == content:
        # If no changes were made, add a new line at the start
        result = "// No changes detected, adding this line\n" + content

    return result


def get_diff(original: str, modified: str, file_path: str) -> str:
    """Get unified diff between original and modified content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # Initialize git repo
        subprocess.run(["git", "init"], cwd=tmp_path, capture_output=True, check=True)

        # Write original file and commit it
        target_file = tmp_path / file_path
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(original)

        subprocess.run(
            ["git", "add", file_path], cwd=tmp_path, capture_output=True, check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "initial"],
            cwd=tmp_path,
            capture_output=True,
            check=True,
        )

        # Write modified file
        target_file.write_text(modified)

        # Get diff
        result = subprocess.run(
            ["git", "diff"],  # Removed --no-prefix to keep a/ and b/ prefixes
            cwd=tmp_path,
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout


@pytest.mark.parametrize(
    "test_case",
    [
        # Simple single-line replacement
        {
            "target": "Hello World\n",
            "diff": """diff --git a/target.txt b/target.txt
--- a/target.txt
+++ b/target.txt
@@ -1 +1 @@
-Hello World
+Goodbye World
""",
            "description": "Single line replacement",
            "id": "single_line",  # Add ID for better test naming
        },
        # Multi-line replacement
        {
            "target": "First line\nSecond line\nThird line\n",
            "diff": """diff --git a/target.txt b/target.txt
--- a/target.txt
+++ b/target.txt
@@ -1,3 +1,3 @@
-First line
+Changed first
 Second line
-Third line
+Last line
""",
            "description": "Multi-line replacement with context",
            "id": "multi_line",
        },
        # Multiple hunks
        {
            "target": "Header\n\nMiddle\n\nFooter\n",
            "diff": """diff --git a/target.txt b/target.txt
--- a/target.txt
+++ b/target.txt
@@ -1 +1 @@
-Header
+New Header
@@ -5 +5 @@
-Footer
+New Footer
""",
            "description": "Multiple hunks",
            "id": "multi_hunk",
        },
        # Empty lines and whitespace
        {
            "target": "  Leading space\nNo space\n   More space  \n",
            "diff": """diff --git a/target.txt b/target.txt
--- a/target.txt
+++ b/target.txt
@@ -1,3 +1,3 @@
-  Leading space
+  Changed space
 No space
-   More space  
+   Final space  
""",
            "description": "Preserving whitespace",
            "id": "whitespace",
        },
    ],
    ids=lambda x: x["id"] if isinstance(x, dict) and "id" in x else None,
)
def test_compare_with_git_apply(test_case: dict) -> None:
    """Compare our diff apply implementation with git apply."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Write target and diff files
        target_file = Path("target.txt")
        target_file.write_text(test_case["target"])

        diff_file = Path("changes.diff")
        diff_file.write_text(test_case["diff"])

        # Get git result
        git_result = apply_with_git(
            test_case["diff"], test_case["target"], "target.txt"
        )

        # Get our result using the CLI
        result = runner.invoke(main, ["changes.diff", "target.txt", "--inplace"])
        assert result.exit_code == 0

        our_result = target_file.read_text()
        assert our_result == git_result, (
            f"Test case '{test_case['description']}' failed:\n"
            f"Git result: {git_result!r}\n"
            f"Our result: {our_result!r}\n"
            f"Diff:\n{test_case['diff']}"
        )


@pytest.mark.parametrize("seed", range(5))  # Run 5 times with different seeds
def test_random_modifications(test_files: dict[str, Path], seed: int) -> None:
    """Test applying random modifications to different file types."""
    random.seed(seed)
    runner = CliRunner()

    for file_path in test_files.values():
        with runner.isolated_filesystem():
            # Read original content
            original = file_path.read_text()

            # Make random modifications
            modified = make_random_changes(original)

            # Get the diff
            diff = get_diff(original, modified, file_path.name)
            if not diff:  # Skip if no changes were made
                continue

            # Write files for our tool
            target_file = Path(file_path.name)
            target_file.write_text(original)

            diff_file = Path("changes.diff")
            diff_file.write_text(diff)

            # Get git's result
            git_result = apply_with_git(diff, original, file_path.name)

            # Get our result
            result = runner.invoke(main, ["changes.diff", file_path.name, "--inplace"])
            assert result.exit_code == 0

            our_result = target_file.read_text()
            assert our_result == git_result, (
                f"Random modification test failed for {file_path.name} "
                f"with seed {seed}:\n"
                f"Original content:\n{original}\n"
                f"Modified content:\n{modified}\n"
                f"Git result: {git_result!r}\n"
                f"Our result: {our_result!r}\n"
                f"Diff:\n{diff}"
            )


def test_include_context() -> None:
    """Test that --include-context option works correctly."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        target = "First line\nSecond line\nThird line\n"
        diff = """diff --git a/target.txt b/target.txt
--- a/target.txt
+++ b/target.txt
@@ -1,3 +1,3 @@
-First line
+Changed first
 Second line
-Third line
+Last line
"""
        # Write files
        target_file = Path("target.txt")
        target_file.write_text(target)

        diff_file = Path("changes.diff")
        diff_file.write_text(diff)

        # Test without context
        result = runner.invoke(main, ["changes.diff", "target.txt", "--inplace"])
        assert result.exit_code == 0
        assert target_file.read_text() == (
            "Changed first\nSecond line\nLast line\n"
        ), f"Failed without context:\nDiff:\n{diff}"

        # Test with context
        target_file.write_text("First line\nDifferent middle\nThird line\n")
        result = runner.invoke(
            main,
            ["changes.diff", "target.txt", "--inplace", "--include-context"],
        )
        assert result.exit_code == 0
        # No changes should be made when context doesn't match
        assert target_file.read_text() == (
            "First line\nDifferent middle\nThird line\n"
        ), f"Failed with context:\nDiff:\n{diff}"


def test_multi_file() -> None:
    """Test that multi-file diffs are handled correctly."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create source directory structure
        src_dir = Path("src")
        src_dir.mkdir()
        tests_dir = Path("tests")
        tests_dir.mkdir()

        # Write initial files
        (src_dir / "hello.py").write_text("def hello():\n" "    return 'Hello World'\n")
        (src_dir / "config.py").write_text("DEBUG = False\n" "VERSION = '1.0.0'\n")
        (tests_dir / "test_hello.py").write_text(
            "def test_hello():\n" "    assert hello() == 'Hello World'\n"
        )

        # Write diff file
        diff = """diff --git a/src/hello.py b/src/hello.py
--- a/src/hello.py
+++ b/src/hello.py
@@ -1,2 +1,2 @@
 def hello():
-    return 'Hello World'
+    return 'Goodbye World'
diff --git a/src/config.py b/src/config.py
--- a/src/config.py
+++ b/src/config.py
@@ -1,2 +1,2 @@
-DEBUG = False
+DEBUG = True
 VERSION = '1.0.0'
diff --git a/tests/test_hello.py b/tests/test_hello.py
--- a/tests/test_hello.py
+++ b/tests/test_hello.py
@@ -1,2 +1,2 @@
 def test_hello():
-    assert hello() == 'Hello World'
+    assert hello() == 'Goodbye World'
"""
        diff_file = Path("changes.diff")
        diff_file.write_text(diff)

        # Apply diff using our tool
        result = runner.invoke(main, ["changes.diff", ".", "--inplace"])
        assert result.exit_code == 0

        # Verify results
        hello_result = (src_dir / "hello.py").read_text()
        config_result = (src_dir / "config.py").read_text()
        test_result = (tests_dir / "test_hello.py").read_text()

        assert hello_result == (
            "def hello():\n" "    return 'Goodbye World'\n"
        ), f"hello.py failed:\nDiff:\n{diff}"
        assert config_result == (
            "DEBUG = True\n" "VERSION = '1.0.0'\n"
        ), f"config.py failed:\nDiff:\n{diff}"
        assert test_result == (
            "def test_hello():\n" "    assert hello() == 'Goodbye World'\n"
        ), f"test_hello.py failed:\nDiff:\n{diff}"
