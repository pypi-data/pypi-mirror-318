from unittest.mock import patch

from tg_bw_helper import __main__ as main


def test_vault_entry(sys_patch, fake_bw_path, capsys):
    with sys_patch("--bw-executable", fake_bw_path, "--vault-item", "item2"):
        main.run()

    captured = capsys.readouterr()
    assert captured.out == "pass"


def test_vault_entry_bw_found_automatically(sys_patch, fake_path_environment, fake_which, capsys):
    with sys_patch("--vault-item", "item2"), patch.object(main, "BASE_BW_EXECUTABLE_NAME", "fake-bw.py"):
        main.run()

    captured = capsys.readouterr()
    assert captured.out == "pass"


def test_vault_entry_is_not_existing(sys_patch, fake_bw_path, capsys):
    with sys_patch("--bw-executable", fake_bw_path, "--vault-item", "item3"):
        main.run()

    captured = capsys.readouterr()
    assert captured.out == "masterpassword"


def test_vault_entry_with_field(sys_patch, fake_bw_path, capsys):
    with sys_patch("--bw-executable", fake_bw_path, "--vault-item", "item1", "--vault-item-field", "Legacy ansible"):
        main.run()

    captured = capsys.readouterr()
    assert captured.out == "$ecure"


def test_vault_entry_with_wrong_field(sys_patch, fake_bw_path, capsys):
    with sys_patch("--bw-executable", fake_bw_path, "--vault-item", "item1", "--vault-item-field", "Pizza delivery"):
        main.run()

    captured = capsys.readouterr()
    assert captured.out == "masterpassword"


def test_vault_entry_with_too_broad_query(sys_patch, fake_bw_path, capsys):
    with sys_patch("--bw-executable", fake_bw_path, "--vault-item", "item"):
        main.run()

    captured = capsys.readouterr()
    assert captured.out == "masterpassword"
