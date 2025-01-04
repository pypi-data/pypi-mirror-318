import logging
import pandas as pd
import requests
from typing import Optional


class GetDevices:
    """
    A class to interact with the devices API and fetch device-related data.
    """

    def __init__(self) -> None:
        """
        Initialize the GetDevices class with default attributes.
        """
        self.user: Optional[str] = None
        self.password: Optional[str] = None
        self.access_token: Optional[str] = None
        self.session: Optional[requests.Session] = None

    def get_devices(
        self, user: str, password: str, verbose: bool = True
    ) -> pd.DataFrame:
        """
        Fetch all devices from the API and return them as a Pandas DataFrame.

        Args:
            user (str): API username.
            password (str): API password.
            verbose (bool): If True, set logging level to INFO; otherwise, set to ERROR.

        Returns:
            pd.DataFrame: A DataFrame containing device information.

        Raises:
            Exception: For connection errors, authentication failures, or other API issues.
        """
        self.user = user
        self.password = password
        self.session = requests.Session()

        # Configure logging based on verbosity
        logging.basicConfig(
            level=logging.INFO if verbose else logging.ERROR,
            format='%(levelname)s - %(message)s',
        )

        def __request_api(page: int) -> requests.Response:
            """
            Helper function to send API requests and handle the response.

            Args:
                page (int): Page number to fetch.

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

            headers = {'accept': '*/*', 'Authorization': f'Bearer {self.access_token}'}
            return self.session.get(
                f'https://sistema.solvis.net.br/api/v1/devices?page={page}',
                headers=headers,
            )

        # Initialize DataFrame and pagination
        devices_df = pd.DataFrame()
        page = 1

        logging.info('Starting device data export...')
        while True:
            try:
                response = __request_api(page)
                if response.status_code != 200:
                    raise Exception(f'Error fetching data: {response.status_code}')

                data = response.json()
                if 'error' in data:
                    raise Exception(f"API error: {data['error']}")

                # Extract and append data
                devices = data.get('data', [])
                if not devices:
                    logging.info(f'Export complete. Total devices: {len(devices_df)}')
                    break

                devices_df = pd.concat(
                    [devices_df, pd.json_normalize(devices)], ignore_index=True
                )
                logging.info(f'Page {page} fetched successfully.')
                page += 1
            except Exception as e:
                logging.error(f'An error occurred: {e}')
                break

        return devices_df
