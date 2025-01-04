# Imports
import pandas as pd


class TransformDevices:
    def __init__(self) -> None:
        pass

    def transform_devices(
        self, dataframe: pd.DataFrame, path_storage: str, file_devices: str
    ) -> None:
        """Read a dataframe and apply transformations

        Args:
            dataframe (pd.DataFrame): Dataframe
        """
        # Dict rename
        rename_columns = {
            'id': 'id_dispositivo',
            'android_id': 'id_android',
            'location_provider': 'localizacao_provedor',
            'location_accuracy': 'localizacao_acuracia',
            'location_latitude': 'localizacao_latitude',
            'location_longitude': 'localizacao_longitude',
            'block_screen': 'tela_bloqueio',
            'full_name': 'nome_unidade_completo',
            'surveyed_unit.id': 'id_unidade',
            'surveyed_unit.name': 'nome_unidade',
            'last_connection.connection_type': 'tipo_conexao',
            'last_connection.created_at': 'ultima_conexao',
        }

        # Set dtypes
        dataframe['id'] = dataframe['id'].astype('int')
        dataframe['android_id'] = dataframe['android_id'].astype('str')
        dataframe['location_provider'] = dataframe['location_provider'].astype('str')
        dataframe['location_accuracy'] = dataframe['location_accuracy'].astype('str')
        dataframe['location_latitude'] = dataframe['location_latitude'].astype('str')
        dataframe['location_longitude'] = dataframe['location_longitude'].astype('str')
        dataframe['block_screen'] = dataframe['block_screen'].astype('bool')
        dataframe['full_name'] = dataframe['full_name'].astype('str')
        dataframe['surveyed_unit.id'] = dataframe['surveyed_unit.id'].astype('str')
        dataframe['surveyed_unit.name'] = dataframe['surveyed_unit.name'].astype('str')
        dataframe['last_connection.connection_type'] = dataframe[
            'last_connection.connection_type'
        ].astype('str')
        dataframe['last_connection.created_at'] = dataframe[
            'last_connection.created_at'
        ].astype('str')

        # Rename columns
        dataframe.rename(rename_columns, axis=1, inplace=True)

        # Create a copy
        df = dataframe.copy()

        # Convert to datetime
        df['ultima_conexao'] = pd.to_datetime(df['ultima_conexao'], utc=True)

        # Export dataset
        df.to_parquet(path_storage + file_devices, compression='gzip', index=False)
