import time

import paramiko

host = '10.10.10.10.'
user = 'userforssh'
secret = '**********'
port = 22


def adduser_mssql(username:str, userpassword:str, email:str, discript:str) -> None:
    """заводим юзверя в базу"""

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host,
                   username=user,
                   password=secret,
                   port=port)
    stdin, stdout, stderr = client.exec_command('ls -l')
    data = stdout.read() + stderr.read()
    # Подключаемся к скулю
    # открываем шел
    channel = client.invoke_shell()
    channel.send('mysql -u root -p' + '\n')
    time.sleep(1)
    channel.send(f"mysqlpassword" + "\n")
    stdout = channel.recv(1024 * 100000)
    channel.send(
        f"""INSERT INTO `mail`.`virtual_users` 
        (`id`, `username`, `userpassword`, `email`, `discrip`, `active`, `auth`,
         `quota`) 
         VALUES (NULL, '{username}', '{userpassword}',
          '{email}', '{discript}', '1', '1', '1000');\n""")
    time.sleep(1)
    stdout = channel.recv(1024 * 100000)
    out_list = stdout.decode().split("\n")
    channel.close()
    client.close()