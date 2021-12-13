import datetime

import allure
import pytest
import requests
from assertpy import soft_assertions, assert_that

from data.prolongate_response_model import ProlongateResponse
from data.response_error import ResponseError

# test data
TEST_URL = 'https://api.worldoftanks.ru/wot/auth/prolongate/'

APPLICATION_ID = '665706907130c05ec28aa85c64eb6589'
access_token = ''
EXPIRES_AT_FIELD = 30000
expires_at_timestamp = datetime.datetime.now() + datetime.timedelta(seconds=EXPIRES_AT_FIELD)
player_account_id = ''

SEARCH_NOT_SPECIFIED = ('', '', 'application_id', 402, 'APPLICATION_ID_NOT_SPECIFIED')
NOT_ENOUGH_SEARCH_LENGTH = ('test' * 50, '', 'application_id', 407, 'INVALID_APPLICATION_ID')
ACCESS_TOKEN_NOT_SPECIFIED = (APPLICATION_ID, '', 'access_token', 402, 'ACCESS_TOKEN_NOT_SPECIFIED')
INVALID_ACCESS_TOKEN = (APPLICATION_ID, 'test', 'access_token', 407, 'INVALID_ACCESS_TOKEN')


@pytest.mark.xfail(reason='access_token НЕ ОПРЕДЕЛЁН')
@allure.feature('Checking valid response')
def test_valid_response():
    response = requests.post(TEST_URL, data={'application_id': APPLICATION_ID,
                                             'access_token': access_token,
                                             'expires_at': EXPIRES_AT_FIELD}).json()
    prolongate_response = ProlongateResponse(**response)
    with soft_assertions():
        assert_that(prolongate_response.data[0].access_token).is_equal_to(access_token)
        assert_that(prolongate_response.data[0].account_id).is_equal_to(player_account_id)
        assert_that(prolongate_response.data[0].expires_at).is_equal_to(expires_at_timestamp)


@pytest.mark.parametrize('application_id, access_token, field, error_code, error_text',
                         [SEARCH_NOT_SPECIFIED, NOT_ENOUGH_SEARCH_LENGTH,
                          ACCESS_TOKEN_NOT_SPECIFIED, INVALID_ACCESS_TOKEN])
@allure.feature('Checking errors')
def test_fields_errors(application_id, access_token, field, error_code, error_text):
    response = requests.post(TEST_URL, data={'application_id': application_id,
                                             'access_token': access_token,
                                             'expires_at': EXPIRES_AT_FIELD}).json()
    prolongate_error_response = ResponseError(**response)
    with soft_assertions():
        assert_that(prolongate_error_response.status).is_equal_to('error')
        assert_that(prolongate_error_response.error.code).is_equal_to(error_code)
        assert_that(prolongate_error_response.error.field).is_equal_to(field)
        assert_that(prolongate_error_response.error.message).is_equal_to(error_text)
