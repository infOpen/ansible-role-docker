# docker

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-docker/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-docker)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-docker/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-docker)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-docker/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-docker/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-docker/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-docker/)
[![Ansible Role](https://img.shields.io/ansible/role/8495.svg)](https://galaxy.ansible.com/infOpen/docker/)

Install and configure Docker package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- Debian Jessie
- Debian Stretch
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Repositories and packages management
#------------------------------------------------------------------------------

# Repositories
docker_repository_update_cache: True
docker_repository_cache_valid_time: 3600
docker_repository_keys_retries: 3
docker_repository_keys_delay: 10
docker_repositories: "{{ _docker_repositories }}"
docker_repositories_keys: "{{ _docker_repositories_keys }}"

# Packages
docker_packages: "{{ _docker_packages }}"
docker_system_dependencies: "{{ _docker_system_dependencies }}"

# Service settings
docker_service_name: 'docker'
docker_service_enabled: True
docker_service_state: 'started'

# Configuration
docker_paths:
  files:
    defaults:
      path: '/etc/default/docker'
    daemon_json:
      path: '/etc/docker/daemon.json'
    systemd_service:
      path: '/lib/systemd/system/docker.service'
  dirs:
    config:
      path: '/etc/docker'
    certs:
      path: '/etc/docker/certs.d'


# Docker registries certificates
#------------------------------------------------------------------------------
docker_registries_certificates: []


# Docker daemon options
#----------------------

docker_daemon_options: "{{ _docker_daemon_options }}"
_docker_daemon_options:
  api-cors-header: ''
  bridge: ''
  bip: ''
  debug: False
  default-gateway: ''
  default-gateway-v6: ''
  cluster-store: ''
  cluster-advertise: ''
  cluster-store-opt: []
  dns: []
  dns-opt: []
  dns-search: []
  default-ulimit: []
  exec-opt: []
  exec-root: '/var/run/docker'
  fixed-cidr: ''
  fixed-cidr-v6: ''
  group: 'docker'
  data-root: '/var/lib/docker'
  hosts: []
  help: False
  icc: True
  insecure-registry: []
  ip: '0.0.0.0'
  ip-forward: True
  ip-masq: True
  iptables: True
  ipv6: False
  log-level: 'info'
  label: []
  log-driver: 'json-file'
  log-opt: []
  mtu: 0
  pidfile: '/var/run/docker.pid'
  registry-mirror: []
  storage-driver: ''
  selinux-enabled: False
  storage-opt: []
  tls: False
  tlsverify: False
  userland-proxy: True
```

### Debian OS family specific vars

``` yaml
# Repositories
_docker_repositories:
  - repo: "deb [arch=amd64] https://download.docker.com/linux/{{ ansible_distribution | lower }} {{ ansible_distribution_release | lower }} stable"

_docker_repositories_keys:
  - keyserver: 'hkp://p80.pool.sks-keyservers.net:80'
    id: '9DC858229FC7DD38854AE2D88D81803C0EBFCD88'

# Packages
_docker_packages:
  - name: 'docker.io*'
    state: 'absent'
  - name: 'docker-engine'
    state: 'absent'
  - name: 'docker-ce'

_docker_system_dependencies:
  - name: 'apt-transport-https'
  - name: 'ca-certificates'
  - name: 'curl'
  - name: 'software-properties-common'
```

### Debian distributions specific vars

``` yaml
_docker_packages:
  - name: 'docker-engine'
    state: 'absent'
  - name: 'docker-ce'
```

## How define registries certificates

Just use the `docker_registries_certificates` with this content structure:
``` yaml
docker_registries_certificates:
  - name: 'foo.bar:8081'
    client_cert: '__x509_client_certificate__'
    client_key: '__client_key__'
    ca_cert: '__ca_certificate__'
```

Each component is optionals. The above example will create this structure, with default paths:
```
|- etc
|   |- docker
|        |- certs.d
|             |- foo.bar:8081
|                  |- ca.crt
|                  |- client.cert
|                  |- client.key
```


## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.docker }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
