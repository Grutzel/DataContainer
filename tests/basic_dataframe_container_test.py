import pandas as pd
from pandas.testing import assert_frame_equal
from data_container import BasicDataContainer


def test_basic_data_container_init(test_data_information):
    # Arrange

    # Act
    bdc = BasicDataContainer(information=test_data_information)

    # Assert
    assert isinstance(bdc, BasicDataContainer)
    assert bdc.shape == (0, 3)
    assert bdc.empty


def test_basic_dataframe_container_check_for_mapping(test_data_information, test_data_frame,
                                                     test_data_frame_after_mapping):
    # Arrange
    bdc = BasicDataContainer(information=test_data_information)

    # Act
    result = bdc.check_for_mapping(test_data_frame)

    # Assert
    assert isinstance(bdc, BasicDataContainer)
    assert isinstance(result, pd.DataFrame)
    assert_frame_equal(result, test_data_frame_after_mapping)


def test_basic_container_dataframe_fill_default_columns(test_data_information, test_data_frame_after_mapping,
                                                        test_data_frame_after_default):
    # Arrange
    bdc = BasicDataContainer(information=test_data_information)

    # Act
    result = bdc.fill_default_columns(test_data_frame_after_mapping)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert_frame_equal(result, test_data_frame_after_default)


def test_basic_container_dataframe_fill_nan(test_data_information, test_dataframe_nan_filler):
    # Assert
    bdc = BasicDataContainer(information=test_data_information)

    # Arrange
    result = bdc.fill_nan_values(test_dataframe_nan_filler)

    # Assert
    assert isinstance(result, pd.DataFrame)