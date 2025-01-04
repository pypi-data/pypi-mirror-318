# Imports
import pandas as pd
import requests
from json import JSONDecodeError


class GetSurveyedUnits:
    def get_all_surveyed_units(
        self, user: str, password: str, env='sistema'
    ) -> pd.DataFrame:
        """Get surveyed units

        Args:
            user (str): API username
            password (str): API password
            env (str): [sistema, staging]

        """

        self.user = user
        self.password = password

        def request_api():
            """Get API and return JSON

            Args:
            Returns:
                json: JSON
            """
            headers_token = {
                'accept': '*/*',
                'Content-Type': 'application/json',
            }

            # Set headers content
            data_token = (
                '{"username":' + f'"{self.user}",'
                f'"password":"{self.password}",'
                '"refresh_token":""}'
            )

            # POST for token
            response = requests.post(
                f'https://{env}.solvis.net.br/api/v1/oauth/token',
                headers=headers_token,
                data=data_token,
            )

            # Get access token
            try:
                self.access_token = response.json()['access_token']
            except KeyError:
                raise Exception('Usuário/Senha incorreto. Favor verificar!')

            # Set headers
            headers = {
                'accept': '*/*',
                'Authorization': f'Bearer {self.access_token}',
            }

            # Create session
            self.session = requests.Session()

            response_survey = self.session.get(
                f'https://{env}.solvis.net.br/api/v1/surveyed_units'
                f'?page={str(page)}',
                headers=headers,
            )

            return response_survey

        # Create empty dataframe
        self.df_temp = pd.DataFrame()

        # Set default page
        page = 1
        total = 0

        while True:
            try:
                response = request_api()
            except (ConnectionError, ConnectionAbortedError) as error:
                raise Exception(error)

            if response.status_code != 200:
                raise Exception(f'Erro: {response.status_code}')
            else:
                try:
                    json = response.json()
                except JSONDecodeError as error:
                    raise Exception(error)

                try:
                    if json['error']:
                        raise Exception(json['error'])
                except KeyError:
                    pass
                answers = json['data']
                count = len(answers)

                if answers:
                    for idx in range(len(answers)):
                        try:
                            questions = answers[idx].pop('surveyed_unit_properties')
                            df_properties = pd.json_normalize(answers[idx])
                            df_properties.set_index(pd.Index([idx]), inplace=True)
                        except KeyError:
                            continue

                        for i in range(len(questions)):
                            try:
                                name = questions[i]['surveyed_unit_property_name'][
                                    'name'
                                ]
                                value = questions[i]['surveyed_unit_property_value'][
                                    'value'
                                ]
                                df_properties[name] = None
                                df_properties.loc[idx, name] = value
                            except KeyError:
                                continue

                        self.df_temp = pd.concat(
                            [self.df_temp, df_properties], ignore_index=False
                        )

                    print(f'Página: {page} - OK!')
                    page += 1
                    total = total + count
                else:
                    print('Fim da exportação!')
                    print(f'Total de unidades com propriedades: {total}')
                    break
        try:
            self.df_temp.drop('schedules', axis=1, inplace=True)
        except KeyError:
            pass

            self.df_temp.reset_index(drop=True, inplace=True)

        return self.df_temp

    def get_surveyed_unit(
        self, user: str, password: str, unit_id: str, env='sistema'
    ) -> pd.DataFrame:
        """Get surveyed units

        Args:
            user (str): API username
            password (str): API password
            unit_id (str): ID of given unit
            env (str): [sistema, staging]

        """

        self.user = user
        self.password = password
        self.unit_id = unit_id

        def request_api():
            """Get API and return JSON

            Args:
            Returns:
                json: JSON
            """
            headers_token = {
                'accept': '*/*',
                'Content-Type': 'application/json',
            }

            # Set headers content
            data_token = (
                '{"username":' + f'"{self.user}",'
                f'"password":"{self.password}",'
                '"refresh_token":""}'
            )

            # POST for token
            response = requests.post(
                f'https://{env}.solvis.net.br/api/v1/oauth/token',
                headers=headers_token,
                data=data_token,
            )

            # Get access token
            try:
                self.access_token = response.json()['access_token']
            except KeyError:
                raise Exception('Usuário/Senha incorreto. Favor verificar!')

            # Set headers
            headers = {
                'accept': '*/*',
                'Authorization': f'Bearer {self.access_token}',
            }

            # Create session
            self.session = requests.Session()

            response_survey = self.session.get(
                f'https://{env}.solvis.net.br/api/v1/surveyed_units/' f'{unit_id}',
                headers=headers,
            )

            return response_survey

        # Create empty dataframe
        self.df_temp = pd.DataFrame()

        try:
            response = request_api()
        except (ConnectionError, ConnectionAbortedError) as error:
            raise Exception(error)

        if response.status_code != 200:
            raise Exception(f'Erro: {response.status_code}')
        else:
            try:
                json = response.json()
            except JSONDecodeError as error:
                raise Exception(error)

            try:
                if json['error']:
                    raise Exception(json['error'])
            except KeyError:
                pass
            answers = json['data']

            if answers:
                try:
                    questions = answers.pop('surveyed_unit_properties')
                    df_properties = pd.json_normalize(answers)
                except KeyError as error:
                    print(error)

                for i in range(len(questions)):
                    try:
                        name = questions[i]['surveyed_unit_property_name']['name']
                        value = questions[i]['surveyed_unit_property_value']['value']
                        df_properties[name] = None
                        df_properties.loc[0, name] = value
                    except KeyError as error:
                        print(error)
                        continue

                self.df_temp = pd.concat(
                    [self.df_temp, df_properties], ignore_index=False
                )
            print('Propriedades exportadas com sucesso!')

        try:
            self.df_temp.drop('schedules', axis=1, inplace=True)
        except KeyError:
            pass

        return self.df_temp
