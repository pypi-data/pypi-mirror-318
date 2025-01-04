# Imports
import requests
import time
from datetime import datetime
from json import JSONDecodeError


class GetEvaluations:
    def __init__(self) -> None:
        self.session = requests.Session()

    def get_evaluations(
        self,
        user: str,
        password: str,
        survey_id: str,
        start_datetime: str,
        end_datetime: str,
        per_page=10000,
        env='sistema',
        scope='answered_at',
    ) -> list[dict]:
        """Get evaluations

        Args:
            user (str): API username
            password (str): API password
            survey_id (str): Survey ID
            start_datetime (str): Start date (format YYYY-MM-DDTHH:MM:SS)
            end_datetime (str): End date (format YYYY-MM-DDTHH:MM:SS)
            per_page (int): Total evaluations per page (max: 100)
            env (str): [sistema, staging]
            scope (str): [answered_at, received_at]

        Returns:
            dict: Pandas Dataframe
        """

        self.user = user
        self.password = password
        self.survey_id = survey_id
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

        # Check for valid period
        date_start = datetime.strptime(self.start_datetime.split('T')[0], '%Y-%m-%d')
        date_end = datetime.strptime(self.end_datetime.split('T')[0], '%Y-%m-%d')
        delta = date_end - date_start

        if delta.days > 31:
            raise Exception('O período selecionado excede o limite máximo de 31 dias!')

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

            response_survey = self.session.get(
                f'https://{env}.solvis.net.br/api/v1/surveys/'
                f'{self.survey_id}/evaluations?search_date_scope={scope}&'
                f'start_date={self.start_datetime}&'
                f'end_date={self.end_datetime}&'
                f'page={str(self.page)}&'
                f'per_page={per_page}',
                headers=headers,
            )

            return response_survey

        # Set default values
        self.page = 1
        total = 0
        evaluations = []

        print('Iniciando exportação de avaliações...')
        time_start = time.perf_counter()
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
                if json['data']:
                    answers = json['data']
                    evaluations.append(answers)
                    count = len(answers)

                    print(f'Página: {self.page} - OK!')
                    self.page += 1
                    total = total + count
                else:
                    time_end = time.perf_counter()
                    time_final = round(time_end - time_start, 2)
                    print('Fim da exportação!')
                    print(f'Total de avaliações: {total}')
                    print(f'Tempo total: {time_final} segundo(s)')
                    break

        # Close connection
        self.session.close()

        return evaluations
