import pytest

import rasprest
import os

password = open(os.path.expanduser('~/.passwd.txt')).readlines()[0]

@pytest.fixture
def client():
    rasprest.app.config['TESTING'] = True
    client = rasprest.app.test_client()

    return client

def test_reboot_without_auth(client):
    resp = client.get('/reboot')
    assert resp.status_code == 401

def test_reboot_with_auth(client):
    resp = client.get('/reboot?password=%s' % password)
    assert resp.status_code == 200

def test_shutdown_without_auth(client):
    resp = client.get('/shutdown')
    assert resp.status_code == 401

def test_shutdown_with_auth(client):
    resp = client.get('/shutdown?password=%s' % password)
    assert resp.status_code == 200