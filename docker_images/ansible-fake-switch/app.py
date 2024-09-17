from fakenos import FakeNOS
network_os = FakeNOS(inventory='network.yaml')
network_os.start()