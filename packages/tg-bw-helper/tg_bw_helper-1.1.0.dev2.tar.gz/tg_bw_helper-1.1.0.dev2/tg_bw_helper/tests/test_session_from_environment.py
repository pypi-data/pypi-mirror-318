import os
from unittest import mock

import pytest

import tg_bw_helper


def fake_get_pass(*args, **kwargs):
    return "secret"


@mock.patch.dict(os.environ, {**os.environ, "BW_SESSION": "test"}, clear=True)
@mock.patch("getpass.getpass", new=fake_get_pass)
def test_session_from_environment(fake_bw_path):
    assert tg_bw_helper.get_bw_session(fake_bw_path) == "test"


@mock.patch.dict(os.environ, {**os.environ, "BW_SESSION": ""}, clear=True)
@mock.patch("getpass.getpass", new=fake_get_pass)
def test_session_from_empty_environment(fake_bw_path):
    assert tg_bw_helper.get_bw_session(fake_bw_path) == "SESSION_TOKEN"


@pytest.mark.no_fake_tty
@mock.patch.dict(os.environ, {**os.environ, "BW_SESSION": ""}, clear=True)
@mock.patch("getpass.getpass", new=fake_get_pass)
def test_session_from_empty_environment_no_tty(fake_bw_path):
    assert tg_bw_helper.get_bw_session(fake_bw_path) is None
