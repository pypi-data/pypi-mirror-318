# Imports
import pandas as pd
from datetime import datetime


class TransformShifts:
    def __init__(self) -> None:
        pass

    def transform_shifts(
        self,
        dataframe_shift: pd.DataFrame,
        dataframe_daily: pd.DataFrame,
        shift_col=None,
    ) -> pd.DataFrame:
        """Transform shifts dataset and assign shifts to surveyed units.

        Args:
            dataframe_shift (pd.DataFrame): DataFrame containing shift information
            dataframe_daily (pd.DataFrame): DataFrame containing daily data to apply shifts
            shift_col (str, optional): Column name for shift data in web data. Defaults to None.

        Returns:
            pd.DataFrame: Transformed DataFrame with assigned shifts
        """
        df_shift = dataframe_shift.copy()
        df_daily = dataframe_daily.copy()

        def correct_shifts(row):
            if row['timestampsFilter.selectionRange'] == 'not_between':
                current_start = datetime.fromisoformat(
                    str(row['timestampsFilter.startTime'])
                )
                current_end = datetime.fromisoformat(
                    str(row['timestampsFilter.endTime'])
                )
                new_first_start = current_start.replace(hour=0, minute=0, second=1)
                new_first_end = current_start
                new_second_start = current_end
                new_second_end = current_start.replace(hour=23, minute=59, second=59)

                new_lines = [
                    {
                        **row,
                        'timestampsFilter.startTime': new_first_start,
                        'timestampsFilter.endTime': new_first_end,
                        'timestampsFilter.selectionRange': 'between',
                    },
                    {
                        **row,
                        'timestampsFilter.startTime': new_second_start,
                        'timestampsFilter.endTime': new_second_end,
                        'timestampsFilter.selectionRange': 'between',
                    },
                ]
                return pd.DataFrame(new_lines)
            return pd.DataFrame([row])

        # Apply correct_shifts function to handle 'not_between' cases
        df_shift = (
            df_shift.apply(lambda x: correct_shifts(x), axis=1)
            .explode()
            .reset_index(drop=True)
        )

        # Set data types
        df_daily = df_daily.astype({'id_pesquisa': 'str', 'id_unidade': 'str'})

        # Filter shifts for Totem data
        df_totem = df_daily[df_daily['origem'] == 'Totem'].copy()
        if not df_totem.empty:
            df_totem['turno'] = None
            for idx, row in df_totem.iterrows():
                unit = row['id_unidade']
                answer_datetime = row['iniciado_em'].time()
                shifts = df_shift[df_shift['surveyedUnit.id'] == unit]

                if shifts.empty:
                    df_totem.at[idx, 'turno'] = 'Sem turno cadastrado'
                else:
                    for _, shift in shifts.iterrows():
                        if (
                            shift['timestampsFilter.startTime'].time()
                            <= answer_datetime
                            <= shift['timestampsFilter.endTime'].time()
                        ):
                            df_totem.at[idx, 'turno'] = shift['shift.name']
                            break
                    else:
                        df_totem.at[idx, 'turno'] = 'Fora do turno'
        else:
            print('Nenhuma unidade TOTEM encontrada!')

        # Handle Web data
        df_web = df_daily[df_daily['origem'] == 'Web'].copy()
        if not df_web.empty:
            df_web['turno'] = df_web[shift_col] if shift_col else 'Sem turno cadastrado'
            df_web['turno'].fillna('Sem turno cadastrado', inplace=True)
        else:
            print('Nenhuma unidade WEB encontrada!')

        return pd.concat([df_totem, df_web], ignore_index=True)
