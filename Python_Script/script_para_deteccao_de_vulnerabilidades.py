import nmap

# Função para realizar a varredura de vulnerabilidades

def scan_vulnerabilities(target_ip):
    nm = nmap.PortScanner()
    print(f"Iniciando varredura de vulnerabilidades no IP: {target_ip}")
    nm.scan(hosts=target_ip, arguments='--script=vuln')

    print("Resultado da varredura de vulnerabilidades:")
    for host in nm.all_hosts():
        print(f"Host: {host} - {nm[host].hostname()}")
        for proto in nm[host].all_protocols():
            print(f"Protocólo: {proto}")
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Porta {port} - {nm[host][proto][port]['state']}")

# Teste com um IP específico

scan_vulnerabilities('192.168.1.1')