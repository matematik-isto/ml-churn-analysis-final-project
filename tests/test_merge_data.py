import pandas as pd

from src.data.consolidation import my_prepare_dataset
from src.data.load_data import my_load_data
from src.utils.utils import my_normalize_string

def test_merge_data(data_folder = 'data/raw'):

    # Arrange: cargar los archivos reales
    data_dict = my_load_data(data_folder)
#    customers = pd.read_csv("data/raw/customer.csv")
#    contracts = pd.read_csv("data/raw/contract.csv")

    # Act: ejecutar la función
    result = my_prepare_dataset(data_dict)

    # Assert: validar el resultado

    # 1. El resultado debe ser un DataFrame
    assert isinstance(result, pd.DataFrame)

    # 2. Debe conservar todas las filas del dataframe izquierdo
    assert len(result) == len(data_dict['contract'])

    # 3. Debe conservar la columna customer_id
    print(type(result))
    print(result.columns)
    assert 'customer_id' in result.columns


    # 4. Debe contener columnas provenientes de ambos archivos
    assert (
        {
            my_normalize_string(col)
            for col in data_dict['contract'].columns
        }.issubset(result.columns)
    )
    assert (
        {
            my_normalize_string(col) 
            for col in data_dict['personal'].columns
        }.issubset(result.columns)
    )
    assert (
        {
            my_normalize_string(col)
            for col in data_dict['phone'].columns
        }.issubset(result.columns)
    )
    assert (
        {
            my_normalize_string(col)
            for col in data_dict['internet'].columns
        }.issubset(result.columns)
    )

    # 5. No debe haber customer_id duplicados en el resultado
    assert result["customer_id"].is_unique