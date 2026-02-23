"""Simple log analysis tool for filtering lines by a keyword.

This script:
- Asks the user for an input log file path.
- Asks for a search keyword.
- Asks for an output file path.
- Searches the log for lines containing the keyword (case-insensitive).
- Writes all matching lines to the output file.
- Prints the total number of matching lines.
- Handles missing/invalid input file paths without crashing.
"""

from __future__ import annotations


def search_log_file(input_path: str, keyword: str, output_path: str) -> int:
    """Search a log file for lines containing a keyword (case-insensitive).

    Args:
        input_path: Path to the input log file.
        keyword:   Keyword to search for (case-insensitive).
        output_path: Path to the output file where matching lines are written.

    Returns:
        The number of lines that contained the keyword.

    Raises:
        OSError: If there is any problem opening/reading/writing the files.
    """
    keyword_lower = keyword.lower()
    match_count = 0

    # Open input for reading and output for writing in a single context.
    with open(input_path, "r", encoding="utf-8") as infile, open(
        output_path, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            if keyword_lower in line.lower():
                outfile.write(line)
                match_count += 1

    return match_count


def main() -> None:
    """Main entry point: collect inputs, run search, and report results."""
    input_path = input("Enter input log file path: ").strip()
    keyword = input("Enter keyword to search for: ").strip()
    output_path = input("Enter output file path for matching lines: ").strip()

    if not input_path:
        print("Error: No input file path provided.")
        return

    if not keyword:
        print("Error: No keyword provided. Nothing to search for.")
        return

    if not output_path:
        print("Error: No output file path provided.")
        return

    try:
        match_count = search_log_file(input_path, keyword, output_path)
    except FileNotFoundError:
        # Specific message for the common case of a missing input file.
        print(f"Error: The input file '{input_path}' does not exist or cannot be found.")
        return
    except OSError as exc:
        # Generic file handling error (permissions, invalid path, etc.).
        print(f"Error: Unable to process files. Details: {exc}")
        return

    print(f"Total matching lines found: {match_count}")


if __name__ == "__main__":
    main()
