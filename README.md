# docker

[![Build Status](https://travis-ci.org/infOpen/ansible-role-docker.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-docker)

Install docker package.

## Requirements

This role requires Ansible 1.5 or higher, and platform requirements are listed
in the metadata file.

## Role Variables

Follow the possible variables with their default values

### Defaults variables for docker

    # Default variables for Debian family repository management
    # Set these variables into a file to erase default values for debian family
    # Set the path of this file to docker_custom_repository_vars_file variable
    docker_custom_repository_vars_file : False
    docker_apt_repository_key_server: ''
    docker_apt_repository_key_id: ''
    docker_apt_repository_file_content: ''

    # Sometimes, key servers respond slowly, add delay and retry
    docker_apt_repository_key_retries: 3
    docker_apt_repository_key_delay: 10

    # Packages to remove before install docker
    docker_packages_to_remove: False

### Specific OS family vars :

#### Debian family specific vars

    # GPG Key used to authenticate repository and packages
    docker_apt_repository_key_server: 'hkp://p80.pool.sks-keyservers.net:80'
    docker_apt_repository_key_id: '58118E89F3A912897C070ADBF76221572C52609D'

    # Repository settings
    docker_apt_repository_content: >
      deb https://apt.dockerproject.org/repo
      {{ ansible_distribution | lower }}-{{ ansible_distribution_release | lower }}
      main

    # Packages to remove before install
    docker_packages_to_remove:
      - lxc-docker*
      - docker.io*

#### Ubuntu distributions specific vars

    # Packages to remove before install
    docker_packages_to_remove:
      - docker.io*

## Misc informations

### Use a custom apt repository

With this role, you can customize the apt repository if you use your own
local mirror per example.

1. Create a file, and set **docker_custom_repository_vars_file** variable with
   its path
2. Into this file, set these variable :
  - docker_apt_repository_key_server
  - docker_apt_repository_key_id
  - docker_apt_repository_file_content

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: achaussier.docker }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro

