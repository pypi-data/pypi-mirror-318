from http import HTTPMethod
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import logging
from typing import Optional, Dict, Any
from http.client import HTTPResponse

from utils_cws_web.exception.integration_error import Integration_error

class Integration:
    DEFAULT_TIMEOUT = 30  # Default timeout for requests (in seconds)
    MAX_RETRIES = 3  # Maximum number of retries for failed requests

    def __init__(
        self,
        base_url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        timeout: int = DEFAULT_TIMEOUT,
        verify_ssl: bool = True
    ):
        # Initializes the Integrations with base URL, headers, parameters, timeout, and SSL verification flag.
        self.__base_url = base_url.rstrip('/')
        self.__headers = headers or {}
        self.__params = params or {}
        self.__timeout = timeout
        self.__verify_ssl = verify_ssl
        self.__logger = logging.getLogger(__name__)

    def __enter__(self):
        # Allows the use of this class in a context manager (with statement)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Handles exceptions when exiting the context manager and logs errors if necessary.
        if exc_type:
            self.__logger.error(f"Error: {exc_val}")
        return False

    def request(
        self,
        method: HTTPMethod,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        retry_count: int = 0
    ) -> Optional[Dict[str, Any]]:
        # Sends an HTTP request to the specified endpoint with the given method and data.
        url = self._build_url(endpoint, params)
        
        headers = {**self.__headers}
        if data is not None:
            headers['Content-Type'] = 'application/json'
            
        req = urllib.request.Request(
            url,
            headers=headers,
            method=method.value
        )

        if data is not None:
            req.data = json.dumps(data).encode('utf-8')

        try:
            # Creates an SSL context if SSL verification is disabled
            context = None if self.__verify_ssl else ssl._create_unverified_context()
            with urllib.request.urlopen(req, timeout=self.__timeout, context=context) as response:
                return self._handle_response(response)
                
        except urllib.error.HTTPError as e:
            # Retries the request if it's a server error (5xx) and retry count is less than MAX_RETRIES
            if retry_count < self.MAX_RETRIES and 500 <= e.code < 600:
                return self.request(method, endpoint, data, params, retry_count + 1)
            raise Integration_error(f"HTTP Error: {e.code} {e.reason}", e.code)

    def _build_url(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> str:
        # Constructs the full URL by appending the endpoint and URL-encoded parameters
        all_params = {**self.__params, **(params or {})}
        url = f"{self.__base_url}/{endpoint.lstrip('/')}"
        if all_params:
            url = f"{url}?{urllib.parse.urlencode(all_params)}"
        return url

    def _handle_response(self, response: HTTPResponse) -> Dict[str, Any]:
        # Reads and handles the HTTP response, raising an error if the response is empty
        content = response.read()
        if not content:
            raise Integration_error("Empty response")
        return json.loads(content.decode('utf-8'))
