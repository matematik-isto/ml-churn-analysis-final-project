# tests/test_clean_sources.py

# run from root folder with the command: pytest tests/test_clean_sources.py -v
from src.data.clean_sources import *
from src.data.load_data import my_load_data


def test_clean_sources():
    data_folder = 'data/raw'
    data = my_load_data(data_folder)
    contract = clean_contract(data['contract'])
    personal = clean_personal(data['personal'])
    internet = clean_internet(data['internet'])
    phone = clean_phone(data['phone'])

    assert "customer_id" in contract.columns
    assert "begin_date" in contract.columns
    assert "end_date" in contract.columns
    assert "type" in contract.columns
    assert "paperless_billing" in contract.columns
    assert "payment_method" in contract.columns
    assert "monthly_charges" in contract.columns
    assert "total_charges" in contract.columns
    assert contract["customer_id"].is_unique
###
    assert "customer_id" in personal.columns
    assert "gender" in personal.columns
    assert "senior_citizen" in personal.columns
    assert "partner" in personal.columns
    assert "dependents" in personal.columns
    assert personal["customer_id"].is_unique
###
    assert "customer_id" in internet.columns
    assert "internet_service" in internet.columns
    assert "online_security" in internet.columns
    assert "online_backup" in internet.columns
    assert "device_protection" in internet.columns
    assert "tech_support" in internet.columns
    assert "streaming_tv" in internet.columns
    assert "streaming_movies" in internet.columns
    assert internet["customer_id"].is_unique
###
    assert "customer_id" in phone.columns
    assert "multiple_lines" in phone.columns
    assert phone["customer_id"].is_unique


#if __name__ == "__main__":
#    test_clean_sources()