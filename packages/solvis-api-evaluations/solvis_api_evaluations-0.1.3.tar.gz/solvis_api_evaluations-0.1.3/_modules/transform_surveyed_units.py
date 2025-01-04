# Imports
import json
import pandas as pd


class TransformSurveyedUnits:
    def __init__(self) -> None:
        pass

    def load_file(self, path_to_asset: str, file_name: str):
        """Read a file and return a list.

        Args:
            path_to_asset (str): Path to file
            file_name (str): Filename

        Returns:
            list: List of keywords from file
        """
        aux_list = []

        if file_name.endswith('.txt'):
            with open(f'{path_to_asset}{file_name}', 'r', encoding='utf-8') as fh:
                for line in fh:
                    line = line.replace('\n', '')
                    aux_list.append(line)
            return aux_list

        elif file_name.endswith('.json'):
            with open(path_to_asset + file_name) as fh:
                json_file = json.load(fh)
            return json_file
        else:
            print('Arquivo de formato inválido!')

    def transform_surveyed_units(
        self,
        dataframe: pd.DataFrame,
        columns_surveyed_units: str,
        columns_rename: str,
        path_storage: str,
        file_surveyed_unit: str,
    ):
        # Rename columns
        dataframe.rename(columns_rename, axis=1, inplace=True)

        # Add missing columns
        for col in columns_surveyed_units:
            if col not in dataframe.columns.tolist():
                dataframe[col] = None
                print(f'Coluna |{col}| criada!')

        # Keep only known columns
        df_final = dataframe[columns_surveyed_units].copy()

        # Set dtypes
        df_final['id_unidade'] = df_final['id_unidade'].astype('str')
        try:
            df_final['nome'] = df_final['nome'].astype('str')
        except KeyError:
            pass

        # Replace NaN values
        df_final.replace('nan', None, inplace=True)

        # Export dataset
        df_final.to_parquet(
            path_storage + file_surveyed_unit, compression='gzip', index=False
        )
