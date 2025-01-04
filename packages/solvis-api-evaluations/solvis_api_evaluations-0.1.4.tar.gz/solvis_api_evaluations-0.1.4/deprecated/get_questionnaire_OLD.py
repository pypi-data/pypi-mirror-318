# Imports
import pandas as pd
import requests
from json import JSONDecodeError


class GetQuestionnaire:
    def get_questionnaire(
        self, user: str, password: str, survey_id: str, env='sistema'
    ) -> list|None:
        """Get current questionnaire

        Args:
            user (str): API username
            password (str): API password
            env (str): [sistema, staging]

        """

        self.user = user
        self.password = password
        self.survey_id = survey_id

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
                f'https://{env}.solvis.net.br/api/v1/surveys/{self.survey_id}',
                headers=headers,
            )

            return response_survey

        # Create empty dataframe
        self.df_temp = pd.DataFrame()

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

                if answers:
                    df_quest = pd.json_normalize(answers)

                    num_questions = len(df_quest['questionnaire.questions'][0])

                    try:
                        cols = []
                        for q in range(num_questions):
                            cols.append(
                                df_quest['questionnaire.questions'][0][q]['text']
                            )
                        return cols
                    except Exception as er:
                        raise Exception(er)
                else:
                    print('Questionário não encontrado!')
                    return None

    def get_questionnaire_version(
        self, user: str, password: str, survey_id: str, env='sistema'
    ) -> int|None:
        """Get current questionnaire version

        Args:
            user (str): API username
            password (str): API password
            env (str): [sistema, staging]

        """

        self.user = user
        self.password = password
        self.survey_id = survey_id

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
                f'https://{env}.solvis.net.br/api/v1/surveys/{self.survey_id}',
                headers=headers,
            )

            return response_survey

        # Create empty dataframe
        self.df_temp = pd.DataFrame()

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

                if answers:
                    df_quest = pd.json_normalize(answers)

                    try:
                        return df_quest['questionnaire.version'][0]
                    except Exception as er:
                        raise Exception(er)
                else:
                    print('Questionário não encontrado!')
                    return None
