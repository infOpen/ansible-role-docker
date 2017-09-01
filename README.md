# docker

[![Build Status](https://travis-ci.org/infOpen/ansible-role-docker.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-docker)

Install docker package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Default variables for Debian family repository management
docker_apt_repo_key_server: 'hkp://p80.pool.sks-keyservers.net:80'
docker_apt_repo_key_id: '58118E89F3A912897C070ADBF76221572C52609D'
docker_apt_repo_file_content: "{{
  'deb https://apt.dockerproject.org/repo '
  ~ (ansible_distribution | lower ) ~ '-'
  ~ (ansible_distribution_release | lower) ~ ' main' }}"

# Sometimes, key servers respond slowly, add delay and retry
docker_apt_repo_key_retries: 3
docker_apt_repo_key_delay: 10

# Packages to remove before install docker, overwrite default role
# docker_default_packages_to_remove variable
docker_packages_to_remove: "{{ docker_default_packages_to_remove }}"

# Packages to install, overwrite default role docker_default_packages_to_install
# variable
docker_packages_to_install: "{{ docker_default_packages_to_install }}"
docker_packages_to_install_state: 'present'

# Service settings
docker_service_name: 'docker'
docker_service_enabled: True
docker_service_state: 'started'

# Configuration
docker_configuration_file_dest: '/etc/default/docker'
docker_configuration_file_mode: '0644'
docker_configuration_file_owner: 'root'
docker_configuration_file_group: 'root'
docker_configuration_binary_file: ''
docker_temporary_files_path: ''

# Docker daemon options
#----------------------

# Set CORS headers in the remote API
docker_daemon_option_api_cors_header: ''

# Attach containers to a network bridge
docker_daemon_option_bridge: ''

# Specify network bridge IP
docker_daemon_option_bip: ''

# Enable debug mode
docker_daemon_option_debug: False

# Container default gateway IPv4 address
docker_daemon_option_default_gateway: ''

# Container default gateway IPv6 address
docker_daemon_option_default_gateway_v6: ''

# URL of the distributed storage backend
docker_daemon_option_cluster_store: ''

# Address of the daemon instance on the cluster
docker_daemon_option_cluster_advertise: ''

# Set cluster options (dict array)
docker_daemon_option_cluster_store_opt: []

# DNS server to use
docker_daemon_option_dns: []

# DNS options to use
docker_daemon_option_dns_opt: []

# DNS search domains to use
docker_daemon_option_dns_search: []

# Set default ulimit settings for containers
docker_daemon_option_default_ulimit: []

# Exec driver to use
docker_daemon_option_exec_driver: ''

# Set exec driver options
docker_daemon_option_exec_opt: []

# Root of the Docker execdriver
docker_daemon_option_exec_root: '/var/run/docker'

# IPv4 subnet for fixed IPs
docker_daemon_option_fixed_cidr: ''

# IPv6 subnet for fixed IPs
docker_daemon_option_fixed_cidr_v6: ''

# Group for the unix socket
docker_daemon_option_group: 'docker'

# Root of the Docker runtime
docker_daemon_option_graph: '/var/lib/docker'

# Daemon socket(s) to connect to
docker_daemon_option_host: []

# Print usage
docker_daemon_option_help: False

# Enable inter-container communication
docker_daemon_option_icc: True

# Enable insecure registry communication
docker_daemon_option_insecure_registry: []

# Default IP when binding container ports
docker_daemon_option_ip: '0.0.0.0'

# Enable net.ipv4.ip_forward
docker_daemon_option_ip_forward: True

# Enable IP masquerading
docker_daemon_option_ip_masq: True

# Enable addition of iptables rules
docker_daemon_option_iptables: True

# Enable IPv6 networking
docker_daemon_option_ipv6: False

# Set the logging level
docker_daemon_option_log_level: 'info'

# Set key: value labels to the daemon
docker_daemon_option_label: []

# Default driver for container logs
docker_daemon_option_log_driver: 'json-file'

# Log driver specific options
docker_daemon_option_log_opt: []

# Set the containers network MTU
docker_daemon_option_mtu: 0

# Do not contact legacy registries
docker_daemon_option_disable_legacy_registry: False

# Path to use for daemon PID file
docker_daemon_option_pidfile: '/var/run/docker.pid'

# Preferred Docker registry mirror
docker_daemon_option_registry_mirror: []

# Storage driver to use
docker_daemon_option_storage_driver: ''

# Enable selinux support
docker_daemon_option_selinux_enabled: False

# Set storage driver options
docker_daemon_option_storage_opt: []

# Use TLS; implied by --tlsverify
docker_daemon_option_tls: False

# Trust certs signed only by this CA
docker_daemon_option_tlscacert: ''

# Path to TLS certificate file
docker_daemon_option_tlscert: ''

# Path to TLS key file
docker_daemon_option_tlskey: ''

# Use TLS and verify the remote
docker_daemon_option_tlsverify: False

# Use userland proxy for loopback traffic
docker_daemon_option_userland_proxy: True
```

### Debian dstributions specific vars

``` yaml
# Packages to remove before install
docker_default_packages_to_remove:
  - 'lxc-docker*'
  - 'docker.io*'

# Packages to install
docker_default_packages_to_install:
  - 'docker-engine'
```

### Ubuntu dstributions specific vars

``` yaml
# Packages to remove before install
docker_default_packages_to_remove:
  - 'docker.io*'

# Packages to install
docker_default_packages_to_install:
  - 'docker-engine'
  - "linux-image-extra-{{ ansible_kernel }}"
  - 'apparmor'
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
