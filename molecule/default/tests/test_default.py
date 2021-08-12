#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_vim_version(host):
  command = host.run('vim --version')
  assert command.rc == 0

def test_claranet1_user(host):
  user = host.user('claranet1')
  assert user.exists
  assert user.shell == '/bin/bash'
  assert user.home == f'/home/{user.name}'
  assert user.group == 'claranet1'

def test_claranet2_user(host):
  user = host.user('claranet2')
  assert user.exists
  assert user.shell == '/bin/bash'
  assert user.home == f'/home/{user.name}'
  assert user.group == 'adm'
  assert 'daemon' in user.groups

def test_claranet1_profile_file(host):
  user_name = 'claranet1'
  file_name = f'/home/{user_name}/.profile'
  file = host.file(file_name)
  assert file.exists
  assert file.is_file
  assert file.user == 'root'
  assert file.group == 'root'
  assert file.mode == 0o644

def test_claranet1_bash_history_file(host):
  user_name = 'claranet1'
  file_name = f'/home/{user_name}/.bash_history'
  file = host.file(file_name)
  assert file.exists
  assert file.is_file
  assert file.user == user_name
  assert file.group == user_name
  assert file.mode == 0o644
  assert 'a' in host.check_output(f'lsattr {file_name}')[:19]

def test_claranet2_profile_file(host):
  user_name = 'claranet2'
  file_name = f'/home/{user_name}/.profile'
  file = host.file(file_name)
  assert file.exists
  assert file.is_file
  assert file.user == 'root'
  assert file.group == 'root'
  assert file.mode == 0o644

def test_claranet2_bash_history_file(host):
  user_name = 'claranet2'
  file_name = f'/home/{user_name}/.bash_history'
  file = host.file(file_name)
  assert file.exists
  assert file.is_file
  assert file.user == user_name
  assert file.group == 'adm'
  assert file.mode == 0o644
  assert 'a' in host.check_output(f'lsattr {file_name}')[:19]

