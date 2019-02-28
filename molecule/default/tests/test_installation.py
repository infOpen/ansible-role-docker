"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    """
    Check installed package
    """

    assert host.package('docker-ce').is_installed


@pytest.mark.parametrize('item_type,path,user,group,mode', [
    ('file', '/etc/docker/daemon.json', 'root', 'root', 0o644),
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


@pytest.mark.parametrize('path,expected_content', [
    ('/etc/docker/certs.d/foo.bar:8081/ca.crt', '__my_ca_cert__'),
    ('/etc/docker/certs.d/foo.bar:8081/client.cert', '__my_client_cert__'),
    ('/etc/docker/certs.d/foo.bar:8081/client.key', '__my_client_key__'),
])
def test_registries_certificates_deployments(host, path, expected_content):
    """
    Ensure Docker registries certificates are properly deployed
    """

    current_item = host.file(path)

    assert current_item.exists
    assert current_item.is_file
    assert expected_content in current_item.content
