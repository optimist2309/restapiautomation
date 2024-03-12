import requests
import pytest
from utils.envParser import *


def test_create_token():
    url = get_nv_value()['API']['base_url'] + get_nv_value()['API']['auth_uri']
    user_name = get_nv_value()['API']['user_name']
    password = get_nv_value()['API']['password']
    payload = {"username": user_name, "password": password}
    resp = requests.post(url=url, json=payload)
    resp_dict = resp.json()
    assert resp.status_code == 200
    assert "token" in resp_dict


def test_not_able_to_create_token():
    url = get_nv_value()['API']['base_url'] + get_nv_value()['API']['auth_uri']
    user_name = get_nv_value()['API']['user_name']
    password = ""
    payload = {"username": user_name, "password": password}
    resp = requests.post(url=url, json=payload)
    resp_dict = resp.json()
    assert resp.status_code == 200
    assert "reason" in resp_dict
    assert resp_dict['reason'] == 'Bad credentials'


def test_not_able_to_create_token_2():
    url = get_nv_value()['API']['base_url'] + get_nv_value()['API']['auth_uri']
    user_name = ""
    password = password = get_nv_value()['API']['password']
    payload = {"username": user_name, "password": password}
    resp = requests.post(url=url, json=payload)
    resp_dict = resp.json()
    assert resp.status_code == 200
    assert "reason" in resp_dict
    assert resp_dict['reason'] == 'Bad credentials'


def test_not_able_to_create_token_3():
    url = get_nv_value()['API']['base_url'] + get_nv_value()['API']['auth_uri']
    user_name = get_nv_value()['API']['user_name_2']
    password = password = get_nv_value()['API']['password_2']
    payload = {"username": user_name, "password": password}
    resp = requests.post(url=url, json=payload)
    resp_dict = resp.json()
    assert resp.status_code == 200
    assert "reason" in resp_dict
    assert resp_dict['reason'] == 'Bad credentials'


def test_not_able_to_create_token_4():
    url = get_nv_value()['API']['base_url'] + get_nv_value()['API']['auth_uri']
    user_name = ""
    password = ""
    payload = {"username": user_name, "password": password}
    resp = requests.post(url=url, json=payload)
    resp_dict = resp.json()
    assert resp.status_code == 200
    assert "reason" in resp_dict
    assert resp_dict['reason'] == 'Bad credentials'
