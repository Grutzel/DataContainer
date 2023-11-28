from data_container import BasicDataContainer, BasicDataInformation
import pytest
from dataclasses import field, dataclass


@pytest.fixture
def test_data_information() -> BasicDataInformation:
    @dataclass
    class TestDataInformation(BasicDataInformation):
        name: str
        age: 'int64' = field(metadata={'check': ['>', 18]})
        street: str = field(metadata={'map': ['address']})
    return TestDataInformation