import logging
import os
from json import dumps
from typing import Union

import allure
from requests import Response


def attach_response_with_limit_size(response: Union[Response, dict],
                                    attachment_name: str):
    # By default response attachment limit = 40KB
    attachment_size_limit = int(os.environ.get('RESPONSE_ATTACHMENT_SIZE_LIMIT_KB', 40))

    if isinstance(response, Response):
        attachment_data = dumps(response.json(), indent=2, ensure_ascii=False)
    else:
        attachment_data = dumps(response, indent=2, ensure_ascii=False)

    attachment_type = allure.attachment_type.JSON

    if len(attachment_data) > attachment_size_limit * 1024:
        attachment_name = f'Limited to {attachment_size_limit}KB ' + attachment_name
        attachment_type = allure.attachment_type.TEXT
        attachment_data = \
            attachment_data[:attachment_size_limit * 1024] + f'\n!!! LIMITED to {attachment_size_limit}KB'

    allure.attach(attachment_data, attachment_name, attachment_type)


def decorator_for_allure_attach(base_function):
    def wrapper(self, method, url, **kwargs):
        with allure.step("Request"):
            # request headers
            request_headers = self._build_request_headers(headers=kwargs.get('headers'))
            allure.attach(dumps(request_headers, indent=2, ensure_ascii=False),
                          f'Headers of {method}-request  to {url}',
                          allure.attachment_type.JSON)

            # Get request params
            get_params = kwargs.get('params')
            if get_params:
                if isinstance(get_params, str):
                    get_params = {'params': get_params}
                elif not isinstance(get_params, dict):
                    get_params = dict(get_params)

                allure.attach(dumps(get_params, indent=2, ensure_ascii=False),
                              f'Params of {method}-request  to {url}',
                              allure.attachment_type.JSON)

            # request body
            if kwargs.get('json'):
                allure.attach(dumps(kwargs.get('json'), indent=2, ensure_ascii=False),
                              f'Body of {method}-request  to {url}',
                              allure.attachment_type.JSON)

        resp: Response = base_function(self, method, url, **kwargs)

        with allure.step("response"):
            logging.info(f'resp: {resp.status_code}')
            # ci/cd could fail if there is too much output (response body is usually huge) --- only for local debug
            logging.debug(f'resp: {resp.status_code} / {resp.content.decode()}')
            try:
                attachment_name = f'response to {method}-request to {url} (status code /{resp.status_code}/)'
                attach_response_with_limit_size(response=resp,
                                                attachment_name=attachment_name)
            except Exception:
                allure.attach(resp.text, f'response to {method}-request to {url} (status code /{resp.status_code}/)',
                              allure.attachment_type.TEXT)
        return resp

    return wrapper


def is_valid_json(text):
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False
