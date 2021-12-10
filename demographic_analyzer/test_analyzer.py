import pytest

import analyzer


@pytest.fixture(scope='module')
def demographic_data():
    return analyzer.calculate_demographic_data(print_data=False)


def test_race_count(demographic_data):
    actual = demographic_data['race_count'].tolist()
    assert actual == [27816, 3124, 1039, 311, 271]


def test_average_age_men(demographic_data):
    assert demographic_data['average_age_men'] == 39.4


def test_percentage_bachelors(demographic_data):
    assert demographic_data['percentage_bachelors'] == 16.4


def test_higher_education_rich(demographic_data):
    assert demographic_data['higher_education_rich'] == 46.5


def test_lower_education_rich(demographic_data):
    assert demographic_data['lower_education_rich'] == 17.4


def test_min_work_hours(demographic_data):
    assert demographic_data['min_work_hours'] == 1


def test_rich_percentage(demographic_data):
    assert demographic_data['rich_percentage'] == 10


def test_highest_earning_country(demographic_data):
    assert demographic_data['highest_earning_country'] == "Iran"


def test_highest_earning_country_percentage(demographic_data):
    assert demographic_data['highest_earning_country_percentage'] == 41.9


def test_top_in_occupation(demographic_data):
    assert demographic_data['top_IN_occupation'] == 'Prof-specialty'
