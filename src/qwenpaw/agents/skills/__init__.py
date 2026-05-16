# -*- coding: utf-8 -*-
"""Agent skills directory."""

import csv
import os


def read_file(file_path: str) -> str:
    """Reads the content of a text or CSV file.

    Args:
        file_path: The path to the file.

    Returns:
        The content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is not supported (e.g., binary spreadsheets).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    workbook_extensions = {".xlsx", ".xls", ".xlsm", ".xlsb", ".ods"}
    if ext in workbook_extensions:
        raise ValueError(
            f"Cannot read raw workbook file '{file_path}'. "
            "Please inspect bounded rows via a spreadsheet reader or export to CSV."
        )

    # Handle CSV by reading and formatting rows, otherwise read as text
    if ext == ".csv":
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return "\n".join([",".join(row) for row in reader])

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
