import logging

import allure
import requests
from requests import Response, ReadTimeout

from mecher_base_api_client.utils import decorator_for_allure_attach, is_valid_json


class API:
    def __init__(self, url: str, timeout: int = 20, default_status_codes: tuple = (200,)):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f'Init ApiClient url={url}')

        self.url = url
        self.timeout = timeout

        self.default_headers_set = {}
        self.default_status_codes = default_status_codes

        self.session = requests.Session()

    @staticmethod
    def join_headers_sets(header_set_one, header_set_two) -> dict:
        header_set_one_keys_lower = {k.lower(): v for k, v in (header_set_one or {}).items()}
        header_set_two_keys_lower = {k.lower(): v for k, v in (header_set_two or {}).items()}
        return header_set_one_keys_lower | header_set_two_keys_lower

    def _build_request_headers(self, headers):
        """
        Method for join and update headers with default headers
        """
        return self.join_headers_sets(self.default_headers_set, headers)

    def assert_status_code_and_errors(self, response: Response):
        with allure.step("Main asserts response"):
            if response.text == 'null':
                response_text = ''
            elif response.text and is_valid_json(response.text):
                response_text = response.json()
            else:
                response_text = ''

            with allure.step(f"Check response code is in {self.default_status_codes}"):
                assert response.status_code in self.default_status_codes, \
                    f'response code {response.status_code} is not in allowed code list {self.default_status_codes} ' \
                    f'{response_text}'

            if response.text and is_valid_json(response.text):
                with allure.step("Check there is no 'error' in response"):
                    assert "error" not in response_text, \
                        f'There is an "error" in response:\n{response_text} \n' \
                        f'URL: {response.url}'

    @decorator_for_allure_attach
    def _request(self, method: str, url: str, **kwargs):
        request_headers = self._build_request_headers(headers=kwargs.get('headers'))
        kwargs.update(headers=request_headers)

        # https://requests.readthedocs.io/en/latest/user/advanced/#timeouts
        resp = self.session.request(method=method, url=url, timeout=(self.timeout, self.timeout), **kwargs)
        return resp

    @staticmethod
    def clear_kwargs_from_arguments(kwargs_for_clear: dict, list_keys_to_delete: list) -> dict:
        filtered_kwargs = {k: v for (k, v) in kwargs_for_clear.items() if k not in list_keys_to_delete}
        return filtered_kwargs

    def send_request_base(self,
                          url: str = None,
                          method: str = 'post',
                          body=None,
                          assert_response: bool = True,
                          **kwargs):
        request_url = url if url else self.url
        endpoint = body.get('name', url) if isinstance(body, dict) else url

        try:
            logging.info(f'Endpoint:/{endpoint}/, Method:{method.upper()}, kwargs:{kwargs}')

            response: requests.Response = self._request(method=method.lower(),
                                                        url=request_url,
                                                        json=body,
                                                        **kwargs)
            if assert_response:
                self.assert_status_code_and_errors(response)

            return response
        except ReadTimeout:
            raise ReadTimeout(f'Connection establishment time, limit value exceeded: {self.timeout} s.')
