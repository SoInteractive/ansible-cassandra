<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cassandra_logo.svg/1280px-Cassandra_logo.svg.png" alt="cassandra logo" title="cassandra" align="right" height="60" /></p>

Ansible Role: cassandra
=======================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/cassandra/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fcassandra/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18249.svg)](https://galaxy.ansible.com/SoInteractive/cassandra/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

This role installs Cassandra cluster and metrics exporter

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: cassandra
  become: true
  roles:
    - SoInteractive.java
    - SoInteractive.cassandra
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- Tests, tests, tests
- Test clustering
- Test credential changing
