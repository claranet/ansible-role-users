#!/usr/bin/env python

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_vim_version(host):
    command = host.run("vim --version")
    assert command.rc == 0


def test_root_user(host):
    user = host.user("root")
    assert user.exists
    assert user.shell == "/bin/bash"
    assert user.home == f"/{user.name}"
    assert user.group == "root"
    assert "adm" in user.groups


def test_root_profile_file(host):
    user_name = "root"
    file_name = f"/{user_name}/.profile"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644
    assert file.contains("\nreadonly HISTFILE\n")
    assert file.contains("\nexport SHELL=/bin/bash\n")
    assert file.contains("\nexport LANG=POSIX\n")


def test_claranet1_user(host):
    user = host.user("claranet1")
    assert user.exists
    assert user.shell == "/bin/bash"
    assert user.home == f"/home/{user.name}"
    assert user.group == "claranet1"


def test_claranet2_user(host):
    user = host.user("claranet2")
    assert user.exists
    assert user.shell == "/bin/bash"
    assert user.home == f"/home/{user.name}"
    assert user.group == "adm"
    assert "daemon" in user.groups


def test_claranet1_profile_file(host):
    user_name = "claranet1"
    file_name = f"/home/{user_name}/.profile"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644
    assert file.contains("\nreadonly HISTFILE\n")
    assert file.contains("\nexport SHELL=/bin/bash\n")


def test_claranet1_bash_history_file(host):
    user_name = "claranet1"
    file_name = f"/home/{user_name}/.bash_history"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == user_name
    assert file.group == user_name
    assert file.mode == 0o600
    assert "a" in host.check_output(f"lsattr {file_name}")[:19]


def test_claranet1_bashrc_file(host):
    user_name = "claranet1"
    file_name = f"/home/{user_name}/.bashrc"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == user_name
    assert file.group == user_name
    assert file.mode == 0o600
    assert file.contains('\nalias gc="git commit"\n')


def test_claranet1_vimrc_file(host):
    user_name = "claranet1"
    file_name = f"/home/{user_name}/.vimrc"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == user_name
    assert file.group == user_name
    assert file.mode == 0o600
    assert file.contains("\ncolor desert\n")


def test_claranet2_profile_file(host):
    user_name = "claranet2"
    file_name = f"/home/{user_name}/.profile"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644
    assert file.contains("\nreadonly HISTFILE\n")
    assert file.contains("\nexport SHELL=/bin/bash\n")


def test_claranet1_ssh_pubkeys(host):
    user_name = "claranet1"
    file_name_public = f"/home/{user_name}/.ssh/id_rsa.pub"
    file_name_private = f"/home/{user_name}/.ssh/id_rsa"
    file_public = host.file(file_name_public)
    file_private = host.file(file_name_private)
    assert file_public.exists
    assert file_public.is_file
    assert file_public.user == "claranet1"
    assert file_public.group == "claranet1"
    assert file_public.mode == 0o600
    assert file_public.contains("xxxpublic")
    assert file_private.exists
    assert file_private.is_file
    assert file_private.user == "claranet1"
    assert file_private.group == "claranet1"
    assert file_private.mode == 0o600
    assert file_private.contains("xxxprivate")


def test_claranet2_bash_history_file(host):
    user_name = "claranet2"
    file_name = f"/home/{user_name}/.bash_history"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == user_name
    assert file.group == "adm"
    assert file.mode == 0o600
    assert "a" in host.check_output(f"lsattr {file_name}")[:19]


def test_installed_packages(host):
    assert host.package("bash").is_installed
    assert host.package("bash-completion").is_installed
    if str(host.system_info.distribution).lower() in ("centos", "redhat", "amzn"):
        assert host.package("vim-enhanced").is_installed
    else:
        assert host.package("vim").is_installed
    assert host.package("e2fsprogs").is_installed


def test_tbd_user(host):
    user = host.user("tbd")
    assert not user.exists


def test_tbd_home(host):
    user_name = "tbd"
    file_name = f"/home/{user_name}"
    file = host.file(file_name)
    assert file.exists
    assert file.is_directory
