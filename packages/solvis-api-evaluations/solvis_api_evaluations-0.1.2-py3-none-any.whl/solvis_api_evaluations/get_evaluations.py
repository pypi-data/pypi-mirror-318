import logging
import requests
from datetime import datetime
from typing import Optional, List, Dict


class GetEvaluations:
    """
    A class to fetch evaluations data from an API.
    """

    def __init__(self) -> None:
        """
        Initialize the EvaluationsFetcher class with default attributes.
        """
        self.user: Optional[str] = None
        self.password: Optional[str] = None
        self.access_token: Optional[str] = None
        self.session: Optional[requests.Session] = None

    def __get_access_token(self) -> None:
        """
        Helper method to authenticate and retrieve the API access token.

        Raises:
            Exception: If authentication fails or the token cannot be retrieved.
        """
        headers_token = {'accept': '*/*', 'Content-Type': 'application/json'}
        data_token = (
            '{"username":' + f'"{self.user}",'
            f'"password":"{self.password}",'
            '"refresh_token":""}'
        )
        response = requests.post(
            'https://sistema.solvis.net.br/api/v1/oauth/token',
            headers=headers_token,
            data=data_token,
        )
        if response.status_code != 200:
            raise Exception('Authentication failed. Check username/password.')

        try:
            self.access_token = response.json()['access_token']
        except KeyError:
            raise Exception('Failed to retrieve access token. Check credentials.')

    def get_evaluations(
        self,
        user: str,
        password: str,
        survey_id: str,
        start_datetime: str,
        end_datetime: str,
        per_page: int = 10000,
        scope: str = 'answered_at',
        verbose: bool = True,
    ) -> List[Dict]:
        """
        Fetch evaluations from the API within a specific date range.

        Args:
            user (str): API username.
            password (str): API password.
            survey_id (str): Survey ID.
            start_datetime (str): Start date (format: YYYY-MM-DDTHH:MM:SS).
            end_datetime (str): End date (format: YYYY-MM-DDTHH:MM:SS).
            per_page (int): Number of evaluations per page (default: 10,000).
            env (str): Environment to query ('sistema' or 'staging').
            scope (str): Scope of the query ('answered_at' or 'received_at').
            verbose (bool): If True, INFO logs are printed; otherwise, only ERROR logs are shown.

        Returns:
            List[Dict]: A list of evaluations.

        Raises:
            Exception: If the date range is invalid or there are API-related errors.
        """
        self.user = user
        self.password = password
        self.session = requests.Session()

        # Configure logging based on verbosity
        logging.basicConfig(
            level=logging.INFO if verbose else logging.ERROR,
            format='%(levelname)s - %(message)s',
        )

        # Validate date range
        date_start = datetime.strptime(start_datetime.split('T')[0], '%Y-%m-%d')
        date_end = datetime.strptime(end_datetime.split('T')[0], '%Y-%m-%d')
        delta = date_end - date_start
        if delta.days > 31:
            raise Exception(
                'The selected date range exceeds the maximum limit of 31 days.'
            )
        if per_page > 10000:
            raise Exception('The maximum number of evaluations per page is 10,000.')

        self.__get_access_token()
        headers = {'accept': '*/*', 'Authorization': f'Bearer {self.access_token}'}

        evaluations = []
        page = 1

        logging.info('Starting export of evaluations...')
        while True:
            try:
                url = (
                    f'https://sistema.solvis.net.br/api/v1/surveys/{survey_id}/evaluations?'
                    f'search_date_scope={scope}&'
                    f'start_date={start_datetime}&'
                    f'end_date={end_datetime}&'
                    f'page={page}&'
                    f'per_page={per_page}'
                )
                response = self.session.get(url, headers=headers)

                if response.status_code != 200:
                    raise Exception(f'Error fetching data: {response.status_code}')

                data = response.json()
                if 'error' in data:
                    raise Exception(f"API error: {data['error']}")

                answers = data.get('data', [])
                if not answers:
                    logging.info('Export complete!')
                    break

                evaluations.extend(answers)
                logging.info(
                    f'Page {page} fetched successfully with {len(answers)} records.'
                )
                page += 1
            except Exception as e:
                logging.error(f'An error occurred: {e}')
                break

        logging.info(f'Total evaluations fetched: {len(evaluations)}')
        return [evaluations]
