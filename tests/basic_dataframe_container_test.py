from data_container import BasicDataContainer


def test_basic_data_container_init(test_data_information):
    # Arrange

    # Act
    bdc = BasicDataContainer(information=test_data_information)

    # Assert
    assert isinstance(bdc, BasicDataContainer)
    assert bdc.shape[0] == 0