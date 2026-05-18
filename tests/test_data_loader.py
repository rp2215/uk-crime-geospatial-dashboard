import pandas as pd
import pytest
from pathlib import Path
from src.crime_dashboard.data_loader import find_csv_files, read_csv_file

def test_find_csv_files_returns_list(tmp_path):

    (tmp_path / "test.csv").write_text("col\nval")

    result = find_csv_files(tmp_path)

    assert len(result) == 1

def test_find_csv_files_empty_dir(tmp_path):

    result = find_csv_files(tmp_path)

    assert result == []

def test_read_csv_file_adds_source_column(tmp_path):

    # write a minimal CSV with all required columns
    from src.crime_dashboard.config import REQUIRED_COLUMNS

    csv_path = tmp_path / "sample.csv"
    header = ",".join(REQUIRED_COLUMNS)
    row = ",".join(["val"] * len(REQUIRED_COLUMNS))
    csv_path.write_text(f"{header}\n{row}")
    
    result = read_csv_file(csv_path)

    assert "source_file" in result.columns
    assert result["source_file"].iloc[0] == "sample.csv"
