import os
import sys
from unittest import mock
import pytest

import tg_bw_helper
from tg_bw_helper import KeyStorage

if not sys.platform.startswith("linux"):
    pytest.skip("skipping linux-only tests", allow_module_level=True)
else:
    from tg_bw_helper.keystorage.linux import LinuxKernelKeyStorage  # noqa


def fake_get_pass(*args, **kwargs):
    return "secret"


@mock.patch.dict(os.environ, {**os.environ, "TG_BW_SESSION_SECRET_NAME": "TG_BW_TESTS_SECRET"}, clear=True)
@mock.patch("getpass.getpass", new=fake_get_pass)
def test_session_from_keystorage(fake_bw_path):
    assert tg_bw_helper.get_bw_session(fake_bw_path) == "SESSION_TOKEN"
    assert KeyStorage.get_storage().get() == "SESSION_TOKEN"

    with mock.patch("tg_bw_helper.bw_client.get_bw_session_interactive") as get_bw_session_interactive:
        assert tg_bw_helper.get_bw_session(fake_bw_path) == "SESSION_TOKEN"
        assert get_bw_session_interactive.call_count == 0


@mock.patch("getpass.getpass", new=fake_get_pass)
def test_session_from_keystorage_invalid_secret_name(fake_bw_path):
    def get_secret_name(*args, **kwargs):
        return "\0"

    with mock.patch("tg_bw_helper.keystorage.linux.LinuxKernelKeyStorage.get_secret_name", new=get_secret_name):
        assert tg_bw_helper.get_bw_session(fake_bw_path) == "SESSION_TOKEN"
        assert KeyStorage.get_storage().get() is None


@mock.patch.dict(os.environ, {**os.environ, "TG_BW_SESSION_SECRET_NAME": "TG_BW_TESTS_SECRET"}, clear=True)
@mock.patch("getpass.getpass", new=fake_get_pass)
def test_session_from_keystorage_garbage_data(fake_bw_path):
    import python_linux_keyutils

    python_linux_keyutils.set_secret("TG_BW_TESTS_SECRET", bytes([0xD8, 0x01, 0xDF, 0xFE]))
    assert KeyStorage.get_storage().get() is None

    assert tg_bw_helper.get_bw_session(fake_bw_path) == "SESSION_TOKEN"
    assert KeyStorage.get_storage().get() == "SESSION_TOKEN"
