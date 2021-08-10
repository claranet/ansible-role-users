# Ansible role - users
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-red?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-users?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-users?style=flat-square)](https://github.com/claranet/ansible-role-users/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-users/Detectors?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-users/actions?query=workflow%3AMolecule)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/users)

> :star: Star us on GitHub — it motivates us a lot!

Configure system's users

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.users
```

## :gear: Role variables

Variable | Default value | Description
---------|---------------|------------
null     | null          | null       

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - users
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
