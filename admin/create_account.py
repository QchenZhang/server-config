from __future__ import print_function

from pssh.clients import ParallelSSHClient

from getpass import getpass

# hosts ip
hosts = ['170.140.151.87', '170.140.151.91']

# this method is using id_rsa to login
# change your method accordingly
# client = ParallelSSHClient(hosts, user="mark", password="passwd")
client = ParallelSSHClient(hosts, user="mark")

passwd = getpass()
username = input("new username: ")
sudo = False


def inputPWD():
    for host in output:
        stdin = output[host].stdin
        stdin.write(passwd+"\n")
        stdin.flush()


output = client.run_command('useradd -m -g phd '+username, sudo=True)
inputPWD()

output = client.run_command('usermod -s /bin/bash '+username, sudo=True)
inputPWD()

output = client.run_command('echo "%s:%s" | chpasswd' %
                            (username, username), sudo=True)
inputPWD()

output = client.run_command('chage -d 0 '+username, sudo=True)
inputPWD()

if sudo:
    output = client.run_command('usermod -aG sudo'+username, sudo=True)
    inputPWD()


# for host, host_output in output.items():
#     for line in host_output.stdout:
#         print(line)
