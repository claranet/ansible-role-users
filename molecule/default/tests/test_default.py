#!/usr/bin/env python

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_vim_version(host):
  command = host.run('vim --version')
  assert command.rc == 0

def test_claranet_user(host):
  user = host.user('claranet')
  assert user.exists
  assert user.shell == '/bin/bash'
  assert user.home == '/home/claranet'
  assert user.group == 'adm'
