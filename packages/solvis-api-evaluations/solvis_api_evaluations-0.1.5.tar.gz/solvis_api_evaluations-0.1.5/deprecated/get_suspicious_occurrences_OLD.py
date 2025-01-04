# Imports
import pandas as pd
import requests
from json import JSONDecodeError


class GetSuspiciousOccurrences:
    def get_suspicious_occurrences(
        self, user: str, password: str, env='sistema'
    ) -> pd.DataFrame:
        """Get all suspicious occurrences

        Args:
            user (str): API username
            password (str): API password
            env (str): [sistema, staging]

        Returns:
            dict: Pandas Dataframe
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

            response = self.session.get(
                f'https://{env}.solvis.net.br/api/v1/suspicious_occurrences?'
                f'page={str(self.page)}',
                headers=headers,
            )

            return response

        # Create empty dataframe
        self.df_temp = pd.DataFrame()

        # Set default values
        self.page = 1
        self.total = 0

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
                    df_so = pd.json_normalize(answers)
                    self.df_temp = pd.concat([self.df_temp, df_so], ignore_index=True)
                    print(f'Página: {self.page} - OK!')
                    self.page += 1
                    total = self.total + count
                else:
                    print('Fim da exportação!')
                    print(f'Total de ocorrências suspeitas: {total}')
                    break

            self.df_temp.reset_index(drop=True, inplace=True)

        return self.df_temp
