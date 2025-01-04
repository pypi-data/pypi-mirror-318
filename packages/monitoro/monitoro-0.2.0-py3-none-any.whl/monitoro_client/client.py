import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from .exceptions import (
    MonitoroAPIError,
    BadRequestError,
    MonitorNotFoundError,
    ServerError,
)


class BaseMonitoro:
    BASE_URL = "https://api.monitoro.app/v1"
    MAX_RETRIES = 3

    def __init__(self, api_token):
        self.api_token = api_token
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json",
            }
        )

    def _extract_single(self, endpoint, payload):
        for attempt in range(self.MAX_RETRIES):
            try:
                response = self.session.post(endpoint, json=payload)
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 400:
                    raise BadRequestError(f"Bad request: {response.text}")
                elif response.status_code == 404:
                    raise MonitorNotFoundError(f"Monitor or template not found: {response.text}")
                elif response.status_code == 500:
                    raise ServerError(f"Server error: {response.text}")
                else:
                    raise MonitoroAPIError(
                        f"API request failed with status code {response.status_code}: {response.text}"
                    )
            except (BadRequestError, MonitorNotFoundError):
                raise
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    raise MonitoroAPIError(
                        f"Failed after {self.MAX_RETRIES} attempts: {str(e)}"
                    )

    def _extract_multiple(self, endpoint, payload, urls):
        successful_extractions = []
        failed_urls = []

        with tqdm(total=len(urls), desc="Extracting data") as pbar:
            for url in urls:
                try:
                    payload['url'] = url
                    data = self._extract_single(endpoint, payload)
                    successful_extractions.append((url, data))
                    yield url, data
                except Exception as e:
                    failed_urls.append((url, str(e)))
                finally:
                    pbar.update(1)

        return successful_extractions, failed_urls


class Monitoro(BaseMonitoro):
    def extract(self, monitor=None, template=None, selectors=None, url=None, urls=None, no_ingest=False):
        """
        Extract data from URLs using a specific monitor's settings, a template, or selectors.

        Args:
            monitor (str, optional): The ID of the monitor to use for extraction.
            template (str, optional): The ID of the template to use for extraction.
            selectors (dict, optional): The selectors to use for extraction.
            url (str, optional): The URL to extract data from.
            urls (list, optional): The list of URLs to extract data from.
            no_ingest (bool, optional): If True, skip running automations. Defaults to False.

        Returns:
            generator: A generator that yields (url, data) tuples for successful extractions,
                       followed by a list of (url, error) tuples for failed extractions.
        """
        if sum(1 for param in (monitor, template, selectors) if param is not None) != 1:
            raise ValueError("Exactly one of monitor, template, or selectors must be provided")

        if url is not None and urls is not None:
            raise ValueError("Only one of url or urls should be provided")

        if url is not None:
            urls = [url]
        elif urls is None:
            raise ValueError("Either url or urls must be provided")

        if monitor:
            endpoint = f"{self.BASE_URL}/monitors/{monitor}/extract"
            payload = {"noIngest": no_ingest}
        elif template:
            endpoint = f"{self.BASE_URL}/templates/extract"
            payload = {"templateId": template}
        else:  # selectors
            endpoint = f"{self.BASE_URL}/herd/extract"
            payload = {"selectors": selectors}

        return self._extract_multiple(endpoint, payload, urls)


class MonitoroSwarm(BaseMonitoro):
    def __init__(self, api_tokens):
        super().__init__(api_tokens[0])
        self.api_tokens = api_tokens
        self.current_token_index = 0

    def _get_next_token(self):
        token = self.api_tokens[self.current_token_index]
        self.current_token_index = (self.current_token_index + 1) % len(self.api_tokens)
        return token

    def _extract_single_swarm(self, args):
        endpoint, payload, url = args
        token = self._get_next_token()
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        payload['url'] = url
        return self._extract_single(endpoint, payload)

    def _extract_multiple_swarm(self, endpoint, payload, urls):
        successful_extractions = []
        failed_urls = []

        with ThreadPoolExecutor(max_workers=len(self.api_tokens)) as executor:
            futures = [
                executor.submit(self._extract_single_swarm, (endpoint, payload.copy(), url))
                for url in urls
            ]
            for future, url in zip(
                tqdm(as_completed(futures), total=len(urls), desc="Extracting data"),
                urls,
            ):
                try:
                    data = future.result()
                    successful_extractions.append((url, data))
                    yield url, data
                except Exception as e:
                    failed_urls.append((url, str(e)))

        return successful_extractions, failed_urls

    def extract(self, template=None, selectors=None, urls=None):
        """
        Extract data from URLs using a template or selectors in a distributed manner.

        Args:
            template (str, optional): The ID of the template to use for extraction.
            selectors (dict, optional): The selectors to use for extraction.
            urls (list): The list of URLs to extract data from.

        Returns:
            generator: A generator that yields (url, data) tuples for successful extractions,
                       followed by a list of (url, error) tuples for failed extractions.
        """
        if (template is None) == (selectors is None):
            raise ValueError("Exactly one of template or selectors must be provided")

        if urls is None:
            raise ValueError("urls must be provided")

        if template:
            endpoint = f"{self.BASE_URL}/templates/extract"
            payload = {"templateId": template}
        else:  # selectors
            endpoint = f"{self.BASE_URL}/herd/extract"
            payload = {"selectors": selectors}

        return self._extract_multiple_swarm(endpoint, payload, urls)
