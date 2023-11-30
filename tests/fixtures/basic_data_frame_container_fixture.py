from data_container import BasicDataContainer, BasicDataInformation
import pytest
import pandas as pd
from dataclasses import field, dataclass
import numpy as np


@pytest.fixture
def data_information_fixture() -> BasicDataInformation:
    @dataclass
    class TestDataInformation(BasicDataInformation):
        name: str
        age: 'int64' = field(metadata={'nan': 18})
        street: str = field(metadata={'map': ['address']})
        money: float = 0.0
    return TestDataInformation


@pytest.fixture
def data_frame_fixture_mapping_and_default() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ['Max', 'Julia'],
        'age': [17, 18],
        'address': ['Muster-Straße 1', 'Testgasse 2']
    })


@pytest.fixture()
def test_data_frame_after_mapping() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ['Max', 'Julia'],
        'age': [17, 18],
        'street': ['Muster-Straße 1', 'Testgasse 2']
    })

@pytest.fixture()
def data_frame_fixture_finished() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ['Max', 'Julia'],
        'age': [17, 18],
        'street': ['Muster-Straße 1', 'Testgasse 2'],
        'money': [0.0, 0.0]
    })

@pytest.fixture()
def test_dataframe_nan_filler() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ['Max', 'Julia'],
        'age': [17, np.nan],
        'street': ['Muster-Straße 1', 'Testgasse 2'],
        'money': [0.0, 0.0]
    })


@pytest.fixture()
def test_dataframe_check_dtype() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ['Max', 'Julia'],
        'age': [17., 18.],
        'street': ['Muster-Straße 1', 'Testgasse 2'],
        'money': ["0.0", "0.0"]
    })


@pytest.fixture()
def test_dataframe_check_dtype_error() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ['Max', 'Julia'],
        'age': ['a', 18.],
        'street': ['Muster-Straße 1', 'Testgasse 2'],
        'money': ["0.0", "0.0"]
    })

@pytest.fixture()
def dataframe_check_dataframe_fixture() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ['Max', 'Julia'],
        'age': [17., np.NAN],
        'street': ['Muster-Straße 1', 'Testgasse 2'],
    })


