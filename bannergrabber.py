from multiprocessing.sharedctypes import Value
import socket
from IPy import IP
''' 
socketX = socket.socket()

ip = input("Please, enter the IP.")

port= input("Please enter the port.")

socketX.connect((ip,int(port)))

print(socketX.recv(1024))
 '''
''' print(socketX.recv(1024))'''

def get_banner(target_socket):
  return target_socket.recv(1024)

def scan(target):
  ip_convert = check_IP_address(target)
  print('\n' + '[-_0 Scanning target.] ' + str(target) )
  for port in range(19, 25):
    banner(ip_convert, port)

def check_IP_address(ip):
  try:
      IP(ip)
      return (ip)
  except ValueError:
    return socket.gethostbyname(ip)

def banner(ip, port):
  try: 
    socketX = socket.socket()
    socketX.settimeout(0.5)
    socketX.connect((ip, int(port)))
    try:
        banner = get_banner(socketX)
        print(f'Connected to {port} - it is open - banner: \n {banner}')
    except:
        print(f'Connected to {port} - could not retrieve banner!')
  except: 
    print(f'[-] Could not connect to {ip} on port {port}.')


targets = input("[+] Please enter the target(s) to scan: ")
if ','  in targets: 
  for ip_address in targets.split(','):
      scan(ip_address.strip(' '))
else: 
  scan(targets)


    

