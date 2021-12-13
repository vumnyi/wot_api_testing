import allure
import pytest
import requests
from assertpy import soft_assertions, assert_that

from data.login_response_model import LoginResponse
from data.response_error import ResponseError

# test data
TEST_URL = 'https://api.worldoftanks.eu/wot/auth/login/'

APPLICATION_ID = '665706907130c05ec28aa85c64eb6589'

URL = 'https://eu.wargaming.net/id/openid/'
REDIRECT_URI = 'https://developers.wargaming.net/reference/all/wot/auth/login/'

SEARCH_NOT_SPECIFIED = ('', 402, 'application_id', 'APPLICATION_ID_NOT_SPECIFIED')


@allure.feature('Checking valid response')
def test_valid_response():
    response = requests.get(TEST_URL, data={'application_id': APPLICATION_ID,
                                            'redirect_uri': REDIRECT_URI,
                                            'nofollow': 1}).json()
    login_response = LoginResponse(**response)
    login_response.data.location = login_response.data.location.replace('%252F', '/').replace('%253A', ':')
    with soft_assertions():
        assert_that(login_response.meta.count).is_equal_to(1)
        assert_that(login_response.data.location).contains(URL)
        assert_that(login_response.data.location).contains(REDIRECT_URI)


@pytest.mark.parametrize('application_id, error_code, field, error_text', [SEARCH_NOT_SPECIFIED])
@allure.feature('Checking errors')
def test_errors(application_id, error_code, field, error_text):
    response = requests.get(TEST_URL, data={'application_id': application_id, 'redirect_uri': REDIRECT_URI}).json()
    player_response_error = ResponseError(**response)
    with soft_assertions():
        assert_that(player_response_error.status).is_equal_to('error')
        assert_that(player_response_error.error.code).is_equal_to(error_code)
        assert_that(player_response_error.error.field).is_equal_to(field)
        assert_that(player_response_error.error.message).is_equal_to(error_text)
