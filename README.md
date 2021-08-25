# Ansible role - users
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-users?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-users?style=flat-square)](https://github.com/claranet/ansible-role-users/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-users/Detectors?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-users/actions?query=workflow%3AMolecule)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/users)

> :star: Star us on GitHub — it motivates us a lot!

Create groups, users and set users's dotfiles.

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.users
```

## :gear: Role variables

### Users
Variable | Default value | Description
---------|---------------|------------
users_default (or users) | **{}** | Create groups, users and enable bashrc, ssh/config, vimrc and profile files

> Please note that we need to chattr -a the .bash_history file in order to manage groups changes !

### Packages
Variable | Default value | Description
---------|---------------|------------
packages | **["bash","bash-completion","vim","e2fsprogs"]** | List of required packages for users

### Global variables
Variable | Default value | Description
---------|---------------|------------
umask | **022** | Default umask for files created by users
lang | **POSIX** | Default lang variable
editor | **vim** | Default editor is vim
ls_options | **--color=auto** | Default ls options

### Dotfiles
Variable | Default value | Description
---------|---------------|------------
user_default_bashrc | defaults/main.yml | Manage .bashrc file content
user_default_vimrc | defaults/main.yml | Manage .vimrc file content
user_default_profile | defaults/main.yml | Manage .profile file content
bashrc_histcontrol | **ignoreboth** |Set HISTCONTROL variable
bashrc_histsize | **5000** | Set HISTSIZE variable
bashrc_histfilesize | **20000** | Set HISTFILESIZE variable
bashrc_histtimeformat | **%d-%m-%y %T** | Set HISTTIMEFORMAT variable
user_bashrc_template | **users/bashrc.j2** | Configures ~/.bashrc
user_ssh_config_template | **users/ssh_config.j2** | Configures ~/.ssh/config
user_vimrc_template | **users/vimrc.j2** | Configures ~/.vimrc
user_profile_template | **users/profile.j2** | Configures ~/.profile

> Dotfiles (bashrc, ssh/config, vimrc, profile) are not enabled by default. You need to defined them explicitly
> in the wanted user. (See example below).

## :arrows_counterclockwise: Dependencies

See [tasks/install.yml](tasks/install.yml).

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  become: true
  become_user: root
  roles:
    - claranet.users
  vars:
    users:
      root:
        home: /root
        group: wheel
        password: "*"
        authorized_keys: ["ssh-rsa xxx"]
        bashrc:
          - 'export PS1=''\[\033[01;31m\]\u\[\033[00m\]@$(hostname -f) \[\033[01;34m\]\w \$\[\033[00m\] '''
        vimrc:
          - "color desert"
        profile: {}
        ssh_config:
          'mysrv*':
            identityFile: /home/user/.ssh/user
        ssh_keys:
          id_rsa:
            public: 'ssh-rsa '
            private: |
              -----BEGIN OPENSSH PRIVATE KEY-----
              b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
              -----END OPENSSH PRIVATE KEY-----
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
