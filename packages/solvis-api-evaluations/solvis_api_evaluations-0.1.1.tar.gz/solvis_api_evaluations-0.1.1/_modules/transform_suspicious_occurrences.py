# Imports
import json
import pandas as pd


class TransformSuspiciousOccurrences:
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

    def transform_suspicious_occurrences(
        self,
        dataframe: pd.DataFrame,
        columns_suspicious_occurrences: str,
        columns_rename: str,
        path_storage: str,
        file_suspicious_occurrences: str,
    ) -> None:
        # Rename columns
        dataframe.rename(columns_rename, axis=1, inplace=True)

        # Keep only known columns
        df_final = dataframe[columns_suspicious_occurrences].copy()

        # Set dtypes
        df_final['id_ocorrencia'] = df_final['id_ocorrencia'].astype('str')
        df_final['nivel'] = df_final['nivel'].astype('str')
        df_final['data_ocorrencia'] = pd.to_datetime(
            df_final['data_ocorrencia'], utc=True
        )
        df_final['id_dispositivo'] = df_final['id_dispositivo'].astype('str')
        df_final['id_unidade'] = df_final['id_unidade'].astype('str')
        df_final['unidade'] = df_final['unidade'].astype('str')

        # Replace NaN values
        df_final.replace('nan', None, inplace=True)

        # Export dataset
        df_final.to_parquet(
            path_storage + file_suspicious_occurrences, compression='gzip', index=False
        )
