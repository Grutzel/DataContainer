import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from data_container import BasicDataContainer


def test_basic_data_container_init(data_information_fixture):
    # Arrange

    # Act
    bdc = BasicDataContainer(information=data_information_fixture)

    # Assert
    assert isinstance(bdc, BasicDataContainer)
    assert bdc.shape == (0, 4)
    assert bdc.empty


def test_basic_dataframe_container_check_for_mapping(data_information_fixture, data_frame_fixture_mapping_and_default,
                                                     test_data_frame_after_mapping):
    # Arrange
    bdc = BasicDataContainer(information=data_information_fixture)

    # Act
    result = bdc.check_for_mapping(data_frame_fixture_mapping_and_default)

    # Assert
    assert isinstance(bdc, BasicDataContainer)
    assert isinstance(result, pd.DataFrame)
    assert_frame_equal(result, test_data_frame_after_mapping)


def test_basic_container_dataframe_fill_default_columns(data_information_fixture, test_data_frame_after_mapping,
                                                        data_frame_fixture_finished):
    # Arrange
    bdc = BasicDataContainer(information=data_information_fixture)

    # Act
    result = bdc.fill_default_columns(test_data_frame_after_mapping)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert_frame_equal(result, data_frame_fixture_finished)


def test_basic_container_dataframe_fill_nan(data_information_fixture, test_dataframe_nan_filler):
    # Assert
    bdc = BasicDataContainer(information=data_information_fixture)

    # Arrange
    result = bdc.fill_nan_values(test_dataframe_nan_filler)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert result.notna().all().all()


def test_dataframe_container_check_data_type(data_information_fixture, test_dataframe_check_dtype,
                                             data_frame_fixture_finished):
    # Arrange
    bdc = BasicDataContainer(information=data_information_fixture)

    # Act
    result = bdc.check_data_type(test_dataframe_check_dtype)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert_frame_equal(result, data_frame_fixture_finished)


def test_dataframe_container_check_data_type_error(data_information_fixture, test_dataframe_check_dtype_error):
    # Arrange
    bdc = BasicDataContainer(information=data_information_fixture)

    # Act
    with pytest.raises(ValueError):
        result = bdc.check_data_type(test_dataframe_check_dtype_error)


def test_dataframe_container_check_dataframe(data_information_fixture, dataframe_check_dataframe_fixture,
                                             data_frame_fixture_finished):
    # Arrange
    bdc = BasicDataContainer(information=data_information_fixture)

    # Act
    result = bdc.check_dataframe(dataframe_check_dataframe_fixture)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert_frame_equal(result, data_frame_fixture_finished)
