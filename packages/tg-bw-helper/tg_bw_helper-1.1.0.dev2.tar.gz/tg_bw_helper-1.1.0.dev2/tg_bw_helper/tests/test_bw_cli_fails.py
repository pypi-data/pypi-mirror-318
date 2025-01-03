from tg_bw_helper import __main__ as main


def test_bw_does_not_exist(sys_patch, fake_bw_path, capsys):
    with sys_patch("--bw-executable", f"{fake_bw_path}--fake", "--vault-item", "item2"):
        main.run()

    captured = capsys.readouterr()
    # This comes directly from user input, in our case from fake_getpass, which is used after master password fails
    # three times
    assert captured.out == "masterpassword"
    assert "Max retries exceeded" not in captured.err


def test_bw_not_found_automatically(sys_patch, fake_path_environment, fake_which, capsys):
    with sys_patch("--vault-item", "item2"):
        main.run()

    captured = capsys.readouterr()
    # This comes directly from user input, in our case from fake_getpass, which is used after master password fails
    # three times
    assert captured.out == "masterpassword"
    assert "Max retries exceeded" not in captured.err


def test_bw_empty_master_password(sys_patch, fake_bw_path_failing_master_password, fake_empty_getpass, capsys):
    with sys_patch("--bw-executable", fake_bw_path_failing_master_password, "--vault-item", "item2"):
        main.run()

    captured = capsys.readouterr()
    # This comes directly from user input, in our case from fake_getpass, which is used after master password fails
    # three times
    assert captured.out == ""
    assert "Max retries exceeded" not in captured.err
    assert "Empty master password" in captured.err


def test_bw_master_password_fails(sys_patch, fake_bw_path_failing_master_password, capsys):
    with sys_patch("--bw-executable", fake_bw_path_failing_master_password, "--vault-item", "item2"):
        main.run()

    captured = capsys.readouterr()
    # This comes directly from user input, in our case from fake_getpass, which is used after master password fails
    # three times
    assert captured.out == "masterpassword"
    assert "Max retries (3) exceeded" in captured.err


def test_bw_not_logged_in(sys_patch, fake_bw_path_not_logged_in, capsys):
    with sys_patch("--bw-executable", fake_bw_path_not_logged_in, "--vault-item", "item2"):
        main.run()

    captured = capsys.readouterr()
    # This comes directly from user input, in our case from fake_getpass, which is used after master password fails
    # three times
    assert captured.out == "masterpassword"
    assert "Use `bw login`" in captured.err


def test_bw_unknown_error(sys_patch, fake_bw_unknown_error, capsys):
    with sys_patch("--bw-executable", fake_bw_unknown_error, "--vault-item", "item2"):
        main.run()

    captured = capsys.readouterr()
    # This comes directly from user input, in our case from fake_getpass, which is used after master password fails
    # three times
    assert captured.out == "masterpassword"
