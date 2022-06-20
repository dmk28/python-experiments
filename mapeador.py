import nmap


nmScanner = nmap.PortScanner()



def map_scanner(endereco_ip, porta_ip):
    nmScanner.scan(endereco_ip, porta_ip)
    for host in nmScanner.all_hosts():
        print(('Host : %s (%s)') % (host, nmScanner[host].hostname()))
        print('Status : %s' % nmScanner[host].state())
        for proto in nmScanner[host].all_protocols():
            print('---------')
            print('Protocolo: %s' % proto)


            lport = nmScanner[host][proto].keys()
            print(lport)

            for port in lport:
                print ('port : %s\tstate: %s' % (port, nmScanner[host][proto][port]['state']))

def verificacao_scanner(): 
    print("Scanner de portas!")
    print("<----------------->")

    endereco_ip = input("Digite o IP para verificar")
    porta_ip = input("Digite o alcance da porta, ex: 130-500")
    print("Esse é o endereço certo? ", endereco_ip, porta_ip)

    resposta_usuario = input("Se sim, digite 'S' ou 'sim'. Caso contrário, digite 'N' ou 'não")

    if (resposta_usuario == 'S' or 'sim'):
            map_scanner(endereco_ip, porta_ip)
    elif (resposta_usuario == 'N' or 'não'): 
        endereco_ip = input("Digite o IP para verificar")
        porta_ip = input("Digite o alcance da porta, ex: 130-500")
        print("Esse é o endereço certo? ", endereco_ip, porta_ip)
        verificacao_scanner(resposta_usuario)













