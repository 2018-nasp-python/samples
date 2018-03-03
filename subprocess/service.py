import subprocess

def is_active(service_name):
    service_query = subprocess.run(
        ['systemctl', 'is-active', service_name ],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    if service_query.returncode == 0:
        return True
    else:
        return False

def is_enabled(service_name):
    service_query = subprocess.run(
        ['systemctl', 'is-enabled', service_name ],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    if service_query.stdout.strip() == 'enabled':
        return True
    else:
        return False


if __name__ == "__main__":
    services = ['network', 'NetworkManager', 'sshd', 'nginx']
    for service in services:
        print('{} active: {}  enabled: {}'.format(service, 
                                                  is_active(service),
                                                  is_enabled(service)))