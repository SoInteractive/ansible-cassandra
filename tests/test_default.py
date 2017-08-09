from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_packages(Package, SystemInfo):
    present = [
        "python-pip",
        "apt-transport-https",
        "ca-certificates",
        "python-support"
    ]
    if present and SystemInfo.distribution == "ubuntu":
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_directories(File):
    present = [
        "/etc/cassandra",
        "/var/lib/cassandra/data",
        "/var/lib/cassandra/commitlog",
        "/var/lib/cassandra/saved_caches"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/cassandra/cassandra.yaml"
    ]
    if present:
        for file in present:
            f = File(file)
            if f == "/etc/cassandra/cassandra.yaml":
                assert f.mode == 0o644
            assert f.exists
            assert f.is_file


def test_services(Service):
    present = [
        "cassandra"
        ]
    for service in present:
        s = Service(service)
        assert s.is_enabled
        assert s.is_running


def test_socket(Socket):
    assert Socket('tcp://0.0.0.0:7080').is_listening
