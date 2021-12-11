import allure
import pytest
import requests
from assertpy import assert_that, soft_assertions

from data.player_response_models import PlayerResponse, PlayerResponseError

TEST_URL = 'https://api.worldoftanks.ru/wot/account/list/?application_id=665706907130c05ec28aa85c64eb6589'


@allure.feature('Checking valid response')
def test_valid_response():
    user_name = 'alibaba'
    response = requests.get(TEST_URL, params={'search': user_name, 'limit': 10}).json()
    player_response = PlayerResponse(**response)
    with soft_assertions():
        assert_that(player_response.status).is_equal_to('ok')
        assert_that(player_response.data[0].nickname.lower()).contains(user_name)


SEARCH_NOT_SPECIFIED = ('', 402, 'SEARCH_NOT_SPECIFIED', '')
NOT_ENOUGH_SEARCH_LENGTH = ('ab', 407, 'NOT_ENOUGH_SEARCH_LENGTH', '')
SEARCH_LIST_LIMIT_EXCEEDED = ('asd,' * 100, 407, 'SEARCH_LIST_LIMIT_EXCEEDED', 'exact')


@pytest.mark.parametrize('search_value, error_code, error_text, search_type', [SEARCH_NOT_SPECIFIED,
                                                                               NOT_ENOUGH_SEARCH_LENGTH,
                                                                               SEARCH_LIST_LIMIT_EXCEEDED])
@allure.feature('Checking errors')
def test_search_errors(search_value, error_code, error_text, search_type):
    response = requests.get(TEST_URL, params={'search': search_value, 'type': search_type}).json()
    player_response_error = PlayerResponseError(**response)
    with soft_assertions():
        assert_that(player_response_error.status).is_equal_to('error')
        assert_that(player_response_error.error.code).is_equal_to(error_code)
        assert_that(player_response_error.error.field).is_equal_to('search')
        assert_that(player_response_error.error.message).is_equal_to(error_text)


@pytest.mark.parametrize('limit, expected_count', [(99, 99), (100, 100), (101, 100)])
@allure.feature('Checking limit parameter')
def test_limits(limit, expected_count):
    response = requests.get(TEST_URL, params={'search': 'Alisa', 'limit': limit}).json()
    player_response = PlayerResponse(**response)
    with soft_assertions():
        assert_that(player_response.meta.count).is_equal_to(expected_count)


@pytest.mark.parametrize('field', ['nickname', 'account_id'])
@allure.feature('Checking excluding field')
def test_exclude_fields(field):
    response = requests.get(TEST_URL, params={'search': 'Alisa', 'fields': f'-{field}', 'limit': 1}).json()
    player_response = PlayerResponse(**response)
    with soft_assertions():
        assert_that(player_response.data[0].__getattribute__(field)).is_equal_to(None)
