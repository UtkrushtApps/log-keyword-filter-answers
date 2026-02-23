# Solution Steps

1. Create a new function `search_log_file(input_path, keyword, output_path)` to hold the core logic instead of putting everything inside `main`.

2. Inside `search_log_file`, convert the `keyword` to lowercase once (e.g., `keyword_lower = keyword.lower()`) so you can perform case-insensitive comparisons efficiently.

3. Open the input file for reading using `open(input_path, "r", encoding="utf-8")` and the output file for writing using `open(output_path, "w", encoding="utf-8")` in a single `with` statement so they are both properly closed afterward.

4. Iterate over each `line` in the input file. For each line, compare `keyword_lower` with `line.lower()`; if `keyword_lower in line.lower()` is `True`, write the original `line` to the output file and increment a `match_count` variable.

5. After finishing the loop, return `match_count` from `search_log_file` so the caller knows how many lines matched.

6. In `main()`, use `input()` three times to ask the user for: the input log file path, the search keyword, and the output file path. Strip whitespace from each answer using `.strip()`.

7. Add simple validation in `main()`: if any of the three values is empty (especially input path, keyword, or output path), print a clear error message and exit the function early with `return`.

8. Wrap the call to `search_log_file` in a `try`/`except` block in `main()` to handle file-related errors gracefully. Catch `FileNotFoundError` separately to show a specific message when the input file does not exist, and catch a general `OSError` to cover other problems like permission errors or invalid paths.

9. If an exception is caught, print a clear error message (without re-raising it) and `return` from `main()` so that the program ends cleanly without showing a traceback.

10. If no exception occurs, print the total number of matching lines using the `match_count` returned from `search_log_file`, for example: `print(f"Total matching lines found: {match_count}")`.

11. Ensure `main()` is called only when the script is run directly by adding the `if __name__ == "__main__": main()` guard at the bottom of the file.

