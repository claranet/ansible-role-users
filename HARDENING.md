# Introduction
In this document, a list of relevant settings for hardening users.
This document is non-exhaustive, however, it provides a solid base of security hardening 
measures.

# Bash & Profile

> If you are a root user, you can change the following values. To keep traces, you must install **auditd**.

- The default shell is **/bin/bash** and is locked in the **~/.profile** file (owner and group: root, mode: 0644), so a
  non-root user can't change this.

- The default history file **~/.bash_history** is unwritable (**chattr +a**). 

- The **HISTFILE** variable is in **readonly mode** (see **~/.profile**), so a non-root user can't change this

```bash
# echo "" > .bash_history
-bash: .bash_history: Operation not permitted

# unset HISTFILE
-bash: unset: HISTFILE: cannot unset: readonly variable

# ls -ld ~/.profile
-rw-r--r-- 1 root root 875 Aug 10 11:54 /root/.profile
```

# File permissions

The following files are set up with the following permissions:
- **~/.bashrc**: mode 0600
- **~/bash_history**: chattr +a
- **~/.profile**: mode 0644 but user: root + group: root
- **~/.ssh folder**: mode 0700
- **~/.ssh/authorized_keys**: mode 0600
- **~/.ssh/config**: mode 0600
- **~/.vimrc**: mode: 0600