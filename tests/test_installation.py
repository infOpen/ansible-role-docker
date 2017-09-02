"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages(host):
    """
    Check installed package
    """

    assert host.package('docker-ce').is_installed


@pytest.mark.parametrize('item_type,path,user,group,mode', [
    ('file', '/etc/default/docker', 'root', 'root', 0o644),
])
def test_paths(host, item_type, path, user, group, mode):
    """
    Test docker files and folders
    """

    current_item = host.file(path)

    assert current_item.exists
    assert current_item.user == user
    assert current_item.group == group
    assert current_item.mode == mode

    if item_type == 'file':
        assert current_item.is_file
    elif item_type == 'directory':
        assert current_item.is_directory


def test_service(host):
    """
    Test service state
    """

    service = host.service('docker')

    assert service.is_enabled
    assert service.is_running


def test_socket(host):
    """
    Test listening port
    """

    assert host.socket('tcp://127.0.0.1:8081').is_listening


def test_process(host):
    """
    Test process
    """

    assert len(host.process.filter(comm='dockerd')) == 1


def test_docker_command(host):
    """
    Test docker command via an image pull
    """

    assert host.run_expect([0], 'docker run hello-world')
