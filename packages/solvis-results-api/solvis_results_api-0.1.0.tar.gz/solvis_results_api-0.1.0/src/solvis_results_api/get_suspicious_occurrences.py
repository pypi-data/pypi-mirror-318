import logging
import pandas as pd
import requests
from typing import Optional


class GetSuspiciousOccurrences:
    """
    A class to fetch and process suspicious occurrences from an API.
    """

    def __init__(self) -> None:
        """
        Initialize the GetSuspiciousOccurrences class with default attributes.
        """
        self.user: Optional[str] = None
        self.password: Optional[str] = None
        self.access_token: Optional[str] = None
        self.session: Optional[requests.Session] = None
        self.page: int = 1

    def get_suspicious_occurrences(
        self, user: str, password: str, verbose: bool = True
    ) -> pd.DataFrame:
        """
        Fetch all suspicious occurrences from the API and return them as a Pandas DataFrame.

        Args:
            user (str): API username.
            password (str): API password.
            verbose (bool): If True, INFO logs are printed; otherwise, only ERROR logs are shown.

        Returns:
            pd.DataFrame: A DataFrame containing suspicious occurrences.

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

            # Fetch data for the given page
            headers = {'accept': '*/*', 'Authorization': f'Bearer {self.access_token}'}
            return self.session.get(
                f'https://sistema.solvis.net.br/api/v1/suspicious_occurrences?page={page}',
                headers=headers,
            )

        # Initialize DataFrame and pagination
        df_temp = pd.DataFrame()

        logging.info('Starting export of suspicious occurrences...')
        while True:
            try:
                response = __request_api(self.page)
                if response.status_code != 200:
                    raise Exception(f'Error fetching data: {response.status_code}')

                data = response.json()
                if 'error' in data:
                    raise Exception(f"API error: {data['error']}")

                # Extract data
                occurrences = data.get('data', [])
                if not occurrences:
                    logging.info('Export complete!')
                    break

                df_occurrences = pd.json_normalize(occurrences)
                df_temp = pd.concat([df_temp, df_occurrences], ignore_index=True)

                logging.info(f'Page {self.page} fetched successfully.')
                self.page += 1
            except Exception as e:
                logging.error(f'An error occurred: {e}')
                break

        df_temp.reset_index(drop=True, inplace=True)
        logging.info(f'Total suspicious occurrences fetched: {len(df_temp)}')
        return df_temp
