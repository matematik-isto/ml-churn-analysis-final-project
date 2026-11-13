# tests/test_load_data.py

# run from root folder with the command: pytest tests/test_load_data.py -v
from src.data.load_data import my_load_data


def test_load_data():
    data_folder = 'data/raw'

    result = my_load_data(data_folder)

#,,,,,,,
    assert len(result) >= 4
    if 'customer_id' in result["internet"].columns:
        assert result["internet"]["customer_id"].is_unique  