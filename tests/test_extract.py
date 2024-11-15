# tests/test_extract.py

import pytest
import pandas as pd
from extract import extract_data

def test_extract_data_success(tmp_path):
    # Create a temporary CSV file
    test_csv = tmp_path / "test_bank_transactions_dataset.csv"
    data = {
        "Customer_id": [1, 2],
        "Age": [30, 45],
        "Transaction_type": ["deposit", "withdrawal"],
        "Balance": [1000.0, 2500.5]
    }
    df = pd.DataFrame(data)
    df.to_csv(test_csv, index=False)

    # Call the extract_data function
    extracted_df = extract_data(str(test_csv))

    # Assertions
    assert not extracted_df.empty, "DataFrame should not be empty"
    assert list(extracted_df.columns) == ["Customer_id", "Age", "Transaction_type", "Balance"], "DataFrame columns mismatch"
