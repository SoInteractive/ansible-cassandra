<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cassandra_logo.svg/1280px-Cassandra_logo.svg.png" alt="cassandra logo" title="cassandra" align="right" height="60" /></p>

Ansible Role: cassandra
=======================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-cassandra.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-cassandra) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.cassandra-blue.svg)](https://galaxy.ansible.com/SoInteractive/cassandra/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-cassandra.svg)](https://github.com/SoInteractive/ansible-cassandra/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

This role installs Cassandra cluster and metrics exporter

# :warning: IMPORTANT NOTICE

THIS PROJECT IS ABANDONED. WE DO NOT ACCEPT ANY NEW ISSUES AND/OR PULL REQUESTS.

Requirements
------------

Docker must be installed on host system. Due to test requirements those few lines have been commented out from meta/main.yml.

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: cassandra
  become: true
  roles:
    - SoInteractive.cassandra
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- Replication factor in system_auth
