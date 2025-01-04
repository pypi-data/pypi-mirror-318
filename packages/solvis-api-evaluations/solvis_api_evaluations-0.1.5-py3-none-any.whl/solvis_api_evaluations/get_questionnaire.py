import logging
import requests
from typing import Optional, List


class GetQuestionnaire:
    """
    A class to interact with the questionnaire API and fetch survey-related data.
    """

    def __init__(self) -> None:
        """
        Initialize the GetQuestionnaire class with default attributes.
        """
        self.user: Optional[str] = None
        self.password: Optional[str] = None
        self.survey_id: Optional[str] = None
        self.access_token: Optional[str] = None
        self.session: Optional[requests.Session] = None

    def get_questionnaire(
        self,
        user: str,
        password: str,
        survey_id: str,
        verbose: bool = True,
    ) -> Optional[List[str]]:
        """
        Fetch the current questionnaire's questions.

        Args:
            user (str): API username.
            password (str): API password.
            survey_id (str): Survey ID.
            verbose (bool): If True, INFO logs are printed; otherwise, only ERROR logs are shown.

        Returns:
            Optional[List[str]]: A list of questions from the questionnaire or None if not found.

        Raises:
            Exception: For connection errors, authentication failures, or other API issues.
        """
        self.user = user
        self.password = password
        self.survey_id = survey_id
        self.session = requests.Session()

        # Configure logging based on verbosity
        logging.basicConfig(
            level=logging.INFO if verbose else logging.ERROR,
            format='%(levelname)s - %(message)s',
        )

        def __request_api() -> requests.Response:
            """
            Helper function to send API requests and handle the response.

            Returns:
                requests.Response: API response object.

            Raises:
                Exception: If access token retrieval fails or response status is not 200.
            """
            # Get access token
            headers_token = {'accept': '*/*', 'Content-Type': 'application/json'}
            data_token = (
                '{"username":' + f'"{self.user}",'
                f'"password":"{self.password}",'
                '"refresh_token":""}'
            )
            response_token = requests.post(
                'https://sistema.solvis.net.br/api/v1/oauth/token',
                headers=headers_token,
                data=data_token,
            )

            if response_token.status_code != 200:
                raise Exception('Authentication failed. Check username/password.')

            try:
                self.access_token = response_token.json()['access_token']
            except KeyError:
                raise Exception('Failed to retrieve access token. Check credentials.')

            # Request questionnaire data
            headers = {'accept': '*/*', 'Authorization': f'Bearer {self.access_token}'}
            return self.session.get(
                f'https://sistema.solvis.net.br/api/v1/surveys/{self.survey_id}',
                headers=headers,
            )

        try:
            response = __request_api()
            if response.status_code != 200:
                raise Exception(f'Error fetching questionnaire: {response.status_code}')

            data = response.json()
            if 'error' in data:
                raise Exception(f"API error: {data['error']}")

            # Extract questions
            questionnaire_data = data.get('data', {})
            questions = questionnaire_data.get('questionnaire', {}).get('questions', [])
            if not questions:
                logging.info('No questions found in the questionnaire.')
                return None

            question_texts = [q.get('text', '') for q in questions]
            logging.info(f'Successfully retrieved {len(question_texts)} questions.')
            return question_texts
        except Exception as e:
            logging.error(f'An error occurred: {e}')

        return None

    def get_questionnaire_version(
        self,
        user: str,
        password: str,
        survey_id: str,
        verbose: bool = True,
    ) -> Optional[int]:
        """
        Fetch the current version of the questionnaire.

        Args:
            user (str): API username.
            password (str): API password.
            survey_id (str): Survey ID.
            verbose (bool): If True, INFO logs are printed; otherwise, only ERROR logs are shown.

        Returns:
            Optional[int]: The version number of the questionnaire or None if not found.

        Raises:
            Exception: For connection errors, authentication failures, or other API issues.
        """
        self.user = user
        self.password = password
        self.survey_id = survey_id
        self.session = requests.Session()

        # Configure logging based on verbosity
        logging.basicConfig(
            level=logging.INFO if verbose else logging.ERROR,
            format='%(levelname)s - %(message)s',
        )

        def __request_api() -> requests.Response:
            """
            Helper function to send API requests and handle the response.

            Returns:
                requests.Response: API response object.

            Raises:
                Exception: If access token retrieval fails or response status is not 200.
            """
            # Get access token
            headers_token = {'accept': '*/*', 'Content-Type': 'application/json'}
            data_token = (
                '{"username":' + f'"{self.user}",'
                f'"password":"{self.password}",'
                '"refresh_token":""}'
            )
            response_token = requests.post(
                'https://sistema.solvis.net.br/api/v1/oauth/token',
                headers=headers_token,
                data=data_token,
            )

            if response_token.status_code != 200:
                raise Exception('Authentication failed. Check username/password.')

            try:
                self.access_token = response_token.json()['access_token']
            except KeyError:
                raise Exception('Failed to retrieve access token. Check credentials.')

            # Request questionnaire data
            headers = {'accept': '*/*', 'Authorization': f'Bearer {self.access_token}'}
            return self.session.get(
                f'https://sistema.solvis.net.br/api/v1/surveys/{self.survey_id}',
                headers=headers,
            )

        try:
            response = __request_api()
            if response.status_code != 200:
                raise Exception(
                    f'Error fetching questionnaire version: {response.status_code}'
                )

            data = response.json()
            if 'error' in data:
                raise Exception(f"API error: {data['error']}")

            # Extract version
            questionnaire_data = data.get('data', {})
            version = questionnaire_data.get('questionnaire', {}).get('version')
            if version is None:
                logging.info('No version information found for the questionnaire.')
                return None

            return version
        except Exception as e:
            logging.error(f'An error occurred: {e}')

        return None
