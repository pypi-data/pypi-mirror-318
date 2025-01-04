import logging
import pandas as pd
import requests
from typing import Optional


class GetSurveyedUnits:
    """
    A class to fetch and process surveyed units data from an API.
    """

    def __init__(self) -> None:
        """
        Initialize the SurveyedUnitsFetcher class with default attributes.
        """
        self.user: Optional[str] = None
        self.password: Optional[str] = None
        self.access_token: Optional[str] = None
        self.session: Optional[requests.Session] = None

    def _get_access_token(self) -> None:
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

    def get_all_units(
        self, user: str, password: str, verbose: bool = True
    ) -> pd.DataFrame:
        """
        Fetch all surveyed units from the API and return them as a Pandas DataFrame.

        Args:
            user (str): API username.
            password (str): API password.
            verbose (bool): If True, INFO logs are printed; otherwise, only ERROR logs are shown.

        Returns:
            pd.DataFrame: A DataFrame containing surveyed units and their properties.
        """
        self.user = user
        self.password = password
        self.session = requests.Session()

        # Configure logging based on verbosity
        logging.basicConfig(
            level=logging.INFO if verbose else logging.ERROR,
            format='%(levelname)s - %(message)s',
        )

        self._get_access_token()
        headers = {'accept': '*/*', 'Authorization': f'Bearer {self.access_token}'}

        df_units = pd.DataFrame()
        page = 1

        logging.info('Starting export of surveyed units...')
        while True:
            try:
                response = self.session.get(
                    f'https://sistema.solvis.net.br/api/v1/surveyed_units?page={page}',
                    headers=headers,
                )
                if response.status_code != 200:
                    raise Exception(f'Error fetching data: {response.status_code}')

                data = response.json()
                if 'error' in data:
                    raise Exception(f"API error: {data['error']}")

                units = data.get('data', [])
                if not units:
                    logging.info('Export complete!')
                    break

                for unit in units:
                    properties = unit.pop('surveyed_unit_properties', [])
                    unit_df = pd.json_normalize(unit)
                    for prop in properties:
                        try:
                            name = prop['surveyed_unit_property_name']['name']
                            value = prop['surveyed_unit_property_value']['value']
                            unit_df[name] = value
                        except KeyError:
                            continue
                    df_units = pd.concat([df_units, unit_df], ignore_index=True)

                logging.info(f'Page {page} fetched successfully.')
                page += 1
            except Exception as e:
                logging.error(f'An error occurred: {e}')
                break

        df_units.reset_index(drop=True, inplace=True)
        logging.info(f'Total surveyed units fetched: {len(df_units)}')
        return df_units

    def get_unit_by_id(
        self,
        user: str,
        password: str,
        unit_id: str,
        verbose: bool = True,
    ) -> pd.DataFrame:
        """
        Fetch a specific surveyed unit by ID from the API and return it as a Pandas DataFrame.

        Args:
            user (str): API username.
            password (str): API password.
            unit_id (str): ID of the surveyed unit.
            verbose (bool): If True, INFO logs are printed; otherwise, only ERROR logs are shown.

        Returns:
            pd.DataFrame: A DataFrame containing the surveyed unit and its properties.
        """
        self.user = user
        self.password = password
        self.session = requests.Session()

        # Configure logging based on verbosity
        logging.basicConfig(
            level=logging.INFO if verbose else logging.ERROR,
            format='%(levelname)s - %(message)s',
        )

        self._get_access_token()
        headers = {'accept': '*/*', 'Authorization': f'Bearer {self.access_token}'}

        try:
            response = self.session.get(
                f'https://sistema.solvis.net.br/api/v1/surveyed_units/{unit_id}',
                headers=headers,
            )
            if response.status_code != 200:
                raise Exception(f'Error fetching data: {response.status_code}')

            data = response.json()
            if 'error' in data:
                raise Exception(f"API error: {data['error']}")

            unit = data.get('data', {})
            properties = unit.pop('surveyed_unit_properties', [])
            unit_df = pd.json_normalize(unit)

            for prop in properties:
                try:
                    name = prop['surveyed_unit_property_name']['name']
                    value = prop['surveyed_unit_property_value']['value']
                    unit_df[name] = value
                except KeyError:
                    continue

            logging.info(f'Successfully fetched unit with ID: {unit_id}.')
            return unit_df
        except Exception as e:
            logging.error(f'An error occurred: {e}')

        return pd.DataFrame()
