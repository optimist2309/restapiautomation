import requests
import pytest
from utils.envParser import *


def test_health_check():
    url = get_nv_value()['API']['base_url'] + get_nv_value()['API']['health_uri']
    resp = requests.get(url=url)
    assert resp.status_code == 201
