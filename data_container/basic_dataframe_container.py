from dataclasses import dataclass, field, MISSING
import pandas as pd

@dataclass
class BasicDataInformation:
    """
    A class that stores the BasicInformation on how the stored dataframe has to look like.
    When inherited, @dataclass needs to be set their again
    E.G.:
    name: str
    age: 'int64' = field(metadata={'check': {'age' > 18}})
    street: str = field(metadata={'map': ['address']}
    """
    pass


@dataclass
class BasicDataContainer:
    """
    Template that uses the information given in a DataInformation class and sets up a dataframe and executes the
    steps and additional functions.

    Args:

    """
    information: BasicDataInformation = BasicDataInformation
    _columns: list = field(default_factory=list)
    _default_columns: dict = field(default_factory=dict)
    _dataframe: pd.DataFrame = field(init=False, default=pd.DataFrame)
    _mapping_dict: dict = field(default_factory=dict)
    _check_dict: dict = field(default_factory=dict)

    def __post_init__(self):
        self.__extract_information()
        self._dataframe = pd.DataFrame(columns=self.columns)

    @property
    def shape(self) -> [int, int]:
        return self._dataframe.shape

    def __getitem__(self, item: str | list):
        return

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe

    @dataframe.setter
    def dataframe(self, df: pd.DataFrame) -> None:
        df = self.check_dataframe(df)
        self._dataframe = df

    @property
    def columns(self) -> list:
        return self._columns

    @property
    def empty(self) -> bool:
        return self.dataframe.empty

    @property
    def empty(self) -> bool:
        return self.dataframe.empty

    @columns.setter
    def columns(self, value):
        raise ValueError('You are not allowed to change the columns')

    def __extract_information(self, **kwargs):
        for key, value in self.information.__dataclass_fields__.items():
            self.__extract_columns(key, value, **kwargs)
            self.__extract_metadata(key, value.metadata)

    def __extract_columns(self, col: str, value, **kwargs):
        """ Extracts the columns and default columns given in the DataInformation.
        """
        if not value.default == MISSING:
            self._default_columns[col] = value.default
        self._columns.append(col)


    def __extract_metadata(self, col: str, metadata, **kwargs):
        """ Extracts the columns where a mapping has to be done
        """
        if len(metadata) > 0:
            for key, value in metadata.items():
                if key == 'check':
                    self.__add_check(col, value, **kwargs)
                elif key == 'map':
                    self._mapping_dict[col] = value
                else:
                    print('Key feature not implemented.')

    def __add_check(self, col: str, check: list, **kwargs):
        """ Will be implemented in future releases

        :param col:
        :param check:
        :param kwargs:
        :return:
        """
        pass

    def append(self, df: pd.DataFrame):
        df = self.check_dataframe(df)

        if self.empty:
            self._dataframe = df
        else:
            self._dataframe = pd.concat([self.dataframe, df], ignore_index=True)

    def check_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.reset_index(drop=True)
        df = self.check_for_mapping(df)
        return df

    def check_for_mapping(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Checks if columns have to be mapped, ore renamed

        :param df:
        :return:
        """

        return df