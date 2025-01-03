import getpass
import os
import pathlib
import sys
from unittest.mock import patch

import pytest

from tg_bw_helper import __main__ as main


@pytest.fixture()
def sys_patch():
    def get_sys_patch(*args):
        return patch.object(sys, "argv", ["__main__.py", *args])

    return get_sys_patch


@pytest.fixture()
def fake_bw_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "fake-bw.py")


@pytest.fixture()
def fake_bw_path_failing_master_password():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fake-bw-failing-master-password.py",
    )


@pytest.fixture()
def fake_bw_path_not_logged_in():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "fake-bw-not-logged-in.py")


@pytest.fixture()
def fake_bw_unknown_error():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "fake-bw-unknown-error.py")


def _fake_getpass(*args, **kwargs):
    return "masterpassword"


@pytest.fixture(autouse=True)
def fake_getpass():
    with patch.object(getpass, "getpass", _fake_getpass):
        yield


def _fake_empty_getpass(*args, **kwargs):
    return ""


@pytest.fixture()
def fake_empty_getpass():
    with patch.object(getpass, "getpass", _fake_empty_getpass):
        yield


@pytest.fixture()
def fake_path_environment(fake_bw_path):
    environ = os.environ.copy()
    environ.update(
        {
            "PATH": ":".join(
                [
                    # Path to the scripts
                    str(pathlib.Path(fake_bw_path).parent.absolute()),
                    # Path to python, that is needed to run which and others
                    str(pathlib.Path(sys.executable).parent.absolute()),
                ]
            )
        }
    )
    with patch.object(
        os,
        "environ",
        environ,
    ):
        yield


@pytest.fixture()
def fake_which():
    with patch.object(main, "WHICH_EXECUTABLE_NAME", "fake-which.py"):
        yield


@pytest.fixture(autouse=True)
def fake_tty(request):
    if "no_fake_tty" in request.keywords:
        yield None
        return
    with patch("sys.stdin.isatty", new=lambda: True):
        yield
