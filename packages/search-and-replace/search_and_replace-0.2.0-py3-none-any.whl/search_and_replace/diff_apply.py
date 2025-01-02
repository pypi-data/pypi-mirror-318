"""Tool for applying diffs as search and replace operations."""

import re
from pathlib import Path
from typing import Dict, List, Tuple, TextIO

import click


# Regex patterns for parsing diffs
FILE_HEADER_PATTERN = re.compile(
    r"^diff --git .*?\n"  # diff --git line
    r"(?:.*?\n)*?"  # Optional index/mode lines
    r"--- ([^\t\n]+)"  # --- line with filename
    r"(?:\t[^\n]*)?\n"  # Optional timestamp
    r"\+\+\+ [^\n]+\n",  # +++ line
    re.MULTILINE,
)

HUNK_HEADER_PATTERN = re.compile(
    r"^@@ -\d+(?:,\d+)? \+\d+(?:,\d+)? @@.*?\n", re.MULTILINE
)


def split_into_files(diff_content: str) -> Dict[str, str]:
    """Split a multi-file diff into individual file diffs using regex.

    Args:
        diff_content: The full diff content.

    Returns:
        A dictionary mapping filenames to their respective diff content.
    """
    files = {}
    pos = 0

    while True:
        match = FILE_HEADER_PATTERN.search(diff_content, pos)
        if not match:
            break

        # Find the start of the next file or end of content
        next_match = FILE_HEADER_PATTERN.search(diff_content, match.end())
        end_pos = next_match.start() if next_match else len(diff_content)

        # Extract filename (removing 'a/' prefix if present)
        filename = match.group(1)
        if filename.startswith("a/"):
            filename = filename[2:]

        # Store the complete diff for this file
        files[filename] = diff_content[match.start() : end_pos]
        pos = end_pos

    return files


def split_into_hunks(diff_content: str) -> List[str]:
    """Split a single file diff into individual hunks using regex.

    Args:
        diff_content: The diff content for a single file.

    Returns:
        A list of individual hunks.
    """
    # Skip the file header
    file_match = FILE_HEADER_PATTERN.search(diff_content)
    if not file_match:
        return []

    content = diff_content[file_match.end() :]
    hunks = []
    pos = 0

    while True:
        hunk_match = HUNK_HEADER_PATTERN.search(content, pos)
        if not hunk_match:
            # Add the last hunk if we have content
            if pos < len(content):
                hunks.append(content[pos:])
            break

        # Find the start of the next hunk or end of content
        next_match = HUNK_HEADER_PATTERN.search(content, hunk_match.end())
        end_pos = next_match.start() if next_match else len(content)

        # Store the complete hunk including its header
        hunks.append(content[hunk_match.start() : end_pos])
        pos = end_pos

    return hunks


def process_hunk(hunk: str, include_context: bool) -> Tuple[str, str]:
    """Process a single hunk and return the search/replace pair.

    Args:
        hunk: The hunk content.
        include_context: Whether to include context lines in the replacements.

    Returns:
        A tuple of (search_text, replace_text).
    """
    search_lines: List[str] = []
    replace_lines: List[str] = []
    context_before: List[str] = []
    context_after: List[str] = []
    in_change = False
    has_removed = False
    has_added = False

    # Skip the hunk header
    lines = HUNK_HEADER_PATTERN.split(hunk)[-1].splitlines(keepends=True)

    # First pass: collect all lines
    for line in lines:
        if line.startswith("-"):
            in_change = True
            has_removed = True
            search_lines.append(line[1:])
        elif line.startswith("+"):
            in_change = True
            has_added = True
            replace_lines.append(line[1:])
        elif line.startswith(" "):
            if not in_change:
                context_before.append(line[1:])
            else:
                context_after.append(line[1:])
                # Add context between changes to both sides
                search_lines.append(line[1:])
                replace_lines.append(line[1:])

    # Second pass: handle context
    if include_context:
        # Include all context in both search and replace
        search_lines = context_before + search_lines + context_after
        replace_lines = context_before + replace_lines + context_after
    elif not has_removed and has_added:
        # If there are only added lines, use the context before as search
        search_lines = context_before + search_lines
        replace_lines = context_before + replace_lines
    elif has_removed and not has_added and not context_after:
        # If there are only removed lines at the end, include context before
        search_lines = context_before + search_lines
        replace_lines = context_before + replace_lines

    # Handle empty lines correctly
    search_text = "".join(search_lines)
    replace_text = "".join(replace_lines)

    return search_text, replace_text


def apply_changes(content: str, replacements: List[Tuple[str, str]]) -> str:
    """Apply a list of replacements to the content.

    Args:
        content: The original content.
        replacements: List of (search, replace) tuples.

    Returns:
        The modified content.
    """
    result = content

    # Apply replacements in reverse order to handle overlapping changes
    for search, replace in reversed(replacements):
        if not search and replace:
            # Handle pure additions by finding the context
            lines = result.splitlines(keepends=True)
            for i, line in enumerate(lines):
                if line == replace:
                    # Found the context, insert the new line after it
                    lines.insert(i + 1, replace)
                    break
            result = "".join(lines)
        else:
            # Replace only first occurrence to avoid overlapping changes
            result = result.replace(search, replace, 1)

    return result


def process_file_diff(
    diff_content: str, include_context: bool
) -> List[Tuple[str, str]]:
    """Process a single file's diff content.

    Args:
        diff_content: The diff content for a single file.
        include_context: Whether to include context lines in the replacements.

    Returns:
        A list of (search, replace) tuples.
    """
    hunks = split_into_hunks(diff_content)
    replacements = []

    for hunk in hunks:
        search, replace = process_hunk(hunk, include_context)
        if search and replace:
            replacements.append((search, replace))

    return replacements


@click.command()
@click.argument("diff_file", type=click.File("r"), default="-")
@click.argument("target", type=click.Path(exists=True))
@click.option(
    "--include-context",
    "-c",
    is_flag=True,
    help="Include context lines in search patterns",
)
@click.option(
    "--inplace",
    "-i",
    is_flag=True,
    help="Modify files in-place instead of printing to stdout",
)
def main(diff_file: TextIO, target: str, include_context: bool, inplace: bool) -> None:
    """Apply unified diff as search and replace operations.

    DIFF_FILE is the unified diff file (use - for stdin).
    TARGET is the target file or directory to apply the diff to.
    """
    try:
        diff_content = diff_file.read()
        file_diffs = split_into_files(diff_content)

        if not file_diffs:
            click.echo("No valid diffs found", err=True)
            raise click.Abort()

        target_path = Path(target)

        for filename, file_diff in file_diffs.items():
            file_path = target_path / filename if target_path.is_dir() else target_path

            if not file_path.exists():
                click.echo(f"Warning: {file_path} not found, skipping", err=True)
                continue

            replacements = process_file_diff(file_diff, include_context)
            if not replacements:
                click.echo(f"No valid replacements found for {filename}", err=True)
                continue

            with open(file_path, "r") as f:
                content = f.read()

            modified_content = apply_changes(content, replacements)

            if inplace:
                with open(file_path, "w") as f:
                    f.write(modified_content)
            else:
                click.echo(modified_content)

    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()


if __name__ == "__main__":
    main()
