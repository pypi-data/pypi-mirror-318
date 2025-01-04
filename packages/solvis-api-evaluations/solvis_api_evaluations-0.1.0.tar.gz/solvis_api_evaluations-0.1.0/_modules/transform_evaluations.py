# Imports
import json
import pandas as pd


class TransformEvaluations:
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

    def transform_evaluations(
        self,
        columns_survey: str,
        columns_rename: str,
        columns_drop: str,
        path_storage: str,
        file_daily: str,
    ):
        # Functions
        def build_id_resposta(x) -> str:
            id_og = str(x['id_resposta'])
            year = str(x['iniciado_em'].year)[-2:]
            month = str(x['iniciado_em'].month)[-2:]
            day = str(x['iniciado_em'].day)[-2:]

            if len(month) == 1:
                month = f'0{month}'
            if len(day) == 1:
                day = f'0{day}'

            final_date = year + month + day
            len_date = len(final_date)
            len_id = len(id_og)
            zeros = 18 - (len_date + len_id)
            final_id = f'{final_date}{"0" * zeros}{id_og}'

            return final_id

        def build_id_universal(x) -> str:
            datetime = (
                str(x['iniciado_em'])
                .split('+')[0]
                .replace('-', '')
                .replace(' ', '')
                .replace(':', '')
            )
            shard = str(x['id_shard'])

            return str(datetime + shard)

        def convert_nps(x: str) -> int|None:
            if x == 'Detrator':
                return -100
            elif x == 'Neutro':
                return 0
            elif x == 'Promotor':
                return 100
            else:
                return None

        # Load dataset
        df = pd.read_parquet(path_storage + file_daily)

        # Transform dataframe
        df.rename(columns_rename, axis=1, inplace=True)
        print('Colunas renomeadas com sucesso!')

        # # Merge columns with same name
        # duplicates = df.columns[df.columns.duplicated()]
        # if duplicates.any():
        #     print(f'Duplicados: {duplicates.tolist()}')
        #     for col in duplicates.tolist():
        #         df.rename(columns={col: f'{col}_temp'}, inplace=True)
        #         df[col] = df[col].fillna(df[f'{col}_temp'])
        #         df.drop(columns=[f'{col}_temp'], inplace=True)

        for col in columns_drop:
            try:
                df.drop(col, axis=1, inplace=True)
            except KeyError:
                print(f'Coluna |{col}| não encontrada!')
                continue

        # Add missing columns
        for col in columns_survey:
            if col not in df.columns.tolist():
                df[col] = None
                print(f'Coluna |{col}| criada!')

        # Set dtypes
        df['id_universal'] = df['id_universal'].astype('str')
        df['id_resposta'] = df['id_resposta'].astype('str')
        df['id_unidade'] = df['id_unidade'].astype('str')
        df['id_pesquisa'] = df['id_pesquisa'].astype('str')
        df['id_dispositivo'] = df['id_dispositivo'].astype('str')
        df['id_dispositivo'] = df['id_dispositivo'].apply(lambda x: x.split('.')[0])
        df['id_shard'] = df['id_shard'].astype('str')
        df['duracao'] = df['duracao'].astype('int')
        df['iniciado_em'] = pd.to_datetime(df['iniciado_em'], utc=True)
        df['criado_em'] = pd.to_datetime(df['criado_em'], utc=True)

        # Build standard id
        df['id_resposta'] = df.apply(lambda x: build_id_resposta(x), axis=1)

        # Build universal id
        df['id_universal'] = df.apply(lambda x: build_id_universal(x), axis=1)

        # Check for NPS col and convert it
        if 'nps_tipo' in df.columns.tolist():
            df['nps'] = df['nps_tipo'].apply(lambda x: convert_nps(x))

        # Export dataset
        df.to_parquet(path_storage + file_daily, compression='gzip', index=False)
