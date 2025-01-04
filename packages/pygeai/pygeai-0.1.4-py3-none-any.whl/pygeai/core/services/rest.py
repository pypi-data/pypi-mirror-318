import json

import requests as req
import logging

logger = logging.getLogger(__name__)


class ApiService:
    """
    Generic service for interacting with RESTful APIs.

    :param base_url: str - The base URL of the API.
    :param username: str - Optional username for authentication.
    :param password: str - Optional password for authentication.
    :param token: str - Optional token for authentication.
    """

    def __init__(self, base_url, username: str = None, password: str = None, token: str = None):
        self._base_url = base_url
        self._username = username
        self._password = password
        self._token = token

    @property
    def base_url(self):
        return self._base_url

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def token(self):
        return self._token

    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        """
        Sends a GET request to the specified API endpoint.

        :param endpoint: str - The API endpoint to send the request to.
        :param params: dict - Optional query parameters for the request.
        :param headers: dict - Optional headers for the request.
        :return: Response object from the GET request.
        """
        try:
            base_url = self.base_url

            url = f"{base_url}/{endpoint}"

            if self.username and self.password:
                response = req.get(
                    url=url,
                    params=params,
                    auth=(
                        self.username,
                        self.password
                    )
                )
            elif not headers and self.token:
                headers = {
                    "Authorization": f"Bearer {self.token}"
                }
                response = req.get(
                    url=url,
                    params=params,
                    headers=headers
                )
            elif headers:
                response = req.get(
                    url=url,
                    params=params,
                    headers=headers
                )
            else:
                response = req.get(
                    url=url,
                    params=params,
                )
        except Exception as e:
            logger.error(f"Error sending GET request: {e}")
        else:
            return response

    def post(self, endpoint: str, data: dict, headers: dict = None, verify: bool = True):
        """
        Sends a POST request to the specified API endpoint.

        :param endpoint: str - The API endpoint to send the request to.
        :param data: dict - The payload to include in the POST request.
        :param headers: dict - Optional headers for the request.
        :param verify: bool - Whether to verify SSL certificates. Defaults to True.
        :return: Response object from the POST request.
        """
        try:
            base_url = self.base_url
            if not headers:
                headers = {
                    "Authorization": f"Bearer {self.token}"
                }
            else:
                headers["Authorization"] = f"Bearer {self.token}"

            url = f"{base_url}/{endpoint}"

            with req.Session() as session:
                if self.username and self.password:
                    session.auth = (
                        self.username,
                        self.password
                    )
                session.verify = verify

                response = session.post(
                    url=url,
                    json=data,
                    headers=headers
                )
        except Exception as e:
            logger.error(f"Error sending POST request: {e}")
        else:
            return response

    def put(self, endpoint: str, data: dict, headers: dict = None, verify: bool = True):
        """
        Sends a PUT request to the specified API endpoint.

        :param endpoint: str - The API endpoint to send the request to.
        :param data: dict - The payload to include in the PUT request.
        :param headers: dict - Optional headers for the request.
        :param verify: bool - Whether to verify SSL certificates. Defaults to True.
        :return: Response object from the PUT request.
        """
        try:
            base_url = self.base_url
            if not headers:
                headers = {
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/json"
                }
            else:
                headers["Authorization"] = f"Bearer {self.token}"
                headers["Content-Type"] = "application/json"

            url = f"{base_url}/{endpoint}"

            with req.Session() as session:
                if self.username and self.password:
                    session.auth = (
                        self.username,
                        self.password
                    )
                session.verify = verify

                response = session.put(
                    url=url,
                    json=data,
                    headers=headers
                )
        except Exception as e:
            logger.error(f"Error sending PUT request: {e}")
        else:
            return response

    def delete(self, endpoint: str, headers: dict = None, verify: bool = True):
        """
        Sends a DELETE request to the specified API endpoint.

        :param endpoint: str - The API endpoint to send the request to.
        :param headers: dict - Optional headers for the request.
        :param verify: bool - Whether to verify SSL certificates. Defaults to True.
        :return: Response object from the DELETE request.
        """
        try:
            base_url = self.base_url
            if not headers:
                headers = {
                    "Authorization": f"Bearer {self.token}"
                }
            else:
                headers["Authorization"] = f"Bearer {self.token}"

            url = f"{base_url}/{endpoint}"

            with req.Session() as session:
                if self.username and self.password:
                    session.auth = (
                        self.username,
                        self.password
                    )
                session.verify = verify

                response = session.delete(
                    url=url,
                    headers=headers
                )
        except Exception as e:
            logger.error(f"Error sending DELETE request: {e}")
        else:
            return response

