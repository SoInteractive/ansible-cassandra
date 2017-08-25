from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_packages(Package, SystemInfo):
    present = [
        "python-pip",
    ]
    if present and SystemInfo.distribution == "ubuntu":
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_directories(File):
    present = [
        "/var/lib/docker/volumes/cass-root-dir/_data/",
        "/var/lib/docker/volumes/cass-data-dir/_data/data",
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/var/lib/docker/volumes/cass-root-dir/_data/cassandra.yaml",
        "/var/lib/docker/volumes/cass-root-dir/_data/cassandra-env.sh"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file

# TODO
# def test_services(Service):
#     present = [
#         "cassandra"
#         ]
#     for service in present:
#         s = Service(service)
#         assert s.is_enabled
#         assert s.is_running
#
#
# def test_socket(Socket):
#     assert Socket('tcp://0.0.0.0:7080').is_listening
